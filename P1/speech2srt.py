import srt
import time
import os
from google.cloud import speech

import transcript 
text = transcript.TRANSCRIPT 

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="../audio2timestamp.json"

def long_running_recognize(uri="./output.mp3", sample_rate_hertz=16000, language_code="en"):
    """
    Transcribe long audio file from Cloud Storage using asynchronous speech
    recognition
    Args:
      storage_uri URI for audio file in GCS, e.g. gs://[BUCKET]/[FILE]
    """

    # print("Transcribing {} ...".format(args.storage_uri))
    client = speech.SpeechClient()

    # Encoding of audio data sent.
    encoding = speech.RecognitionConfig.AudioEncoding.LINEAR16
    config = {
        "enable_word_time_offsets": True,
        "enable_automatic_punctuation": True,
        "sample_rate_hertz": sample_rate_hertz,
        "language_code": language_code,
        "encoding": encoding,
    }
    audio = {"uri": uri}

    operation = client.long_running_recognize(
        request={
            "config": config,
            "audio": audio,
            }
    )
    response = operation.result()

    subs = []

    for result in response.results:
        # First alternative is the most probable result
        subs = break_sentences(args, subs, result.alternatives[0])

    print("Transcribing finished")
    return subs


def write_srt(args, subs):
    srt_file = args.out_filename + ".srt"
    f = open(srt_file, 'w')
    f.writelines(srt.compose(subs))
    f.close()
    return


subs = long_running_recognize()
write_srt(out_filename="output")
