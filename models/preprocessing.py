import pandas as pd


class DataPreprocessor:

    def load_csv(self, filepath):

        return pd.read_csv(filepath)

    def clean_data(self, dataframe):

        dataframe = dataframe.drop_duplicates()
        dataframe = dataframe.fillna(0)

        return dataframe

    def preprocess(self, filepath):

        data = self.load_csv(filepath)

        data = self.clean_data(data)

        required_columns = [
            "failed_login",
            "unknown_ip",
            "malware_detected"
        ]

        for column in required_columns:

            if column not in data.columns:

                data[column] = 0

        return data[required_columns]