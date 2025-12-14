import pandas as pd

from credit_card_fraud_detection import PROJECT_ROOT


class CreditCardDataLoader:
    def __init__(self, raw_data_path="data/raw/creditcard.csv"):
        self.raw_data_path = PROJECT_ROOT / raw_data_path

        if not self.raw_data_path.exists():
            raise FileNotFoundError(
                f"Raw data file not found at {self.raw_data_path}. "
                "Please download the dataset first."
            )

    def load_raw_data(self):
        df = pd.read_csv(self.raw_data_path)

        return df
