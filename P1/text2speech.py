#!/usr/bin/env python
# Script Written by - Mikhail Kulin 2020 www.kulin.co
# Copyright 2018 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Google Cloud Text-To-Speech API sample application .
Example usage:
python quickstart.py
"""

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="../mypjkey.json"
from google.cloud import texttospeech

import transcript 
text = transcript.TRANSCRIPT 

# Instantiates a client

client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized
synthesis_input = texttospeech.SynthesisInput(text=text)

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("female")
voice = texttospeech.VoiceSelectionParams(
language_code='en-GB',
name='en-GB-Wavenet-B',
ssml_gender=texttospeech.SsmlVoiceGender.MALE)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
audio_encoding=texttospeech.AudioEncoding.MP3,
pitch=-4.0,
speaking_rate=1)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(
	input=synthesis_input, voice=voice, audio_config=audio_config
)

# The response's audio_content is binary.
with open('output.mp3', 'wb') as out:
	# Write the response to the output file.
	out.write(response.audio_content)
print('Audio content written to file "output.mp3"')
