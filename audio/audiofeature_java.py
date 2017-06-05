from scipy.io import wavfile as wav
from scipy.fftpack import fft
import numpy as np
import os

# Define root directory.
# All audio files are stored in this directory (or subdirectory)
#root_dir = '/disk02/data/eLearning/AudioAnalysis/Sample/AudioData'
root_dir = '/disk02/data/eLearning/raw_teaching_material/Java_audio_channel/split/'
# List all the file and subdirectory name
path_factor = os.listdir('/disk02/data/eLearning/AudioAnalysis/newchannel')



with open("/disk02/data/eLearning/AudioAnalysis/newchannel/result_java.txt", "w+") as f:
    
    for directory, subdirectories, files in os.walk(root_dir):
        for file in files:
            #print file
            rate, data = wav.read(root_dir+"/"+file)
            if file.endswith(".wav"):
                feature_line = []
                feature_line.append(file)
                # Fast fft transfer
                #print len(data)
                if len(data) == 0:
                    continue
                fft_out = fft(data)
                abs_signal = np.abs(fft_out)
                abs_signal = abs_signal[19:19999]
                #print np.mean(abs_signal)
                feature_line = []
                # Compute feature
                # Feature 1 Mean
                feature_line.append(np.mean(abs_signal))
                # Feature 2 Median
                feature_line.append(np.median(abs_signal))
                
                feature_line.append(np.ptp(abs_signal))
                feature_line.append(np.var(abs_signal))
                feature_line.append(np.std(abs_signal))
                feature_line.append(np.mean(abs_signal) / np.std(abs_signal))
                feature_line.append(np.percentile(abs_signal, 25))
                feature_line.append(np.percentile(abs_signal, 50))
                feature_line.append(np.percentile(abs_signal, 75))
                feature_line.append(np.max(abs_signal))
                feature_line.append(np.min(abs_signal))
                feature_line.append(np.max(abs_signal) - np.min(abs_signal))
                feature_line.append(file)
                f.writelines([str(line) + "\t" for line in feature_line])
            #f.writelines("\n")
            
            print "Finish processing file", file

f.close()
