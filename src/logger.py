import logging 
import os
from datetime import datetime

# Using microseconds to ensure a unique log filename
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%f')}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)  # even though there is a folder with same name, keep on appending the files

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s -%(levelname)s - %(message)s",
    level=logging.INFO,
)

# if __name__ == "__main__":
#     logging.info("Logging has started")
