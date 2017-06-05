from scipy.io import wavfile as wav
from scipy.fftpack import fft
import numpy as np
import os

# Define root directory.
# All audio files are stored in this directory (or subdirectory)
#root_dir = '/disk02/data/eLearning/AudioAnalysis/Sample/AudioData'
root_dir = '/disk02/data/eLearning/AudioAnalysis/newchannel'
# List all the file and subdirectory name
path_factor = os.listdir('/disk02/data/eLearning/AudioAnalysis/newchannel')

count = 0

with open("/disk02/data/eLearning/AudioAnalysis/newchannel/resultv3.txt", "w+") as f:
    
    for i in range(0,len(path_factor)):
        
        # If it is a subdir
        if os.path.isdir(os.path.join(root_dir,path_factor[i])):
            # Combine dir
            print os.path.join(root_dir,path_factor[i])
            dir_temp = os.path.join(root_dir,path_factor[i])
            for directory, subdirectories, files in os.walk(dir_temp):
                for file in files:
                    f_name = os.path.splitext(file)
                    ## split file name and ".wav"
                    file_name = filter(str.isalpha, f_name[0])
                    if (file_name == 'n') or (file_name =='h') or (file_name =='su') or (file_name =='a'):
                        # Combine dir
                        dir_temp_read = os.path.join(dir_temp,file)
                        print dir_temp_read
                        # Read wav file
                        rate, data = wav.read(dir_temp_read)
                        # Fast fft transfer
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
                        ## Get label
                        if file_name =='n':
                            #   feature_line.append(filter(str.isalpha, f_name[0]))
                            feature_line.append(-1)
                        elif file_name =='a' or file_name =='su' or file_name =='h':
                            feature_line.append(1)
                        print file_name
                        f.writelines([str(line) + "\t" for line in feature_line])
                        #f.writelines("\n")
                        count = count + 1
                        print count
#print feature_line
f.close()
