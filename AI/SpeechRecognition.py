# 文本转语音
from comtypes.client import CreateObject
import comtypes.client
# try:
#     from comtypes.gen import SpeechLib # comtypes
# except ImportError:
#     # Generate the SpeechLib lib and any associated files
#     engine = comtypes.client.CreateObject("SAPI.SpVoice")
#     stream = comtypes.client.CreateObject("SAPI.SpFileStream")
#     from comtypes.gen import SpeechLib
#
# engine = CreateObject("SAPI.SpVoice")
# stream = CreateObject('SAPI.SpFileStream')
# infile = 'txttomv.txt'
# outfile = 'txttomv.wav'
# stream.open(outfile, SpeechLib.SSFMCreateForWrite)
# engine.AudioOutputStream = stream
# f = open(infile, 'r', encoding='utf-8')
# theText = f.read()
# f.close()
# engine.speak(theText)
# stream.close()
# print('转换成功')

# 语言转文字
# import pyttsx3 as pyttsx
# engine=pyttsx.init()
# engine.say('你好 Zoe')
# engine.runAndWait()


#语言转文字
# print(sr.__version__)
# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
import speech_recognition as sr

# obtain path to "english.wav" in the same folder as this script
from os import path
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "录音.wav")
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "french.aiff")
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "chinese.flac")
print(AUDIO_FILE)
# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file

# recognize speech using Sphinx
try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio,language='zh-CN'))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))


