import asyncio
from dotenv import load_dotenv
from livekit.agents import AutoSubscribe, JobContext, WorkerOptions, cli, llm
from livekit.plugins import openai, silero
from api import AssistantFnc

load_dotenv()

async def entrypoint(ctx: JobContext):
    initial_ctx = llm.ChatContext().append(
        role="system",
        text=(
            "You are a voice assistant created by LiveKit. "
            "Your interface with users will be voice. "
            "Keep responses short and avoid unpronounceable punctuation."
        ),
    )

    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)

    fnc_ctx = AssistantFnc()

    # Instead of VoiceAssistant (which caused errors), we’ll just show TTS usage.
    tts = openai.TTS()

    await asyncio.sleep(1)
    print("Hey, how can I help you today?")
    await tts.speak("Hey, how can I help you today!")

if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
