import numpy as np
import soundfile as sf
from pydub.playback import play
from matplotlib.animation import FuncAnimation
from pydub import AudioSegment
import matplotlib.pyplot as plt

data = np.random.random(1000)

fig=plt.figure()
fig.add_axes()
ax=plt.subplot(1,1,1)

rx=1

wavFile = r"*Path of the wav file*\tjn.wav"

# Retrieve the data from the wav file
data1, samplerate = sf.read(wavFile)

n = len(data1)  # the length of the arrays contained in data
Fs = samplerate  # the sample rate

# Working with stereo audio, there are two channels in the audio data.
# Let's retrieve each channel seperately:
ch1, ch2 = data1.transpose()
data=ch1[0:(int(n/Fs)*Fs)]
#preparing data for reshaping

data = data.reshape(int(n/Fs)*50,int(Fs/50))
#Reshaping data to pass in the imshow() function

print(Fs)
def playing_audio():
    song = AudioSegment.from_wav(wavFile)
    play(song)


def init_func():
    ax.clear()

def update_plot(i):
    ax.clear()
    x=data[i]
    fig=plt.imshow(x.reshape(42,21),aspect='equal',interpolation='nearest')
    #adjust the values of the atrributes of the reshape function for individual audio file
    

    

def req_plot():
    anim = FuncAnimation(fig,update_plot,init_func=init_func,interval=10,frames=int(n/Fs)*50,repeat=False)
    plt.show()
    # anim.save(r'*Path of the file*\filename.mp4', writer='ffmpeg')
    # To save the animation if you wnat to
