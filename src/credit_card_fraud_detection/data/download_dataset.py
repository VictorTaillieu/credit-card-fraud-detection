import logging
import shutil

import kagglehub

from credit_card_fraud_detection import PROJECT_ROOT

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)


def download_creditcard_data(output_dir="data/raw"):
    output_dir = PROJECT_ROOT / output_dir

    logging.info("Downloading dataset from Kaggle...")

    dataset_path = kagglehub.dataset_download("mlg-ulb/creditcardfraud")

    # Copy to data/raw
    shutil.copytree(dataset_path, output_dir, dirs_exist_ok=True)

    logging.info(f"Dataset saved to {output_dir}")


if __name__ == "__main__":
    download_creditcard_data()
