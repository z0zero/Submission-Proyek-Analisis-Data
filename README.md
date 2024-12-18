# Bike Sharing Dashboard 🚲

Dashboard interaktif untuk menganalisis data penggunaan layanan bike sharing.

## Setup Environment

### Menggunakan Conda

```bash
conda create --name bike-sharing python=3.9
conda activate bike-sharing
pip install -r requirements.txt
```

### Menggunakan pip

```bash
python -m venv bike-sharing-env
source bike-sharing-env/bin/activate  # Linux/macOS
bike-sharing-env\Scripts\activate    # Windows
pip install -r requirements.txt
```

## Instalasi Requirements

Buat file `requirements.txt` dengan packages berikut:

```txt
matplotlib==3.10.0
numpy==2.2.0
pandas==2.2.3
plotly==5.24.1
protobuf==5.29.1
scipy==1.14.1
seaborn==0.13.2
streamlit==1.41.1
```

## Struktur Direktori

```plaintext
Submission-Proyek-Analisis-Data
├───dashboard
| └───dashboard.py
├───data
| ├───data_1.csv
| └───data_2.csv
├───notebook.ipynb
├───README.md
└───requirements.txt
└───url.txt
```

## Menjalankan Dashboard

1. Pastikan Anda berada di direktori yang tepat

```bash
cd Submission-Proyek-Analisis-Data/
```

2. Jalankan aplikasi Streamlit

```bash
streamlit run dashboard/dashboard.py
```

3. Dashboard akan terbuka di browser default Anda dengan URL: [http://localhost:8501](http://localhost:8501)

## Fitur Dashboard

Dashboard ini memiliki 4 menu analisis:

1. **Overview**: Menampilkan metrics utama dan tren tahunan
2. **Time Analysis**: Analisis pola berdasarkan jam dan bulan
3. **Weather Impact**: Dampak cuaca terhadap penggunaan
4. **User Behavior**: Analisis perilaku pengguna casual vs registered

## Author

- **z0zero**

## Sumber Data

Dataset yang digunakan: [Bike Sharing Dataset](https://archive.ics.uci.edu/ml/datasets/bike+sharing+dataset)
