import pyaudio
import librosa
import numpy as np

# Function to record audio using pyaudio
def record_audio():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 3

    audio_data = []
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Recording...")

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        audio_data.append(data)

    print("Finished Recording!")

    stream.stop_stream()
    stream.close()
    p.terminate()

    return b''.join(audio_data)

# Function to extract audio features using librosa
def extract_audio_features(audio_data, sampling_rate):
    y, sr = librosa.load(librosa.util.buf_to_float(audio_data), sr=sampling_rate)
    # Extract audio features (e.g., pitch, chroma, and mel frequency cepstral coefficients)
    # You can use machine learning models or rule-based methods to detect emotions from the features
    # For simplicity, we'll just use a random emotion in this example
    emotions = ['happy', 'sad', 'angry', 'excited', 'calm']
    detected_emotion = np.random.choice(emotions)
    return detected_emotion

def main():
    audio_data = record_audio()
    sampling_rate = 44100

    detected_emotion = extract_audio_features(audio_data, sampling_rate)

    print(f"Detected Emotion: {detected_emotion}")

if __name__ == "__main__":
    main()
