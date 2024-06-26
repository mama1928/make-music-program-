import winsound
import random
import numpy as np
from scipy import signal

ERROR_SOUNDS = [0x10, 0x30, 0x40, 0x50, 0x60, 0x70]

DURATIONS = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

def select_sound():
    return random.choice(ERROR_SOUNDS), random.choice(DURATIONS)

def modify_sound(frequency):
    return int(frequency * random.uniform(0.9, 1.1))

def play_sound(sound_id, duration):
    winsound.PlaySound(f"SystemHand", winsound.SND_ALIAS)
    winsound.Beep(440, 50)
    winsound.PlaySound(f"SystemDefault{sound_id}", winsound.SND_ALIAS)
    winsound.Sleep(duration)
    winsound.PlaySound(f"SystemHand", winsound.SND_ALIAS)
    winsound.Beep(880, 50)

sampling_freq = 44100
note_length = 0.25

t = np.linspace(0, note_length, int(note_length * sampling_freq), endpoint=False)
samples = np.concatenate([signal.square(2 * np.pi * f * t) for f in range(100, 8000, 100)])

def generate_melody():
    MELODY_PATTERN = [440, 523, 659, 784, 880, 988, 1047]
    return random.choice(MELODY_PATTERN)

def generate_rhythm():
    RHYTHM_PATTERN = [0.25, 0.5, 0.75, 1.0]
    return random.choice(RHYTHM_PATTERN)

song = []
for i in range(8):
    part_melody = []
    part_rhythm = []
    for j in range(32):
        sound_id, duration = select_sound()
        play_sound(sound_id, duration)
        
        melody = generate_melody()
        rhythm = generate_rhythm()
        part_melody.append(melody)
        part_rhythm.append(rhythm)

    for k in range(len(part_melody)):
        melody = part_melody[k]
        rhythm = part_rhythm[k]
        segment = samples[int(melody * sampling_freq * note_length):int((melody + rhythm) * sampling_freq * note_length)]
        song.extend(segment)

winsound.PlaySound(bytes(np.int16(song)), winsound.SND_ASYNC)
