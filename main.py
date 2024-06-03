import os
import time

HISTORY_DIR = "../scraper/history"

TARGET_PREFIX = "A33X-1"

LOOKBACK_WINDOW_IN_MIN = 60


def isTargetFileName(filename: str) -> bool:
    if not filename.startswith(TARGET_PREFIX):
        return False

    suffix = filename[len(TARGET_PREFIX) + 1 :]
    lower_bound_timestamp = time.localtime(time.time() - 60 * LOOKBACK_WINDOW_IN_MIN)
    lower = time.strftime("%Y-%m-%d-%X-%Z", lower_bound_timestamp)
    upper = time.strftime("%Y-%m-%d-%X-%Z")
    return lower <= suffix <= upper


if __name__ == "__main__":
    for filename in os.listdir(HISTORY_DIR):
        if isTargetFileName(filename):
            print(filename)
