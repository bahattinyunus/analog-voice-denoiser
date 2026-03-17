<p align="center">
  <img src="assets/signal_analysis.png" width="800" alt="Analog Voice Denoiser Visual Analysis">
</p>

# Analog Voice Denoiser (AVD)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Status: Research](https://img.shields.io/badge/Status-Research-orange.svg)]()

**Analog Voice Denoiser (AVD)** is a high-fidelity audio processing utility designed to neutralize spectral noise, static interference, and analog hiss from voice recordings. Utilizing advanced Spectral Gating algorithms, AVD isolates human vocal frequencies while surgically suppressing the underlying noise floor.

---

## 🔬 Core Methodology

AVD operates in the frequency domain to ensure precise signal manipulation. The process follows a rigorous pipeline:

1.  **Fast Fourier Transform (FFT):** Decomposition of time-domain audio into constitutive frequency components.
2.  **Spectral Analysis:** Real-time calculation of the dynamic noise floor using statistical variance estimation.
3.  **Binary Gating:** Application of a non-destructive mask that filters out low-energy frequency bins associated with background noise.
4.  **Inverse FFT:** Reconstruction of the cleaned signal back into the time domain for high-fidelity output.

## 🌟 Key Features

- **Advanced Spectral Gating:** Precision-engineered noise suppression with minimal phase distortion.
- **Dynamic Thresholding:** Adaptive noise floor detection that adjusts to varying recording environments.
- **English/Professional Standard:** Fully documented in English for global accessibility and collaboration.
- **Integrated Visualizer:** Professional-grade dashboard for real-time spectral monitoring.

## 📊 Analytics Dashboard

The project includes a `DASHBOARD.html` file, providing a premium visual interface for monitoring denoising performance, SNR (Signal-to-Noise Ratio) improvements, and system latency. It utilizes modern web technologies to simulate a high-end audio engineering workstation.

## 🛠 Installation & Usage

### Prerequisites
- Python 3.8 or higher
- NumPy

### Quick Start
```bash
# Clone the repository
git clone https://github.com/bahattinyunus/analog-voice-denoiser.git
cd analog-voice-denoiser

# Install dependencies
pip install -r requirements.txt

# Run diagnostic test
python denoiser.py --test
```

### CLI Options
```bash
python denoiser.py --input <input.wav> --output <output.wav> --verbose
```

## 🗺 Roadmap

- [x] **Phase I:** Spectral gating engine implementation.
- [x] **Phase II:** Professional UI/Dashboard architecture.
- [ ] **Phase III:** Real-time stream processing support (ASIO/CoreAudio).
- [ ] **Phase IV:** Neural networks for intelligent noise profile estimation.

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---

<p align="right">
  <i>Engineered for professional signal integrity and vocal clarity.</i>
</p>