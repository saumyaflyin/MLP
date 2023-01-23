from Insurance.logger import logging
from Insurance.exception import InsuranceException
import os
import sys
from Insurance.utils import get_collection_as_dataframe
from Insurance.entity.config_entity import DataIngestionConfig
from Insurance.entity import config_entity

def test_logger_exception():
    try:
        logging.info("starting the test_logger_exception")
        result = 3/10
        print(result)
        logging.info("ending the test_logger_exception")
    except Exception as e:
        logging.debug(str(e))
        raise InsuranceException(e, sys)

if __name__ == "__main__":
    try:
        #test_logger_exception()
        #start_training_pipeline()
        #get_collection_as_dataframe(database_name = "INSURANCE", collection_name= "INSURANCE_PROJECT")
         training_pipeline_config= config_entity.TrainingPipelineConfig()
         data_ingestion_config = config_entity.DataIngestionConfig(training_pipeline_config)
         print(data_ingestion_config.to_dict())
    except Exception as e:
        print(e)

