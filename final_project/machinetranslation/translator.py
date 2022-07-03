import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()


#apikey = os.environ['apikey']
#url = os.environ['url']

apikey="9XjcO-rzOjZWVRMZSG5Kfh8XiPvRna-xPOdBuh4XAUMb"
url="https://api.us-south.language-translator.watson.cloud.ibm.com/instances/6271cc42-76bd-423a-b0a4-cbe758372bfd"

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def french_to_english(frenchText):
    """takes french text as input and returned the translated english text """
    english_text = language_translator.translate(text=frenchText,model_id='fr-en').get_result()
    return english_text['translations'][0]['translation'] #i want only the translation not the dictionnary

def english_to_french(englishText):
    """takes english text as input and returned the translated french text """
    french_text = language_translator.translate(text=englishText,model_id='en-fr').get_result()
    return french_text['translations'][0]['translation'] #I want only the translation not the dictionnary
