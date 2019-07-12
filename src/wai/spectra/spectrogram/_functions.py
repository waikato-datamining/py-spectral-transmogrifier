from typing import Optional, Tuple, List

import numpy as np
from pyAudioAnalysis import audioFeatureExtraction as aFEx
import png

from wai.keras.file.spec.Spectrum import Spectrum
from ._WaveData import WaveData


def spectrum_to_wave(spectrum: Spectrum, out: Optional[WaveData] = None) -> WaveData:
    """
    Converts the given spectrum into an audio WAV.

    :param spectrum:    The spectrum to convert.
    :param out:         If supplied, the spectrum is appended to this,
                        otherwise a new WAV is created.
    :return:            The resulting WAV data.
    """
    # Use a default WAV if none is provided
    if out is None:
        out = WaveData()

    # Get the maximum-allowed sample value
    max_val: int = out.max_possible_sample_val()

    # Get the normalisation constant
    norm: float = spectrum.max_amplitude.amplitude

    # Convert each spectral sample into an audio sample
    for point in spectrum.points:
        # Normalise the sample amplitude
        amp = point.amplitude / norm

        # Convert to audio foramt
        sample: int = int(max_val * amp)

        # Add to the WAV
        out.add_sample(sample)

    return out


def wave_to_spectrogram(wav: WaveData, window_size, window_step) -> np.ndarray:
    """
    Converts the given WAV data into a spectrogram.

    :param wav:                 The WAV data to convert.
    :param window_size:         The width of the sampling window in samples.
    :param window_step:         The step the sampling window takes between FFTs.
    :return:                    A spectrogram.
    """
    # Convert the WAV data in a Numpy array
    wav_array: np.ndarray = np.array(wav.data)

    # Get the spectrogram using pyAudioAnalysis
    return aFEx.stSpectogram(wav_array, 1, window_size, window_step, False)[0]


def logarithmically_normalise_spectrogram(spectrogram: np.ndarray) -> np.ndarray:
    """
    Returns the normalised logarithm of the given spectrogram.

    :param spectrogram:     The spectrogram to normalise.
    :return:                The normalised spectrogram.
    """
    # Get the min and max components from the spectrogram
    max_ampl = np.max(spectrogram)
    min_ampl = np.min(spectrogram)

    # Logarithmically scale and return the spectrogram
    return np.log10(spectrogram / min_ampl) / np.log10(max_ampl / min_ampl)


def save_spectrogram(filename: str, spectrogram: np.ndarray, palette: List[Tuple[int, int, int]]):
    """
    Saves the spectrogram as a PNG image.

    :param filename:        The name to save the spectrogram under.
    :param spectrogram:     The spectrogram to save.
    :param palette:         List of RGB triples to use to encode amplitudes
                            in the spectrum as colour.
    """
    # Add the PNG extension
    if not filename.endswith(".png"):
        filename += ".png"

    # Convert the spectrogram to a palette index table
    max_index: int = len(palette) - 1
    spectrogram: np.ndarray = spectrogram * max_index
    spectrogram = spectrogram.astype(np.int)

    # Transpose the spectrogram so time is on the horizontal axis
    spectrogram = spectrogram.transpose()

    # Convert the spectrum into the expected PNG format
    spectrogram_index_list: List[List[int]] = list(spectrogram.tolist())
    spectrogram_list: List[List[int]] = []
    for index_row in spectrogram_index_list:
        row: List[int] = []
        for palette_index in index_row:
            row += list(palette[palette_index])
        spectrogram_list.append(row)

    # Create a PNG writer
    png_writer: png.Writer = png.Writer(len(spectrogram_list[0]) // 3, len(spectrogram_list))

    # Open the file for writing
    with open(filename, 'wb') as file:
        png_writer.write(file, reversed(spectrogram_list))
