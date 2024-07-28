from abc import ABC
from transformers import pipeline

class PipelineTaskFactory(ABC):

    def __init__(self, pipeline_task: str, input_text: str):
        self.pipeline_task = pipeline_task
        self.input_text = input_text

    def text_to_pipeline(self):
        classifier = pipeline(self.pipeline_task)
        return classifier(self.input_text)

class SentimentAnalysis(PipelineTaskFactory):
    def __init__(self, pipeline_task: str, input_text: str):
        super().__init__(pipeline_task, input_text)

    def text_to_pipeline(self):
        return super().text_to_pipeline()

class PipelineFactory:
    pipeline_mappings = {
        "sentiment-analysis" : SentimentAnalysis
        }
           
    def create_pipeline(self, select_pipeline: str, **kwargs):
        if select_pipeline in self.pipeline_mappings:
            return self.pipeline_mappings[select_pipeline](**kwargs)
        else:
            raise ValueError(f"Unknown model type: {select_pipeline}. Pass in one of the following model types: {list(self.pipeline_mappings.keys())}")