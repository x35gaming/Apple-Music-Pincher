# Apple-Music-Pincher
# By X35gaming (https://github.com/x35gaming)
# Cracks Apple-Music DRM by... Playing it... Then saving it...
# ARR! 'me music!

# Only works on Windows

import win32com.client
#import time
import pyaudio
import wave
import concurrent.futures
frames = []

def rec_start_thread(filename):
    global recording, stream, fName, frames, deviceNo, current_track_data, itunes, song_id, artist_name, album_name, song_name
    fName = filename
    if not recording:
        recording = True
        print(f"Recording started to '{filename}'...")
        print(str(deviceNo))
        frames = []
        while recording:
            data = stream.read(chunk)
            frames.append(data)
            track = itunes.currentTrack
            track_data = (track.Name, track.Artist, track.Album)  # Combine properties

            if track_data != current_track_data:
                if current_track_data is not None:
                    song_has_ended()

                current_track_data = track_data
                artist_name = track.Artist
                album_name = track.Album
                song_name = track.Name
                song_id = song_id + 1
                #pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)
                song_has_started(song_id, artist_name, album_name, song_name)

def rec_stop():
    global recording, stream, fName, frames
    if recording:
        recording = False
        print("Recording stopped.")
        print("Test Point 1")
        print(type(frames))
        frames_bytes = b"".join(frames)
        print(type(frames_bytes))
        print(len(frames_bytes))
        print("Test Point 2")
        wf = wave.open(fName, "wb")
        print("hello?")
        print(type(frames_bytes))
        wf.setnchannels(2)
        print("hello??")
        wf.setsampwidth(3)  # Bytes per sample for 24-bit audio
        print("hello???")
        wf.setframerate(44100)
        print("hello????")
        print(len(frames_bytes))
        wf.writeframes(frames_bytes)
        print("Test Point 3")
        wf.close()

def song_has_started(song_id, artist_name, album_name, song_name):
    print(f"Song has started:.\songs\{song_id} - {song_name} by {artist_name} from {album_name}.wav")
    #pool.submit(rec_start_thread,(f"{song_id} - {song_name} by {artist_name} from {album_name}.wav",))
    rec_start_thread(f".\songs\{song_id} - {song_name} by {artist_name} from {album_name}.wav")

def song_has_ended():
    #global recording_thread
    print("Song has ended.")
    rec_stop()

itunes = win32com.client.Dispatch("iTunes.Application")
recording = False
chunk = 512  # Adjust chunk size as needed
fName = None

deviceNo = 0
deviceNo = 38
song_id = 0
current_track_data = None
stream = pyaudio.PyAudio().open(
    format=pyaudio.paInt24,  # 24-bit audio
    channels=2,  # Stereo
    rate=44100,
    input=True,
    input_device_index=deviceNo,
    frames_per_buffer=chunk
)
while True:
    try:
        track = itunes.currentTrack
        track_data = (track.Name, track.Artist, track.Album)  # Combine properties

        if track_data != current_track_data:
            if current_track_data is not None:
                song_has_ended()

            current_track_data = track_data
            artist_name = track.Artist
            album_name = track.Album
            song_name = track.Name
            song_id = song_id + 1
            #pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)
            song_has_started(song_id, artist_name, album_name, song_name)

        #time.sleep(0.5)  # Check frequently
    except Exception as e:
        print(f"Error: {e}")
        #time.sleep(5)  # Retry after a delay

stream.stop_stream()
stream.close()