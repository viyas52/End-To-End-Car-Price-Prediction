from car_price_pred import logger
from car_price_pred.pipeline.stage_01_data_ingestion import DataIngestiontrainingPipeline
from car_price_pred.pipeline.stage_02_data_validation import DataValidationTraningPipeline
from car_price_pred.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from car_price_pred.pipeline.stage_04_model_trainer import ModeltrainerTrainingPipeline
from car_price_pred.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
  
STAGE_NAME = "data ingestion stage"
try:
    logger.info(f'>>>>>>> stage {STAGE_NAME} started <<<<<<<<')
    data_ingestion=DataIngestiontrainingPipeline()
    data_ingestion.main()
    logger.info(f'>>>>>>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<< \n\n x=========================x')
                    
except Exception as e :
    logger.exception(e)
    raise e 

STAGE_NAME = "data validation stage"
try:
    logger.info(f'>>>>>>> stage {STAGE_NAME} started <<<<<<<<')
    data_validation=DataValidationTraningPipeline()
    data_validation.main()
    logger.info(f'>>>>>>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<< \n\n x=========================x')
                    
except Exception as e :
    logger.exception(e)
    raise e 

STAGE_NAME = "data transformation stage"
try:
    logger.info(f'>>>>>>> stage {STAGE_NAME} started <<<<<<<<')
    data_transformation=DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f'>>>>>>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<< \n\n x=========================x')
                    
except Exception as e :
    logger.exception(e)
    raise e 

STAGE_NAME = "model trainer stage"
try:
    logger.info(f'>>>>>>> stage {STAGE_NAME} started <<<<<<<<')
    model_trainer=ModeltrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f'>>>>>>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<< \n\n x=========================x')
                    
except Exception as e :
    logger.exception(e)
    raise e 



STAGE_NAME = "model evaluation stage"
try:
    logger.info(f'>>>>>>> stage {STAGE_NAME} started <<<<<<<<')
    model_evaluation= ModelEvaluationTrainingPipeline()
    model_evaluation.main()
    logger.info(f'>>>>>>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<< \n\n x=========================x')
                    
except Exception as e :
    logger.exception(e)
    raise e 