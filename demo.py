from nlp_hate_classification.logger import logging
from nlp_hate_classification.exception import CustomException
import sys

#logging.info("This is an info message")
'''
try:
    a= 10/"0"
except Exception as e:
    logging.error("This is an error message")
    raise CustomException(e, sys) from e

'''

from nlp_hate_classification.configuration.awscloud import AWSS3Sync
objaws = AWSS3Sync()
objaws.sync_file_from_s3("hate-classification-nlp-bucket", "hate-classification-nlp-bucket/dataset.zip", "download_data.zip")

