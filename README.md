# Convert Whisper Output (VTT) to SRT Format

OpenAI's Whisper model is extremely effective at transcribing and translating audio. However, Whisper's output is in VTT file format. This is a simple Python script that converts outputs from Whisper into .srt format so that transcriptions can be used as video subtitles. 

To use the program:

1. Make sure you have Python installed. 
2. Open a Terminal window and navigate to the directory where the convert_whisper_to_srt.py file is saved.
3. Type into terminal ```convert_whisper_to_srt.py <path-to-whisper-output> <output-file-name>```, replacing <path-to-whisper-output> with the path to the Whisper output you wish to convert, and replacing <output-file-name> with your preferred output filename. 

NOTE: This only works with audio files less than 60 minutes long. 