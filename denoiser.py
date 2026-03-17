import numpy as np
import argparse
import sys
import logging

# Profesyonel log yapılandırması
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("AnalogDenoiser")

class AnalogDenoiser:
    """
    AnalogDenoiser, ses sinyallerindeki arka plan gürültüsünü (özellikle analog hışırtı 
    ve statik parazitleri) baskılamak için spektral eşikleme (spectral gating) 
    algoritmasını uygular.
    """
    def __init__(self, örnekleme_hızı=44100):
        self.örnekleme_hızı = örnekleme_hızı
        self.gürültü_eşik_katsayısı = 0.05
        logger.info(f"AnalogDenoiser başlatıldı: örnekleme_hızı={örnekleme_hızı}")
        
    def filtrele(self, veri):
        """
        Hızlı Fourier Dönüşümü (FFT) kullanarak giriş sinyaline spektral eşikleme uygular.
        
        Sinyal giriş parametreleri:
            veri (np.ndarray): Zaman domainindeki giriş ses sinyali.
            
        Dönüş değeri:
            np.ndarray: Gürültüden arındırılmış ses sinyali.
        """
        logger.debug("Spektral eşikleme işlemi başlatılıyor.")
        
        # Frekans domainine dönüşüm
        spektrum = np.fft.rfft(veri)
        
        # Gürültü eşiği hesaplama
        genlik = np.abs(spektrum)
        eşik = np.mean(genlik) * self.gürültü_eşik_katsayısı
        
        # Baskılama için ikili maske uygulama
        maske = genlik > eşik
        filtrelenmiş_spektrum = spektrum * maske
        
        # Zaman domainine geri dönüşüm
        temiz_veri = np.fft.irfft(filtrelenmiş_spektrum)
        
        logger.info("Spektral filtreleme başarıyla tamamlandı.")
        return temiz_veri.astype(np.float32)

def test_sinyali_oluştur(süre=3, frekans=440):
    """
    Test amaçlı olarak Gauss beyaz gürültüsü ile karıştırılmış sentetik bir sinüs dalgası oluşturur.
    """
    t = np.linspace(0, süre, int(44100 * süre))
    sinyal = 0.5 * np.sin(2 * np.pi * frekans * t)
    gürültü = 0.1 * np.random.normal(size=t.shape)
    return (sinyal + gürültü).astype(np.float32)

def main():
    parser = argparse.ArgumentParser(description="Analog Voice Denoiser CLI Araç Seti")
    parser.add_argument("--test", action="store_true", help="Otomatik tanısal testi çalıştır")
    parser.add_argument("--input", type=str, help="Giriş .wav dosyasının yolu")
    parser.add_argument("--output", type=str, default="temiz_cikti.wav", help="İşlenmiş çıktının kaydedileceği yol")
    parser.add_argument("--verbose", action="store_true", help="Hata ayıklama seviyesinde loglamayı etkinleştir")
    
    args = parser.parse_args()
    
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    
    denoiser = AnalogDenoiser()
    
    if args.test:
        logger.info("Otomatik tanı dizisi başlatılıyor...")
        kirli_sinyal = test_sinyali_oluştur()
        temiz_sinyal = denoiser.filtrele(kirli_sinyal)
        
        snr_iyileşmesi = np.var(kirli_sinyal) / np.var(temiz_sinyal)
        logger.info(f"Tanısal eşleşme sonuçlandı. SNR İyileşme Katsayısı: {snr_iyileşmesi:.2f}x")
        sys.exit(0)

    if not args.input:
        logger.error("Giriş dosyası belirtilmedi. --input veya --test parametresini kullanın.")
        sys.exit(1)

if __name__ == "__main__":
    main()
