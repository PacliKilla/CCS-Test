import os
import subprocess
import speech_recognition as sr
from gtts import gTTS
import pygame
from gpt4all import GPT4All
import time

# Process the audio using Google speech recognition
def convert_audio_to_text(audio_file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
    return text

# Convert the text to speech using gTTS library
def convert_text_to_speech(text, output_audio_path):
    tts = gTTS(text)
    tts.save(output_audio_path)

# Initialize pygame for audio playback
def play_audio(audio_file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file_path)
    pygame.mixer.music.play()
    # Wait until the playback is finished
    while pygame.mixer.music.get_busy():  
        time.sleep(0.1)

def main():
    print("Welcome!")
    input_audio_path = input("Enter the path to the input audio file (must be a WAV file): ")

    # Check if the file even exists
    while not os.path.exists(input_audio_path):
        print("Error: There is no such file. Please check again or use the absolute path.")
        input_audio_path = input("Enter the path to the input audio file (must be a WAV file): ")

    # Check if the file extension is WAV
    while not input_audio_path.lower().endswith(".wav"):
        print("Error: Only WAV files are supported. Please choose a WAV file.")
        input_audio_path = input("Enter the path to the input audio file (must be a WAV file): ")

    try:
        converted_text = convert_audio_to_text(input_audio_path)
        print(f"Converted text: {converted_text}")
    except sr.UnknownValueError:
        print("Error: Could not recognize audio.")

    model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")
    print("Generating expert response...")
    gpt_response = model.generate(f"User says: {converted_text}. Now respond shortly as a financial advisor: ")
    # We can limit the response length using "max_token" Two tokens can represent an average word. 
    # The current limit of GPT4ALL is 2048 tokens.

    print("GPT response:", gpt_response)

    # Specify the output audio file path
    output_audio_path = "audio/output_audio.mp3"

    # Convert the GPT response to speech and save it to the output audio file
    convert_text_to_speech(gpt_response, output_audio_path)
    print(f"GPT response saved as {output_audio_path}")

    print("Playing the final audio response...")
    play_audio(output_audio_path)

if __name__ == "__main__":
    main()
