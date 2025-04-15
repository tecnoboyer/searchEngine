from google.cloud import texttospeech

client = texttospeech.TextToSpeechClient()

ssml = """<speak>
  I know how it feels—<prosody rate="slow" volume="soft">overwhelmed by the never-ending tasks of job hunting</prosody>, 
  <prosody rate="slow">buried under endless writing</prosody>, 
  and <emphasis level="strong">struggling to craft just a handful of tailored resumes and cover letters</emphasis>.
  <break time="500ms"/>

  You're ready to dive into the job market. 
  <emphasis level="moderate">You’re eager to showcase your skills</emphasis>, 
  <prosody pitch="+5%">highlight your experience</prosody>, 
  and <emphasis level="strong">land the right opportunity</emphasis>.
  <break time="300ms"/>
  But then, reality hits, and <prosody rate="slow" pitch="-5%">motivation starts slipping away</prosody>.
  <break time="700ms"/>


</speak>"""  # Paste the SSML above here

response = client.synthesize_speech(
    input=texttospeech.SynthesisInput(ssml=ssml),
    voice=texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Neural2-C"  # Expressive voice for narration
    ),
    audio_config=texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
    ),
)

with open("Intro2.mp3", "wb") as out:
    out.write(response.audio_content)