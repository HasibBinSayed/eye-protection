# MP3 Playback Program Setup Guide

1. **Install Libraries:**
   - Ensure Python is installed and run:
     ```bash
     pip install -r requirements.txt
     ```

2. **Prepare Python Script:**
   - Copy the script to a `.py` file (e.g., `mp3_player.py`).

3. **Download MP3 File:**
   - Place the desired MP3 file in the script's directory, named "sound.mp3".

4. **Run the Script:**
   - Execute the script with `python mp3_player.py`.

## Task Scheduler Setup

1. **Open Task Scheduler:**
   - Press `Win + R`, type `taskschd.msc`, and press Enter.

2. **Create a New Task:**
   - Name it (e.g., "MP3 Player Task").

3. **Set Trigger:**
   - Choose when the task starts (e.g., "At log on").
   - Repeat every 20 minutes.

4. **Configure Action:**
   - Use Python (`python.exe`) as the program.
   - Set script path as the argument (`mp3_player.py`).
   - Start in the script's directory.

5. **Adjust Settings:**
   - Configure additional conditions or notifications as needed.

6. **Testing and Saving:**
   - Test the task to ensure it works as expected.
   - Save the task.

### Note:
Press "Shift + L" to stop playback as specified in the script.

This setup plays the MP3 file and stops it after 20 minutes. Customize settings as required.
