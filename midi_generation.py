import mido
from mido import MidiFile, MidiTrack, Message, MetaMessage

def notes_to_midi(notes, output_file='output.mid', tempo=50000):
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    # Add tempo meta message
    track.append(MetaMessage('set_tempo', tempo=tempo))

    ticks_per_beat = mid.ticks_per_beat

    for note in notes:
        note_number, duration = note
        ticks = int((duration * ticks_per_beat) / (tempo / 1000000))
        track.append(Message('note_on', note=note_number, velocity=64, time=0))
        track.append(Message('note_off', note=note_number, velocity=64, time=ticks))

    mid.save(output_file)
    print(f"MIDI file saved as {output_file}")