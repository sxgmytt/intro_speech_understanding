import numpy as np

def waveform_to_frames(waveform, frame_length, step):
    """
    Chop a waveform into overlapping frames.

    @params:
    waveform (np.ndarray(N)) - the waveform
    frame_length (scalar) - length of the frame, in samples
    step (scalar) - step size, in samples

    @returns:
    frames (np.ndarray((frame_length, num_frames))) - waveform chopped into frames

    num_frames should be at least int((len(speech)-frame_length)/step); it may be longer.
    For every n and t such that 0 <= t*step+n <= N-1, it should be the case that 
       frames[n,t] = waveform[t*step+n]
    """
    N = len(waveform)
    num_frames = int((N - frame_length) / step) + 1

    frames = np.zeros((frame_length, num_frames))

    for t in range(num_frames):
        start = t * step
        end = start + frame_length
        frames[:, t] = waveform[start:end]

    return frames
def frames_to_stft(frames):
    """
    Take the FFT of every column of the frames matrix.

    @params:
    frames (np.ndarray((frame_length, num_frames))) - the speech samples (real-valued)

    @returns:
    stft (np.ndarray((frame_length, num_frames)), dtype=np.complex128) - the STFT (complex-valued)
    """
    frame_length, num_frames = frames.shape
    stft = np.zeros((frame_length, num_frames), dtype=np.complex128)

    for t in range(num_frames):
        stft[:, t] = np.fft.fft(frames[:, t])

    return stft

def stft_to_spectrogram(stft):
    magnitude = np.abs(stft)

    spectrogram = 20 * np.log10(magnitude)

    spectrogram = np.clip(spectrogram, a_min=-60, a_max=None)

    return spectrogram

