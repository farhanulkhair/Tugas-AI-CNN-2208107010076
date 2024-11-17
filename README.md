<h2>Tugas AI CNN Farhanul Khair (2208107010076)</h2>
<h3>Nama        : Farhanul Khair </h3>
<h3>NPM         : 2208107010076 </h3>
<h3>Mata Kuliah : Artificial Intellegent </h3>
<br>
<h2>CNN menggunakan data CIFAR-10</h2>
<p>Code dengan nama file "train_model.py" bertujuan untuk melatih model CNN (Convolutional Neural Network) menggunakan dataset CIFAR-10, serta mengevaluasi dan menyimpan model yang telah dilatih.</p>

<ol>
  <li><b>Memuat dan Menyiapkan Dataset CIFAR-10</b>
      <ul>
        <li>"cifar10.load_data()": Fungsi ini memuat dataset CIFAR-10, yang terdiri dari 60.000 gambar berukuran 32x32 piksel, terbagi menjadi 50.000 gambar untuk pelatihan (training) dan 10.000 gambar untuk pengujian (testing). Setiap gambar dikategorikan dalam salah satu dari 10 kelas: pesawat, mobil, burung, kucing, rusa, anjing, katak, kuda, kapal, dan truk.</li>
        <li><b>Normalisasi gambar:</b> Untuk memastikan nilai piksel gambar berada di antara 0 dan 1, gambar yang awalnya memiliki nilai piksel antara 0 dan 255, dibagi dengan 255.0. Proses ini disebut normalisasi.</li>
        <li><b>Konversi label:</b> to_categorical digunakan untuk mengubah label numerik (seperti 0, 1, 2, dll.) menjadi representasi one-hot encoded. Ini berarti label untuk setiap gambar diubah menjadi vektor di mana hanya satu elemen yang bernilai 1, sementara sisanya bernilai 0. Misalnya, label 3 (untuk kucing) akan menjadi [0, 0, 0, 1, 0, 0, 0, 0, 0, 0].</li>
      </ul>
  </li>
  <li><b>Membangun Model CNN (Convolutional Neural Network)</b>
      <ul>
        <li><b>Conv2D:</b> Ini adalah layer konvolusional yang melakukan operasi konvolusi untuk menangkap pola di gambar. Setiap konvolusi akan menghasilkan fitur penting yang akan dipelajari oleh model.
          <ul>
            <li>32, 64, 128 adalah jumlah filter (kernel) yang digunakan di setiap layer. Filter ini digunakan untuk mendeteksi berbagai fitur seperti tepi, tekstur, dan pola.</li>
            <li>(3, 3) adalah ukuran filter. Ini berarti filter akan berukuran 3x3 piksel.</li>
            <li>ReLU (Rectified Linear Unit) adalah fungsi aktivasi yang membantu memperkenalkan non-linearitas ke dalam model.</li>
          </ul>
        </li>
        <li>"MaxPooling2D": Layer ini melakukan pooling untuk mengurangi dimensi output dari layer konvolusional. Pooling membantu model untuk menangkap fitur penting tanpa terlalu terpengaruh oleh pergeseran kecil atau transformasi lainnya pada gambar.</li>
        <li>"Flatten": Layer ini mengubah output dari layer konvolusi dan pooling yang berbentuk matriks 2D menjadi vektor 1D, sehingga dapat diproses oleh layer dense.</li>
        <li>"Dense": Layer ini adalah fully connected layer, yang berarti setiap neuron di layer ini terhubung ke semua neuron di layer sebelumnya. Pada layer ini, model belajar untuk menggabungkan fitur-fitur yang telah dipelajari di layer sebelumnya.
            <ul>
              <li>128 adalah jumlah neuron di layer ini.</li>
              <li>ReLU digunakan sebagai fungsi aktivasi untuk memperkenalkan non-linearitas.</li>
            </ul>
        </li>
        <li>"Dropout": Layer ini digunakan untuk mengurangi overfitting. Dropout secara acak menonaktifkan sejumlah neuron selama pelatihan, yang mencegah model untuk bergantung terlalu banyak pada neuron tertentu.
            <ul>
              <li>0.5 berarti 50% neuron di layer ini akan dinonaktifkan selama pelatihan.</li>
            </ul>
        </li>
        <li>"Softmax": Fungsi aktivasi pada layer output yang digunakan untuk multi-class classification. Fungsi ini mengubah output model menjadi probabilitas kelas.</li>
      </ul>
  </li>
  <li><b>Ringkasan Model</b>
      <ul>
        <li>"model.summary()": Ini akan menampilkan informasi tentang arsitektur model yang telah dibangun, termasuk jenis layer, output shape dari setiap layer, dan jumlah parameter yang dapat dipelajari oleh model.  
        </li>
      </ul>
  </li>
  <li><b>Kompilasi Model</b>
      <ul>
        <li>"optimizer='adam'": Adam adalah algoritma optimasi yang populer yang mengadaptasi laju pembelajaran selama pelatihan. Ini sangat baik untuk jaringan neural dalam banyak kasus.</li>
        <li>"loss='categorical_crossentropy'": Fungsi loss yang digunakan untuk klasifikasi multi-kelas (karena ada 10 kelas di dataset CIFAR-10).</li>
        <li>"metrics=['accuracy']": Ini berarti kita akan melacak akurasi selama pelatihan dan evaluasi.</li>
      </ul>
  </li>
  <li><b>Melatih Model</b>
      <ul>
        <li>
          "fit": Fungsi ini digunakan untuk melatih model.
          <ul>
            <li>train_images, train_labels: Data pelatihan (gambar dan label).</li>
            <li>epochs=10: Model akan dilatih selama 10 iterasi atas seluruh data pelatihan.</li>
            <li>batch_size=64: Model akan memproses 64 gambar dalam satu batch sebelum memperbarui bobotnya.</li>
            <li>validation_data=(test_images, test_labels): Data pengujian digunakan untuk memvalidasi model setelah setiap epoch pelatihan. Ini membantu memantau apakah model overfitting.</li>
          </ul>
        </li>
      </ul>
  </li>
  <li><b>Menyimpan Model</b>
      <ul>
        <li>model.save('model.h5'): Menyimpan model yang sudah dilatih ke dalam file dengan format HDF5. File ini bisa digunakan untuk memuat model di lain waktu tanpa perlu melatih ulang.</li>
      </ul>
  </li>
  <li><b>Evaluasi Model</b>
      <ul>
        <li>evaluate: Fungsi ini digunakan untuk mengevaluasi kinerja model pada data pengujian.
            <ul>
              <li>test_images, test_labels: Data pengujian (gambar dan label).</li>
              <li>Fungsi ini mengembalikan dua nilai: loss dan accuracy.</li>
            </ul>
        </li>
        <li>test_acc: Menampilkan akurasi model pada data pengujian.</li>
      </ul>
  </li>
</ol>
