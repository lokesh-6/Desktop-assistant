import speech_recognition as sr
import os
import pyttsx3
import pyaudio
import webbrowser
import win32com.client
from datetime import datetime
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from transformers import pipeline
import random
import torch
model_name = 'gpt2'  # or other GPT variants like 'gpt2-medium', 'gpt2-large', etc.
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def ai(prompt):
    input_ids = tokenizer.encode(prompt, return_tensors='pt')
    response = model.generate(input_ids, max_length=100,num_beams=5,no_repeat_ngram_size=2,early_stopping=True,num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)

    response_text = tokenizer.decode(response[0], skip_special_tokens=True)
    print("AI Response:", response_text)
    say(response_text)
    if not os.path.exists("Hummer"):
        os.mkdir("Hummer")
    with open(f"Hummer/prompt-{random.randint(1, 25554558666)}.txt", "w") as f:
        f.write(f"Prompt: {prompt}\n")
        f.write(f"Response: {response_text}\n")




def say(text):
    speaker.Speak(text)


def takecmd():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query1 = r.recognize_google(audio, language="en-in")
            print(f"User said: {query1}")
            return query1
        except Exception as e:
            return "Some error occurred"

if __name__ == '__main__':
    print('PyCharm')
    say("Hello, I am levi")
    while True:
        print("Listening...")
        query = takecmd()
        sites = [["youtube", "youtube.com"], ["wikipedia", "wikipedia.org"], ["google", "google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]}...")
                webbrowser.open(site[1])
        if "play music" in query:
            mp = r"C:\Users\Lokesh\Downloads\Cupid i Gave A Second Chance Song Download Mp3(SongsZilla.Net).mp3"
            os.startfile(mp)
        if "the time" in query:
            strfTime = datetime.now().strftime("%H:%M:%S")
            say(f"Sir, the time is {strfTime}")
        if "open code" in query:
            code_path = r"C:\Users\Lokesh\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(code_path)
        if "hello" in query:
            prompt = query  # Use the query as the prompt
            ai(prompt)
