from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def text_to_speech_ibm(text_content, output_audio_path, api_key, service_url,voice='en-US_KevinV3Voice',speed=100):
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
