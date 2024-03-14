# TextTest

![Screenshot](https://drive.google.com/uc?export=view&id=1j-1HVA6f2nhLO_TNwPk4YQWXPSQrlzYVwzj)


## Overview

TextTest is a Python application that automates the conversion of speech to text, processes the text through a preconfigured GPT model acting as a specific expert, converts the GPT's response back to speech, and finally plays the resulting audio.

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/PacliKilla/CCS-Test.git
    ```

2. Navigate to the project directory:

    ```
    cd CCS-Test
    ```

3. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```
3.5 If you use VS Code or any other IDE, just open the cloned folder, and you will most probably get prompted to install all dependencies from requirements.txt but if there is no prompt, open the IDE Terminal and write the above mentioned pip install -r requirements.txt


## Usage

1. Ensure you have a WAV audio file containing the speech you want to process.(Or use my audio files in the folder audio)

2. Open a terminal or command prompt.

3. Navigate to the project directory.

4. Run the Python script:

    ```
    python TextTest.py
    ```

4.5 Or just open TextTest.py in VS Code or any other python IDE with python 3.10 installed and refer to step 3.5.

5. Follow the prompts to enter the path to the input audio file. (audio/sample_audio.wav)

6. On the first run of the script it will begin downloading the GPT4all model it will take around 1.9gb of memory and some time. The application then will process the audio, generate expert responses, and play the final audio response.

![Screenshot](https://drive.google.com/uc?export=view&id=1j-HJPaZHxwnE2FYbSs3i-2t_yg9aI42r)

## Functionality

- **Audio Input**: The application accepts WAV (and only wav files) audio files as input, containing the speech to be converted to text.

- **Speech to Text**: The speech from the audio file is converted into text using the `speech_recognition` library.

- **GPT Processing**: The converted text is passed to a local GPT model, preconfigured to simulate a specific expert in my case a financial advisor), using the `gpt4all` library, specifically im using orca_mini_3b model as it shows decent results but more importantly it is lightweight, it is only 1.9 gb, for comparison models such as gpt4 and Nous-Hermes2 are around 40gb.

- **Text to Speech**: The textual response from the GPT model is converted back to speech using the `gtts` library.

- **Audio Output**: The resulting speech is saved as an audio file and played using the `pygame` library.

## Testing

Basic unit tests are included to verify the functionality of key components such as speech to text conversion and text to speech conversion. You can run the tests by executing the Unit_tests script, i also include the unit test audio file in the audio folder.

## Dependencies

- `speech_recognition`: For converting speech to text.
- `gtts`: For converting text to speech.
- `pygame`: For audio playback.
- `gpt4all`: For interacting with the local GPT model.


