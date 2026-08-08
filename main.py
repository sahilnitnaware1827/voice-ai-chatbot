from audio import record_audio
from stt import transcribe_audio
from llm import generate_response
from tts import text_to_speech, play_audio
import asyncio


while True:

    try:
        record_audio()

        user_text = transcribe_audio("audio.wav")

        if not user_text.strip(): # type: ignore
            print("No speech detected. Please try again.")
            continue

        print("You:", user_text)

        if user_text.lower().strip() in ["exit", "quit", "bye"]: # type: ignore
            farewell = "Goodbye! Have a great day."

            print("AI:", farewell)

            audio_file = asyncio.run(text_to_speech(farewell))
            play_audio(audio_file)

            break

        response = generate_response(user_text)

        if not response.strip():
            print("AI did not generate a response.")
            continue

        print("AI:", response)

        audio_file = asyncio.run(text_to_speech(response))
        play_audio(audio_file)

    except Exception as e:
        print("Something went wrong:", e)
        print("Let's try again.")
        