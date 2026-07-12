import os
import pickle
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


class ThreatModelTrainer:

    def train(self, csv_path):

        # Load Dataset
        data = pd.read_csv(csv_path)

        # Check required column
        if "label" not in data.columns:
            raise Exception(
                "Dataset must contain a 'label' column."
            )

        # Features
        X = data.drop("label", axis=1)

        # Target
        y = data["label"]

        # Train/Test Split
        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )

        # AI Model
        model = RandomForestClassifier(
            n_estimators=100,
            random_state=42
        )

        model.fit(X_train, y_train)

        # Save Model
        model_path = os.path.join(
            os.getcwd(),
            "model.pkl"
        )

        with open(model_path, "wb") as file:
            pickle.dump(model, file)

        accuracy = model.score(X_test, y_test)

        return accuracy


if __name__ == "__main__":

    trainer = ThreatModelTrainer()

    accuracy = trainer.train(
        "dataset/train.csv"
    )

    print(f"Model Trained Successfully")
    print(f"Accuracy : {accuracy:.2%}")