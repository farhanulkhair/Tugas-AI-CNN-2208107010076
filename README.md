# Tugas AI CNN Farhanul Khair (2208107010076)

### Nama        : Farhanul Khair  
### NPM         : 2208107010076  
### Mata Kuliah : Artificial Intelligence

---

## CNN menggunakan data CIFAR-10

File `train_model.py` bertujuan untuk melatih model CNN (Convolutional Neural Network) menggunakan dataset CIFAR-10, serta mengevaluasi dan menyimpan model yang telah dilatih.

### 1. Memuat dan Menyiapkan Dataset CIFAR-10
- **`cifar10.load_data()`**: Fungsi ini memuat dataset CIFAR-10, yang terdiri dari 60.000 gambar berukuran 32x32 piksel, terbagi menjadi 50.000 gambar untuk pelatihan (training) dan 10.000 gambar untuk pengujian (testing). Setiap gambar dikategorikan dalam salah satu dari 10 kelas: pesawat, mobil, burung, kucing, rusa, anjing, katak, kuda, kapal, dan truk.
- **Normalisasi gambar**: Untuk memastikan nilai piksel gambar berada di antara 0 dan 1, gambar yang awalnya memiliki nilai piksel antara 0 dan 255, dibagi dengan 255.0. Proses ini disebut normalisasi.
- **Konversi label**: `to_categorical` digunakan untuk mengubah label numerik (seperti 0, 1, 2, dll.) menjadi representasi one-hot encoded. Ini berarti label untuk setiap gambar diubah menjadi vektor di mana hanya satu elemen yang bernilai 1, sementara sisanya bernilai 0. Misalnya, label 3 (untuk kucing) akan menjadi `[0, 0, 0, 1, 0, 0, 0, 0, 0, 0]`.

### 2. Membangun Model CNN (Convolutional Neural Network)
- **`Conv2D`**: Ini adalah layer konvolusional yang melakukan operasi konvolusi untuk menangkap pola di gambar. Setiap konvolusi akan menghasilkan fitur penting yang akan dipelajari oleh model.
  - `32, 64, 128` adalah jumlah filter (kernel) yang digunakan di setiap layer. Filter ini digunakan untuk mendeteksi berbagai fitur seperti tepi, tekstur, dan pola.
  - `(3, 3)` adalah ukuran filter. Ini berarti filter akan berukuran 3x3 piksel.
  - **ReLU** (Rectified Linear Unit) adalah fungsi aktivasi yang membantu memperkenalkan non-linearitas ke dalam model.
- **`MaxPooling2D`**: Layer ini melakukan pooling untuk mengurangi dimensi output dari layer konvolusional. Pooling membantu model untuk menangkap fitur penting tanpa terlalu terpengaruh oleh pergeseran kecil atau transformasi lainnya pada gambar.
- **`Flatten`**: Layer ini mengubah output dari layer konvolusi dan pooling yang berbentuk matriks 2D menjadi vektor 1D, sehingga dapat diproses oleh layer dense.
- **`Dense`**: Layer ini adalah fully connected layer, yang berarti setiap neuron di layer ini terhubung ke semua neuron di layer sebelumnya. Pada layer ini, model belajar untuk menggabungkan fitur-fitur yang telah dipelajari di layer sebelumnya.
  - `128` adalah jumlah neuron di layer ini.
  - **ReLU** digunakan sebagai fungsi aktivasi untuk memperkenalkan non-linearitas.
- **`Dropout`**: Layer ini digunakan untuk mengurangi overfitting. Dropout secara acak menonaktifkan sejumlah neuron selama pelatihan, yang mencegah model untuk bergantung terlalu banyak pada neuron tertentu.
  - `0.5` berarti 50% neuron di layer ini akan dinonaktifkan selama pelatihan.
- **`Softmax`**: Fungsi aktivasi pada layer output yang digunakan untuk multi-class classification. Fungsi ini mengubah output model menjadi probabilitas kelas.

### 3. Ringkasan Model
- **`model.summary()`**: Ini akan menampilkan informasi tentang arsitektur model yang telah dibangun, termasuk jenis layer, output shape dari setiap layer, dan jumlah parameter yang dapat dipelajari oleh model.

### 4. Kompilasi Model
- **`optimizer='adam'`**: Adam adalah algoritma optimasi yang populer yang mengadaptasi laju pembelajaran selama pelatihan. Ini sangat baik untuk jaringan neural dalam banyak kasus.
- **`loss='categorical_crossentropy'`**: Fungsi loss yang digunakan untuk klasifikasi multi-kelas (karena ada 10 kelas di dataset CIFAR-10).
- **`metrics=['accuracy']`**: Ini berarti kita akan melacak akurasi selama pelatihan dan evaluasi.

### 5. Melatih Model
- **`fit`**: Fungsi ini digunakan untuk melatih model.
  - `train_images, train_labels`: Data pelatihan (gambar dan label).
  - `epochs=10`: Model akan dilatih selama 10 iterasi atas seluruh data pelatihan.
  - `batch_size=64`: Model akan memproses 64 gambar dalam satu batch sebelum memperbarui bobotnya.
  - `validation_data=(test_images, test_labels)`: Data pengujian digunakan untuk memvalidasi model setelah setiap epoch pelatihan. Ini membantu memantau apakah model overfitting.

### 6. Menyimpan Model
- **`model.save('model.h5')`**: Menyimpan model yang sudah dilatih ke dalam file dengan format HDF5. File ini bisa digunakan untuk memuat model di lain waktu tanpa perlu melatih ulang.

### 7. Evaluasi Model
- **`evaluate`**: Fungsi ini digunakan untuk mengevaluasi kinerja model pada data pengujian.
  - `test_images, test_labels`: Data pengujian (gambar dan label).
  - Fungsi ini mengembalikan dua nilai: loss dan accuracy.
- **`test_acc`**: Menampilkan akurasi model pada data pengujian.

---

### `predict_image.py`

File `predict_image.py` bertujuan untuk memuat model CNN yang telah dilatih menggunakan dataset CIFAR-10 dan menggunakannya untuk memprediksi kelas gambar yang dipilih oleh pengguna melalui antarmuka grafis dengan tkinter.

#### 1. Memuat dan memproses gambar
- Fungsi **`load_and_prepare_image(file_path)`** digunakan untuk membuka gambar, mengubah ukurannya menjadi 32x32 piksel (sesuai dengan input model), menormalisasi piksel gambar ke rentang [0, 1], dan menambahkan dimensi batch.

#### 2. Membuat Model
- Model yang telah dilatih dan disimpan dalam file `model.h5` dimuat dengan `load_model()`.

#### 3. Dialog Pemilihan File Gambar
- Menggunakan **`tkinter.filedialog.askopenfilename()`**, pengguna dapat memilih file gambar (dengan ekstensi .png, .jpg, atau .jpeg) dari sistem file.

#### 4. Prediksi Gambar
- Setelah gambar dipilih, fungsi **`model.predict()`** digunakan untuk memprediksi kelas gambar. Hasil prediksi diproses untuk mendapatkan indeks kelas dengan **`np.argmax()`** dan kemudian diterjemahkan menjadi nama kelas menggunakan daftar `class_names`.

#### 5. Menampilkan Hasil
- Nama kelas yang diprediksi dan indeksnya dicetak ke layar.

---

## Convolutional Neural Network (CNN) untuk Klasifikasi Anjing dan Kucing

Kode ini digunakan untuk melatih dan menguji model Convolutional Neural Network (CNN) dalam mengklasifikasikan gambar. Secara khusus, model ini digunakan untuk memprediksi apakah gambar yang diberikan berisi gambar kucing (cat) atau anjing (dog).

---

# **Klasifikasi Gambar Anjing dan Kucing dengan CNN**

Proyek ini bertujuan untuk **membangun dan melatih model Convolutional Neural Network (CNN)** untuk **mengklasifikasikan gambar anjing dan kucing**. Model ini dilatih menggunakan dataset gambar yang terdiri dari gambar anjing dan kucing, dan digunakan untuk memprediksi kelas gambar (anjing atau kucing) berdasarkan input gambar.

## **Fitur Utama:**

- **Training Model:** Model CNN dibangun dan dilatih pada dataset gambar anjing dan kucing menggunakan Keras dan TensorFlow.
- **Data Augmentasi:** Gambar dalam dataset dilatih dengan augmentasi seperti rotasi, zoom, dan flipping untuk meningkatkan kinerja model.
- **Prediksi Gambar:** Setelah model dilatih, file `predict.py` digunakan untuk memprediksi kelas gambar (anjing atau kucing) dari gambar yang diunggah pengguna.
- **Output Prediksi:** Model akan mengklasifikasikan gambar baru dan mencetak jumlah gambar yang diprediksi sebagai anjing dan kucing.

## **Struktur Proyek:**

- **`train.py`:** Skrip ini digunakan untuk melatih model CNN menggunakan dataset gambar anjing dan kucing. Dataset dibagi menjadi dua bagian: training set dan test set.
- **`predict.py`:** Skrip ini digunakan untuk menguji model terlatih pada gambar baru (test set) dan menghasilkan prediksi (anjing atau kucing).
- **`dataset/`:** Folder ini berisi dataset gambar yang diperlukan untuk melatih dan menguji model.

## **Langkah-langkah untuk Menjalankan Proyek:**

1. **Persiapan Lingkungan:**
   Pastikan Anda telah menginstal TensorFlow dan Keras. Anda dapat menginstalnya dengan menjalankan:
   ```bash
   pip install tensorflow keras
   ```

2. **Dataset:**
   Anda perlu menyiapkan dataset yang terdiri dari dua kategori gambar: **anjing (dogs)** dan **kucing (cats)**. Dataset ini perlu diletakkan dalam folder **`dataset/`** dengan struktur sebagai berikut:
   ```
   dataset/
   ├── training_set/
   │   ├── cats/
   │   └── dogs/
   └── test_set/
       ├── cats/
       └── dogs/
   ```

3. **Melatih Model:**
   Jalankan skrip **`train.py`** untuk melatih model CNN dengan dataset yang disiapkan. Setelah pelatihan selesai, model akan disimpan dalam file `model.h5`.

   ```bash
   python train.py
   ```

4. **Prediksi Gambar:**
   Jalankan skrip **`predict.py`** untuk menguji model dengan gambar baru dan mencetak hasil prediksi (anjing atau kucing).

   ```bash
   python predict.py
   ```

5. **Hasil Prediksi:**
   Skrip **`predict.py`** akan mencetak jumlah gambar yang diprediksi sebagai anjing dan kucing, serta informasi lainnya terkait prediksi.

## **Lisensi:**

Proyek ini dilisensikan di bawah **MIT License**. Lihat file `LICENSE` untuk informasi lebih lanjut.

---

Dengan README ini, pengguna GitHub dapat dengan mudah memahami tujuan proyek, cara untuk mengatur dan menjalankan kode, serta bagaimana memanfaatkan model CNN untuk klasifikasi gambar anjing dan kucing.
