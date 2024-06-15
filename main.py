from car_price_pred import logger
from car_price_pred.pipeline.stage_01_data_ingestion import DataIngestiontrainingPipeline

STAGE_NAME = "data ingestion stage"
try:
    logger.info(f'>>>>>>> stage {STAGE_NAME} started <<<<<<<<')
    obj = DataIngestiontrainingPipeline()
    obj.main()
    logger.info(f'>>>>>>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<< \n\n x=========================x')
                    
except Exception as e :
    logger.exception(e)
    raise e   