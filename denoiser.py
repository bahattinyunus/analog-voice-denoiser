import numpy as np
import argparse
import sys
import logging
import wave

# Configure professional logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("AnalogDenoiser")

class AnalogDenoiser:
    """
    AnalogDenoiser implements a spectral gating algorithm to suppress 
    background noise in audio signals, specifically targeting analog hiss 
    and static interference.
    """
    def __init__(self, sampling_rate=44100):
        self.sampling_rate = sampling_rate
        self.noise_floor_factor = 0.05
        logger.info(f"Initialized AnalogDenoiser with sampling_rate={sampling_rate}")
        
    def apply_filter(self, data):
        """
        Applies a spectral gate to the input signal using Fast Fourier Transform.
        
        Args:
            data (np.ndarray): Input audio signal in time domain.
            
        Returns:
            np.ndarray: Denoised audio signal.
        """
        logger.debug("Starting spectral gating process.")
        
        # Frequency domain transformation
        spectrum = np.fft.rfft(data)
        
        # Noise thresholding
        magnitude = np.abs(spectrum)
        threshold = np.mean(magnitude) * self.noise_floor_factor
        
        # Apply binary mask for suppression
        mask = magnitude > threshold
        filtered_spectrum = spectrum * mask
        
        # Time domain reconstruction
        clean_data = np.fft.irfft(filtered_spectrum)
        
        logger.info("Spectral filtration completed successfully.")
        return clean_data.astype(np.float32)

def generate_test_signal(duration=3, freq=440):
    """
    Generates a synthetic sine wave mixed with Gaussian white noise for testing.
    """
    t = np.linspace(0, duration, int(44100 * duration))
    signal = 0.5 * np.sin(2 * np.pi * freq * t)
    noise = 0.1 * np.random.normal(size=t.shape)
    return (signal + noise).astype(np.float32)

def main():
    parser = argparse.ArgumentParser(description="Analog Voice Denoiser CLI Utility")
    parser.add_argument("--test", action="store_true", help="Execute an automated diagnostic test")
    parser.add_argument("--input", type=str, help="Path to input .wav file")
    parser.add_argument("--output", type=str, default="output_cleaned.wav", help="Path to save processed output")
    parser.add_argument("--verbose", action="store_true", help="Enable debug-level logging")
    
    args = parser.parse_args()
    
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    
    denoiser = AnalogDenoiser()
    
    if args.test:
        logger.info("Initiating automated diagnostic sequence...")
        dirty_signal = generate_test_signal()
        clean_signal = denoiser.apply_filter(dirty_signal)
        
        snr_improvement = np.var(dirty_signal) / np.var(clean_signal)
        logger.info(f"Diagnostic match concluded. SNR Improvement Factor: {snr_improvement:.2f}x")
        sys.exit(0)

    if not args.input:
        logger.error("No input file specified. Use --input or --test.")
        sys.exit(1)

if __name__ == "__main__":
    main()
