
import edge_tts
import asyncio
import pygame
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
AUDIO_FILE = BASE_DIR / "output.mp3"


async def _Text_To_Speech(text):
    communicate = edge_tts.Communicate(
        text=text,
        voice="ar-SA-HamedNeural",
        rate="+20%"
    )

    await communicate.save(str(AUDIO_FILE))


def Text_To_Speech(response):

    # Generate audio
    asyncio.run(_Text_To_Speech(response))

    # Initialize audio player
    if not pygame.mixer.get_init():
        pygame.mixer.init()

    # Play audio
    pygame.mixer.music.load(str(AUDIO_FILE))
    pygame.mixer.music.play()

    # Wait until playback finishes
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(20)

    # Release audio file
    pygame.mixer.music.unload()
