import os

from google.cloud.speech_v2 import SpeechClient
from google.cloud.speech_v2.types import cloud_speech
project_id = 'concise-decker-350904' #os.getenv('GOOGLE_CLOUD_PROJECT')


def transcribe(
    audio_file
) -> cloud_speech.RecognizeResponse:
    """Transcribe an audio file."""
    # Instantiates a client
    client = SpeechClient()
    content= audio_file
    config = cloud_speech.RecognitionConfig(
        auto_decoding_config={}, language_codes=["en-US"], model="latest_long"
    )
    request = cloud_speech.RecognizeRequest(
        recognizer=f"projects/{str(project_id)}/locations/global/recognizers/_",
        config=config,
        content=content,
    )

    # Transcribes the audio into text
    response = client.recognize(request=request)
    final_response=''
    for result in response.results:
        print(f"Transcript: {result.alternatives[0].transcript}")
        final_response = final_response + ' ' + result.alternatives[0].transcript

    return final_response