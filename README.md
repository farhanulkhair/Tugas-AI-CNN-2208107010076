<h2>Tugas AI CNN Farhanul Khair (2208107010076)</h2>
<h3>Nama        : Farhanul Khair </h3>
<h3>NPM         : 2208107010076 </h3>
<h3>Mata Kuliah : Artificial Intellegent </h3>
<br>
<h2>CNN menggunakan data CIFAR-10</h2>
<p>Code dengan nama file ` train_model ` bertujuan untuk melatih model CNN (Convolutional Neural Network) menggunakan dataset CIFAR-10, serta mengevaluasi dan menyimpan model yang telah dilatih.</p>

<ol>
  <li><b>Memuat dan Menyiapkan Dataset CIFAR-10</b>
      <ul>
        <li>` cifar10.load_data() `: Fungsi ini memuat dataset CIFAR-10, yang terdiri dari 60.000 gambar berukuran 32x32 piksel, terbagi menjadi 50.000 gambar untuk pelatihan (training) dan 10.000 gambar untuk pengujian (testing). Setiap gambar dikategorikan dalam salah satu dari 10 kelas: pesawat, mobil, burung, kucing, rusa, anjing, katak, kuda, kapal, dan truk.</li>
        <li><b>Normalisasi gambar:</b> Untuk memastikan nilai piksel gambar berada di antara 0 dan 1, gambar yang awalnya memiliki nilai piksel antara 0 dan 255, dibagi dengan 255.0. Proses ini disebut normalisasi.</li>
        <li><b>Konversi label:</b> to_categorical digunakan untuk mengubah label numerik (seperti 0, 1, 2, dll.) menjadi representasi one-hot encoded. Ini berarti label untuk setiap gambar diubah menjadi vektor di mana hanya satu elemen yang bernilai 1, sementara sisanya bernilai 0. Misalnya, label 3 (untuk kucing) akan menjadi [0, 0, 0, 1, 0, 0, 0, 0, 0, 0].</li>
      </ul>
  </li>
  <li></li>
  <li></li>
</ol>
