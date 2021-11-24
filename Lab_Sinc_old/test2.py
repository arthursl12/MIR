# Pega a lista de músicas da pasta mp3s
import os
import librosa
from fastdtw import fastdtw
import scipy.spatial as ss

mp3s = []
for filename in os.listdir("mp3s/"):
    if filename.endswith(".mp3"): 
        mp3s.append(filename)
        continue
    else:
        continue
    
# Get recent version for comparison
recent_idx = mp3s.index('Tony Bennett, Amy Winehouse - Body and Soul (from Duets II - The Great Performances)-_OFMkCeP6ok.mp3')
recent = mp3s[recent_idx]
mp3s.remove('Tony Bennett, Amy Winehouse - Body and Soul (from Duets II - The Great Performances)-_OFMkCeP6ok.mp3')
mp3s

def similarity(music1, music2):
    wave1, sr = librosa.load(music1, duration=15)
    chroma1 = librosa.feature.chroma_cens(wave1, sr=sr)
    
    wave2, sr = librosa.load(music2, duration=15)
    chroma2 = librosa.feature.chroma_cens(wave2, sr=sr)
    
    distance, path = fastdtw(chroma1.T, chroma2.T, dist=ss.distance.cosine)
    return distance,path

directory = 'mp3s/'
music1 = directory + 'Tony Bennett, Amy Winehouse - Body and Soul (from Duets II - The Great Performances)-_OFMkCeP6ok.mp3'
music2 = directory + mp3s[1]

similarity(music1, music2)