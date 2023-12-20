# Desktop Assistant - Jarvis

## Description

This project implements a desktop assistant named Jarvis. It utilizes various Python libraries and APIs to perform tasks based on voice commands and AI-driven responses.

## Features

- **Voice Recognition:** Utilizes the `speech_recognition` library to recognize voice commands.
- **Speech Synthesis:** Employs the `pyttsx3` library for text-to-speech synthesis.
- **Web Browsing:** Opens specific websites based on user commands using the `webbrowser` module.
- **Time Reporting:** Retrieves and reports the current time upon request.
- **AI-Powered Responses:** Leverages Hugging Face's GPT-2 model to generate AI-driven responses based on user prompts.
- **Music Playback:** Plays a specific music file upon command.

## Requirements

- Python 3.x
- Libraries:
  - `speech_recognition`
  - `pyttsx3`
  - `transformers`
  - `torch`
  - `openai`

## Usage

1. Ensure all required libraries are installed.
2. Run the `main.py` script.
3. Interact with Jarvis by speaking commands.
4. Jarvis responds to various commands for web browsing, music playback, time reporting, and AI-driven conversation.

## Files

- `main.py`: Main script containing the assistant's functionalities.
- `config.py`: File storing API keys or configurations (sensitive information, not provided).
- `Hummer/`: Directory to store prompt-response logs.
- `PyAudio-0.2.11-cp310-cp310-win_amd64.whl`: Library file.
- Other auxiliary files and dependencies.

## References

- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [OpenAI GPT-2](https://beta.openai.com/)
- Documentation of used libraries and APIs
