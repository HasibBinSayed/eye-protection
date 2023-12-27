from gtts import gTTS
import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment  # Import AudioSegment from pydub

def text_to_wav():
    text = text_entry.get("1.0", "end-1c")  # Retrieve text from the input field
    filename = filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("WAV files", "*.wav")])
    if text and filename:  # Check if text and filename are provided
        tts = gTTS(text=text, lang='en')  # Create a gTTS object
        tts.save("temp.mp3")  # Save the generated speech as a temporary MP3 file
        sound = AudioSegment.from_mp3("temp.mp3")  # Load the temporary MP3 file
        sound.export(filename, format="wav")  # Save the converted WAV file
        status_label.config(text=f"Text converted to WAV. Saved as '{filename}'")
    else:
        status_label.config(text="Please provide text and choose a filename!")

# Create the main window
root = tk.Tk()
root.title("Text to WAV Converter")

# Text input field
text_label = tk.Label(root, text="Enter the text:")
text_label.pack()
text_entry = tk.Text(root, height=10, width=50)
text_entry.pack()

# Button to convert text to WAV
convert_button = tk.Button(root, text="Convert to WAV", command=text_to_wav)
convert_button.pack()

# Status label to display conversion status
status_label = tk.Label(root, text="")
status_label.pack()

# Run the GUI
root.mainloop()
