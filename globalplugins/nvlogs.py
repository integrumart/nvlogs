import os
import shutil
import datetime
import globalVars
import addonHandler

# Eklenti çeviri desteği (gerekli durumlar için)
addonHandler.initTranslation()

def save_nvda_log():
    """NVDA log dosyasını Belgelerim altına kopyalar."""
    try:
        # 1. Hedef klasörü oluştur (Belgelerim/nvlogs_logs_nvda)
        documents_path = os.path.join(os.path.expanduser("~"), "Documents")
        target_dir = os.path.join(documents_path, "nvlogs_logs_nvda")
        
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        
        # 2. NVDA'nın o an kullandığı aktif log dosyasını tespit et
        # globalVars üzerinden mevcut log dosyasının yolunu alıyoruz
        log_file_source = getattr(globalVars.appArgs, "logFileName", None)
        
        # Eğer yukarıdaki yöntem boş dönerse (nadiren), geçici klasöre bak
        if not log_file_source or not os.path.exists(log_file_source):
            temp_log = os.path.join(os.environ.get('TEMP', ''), 'nvda.log')
            if os.path.exists(temp_log):
                log_file_source = temp_log

        # 3. Eğer log dosyası bulunduysa kopyalama işlemini yap
        if log_file_source and os.path.exists(log_file_source):
            # Dosya adını tarih ve saatle oluştur (Sıralama için Yıl-Ay-Gün)
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            target_file_name = f"nvda_log_{timestamp}.log"
            target_path = os.path.join(target_dir, target_file_name)
            
            # shutil.copy2 kullanarak meta verileriyle (zaman damgası vb.) kopyala
            shutil.copy2(log_file_source, target_path)
            
    except Exception:
        # Kullanıcıyı rahatsız etmemek için hataları arka planda yutuyoruz
        pass

# NVDA eklentiyi yüklediğinde (veya her yeniden başladığında) fonksiyonu çalıştır
save_nvda_log()

class AddonStore(addonHandler.Addon):
    def __init__(self):
        super().__init__()