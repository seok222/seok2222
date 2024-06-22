from gtts import gTTS
text = 'Can I help you?'
file_name = 'sample.mp3'
tts_en = gTTS(text=text, lang='en')
tts_en.save(file_name)

from playsound import playsound
playsound(file_name) # .mp3 파일 재생