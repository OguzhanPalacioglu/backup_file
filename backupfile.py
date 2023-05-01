import shutil
import os
import time
from datetime import datetime

def backup_files(source_folder, destination_folder):
    print("Backup process has started. Please do not close this window.  !!!")
    # Kaynak klasörü kontrol edelim ve varsa hedef klasörü oluşturalım
    if not os.path.exists(source_folder):
        print(f"{source_folder} Folder not found.")
        return

    today = datetime.today().strftime('%d-%m-%Y TIME- %H-%M')
    destination_folder = os.path.join(destination_folder, today)

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Yedekleme işlemi için zaman başlangıcı
    start_time = time.time()

    # Dosyaları ve klasörleri kopyalayalım
    for root, dirs, files in os.walk(source_folder):
        for directory in dirs:
            source_directory_path = os.path.join(root, directory)
            destination_directory_path = source_directory_path.replace(source_folder, destination_folder, 1)
            if not os.path.exists(destination_directory_path):
                os.makedirs(destination_directory_path)

        for file_name in files:
            source_file_path = os.path.join(root, file_name)
            destination_file_path = source_file_path.replace(source_folder, destination_folder, 1)
            shutil.copy(source_file_path, destination_file_path)

    # Yedekleme işlemi için zaman bitişi
    end_time = time.time()

    # Yedekleme işleminin ne kadar sürdüğünü hesaplayalım
    duration = end_time - start_time

    print(f"{source_folder} folder's files are backed up to {destination_folder} folder. (Took {duration:.2f} seconds).")


# Kullanım örneği
if __name__ == "__main__":
    source_folder = r"source file path"
    destination_folder = r"destination file path"
    backup_files(source_folder, destination_folder)

    time.sleep(5)



# import subprocess

# # SQL Server'ı durdurmak için komutu oluşturalım
# stop_sql_server_command = "net stop MSSQLSERVER"

# # Komutu çalıştıralım
# subprocess.call(stop_sql_server_command, shell=True)
