import simpleaudio as sa
wave_read = wave.open("Untitled.wav", 'rb')
wave_obj = sa.WaveObject.from_wave_read(wave_read)
play_obj = wave_obj.play()
print("PLAYING SOUND PLAYING SOUND PLAYING SOUND")
play_obj.wait_done()
