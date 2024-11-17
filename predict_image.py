from keras.models import load_model
from tkinter import filedialog, Tk
from PIL import Image
import numpy as np

# Fungsi untuk memuat dan memproses gambar
def load_and_prepare_image(file_path):
    img = Image.open(file_path)
    img = img.resize((32, 32))  # Sesuaikan dengan dimensi yang model Anda harapkan
    img = np.array(img) / 255.0  # Normalisasi
    img = np.expand_dims(img, axis=0)  # Tambahkan batch dimension
    return img

# Nama-nama kelas untuk dataset CIFAR-10
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

# Memuat model yang telah disimpan
model = load_model('model.h5')  # Memuat model yang telah disimpan

# Membuka jendela dialog untuk memilih file gambar menggunakan tkinter
root = Tk()
root.withdraw()  # Menyembunyikan jendela utama tkinter
file_path = filedialog.askopenfilename(title="Pilih gambar", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

# Memeriksa apakah pengguna memilih file
if file_path:
    # Memproses gambar dan membuat prediksi
    img = load_and_prepare_image(file_path)
    prediction = model.predict(img)
    predicted_class_index = np.argmax(prediction, axis=1)[0]  # Dapatkan indeks kelas
    predicted_class_name = class_names[predicted_class_index]  # Dapatkan nama kelas
    print(f'File: {file_path}, Predicted Class Index: {predicted_class_index}, Predicted Class Name: {predicted_class_name}')
else:
    print("Tidak ada file yang dipilih.")
