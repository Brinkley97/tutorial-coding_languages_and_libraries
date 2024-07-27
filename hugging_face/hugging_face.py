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

# class ChoosePipelineTask():
#     def task(pipeline_task, input_text):
#         pass 

#     pipelines = {
#         "sentiment-analysis" : SentimentAnalysis(pipeline_task, input_text)
#     }