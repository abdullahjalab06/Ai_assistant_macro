import os
import edge_tts
import asyncio


async def _Text_To_Speech(text):
    communicate = edge_tts.Communicate(
        text=text,
        voice="ar-SA-HamedNeural",
        rate="+20%"
    )

    await communicate.save("output.mp3")


def Text_To_Speech(response):

    asyncio.run(_Text_To_Speech(response))

    os.startfile("output.mp3")


