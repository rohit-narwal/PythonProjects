# it will translate from 1 language to another
# only text
# import googletrans
# # making the object
# transalator = googletrans.Translator()
# # translating the languages
# translated = transalator.translate('I love india', dest = 'hi')
# print(translated)
# print(googletrans.LANGUAGES)

# with audio
import googletrans
import speech_recognition as sr
# making the object
transalator = googletrans.Translator()
# translating the languages
translated = transalator.translate('I love india', dest = 'hi')
print(translated)