import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page config
st.set_page_config(
    page_title="Bike Sharing Dashboard",
    page_icon="🚲",
    layout="wide"
)

# Load data
@st.cache_data
def load_data():
    df_day = pd.read_csv('data/day.csv')
    df_hour = pd.read_csv('data/hour.csv')
    
    # Data preprocessing
    df_day['dteday'] = pd.to_datetime(df_day['dteday'])
    df_hour['dteday'] = pd.to_datetime(df_hour['dteday'])
    
    # Mapping untuk season dan weathersit
    season_map = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
    weather_map = {1: 'Clear', 2: 'Mist', 3: 'Light Snow/Rain', 4: 'Heavy Rain/Snow'}
    
    df_day['season'] = df_day['season'].map(season_map)
    df_day['weathersit'] = df_day['weathersit'].map(weather_map)
    df_hour['season'] = df_hour['season'].map(season_map)
    df_hour['weathersit'] = df_hour['weathersit'].map(weather_map)
    
    return df_day, df_hour

# Load data
df_day, df_hour = load_data()

# Title
st.title('🚲 Bike Sharing Dashboard')
st.write('Dashboard ini menampilkan analisis penggunaan layanan bike sharing')

# Sidebar
st.sidebar.header('Dashboard Options')
analysis_type = st.sidebar.selectbox(
    'Pilih Tipe Analisis',
    ['Overview', 'Time Analysis', 'Weather Impact', 'User Behavior']
)

# Overview Section
if analysis_type == 'Overview':
    st.header('Overview Penggunaan Bike Sharing')
    
    # Key Metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Peminjaman", f"{df_day['cnt'].sum():,}")
    with col2:
        st.metric("Rata-rata Harian", f"{int(df_day['cnt'].mean()):,}")
    with col3:
        st.metric("Maksimum Harian", f"{df_day['cnt'].max():,}")
    
    # Yearly Trend
    st.subheader('Tren Penggunaan per Tahun')
    yearly_trend = df_day.groupby(df_day['dteday'].dt.year)['cnt'].mean()
    fig, ax = plt.subplots(figsize=(10, 6))
    yearly_trend.plot(kind='bar', ax=ax)
    plt.title('Rata-rata Penggunaan per Tahun')
    plt.xlabel('Tahun')
    plt.ylabel('Rata-rata Peminjaman')
    st.pyplot(fig)

# Time Analysis Section
elif analysis_type == 'Time Analysis':
    st.header('Analisis Berdasarkan Waktu')
    
    # Hourly Pattern
    st.subheader('Pola Penggunaan per Jam')
    hourly_pattern = df_hour.groupby('hr')[['casual', 'registered']].mean()
    fig, ax = plt.subplots(figsize=(12, 6))
    hourly_pattern.plot(kind='line', marker='o', ax=ax)
    plt.title('Pola Penggunaan Sepeda per Jam')
    plt.xlabel('Jam')
    plt.ylabel('Rata-rata Peminjaman')
    plt.grid(True)
    st.pyplot(fig)
    
    # Monthly Pattern
    st.subheader('Pola Penggunaan per Bulan')
    monthly_pattern = df_day.groupby(df_day['dteday'].dt.month)['cnt'].mean()
    fig, ax = plt.subplots(figsize=(12, 6))
    monthly_pattern.plot(kind='line', marker='o', ax=ax)
    plt.title('Rata-rata Penggunaan per Bulan')
    plt.xlabel('Bulan')
    plt.ylabel('Rata-rata Peminjaman')
    plt.grid(True)
    st.pyplot(fig)

# Weather Impact Section
elif analysis_type == 'Weather Impact':
    st.header('Dampak Cuaca Terhadap Penggunaan')
    
    # Weather Impact
    st.subheader('Penggunaan Berdasarkan Kondisi Cuaca')
    weather_impact = df_day.groupby('weathersit')[['casual', 'registered']].mean()
    fig, ax = plt.subplots(figsize=(10, 6))
    weather_impact.plot(kind='bar', ax=ax)
    plt.title('Pengaruh Cuaca terhadap Penggunaan Sepeda')
    plt.xlabel('Kondisi Cuaca')
    plt.ylabel('Rata-rata Peminjaman')
    plt.xticks(rotation=45)
    st.pyplot(fig)
    
    # Temperature Impact
    st.subheader('Pengaruh Temperatur')
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.scatter(df_day['temp'], df_day['cnt'])
    plt.title('Hubungan Temperatur dengan Jumlah Peminjaman')
    plt.xlabel('Temperatur (Normalized)')
    plt.ylabel('Jumlah Peminjaman')
    st.pyplot(fig)

# User Behavior Section
else:
    st.header('Analisis Perilaku Pengguna')
    
    # User Type Comparison
    st.subheader('Perbandingan Casual vs Registered Users')
    user_comparison = pd.DataFrame({
        'User Type': ['Casual', 'Registered'],
        'Total Rentals': [df_day['casual'].sum(), df_day['registered'].sum()]
    })
    fig, ax = plt.subplots(figsize=(10, 6))
    user_comparison.plot(kind='bar', x='User Type', y='Total Rentals', ax=ax)
    plt.title('Total Peminjaman berdasarkan Tipe Pengguna')
    plt.xlabel('Tipe Pengguna')
    plt.ylabel('Total Peminjaman')
    st.pyplot(fig)
    
    # Seasonal Pattern by User Type
    st.subheader('Pola Musiman berdasarkan Tipe Pengguna')
    seasonal_pattern = df_day.groupby('season')[['casual', 'registered']].mean()
    fig, ax = plt.subplots(figsize=(10, 6))
    seasonal_pattern.plot(kind='bar', ax=ax)
    plt.title('Rata-rata Penggunaan per Musim')
    plt.xlabel('Musim')
    plt.ylabel('Rata-rata Peminjaman')
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Footer
st.markdown('---')
st.markdown('Created by [Brian Sangapta] | Data Source: Bike Sharing Dataset')