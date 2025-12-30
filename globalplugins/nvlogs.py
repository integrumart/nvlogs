import os
import shutil
import datetime
import globalVars
import addonHandler
import globalPluginHandler

# 1. Uluslararası Dil Desteğini Başlat (Joseph'in 3. maddesi için)
addonHandler.initTranslation()
_ = addonHandler.getTranslation()

def save_nvda_log():
    """NVDA log dosyasını Belgelerim altına kopyalar."""
    try:
        # Hedef klasör (Belgelerim/nvlogs_logs_nvda)
        documents_path = os.path.join(os.path.expanduser("~"), "Documents")
        target_dir = os.path.join(documents_path, "nvlogs_logs_nvda")
        
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        
        # NVDA'nın o an kullandığı aktif log dosyasını tespit et
        log_file_source = getattr(globalVars.appArgs, "logFileName", None)
        
        if not log_file_source or not os.path.exists(log_file_source):
            temp_log = os.path.join(os.environ.get('TEMP', ''), 'nvda.log')
            if os.path.exists(temp_log):
                log_file_source = temp_log

        if log_file_source and os.path.exists(log_file_source):
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            target_file_name = f"nvda_log_{timestamp}.log"
            target_path = os.path.join(target_dir, target_file_name)
            shutil.copy2(log_file_source, target_path)
            
    except Exception:
        pass

# 2. Joseph'in 2. Maddesi: Boş sınıf hatasını "pass" ile çözüyoruz
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    """
    Bu sınıf NVDA eklenti standartları gereği eklenmiştir.
    Joseph'in önerisiyle içi 'pass' ile doldurularak log hataları engellenmiştir.
    """
    
    def __init__(self):
        super().__init__()
        # Eklenti başladığında otomatik log kaydı al
        save_nvda_log()

    # 3. Joseph'in 1. Maddesi: Kısayolu kullanıcıya bırakıyoruz.
    # Kullanıcı Girdi Sözlükleri altından bu scripti bulup tuş atayabilir.
    def script_saveLogManually(self, gesture):
        save_nvda_log()
    
    # Scriptin menüde nasıl görüneceğini tanımlıyoruz (İngilizce ana metin)
    script_saveLogManually.__doc__ = _("Saves the current NVDA log to the Documents folder.")