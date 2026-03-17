<p align="center">
  <img src="assets/signal_analysis.png" width="800" alt="Analog Voice Denoiser Görsel Analiz">
</p>

# Analog Voice Denoiser (AVD)

[![Lisans: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Durum: Araştırma](https://img.shields.io/badge/Durum-Ara%C5%9Ft%C4%B1rma-orange.svg)]()

**Analog Voice Denoiser (AVD)**, ses kayıtlarındaki spektral gürültüyü, statik paraziti ve analog hışırtıyı nötralize etmek için tasarlanmış yüksek sadakatli bir ses işleme aracıdır. Gelişmiş Spektral Eşikleme (Spectral Gating) algoritmalarını kullanan AVD, gürültü tabanını cerrahi bir hassasiyetle bastırırken insan vokal frekanslarını izole eder.

---

## 🔬 Temel Metodoloji

AVD, hassas sinyal manipülasyonu sağlamak için frekans domaininde çalışır. Süreç titiz bir boru hattını takip eder:

1.  **Hızlı Fourier Dönüşümü (FFT):** Zaman domainindeki sesin kurucu frekans bileşenlerine ayrıştırılması.
2.  **Spektral Analiz:** İstatistiksel varyans kestirimi kullanarak dinamik gürültü tabanının gerçek zamanlı hesaplanması.
3.  **İkili Eşikleme (Binary Gating):** Arka plan gürültüsüyle ilişkili düşük enerjili frekans bölmelerini filtreleyen tahribatsız bir maske uygulaması.
4.  **Ters FFT:** Temizlenmiş sinyalin yüksek sadakatli çıktı için zaman domainine geri dönüştürülmesi.

## 🌟 Öne Çıkan Özellikler

- **Gelişmiş Spektral Eşikleme:** Minimum faz distorsiyonu ile hassas gürültü bastırma.
- **Dinamik Eşikleme:** Değişen kayıt ortamlarına uyum sağlayan adaptif gürültü tabanı algılama.
- **Profesyonel Türkçe Dokümantasyon:** Teknik standartlara uygun, tamamen Türkçe içerik.
- **Entegre Görselleştirici:** Gerçek zamanlı spektral izleme için profesyonel düzeyde kontrol paneli.

## 📊 Analitik Kontrol Paneli

Proje, gürültü giderme performansını, SNR (Sinyal-Gürültü Oranı) iyileştirmelerini ve sistem gecikmesini izlemek için premium bir görsel arayüz sunan `DASHBOARD.html` dosyasını içerir. Modern web teknolojilerini kullanarak yüksek kaliteli bir ses mühendisliği iş istasyonunu simüle eder.

## 🛠 Kurulum ve Kullanım

### Gereksinimler
- Python 3.8 veya üzeri
- NumPy

### Hızlı Başlangıç
```bash
# Depoyu klonlayın
git clone https://github.com/bahattinyunus/analog-voice-denoiser.git
cd analog-voice-denoiser

# Bağımlılıkları yükleyin
pip install -r requirements.txt

# Tanısal testi çalıştırın
python denoiser.py --test
```

### CLI Seçenekleri
```bash
python denoiser.py --input <giriş.wav> --output <çıkış.wav> --verbose
```

## 🗺 Yol Haritası

- [x] **Aşama I:** Spektral eşikleme motoru uygulaması.
- [x] **Aşama II:** Profesyonel UI/Dashboard mimarisi.
- [ ] **Aşama III:** Gerçek zamanlı akış işleme desteği (ASIO/CoreAudio).
- [ ] **Aşama IV:** Akıllı gürültü profili kestirimi için sinir ağları.

## 📜 Lisans

MIT Lisansı altında dağıtılmaktadır. Daha fazla bilgi için `LICENSE` dosyasına bakın.

---

<p align="right">
  <i>Profesyonel sinyal bütünlüğü ve vokal netliği için tasarlandı.</i>
</p>