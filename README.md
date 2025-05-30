YouTube Downloader GUI (yt-dlp)

A simple GUI application for downloading YouTube videos and audio using the powerful yt-dlp backend. Built with Python and Tkinter, this tool allows users to download content in MP4, MP3, or M4A formats with a friendly graphical interface.
Features

    Download videos in the best available quality.

    Extract audio in MP3 (192kbps) or M4A format.

    Live download progress bar and status display.

    Option to choose your download folder.

    Automatically handles merging, format conversion, and naming.

Requirements

    Python 3.6+

    yt-dlp Python package
    
Install with:

    pip install yt-dlp

FFmpeg (required for audio conversion and video merging)
Install via Chocolatey (used in this script):

    choco install ffmpeg

Setup

    Clone or download this repository.

    Ensure ffmpeg is installed to:
    C:\ProgramData\chocolatey\lib\ffmpeg\tools\ffmpeg\bin
    (or change the ffmpeg_path in the script accordingly).

Run the script:

    python youtube_downloader_gui.py

Usage

    Paste a YouTube video URL into the entry field.

    Choose a download format:

        Video: best quality MP4 (video + audio merged)

        Audio (MP3): audio-only, converted to MP3

        Audio (M4A): downloads the audio in M4A format without conversion

    Click "Choose Folder" to select your download location.

    Click "Download" to start the download process.

    Watch the progress bar and wait for the success message.

Notes

    The program disables overwriting existing files.

    Playlist downloads are disabled for simplicity.

    Filenames are sanitized for Windows compatibility.

    Certificate checking is disabled to help users behind restrictive networks (e.g., school/work).

Troubleshooting

    If you see an error about FFmpeg, verify the path to the ffmpeg binary.

    For SSL or certificate errors, make sure your Python and yt-dlp are updated.

    Use the console output (run from terminal) for full traceback/debug information.

License

This project is released under the MIT License. Feel free to use and modify it.
