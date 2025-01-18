# Create list_midi_files.py
import os
import json

# Directory containing MIDI files
midi_dir = "my_midi"

# Get all MIDI files recursively
midi_files = []
for root, dirs, files in os.walk(midi_dir):
    for file in files:
        if file.endswith(('.mid', '.midi', '.MID', '.MIDI')):
            # Get the full path to the MIDI file
            full_path = os.path.join(root, file)
            # Create the JSON object for this file
            midi_files.append({"name": full_path})

# Write to JSON file
with open('all_files_list_random.json', 'w') as f:
    for midi_file in midi_files:
        json.dump(midi_file, f)
        f.write('\n')

print(f"Found {len(midi_files)} MIDI files")