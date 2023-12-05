# coding=utf-8

import asyncio  
# pip install edge_tts
import edge_tts  
import vadSound
  
# TEXT = "Most of us compare ourselves with anyone we think is happier — a relative, someone we know a lot, or someone we hardly know. As a result, what we do remember is anything that makes others happy, anything that makes ourselves unhappy, totally forgetting that there is something happy in our own life."
# VOICE = "en-US-MichelleNeural"  
# OUTPUT_FILE = "./test1.mp3"  
  
  
# async def _main() -> None:  
#     communicate = edge_tts.Communicate(TEXT, VOICE)  
#     await communicate.save(OUTPUT_FILE) 

# def _main():  
#     communicate = edge_tts.Communicate(TEXT, VOICE)  
#     communicate.save(OUTPUT_FILE)  
  
  
if __name__ == "__main__":  
    # asyncio.run(_main())
    #_main()
    vadSound.play_sound()