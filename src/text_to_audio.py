from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import requests

def text_to_speech_ibm(text_content, output_audio_path, api_key, service_url,voice='en-US_KevinV3Voice',speed=0):
    """
    Converts text to speech using IBM Watson's Text to Speech service.

    Parameters:
    text_content (str): The text to be converted to speech.
    output_audio_path (str): The file path to save the audio file.
    api_key (str): The API key for IBM Watson Text to Speech service.
    service_url (str): The URL for the IBM Watson Text to Speech service.
    voice (str): The voice for the IBM Watson Text to Speech service.
    speed (number): The speed for the IBM Watson Text to Speech service.
    """
    # Set up the authenticator with the API key
    authenticator = IAMAuthenticator(api_key)
    
    # Create the Text to Speech client
    text_to_speech = TextToSpeechV1(authenticator=authenticator)
    
    # Set the service URL
    text_to_speech.set_service_url(service_url)
    
    # Synthesize the text content and write the result to an audio file
    with open(output_audio_path, 'wb') as audio_file:
        synthesis = text_to_speech.synthesize(
            text_content,
            accept='audio/mp3',
            voice=voice,  # This is one of the voices you can choose
            rate_percentage=speed
        ).get_result()
        
        audio_file.write(synthesis.content)
    print(f"Audio content written to {output_audio_path}")

def text_to_speech_elevenlabs(text_content, output_audio_path, api_key, service_url='https://api.elevenlabs.io/v1/text-to-speech/',voice='pNInz6obpgDQGcFmaJgB',speed=0):
    CHUNK_SIZE = 1024
    url = f"{service_url}{voice}"

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": api_key
    }

    data = {
        "text": text_content,
        # "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }
    
    response = requests.post(url, json=data, headers=headers)
    with open(output_audio_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)
    print(f"Audio content written to {output_audio_path}")
