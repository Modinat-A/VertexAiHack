import os
import vertexai
from vertexai.language_models import TextGenerationModel
project_id = os.getenv('GOOGLE_CLOUD_PROJECT')


def summary(text):
    vertexai.init(project=project_id , location="us-central1")
    parameters = {
        "temperature": 0.2,
        "max_output_tokens": 256,
        "top_p": 0.95,
        "top_k": 40
    }
    model = TextGenerationModel.from_pretrained("text-bison@001")
    response = model.predict(
       f'Provide a summary with about two sentences for the following :{text} ', **parameters
    )
    return response.text
