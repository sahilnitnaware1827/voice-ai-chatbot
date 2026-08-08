# 🎙️ Voice AI Chatbot

A Python-based Voice AI chatbot that enables continuous voice conversations using **Speech-to-Text (STT), Large Language Models (LLMs), and Text-to-Speech (TTS)**.

The project captures the user's voice, converts it into text using OpenAI Whisper, generates an AI response using Google Gemini, converts the response back into speech using Edge-TTS, and plays the generated audio.

> **Project Status:** MVP / Learning Project

---

## 🚀 Features

* 🎤 Voice input using microphone
* 📝 Speech-to-Text using OpenAI Whisper
* 🧠 AI response generation using Google Gemini
* 🔊 Text-to-Speech using Edge-TTS
* 🔁 Continuous conversation loop
* 🚪 Voice commands to exit the conversation
* 🛡️ Basic handling for empty/silent input
* 🧩 Modular Python architecture

---

## 🏗️ Architecture

```text
                🎤 User Voice
                     │
                     ▼
                audio.py
                     │
                     ▼
              audio.wav
                     │
                     ▼
                 stt.py
                     │
                     ▼
             Whisper STT Model
                     │
                     ▼
                User Text
                     │
                     ▼
                 llm.py
                     │
                     ▼
              Google Gemini
                     │
                     ▼
              AI Text Response
                     │
                     ▼
                 tts.py
                     │
                     ▼
                 Edge-TTS
                     │
                     ▼
                🔊 AI Voice
```

---

## 📁 Project Structure

```text
Voice_AI_Chatbot/
│
├── audio.py
├── stt.py
├── llm.py
├── tts.py
├── main.py
│
├── requirements.txt
├── README.md
├── .gitignore
│
└── .env                 # Create locally - not included in Git
```

### File Description

| File               | Purpose                                                      |
| ------------------ | ------------------------------------------------------------ |
| `audio.py`         | Records audio from the microphone                            |
| `stt.py`           | Converts recorded audio into text using Whisper              |
| `llm.py`           | Sends user text to Google Gemini and returns the AI response |
| `tts.py`           | Converts AI text into speech and plays the generated audio   |
| `main.py`          | Controls the complete conversation pipeline                  |
| `requirements.txt` | Contains Python dependencies                                 |
| `.env`             | Stores API keys and environment variables locally            |

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/voice-ai-chatbot.git
```

Move into the project directory:

```bash
cd voice-ai-chatbot
```

---

## 2. Create a virtual environment

Windows:

```powershell
python -m venv .Voice_AI_venv
```

Activate it:

```powershell
.\.Voice_AI_venv\Scripts\Activate.ps1
```

You should see:

```text
(.Voice_AI_venv)
```

---

## 3. Install dependencies

```powershell
pip install -r requirements.txt
```

---

# 🔐 4. Create the `.env` file

The `.env` file is **not included in the GitHub repository** because it may contain secret API credentials.

Create a new file in the project root:

```text
Voice_AI_Chatbot/
│
├── .env
├── main.py
├── llm.py
├── audio.py
├── stt.py
└── tts.py
```

Add your Google Gemini API key:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

Do **not** upload this file to GitHub.

The project `.gitignore` already excludes:

```text
.env
```

---

# 🔑 Getting a Gemini API Key

Create a Gemini API key through Google's AI developer platform.

After obtaining the key, put it in:

```env
GOOGLE_API_KEY=your_api_key_here
```

Never hardcode your API key directly into Python source code.

---

# 🎧 5. Install FFmpeg

Whisper requires **FFmpeg** for processing audio files.

Verify that FFmpeg is available:

```powershell
ffmpeg -version
```

If the command prints the FFmpeg version, it is installed correctly.

If Windows cannot find the command, install FFmpeg and add its `bin` directory to your system PATH.

---

# ▶️ 6. Run the chatbot

Make sure the virtual environment is activated:

```powershell
.\.Voice_AI_venv\Scripts\Activate.ps1
```

Then run:

```powershell
python main.py
```

You should see:

```text
Recording...
Recording Saved.
```

Speak into your microphone.

Example:

```text
You: Hello, can you hear me?

AI: Hello! Yes, I can hear you. How can I help you today?
```

The AI response will then be converted into speech and played through your speakers.

---

# 🗣️ Voice Conversation

The chatbot supports continuous conversation:

```text
User speaks
     ↓
Speech → Text
     ↓
Gemini generates response
     ↓
Text → Speech
     ↓
AI speaks
     ↓
User speaks again
     ↓
...
```

You can end the conversation using:

```text
exit
quit
bye
```

---

# 🧠 Technologies Used

* **Python**
* **LangChain**
* **Google Gemini**
* **OpenAI Whisper**
* **Edge-TTS**
* **SoundDevice**
* **Pygame**
* **FFmpeg**

---

# 🔄 Core Pipeline

The complete pipeline is:

```text
Microphone
    ↓
SoundDevice
    ↓
WAV Audio
    ↓
Whisper
    ↓
Text
    ↓
LangChain + Gemini
    ↓
AI Response
    ↓
Edge-TTS
    ↓
MP3 Audio
    ↓
Pygame
    ↓
Speaker
```

---

# ⚠️ Current Limitations

This project is an **MVP / learning implementation**, not a production-ready voice AI system.

Current limitations include:

* Fixed-duration audio recording
* No Voice Activity Detection (VAD)
* Non-streaming STT
* Non-streaming LLM responses
* Non-streaming TTS
* Basic error handling
* Local audio processing
* No authentication
* No persistent conversation memory
* No production monitoring
* Edge-TTS voice is suitable for prototyping but can be replaced with a more natural conversational voice provider

---

# 🚀 Future Improvements

Possible improvements for a production version:

* Real-time Voice Activity Detection
* Streaming Speech-to-Text
* Streaming LLM responses
* Streaming Text-to-Speech
* Natural conversational voices
* Conversation memory
* Tool calling
* Agentic AI capabilities
* FastAPI backend
* Web-based voice interface
* Authentication
* Logging and monitoring
* Docker deployment
* Cloud deployment
* Better latency optimization

---

# 🎯 Learning Objective

This project was created to understand the fundamental architecture behind Voice AI systems:

```text
Speech
  ↓
Speech-to-Text
  ↓
LLM
  ↓
Text-to-Speech
  ↓
Speech
```

It provides a foundation for building more advanced **real-time Voice AI Agents** and integrating agentic capabilities such as tools, memory, and external services.

---

## 📌 Project Status

**MVP completed.**

The project successfully demonstrates an end-to-end voice conversation pipeline using:

**STT → LLM → TTS**

A future production version can extend this architecture with real-time streaming, memory, tools, and agentic workflows.
