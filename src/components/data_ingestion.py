import os
import sys
from src.exception import customException
from src.logger import logging
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from dataclasses import dataclass



''' 
where I have to save the train, test and raw data
what kind of input is require in application, that all information and inputs are creating inside this class
'''
@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifact',"train.csv")
    test_data_path: str = os.path.join('artifact',"test.csv")
    raw_data_path: str = os.path.join('artifact',"raw.csv")
    # this all are the input that I give to DataIngestion Component and DataIngestion Component knows were to store this train,test and raw data


class DataIngestion:
    def __init__(self):

        # train,test and raw data path are stored in this variable
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):

        # if your data is stored in some databases then You have to write your code here to retrive that data
        logging.info("Entered the data ingestion coomponent")

        try:
            df = pd.read_csv(r'notebook\data\stud.csv')
            logging.info("Exported/read the dataset as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok = True)

            df.to_csv(self.ingestion_config.raw_data_path,index = False,header=True)

            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index = False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index = False,header=True)

            logging.info("Ingestion of data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        
        except Exception as e:
            raise customException(e,sys)
        
if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()