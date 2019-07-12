from typing import List


class WaveData:
    """
    A (severely) limited representation of the WAV file format.
    """
    def __init__(self):
        self.data: List[int] = []  # The audio samples
        self.bits_per_sample: int = 16  # The number of bits per audio sample
        self.sample_rate: int = 1  # The number of samples per second

    def add_sample(self, amplitude: int):
        """
        Adds a sample to the audio data.

        :param amplitude:   The signed amplitude of the sample.
        """
        # Make sure the amplitude is within bounds
        if amplitude > self.max_possible_sample_val():
            raise RuntimeError("Sample amplitude of " +
                               str(amplitude) +
                               " is too big for " +
                               str(self.bits_per_sample) +
                               "-bit samples (max = " +
                               str(self.max_possible_sample_val()) +
                               ")")
        elif amplitude < self.min_possible_sample_val():
            raise RuntimeError("Sample amplitude of " +
                               str(amplitude) +
                               " is too small for " +
                               str(self.bits_per_sample) +
                               "-bit samples (min = " +
                               str(self.min_possible_sample_val()) +
                               ")")

        # Add the sample to the data
        self.data.append(amplitude)

    def max_possible_sample_val(self) -> int:
        """
        Gets the maximum value a sample can take.
        """
        return (1 << (self.bits_per_sample - 1)) - 1

    def min_possible_sample_val(self) -> int:
        """
        Gets the minimum value a sample can take.
        """
        return -(1 << (self.bits_per_sample - 1))
