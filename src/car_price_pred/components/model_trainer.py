import pandas as pd
import os
from car_price_pred import logger
from sklearn.ensemble import GradientBoostingRegressor
import joblib

from car_price_pred.entity.config_entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
        
    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)


        x_train = train_data.drop([self.config.target_column], axis=1)
        x_test = test_data.drop([self.config.target_column], axis=1)
        y_train = train_data[[self.config.target_column]]
        y_test = test_data[[self.config.target_column]]

        model = GradientBoostingRegressor(learning_rate=self.config.learning_rate, n_estimators=self.config.n_estimators, max_depth=self.config.max_depth)
        model.fit(x_train, y_train)

        joblib.dump(model, os.path.join(self.config.root_dir, self.config.model_name))