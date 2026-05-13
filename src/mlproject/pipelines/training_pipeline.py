import sys
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_transformation import DataTransformation
from src.mlproject.components.model_trainer import ModelTrainer
from src.mlproject.exception import CustomException


class TrainPipeline:

    def start_training_pipeline(self):

        try:
            # Data Ingestion
            data_ingestion = DataIngestion()

            train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

            # Data Transformation
            data_transformation = DataTransformation()

            train_arr, test_arr, _ = data_transformation.initiate_data_transormation(
                train_data_path,
                test_data_path
            )

            # Model Training
            model_trainer = ModelTrainer()

            print(model_trainer.initiate_model_trainer(train_arr, test_arr))

        except Exception as e:
            raise CustomException(e, sys)