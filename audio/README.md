# Audio Feature Extraction and Prediction

This function include how do we extract audio feature from .wav file and how do we apply machine learning model to predict teaching material quality.

# Audio Database We Use

Our learning data comes from  SAVEE Database, which provides labeled audio data for academic use.

# What We Have Done:

We use some open-source emotion database, collect labeled data, use statistical methods to extract features, and train a machine learning mdoel to predict emotion for audio files. The predicted scores and predicted emotion changes will be used as a part of measurement for teaching material quality judgement.



# Preprocessing and Training stage on Open-source Material

## Introduction to SAVEE Database

1. Speakers: 'DC', 'JE', 'JK' and 'KL' are four male speakers recorded for the SAVEE database

2. Audio data: Audio files consist of audio WAV files sampled at 44.1 kHz. There are 15 sentences for each of the 7 emotion categories. The initial letter(s) of the file name represents the emotion class, and the following digits represent the sentence number. The letters 'a', 'd', 'f', 'h', 'n', 'sa' and 'su' represent 'anger', 'disgust', 'fear', 'happiness', 'neutral', 'sadness' and 'surprise' emotion classes respectively. 


Since we only focus on emotion variance, we only use 'n' for neutral with labeled -1, 'a' ,'su' and 'h' with labeled +1 represent no emotion and rich emotion.

## What You Need to Install

1.  

## Preprocessing and Feature Engineering

1. FFT

```python
  rate, data = wav.read(dir_temp_read)
  # Fast fft transfer
  fft_out = fft(data)
  abs_signal = np.abs(fft_out)
```

2. Limit frequency range from 20 to 20000

```python
  abs_signal = abs_signal[19:19999]
```
