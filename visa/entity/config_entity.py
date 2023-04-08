from collections import namedtuple #tuple is mutable and namedtuple is immutable and works as dict

DataIngestionConfig = namedtuple("DataIngestionConfig",
["dataset_download_url","raw_data_dir","ingested_train_dir","ingested_test_dir"])

DataValidationConfig = namedtuple("DataValidationConfig", ["schema_file_path"])


TrainingPipelineConfig = namedtuple("TrainingPipelineConfig", ["artifact_dir"])