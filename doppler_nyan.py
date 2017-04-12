
import soundfile as sf
import numpy as np

duration = 10
offset = 30.5

sig, samplerate = sf.read('nyancat.wav')
subsig = sig[samplerate*offset:samplerate*(offset+duration), :]

offset_distance = 3 # [m]
sound_speed = 340.29 # [m/s]
speed_cat = 30 # [m/s]

t = np.arange(0, duration, 1.0/samplerate)
radial_distance = np.sqrt(offset_distance**2 + (speed_cat*(t-duration/2))**2)

nyan_t = t - radial_distance/sound_speed;

nyan_sound = np.array([np.interp(nyan_t, t, subsig[:, 0]), np.interp(nyan_t, t, subsig[:, 1])])
nyan_sound = np.transpose(nyan_sound)
nyan_sound = offset_distance/np.transpose(np.tile(radial_distance, (2,1))) * nyan_sound

# Write output
sf.write('nyan_doppler.wav', nyan_sound, samplerate)