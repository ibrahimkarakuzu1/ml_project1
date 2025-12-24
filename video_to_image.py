import cv2
import os

def extract_and_resize(video_path, class_name, output_folder='dataset'):
    # Klasör yapısını oluştur
    class_folder = os.path.join(output_folder, class_name)
    if not os.path.exists(class_folder):
        os.makedirs(class_folder)

    cap = cv2.VideoCapture(video_path)
    count = 0
    saved_count = 0
    
    # Video FPS (saniyedeki kare sayısı) değerini alalım
    fps = cap.get(cv2.CAP_PROP_FPS)
    print(f"{class_name} işleniyor... (Video FPS: {fps})")

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # GÜNCELLEME: Her 10 karede bir fotoğraf al (
        # Bu ayar 30-40 saniyelik videolardan yaklaşık 90-120 fotoğraf çıkarır.
        if count % 10 == 0: 
            # 1. Yeniden Boyutlandır (128x128)
            resized_frame = cv2.resize(frame, (128, 128))
            
            # 2. Kaydet
            file_name = f"{class_name}_{saved_count}.jpg"
            file_path = os.path.join(class_folder, file_name)
            cv2.imwrite(file_path, resized_frame)
            saved_count += 1
            
        count += 1

    cap.release()
    print(f"✅ Tamamlandı: {class_name} sınıfı için {saved_count} fotoğraf kaydedildi.")

# --- VİDEO LİSTESİ ---
# Videolarınızın tam adlarını buraya yazın
video_list = [
    ("class1_50tl.mp4", "50_tl"),   # 1. Video adı ve sınıfı
    ("class2_100tl.mp4", "100_tl")   # 2. Video adı ve sınıfı
]

# İşlemi Başlat
for video, sinif in video_list:
    extract_and_resize(video, sinif)