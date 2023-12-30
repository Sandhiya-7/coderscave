import pyaudio
import wave
import time

def record_audio(file_name, duration):
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = duration

    audio = pyaudio.PyAudio()

    # start recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    print("Recording...")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    # stop recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # save the recorded audio to a file
    wave_file = wave.open(file_name, 'wb')
    wave_file.setnchannels(CHANNELS)
    wave_file.setsampwidth(audio.get_sample_size(FORMAT))
    wave_file.setframerate(RATE)
    wave_file.writeframes(b''.join(frames))
    wave_file.close()

    print("Audio recording has been saved.")

def main():
    file_name = input("Enter the name of the audio file: ")
    duration = int(input("Enter the duration of the recording (in seconds): "))

    record_audio(file_name, duration)

if __name__ == "__main__":
    main()























































































































