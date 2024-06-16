import os
from car_price_pred import logger
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pandas as pd

from car_price_pred.entity.config_entity import DatatransformationConfig

class DataTransformation:
    def __init__(self, config: DatatransformationConfig):
        self.config = config

    def preprocessing(self):
        df = pd.read_csv(self.config.data_path)
        
        df = df.dropna()
        
        df.drop_duplicates(inplace=True)
        
        encoder = LabelEncoder()
        
        df['Fuel_Type'] = encoder.fit_transform(df['Fuel_Type'])
        df['Seller_Type'] = encoder.fit_transform(df['Seller_Type'])
        df['Transmission'] = encoder.fit_transform(df['Transmission'])
        df['Car_Name'] = encoder.fit_transform(df['Car_Name'])  
        
        train,test = train_test_split(df,random_state=42,test_size=0.2)
        
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)
        logger.info(train.head())
        logger.info(test.head())

        print(train.shape)
        print(test.shape)
        print(train.head())
        print(test.head())
        
        