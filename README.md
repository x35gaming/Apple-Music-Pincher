# Apple-Music-Pincher: Record iTunes songs on the fly
Tired of DRM restrictions preventing you from saving your favorite iTunes tracks? Apple-Music-Pincher cracks the code (sort of) by playing and then recording your music, ensuring you have a high-quality, DRM-free copy in no time.

This Python script is a lifesaver for music lovers who:

- Want to listen to their iTunes library offline
- Build their own personal music collection
- Share tunes with friends without copyright hassles
## How it works:

- Monitor iTunes: Apple-Music-Pincher keeps an eye on your currently playing track in iTunes.
- Song change detected: When a new song starts, the script grabs its metadata like artist, title, and album.
- Automatic recording: Based on your preferences, the script starts recording the new song.
- Smart file saving: The recording is saved as a high-quality WAV file with a filename based on the song's metadata.
- Seamlessly repeat: As you listen to your music, the script automatically captures each new song without manual intervention.
## Features:

- Automatic song detection and recording
- Customizable filename format based on song metadata
- Multi-threaded recording for smooth performance
- Error handling and feedback for a user-friendly experience
## Getting started:

- Install Python and PyAudio library.
- Download the Apple-Music-Pincher script.
- Configure your preferred audio input device and chunk size.
- turn off system sounds or you'll be having a bad day...
- run `python .\AppleMusicPincher.py`
- wait about 8 hours...
## Additional notes:

- This script currently works on Windows only.
- DRM removal is achieved through playback and recording, not directly tampering with iTunes files.
- Consider the legality of recording copyrighted material in your region.
