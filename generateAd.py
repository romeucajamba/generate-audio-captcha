import random
from captcha.audio import AudioCaptcha

def generate_random_captcha(length=6):
    charters = '1234567890'
    captcha_text = ''.join(random.choices(charters, k=length))
    
    return captcha_text

audio = AudioCaptcha()
captcha_text = generate_random_captcha()
print("Generate Captcha text: ", captcha_text)
audio.write(captcha_text, 'Audio_captcha.wav')
print('Audio captcha genereted: Audio_captcha.wav')