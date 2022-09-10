from scipy import signal
from scipy.io import wavfile
from matplotlib import pyplot as plt
import numpy as np
import io
from PIL import Image

# open .wav audio file
rate, audio = wavfile.read('./input.wav')

# convert to mono
audio = np.mean(audio, axis=1)

# apply FFT
freqs, times, Sx = signal.spectrogram(audio, fs=rate, window='hann', 
                                      nperseg=1024, noverlap=100,
                                      detrend=False, scaling='spectrum')

# switch off interactive mode and axis
plt.ioff()
plt.axis('off')

# render and save image as .png
plt.pcolormesh(10 * np.log10(Sx))
img_buf = io.BytesIO()
plt.savefig(img_buf, bbox_inches='tight', pad_inches = 0, format='png')
im = Image.open(img_buf).save('output.png')
