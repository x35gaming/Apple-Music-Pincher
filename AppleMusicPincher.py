# Apple-Music-Pincher
# By X35gaming (https://github.com/x35gaming)
# Cracks Apple-Music DRM by... Playing it... Then saving it...
# ARR! 'me music!

# Only works on Windows

import win32com.client
import pyaudio
import wave
import threading

def checkLoop():
    global frames_bytes, itunes, recording, stream, fName, frames, deviceNo, current_track_data, itunes, song_id, artist_name, album_name, song_name, track_data
    stream = pyaudio.PyAudio().open(
        format=pyaudio.paInt24,  # 24-bit audio
        channels=2,  # Stereo
        rate=44100,
        input=True,
        input_device_index=deviceNo,
        frames_per_buffer=chunk
    )
    while True:
        if recording:
            frames = []
            while recording:
                data = stream.read(chunk)
                frames.append(data)

        


def rec_start_thread(filename):
    global recording, stream, fName, frames, deviceNo, current_track_data, itunes, song_id, artist_name, album_name, song_name, track_data, checkThread
    fName = filename
    if not recording:
        recording = True
        print(f"Recording started to '{filename}'...")
        print(str(deviceNo))
        frames = []
    while recording:
        track = itunes.currentTrack
        track_data = (track.Name, track.Artist, track.Album)  # Combine properties    
        if track_data != current_track_data:
            if current_track_data is not None:
                song_has_ended()


            #current_track_data = track_data
            #artist_name = track.Artist
            #album_name = track.Album
            #song_name = track.Name
            #song_id = song_id + 1
            #song_has_started(song_id, artist_name, album_name, song_name)


        

def rec_stop():
    global frames_bytes, recording, stream, fName, frames
    if recording:
        recording = False
        #checkThread.join()
        print(len(frames))
        frames_bytes = b"".join(frames)
        wf = wave.open(fName, "wb")
        wf.setnchannels(2)
        wf.setsampwidth(3)  # Bytes per sample for 24-bit audio
        wf.setframerate(44100)
        wf.writeframes(frames_bytes)
        wf.close()
    #Process(target=loop_a).kill()
    #Process(target=loop_b).kill()

def song_has_started(song_id, artist_name, album_name, song_name):
    print(f"Song has started:.\songs\{song_id} - {song_name} by {artist_name} from {album_name}.wav")
    #pool.submit(rec_start_thread,(f"{song_id} - {song_name} by {artist_name} from {album_name}.wav",))
    rec_start_thread(f".\songs\{song_id} - {song_name} by {artist_name} from {album_name}.wav")

def song_has_ended():
    #global recording_thread
    print("Song has ended.")
    rec_stop()

itunes = win32com.client.Dispatch("iTunes.Application")

chunk = 2048  # Adjust chunk size as needed
fName = None
recording = False
deviceNo = 38

checkThread = threading.Thread(target=checkLoop)
song_id = 0
current_track_data = None

frames = []
for i in range(pyaudio.PyAudio().get_device_count()):
    print(str(i) + ' ' + pyaudio.PyAudio().get_device_info_by_index(i)["name"])
deviceNo = int(input('Enter the index of the desired input device: ').strip() or "38")


checkThread.start()
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
        if recording:
            song_has_ended()
        #time.sleep(5)  # Retry after a delay

stream.stop_stream()
stream.close()
