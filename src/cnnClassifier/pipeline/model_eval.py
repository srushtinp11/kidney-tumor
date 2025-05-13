import sys
import os
sys.path.append(os.getcwd()) 

from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.model_eval_04 import Evaluation
from src.cnnClassifier import logger
import os
# import mlflow


STAGE_NAME = "Evaluation stage"


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()
        # os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/srushtinp11/kidney-tumor.mlflow"
        # os.environ["MLFLOW_TRACKING_USERNAME"]="srushtinp11"
        # os.environ["MLFLOW_TRACKING_PASSWORD"]="6d3ab3ade894f33c299eefad34a74749eb5bb472"

        # # # Set MLflow tracking URI
        # mlflow.set_tracking_uri("https://dagshub.com/srushtinp11/kidney-tumor.mlflow")
        # evaluation.log_into_mlflow()


if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e