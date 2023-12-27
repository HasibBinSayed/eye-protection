from gtts import gTTS
import tkinter as tk
from tkinter import filedialog

def text_to_mp3():
    text = text_entry.get("1.0", "end-1c")  # Retrieve text from the input field
    filename = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
    if text and filename:  # Check if text and filename are provided
        tts = gTTS(text=text, lang='en')  # Create a gTTS object
        tts.save(filename)  # Save the generated speech as an MP3 file
        status_label.config(text=f"Text converted to MP3. Saved as '{filename}'")
    else:
        status_label.config(text="Please provide text and choose a filename!")

# Create the main window
root = tk.Tk()
root.title("Text to MP3 Converter")

# Text input field
text_label = tk.Label(root, text="Enter the text:")
text_label.pack()
text_entry = tk.Text(root, height=10, width=50)
text_entry.pack()

# Button to convert text to MP3
convert_button = tk.Button(root, text="Convert to MP3", command=text_to_mp3)
convert_button.pack()

# Status label to display conversion status
status_label = tk.Label(root, text="")
status_label.pack()

# Run the GUI
root.mainloop()
