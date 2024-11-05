import os
from typing import Any, List

import requests
from dotenv import load_dotenv

from dlnanny.logging import logger


def requeue_sonarr() -> Any:
    """Requeue Stuck Downloads in Sonarr."""
    load_dotenv()
    SONARR_URL = os.getenv("SONARR_URL")
    SONARR_API_KEY = os.getenv("SONARR_API_KEY")

    # Get Activity
    activity_url = f"{SONARR_URL}/queue"
    problem_children: List[dict] = []

    response = requests.get(activity_url, headers={"X-Api-Key": SONARR_API_KEY}, timeout=10)
    SUCCESS = 200

    if response.status_code == SUCCESS:
        activity_queue = response.json()

        for record in activity_queue['records']:
            if not record['episodeHasFile']:  # Simplified boolean check
                problem_children = [
                    {
                        "seriesId": record["seriesId"],
                        "episodeId": record["episodeId"],
                        "id": record["id"],
                    },
                ]
        logger.error("Failed to retrieve activity queue: %s - %s", response.status_code, response.text)
        return  # Early exit if retrieval fails

    # Iterate through IDs and delete them
    NO_CONTENT = 204
    for problem_child in problem_children:
        delete_response = requests.delete(f"{activity_url}/{problem_child['id']}", headers={"X-Api-Key": SONARR_API_KEY}, timeout=10)
        if delete_response.status_code in (SUCCESS, NO_CONTENT):
            logger.info(f"Successfully deleted item with ID {problem_child['id']}")
            # Prepare re-queue payload after deletion
            requeue_payload = {
                "seriesId": problem_child['seriesId'],
                "episodeId": problem_child['episodeId'],
            }
            # Re-queue the stuck episodes
            requeue_response = requests.post(f"{SONARR_URL}/command/rosource", json=requeue_payload, headers={"X-Api-Key": SONARR_API_KEY}, timeout=10)
            SUCCESS_ALT = 201
            if requeue_response.status_code == SUCCESS_ALT:
                logger.info(f"Successfully re-queued episode {problem_child['episodeId']}")
            else:
                logger.error(f"Failed to re-queue episode {problem_child['episodeId']}: {requeue_response.status_code} - {requeue_response.text}")
        else:
            logger.error(f"Failed to delete item with ID {problem_child['id']}: {delete_response.status_code} - {delete_response.text}")
