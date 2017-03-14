'''###############################################################################
import pyttsx
engine = pyttsx.init()
#engine.say('Sally sells seashells by the seashore.')
engine.say(u"Welcome, Water Buffalo")
engine.runAndWait()
print 'waited now i guess.... '
engine.stop()'''

'''#!/usr/bin/env python
from os import environ, path
from pocketsphinx import LiveSpeech, get_model_path, AudioFile, get_data_path
from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *

MODELDIR = "pocketsphinx/model"
model_path = get_model_path()
DATADIR = "pocketsphinx/test/data"

# Create a decoder with certain model
config = Decoder.default_config()
config.set_string('-hmm', path.join(model_path, 'en-us'))
config.set_string('-lm', path.join(model_path, 'en-us.lm.bin'))
config.set_string('-dict', path.join(model_path, 'cmudict-en-us.dict'))
decoder = Decoder(config)

# Decode streaming data.
decoder = Decoder(config)
decoder.start_utt()
stream = open('speech-to-text-websockets-python/recordingsCopy/0001.wav', 'rb')
while True:
  buf = stream.read(1024)
  if buf:
    decoder.process_raw(buf, False, False)
  else:
    break
decoder.end_utt()
print ('Best hypothesis segments: ', [seg.word for seg in decoder.seg()])'''

import speech_recognition as sr
import io, json
r = sr.Recognizer()
r.energy_threshold = 4000
with io.open('secret.json') as cred:
    creds = json.load(cred)
#audio_data = sr.AudioData('speech-to-text-websockets-python/recordingsCopy/0001.wav', 8000, 1)
#audio_data.get_wav_data(convert_rate = None, convert_width = None)
with sr.AudioFile('output2.wav') as source:    # open the audio file for reading
    audio_data = r.record(source) #read the entire audio file
print r.recognize_wit(audio_data, key=str(creds['wit_ai']), show_all = True)
print r.recognize_bing(audio_data, key=str(creds['bing_api']), language = "en-US", show_all = True)
