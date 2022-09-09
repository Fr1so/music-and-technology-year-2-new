import simpleaudio as sa

wave_obj = sa.WaveObject.from_wave_file("/home/fr1so/Documents/CSD2/music-and-technology-year-2-new/python_basics/Tuk_1.wav")
play_obj = wave_obj.play()
play_obj.wait_done()