import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Peminjaman sepeda')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv('hour.csv')
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')

st.subheader('Banyak peminjaman sepeda per jam menurut hari')
fig1, ax = plt.subplots(figsize=(20,5))
sns.pointplot(data=data, x='hr', y='cnt', hue='weekday', ax=ax)
ax.set(title='Banyak peminjaman sepeda per jam menurut hari');
st.pyplot(fig1)

st.subheader('Banyak peminjaman sepeda per jam menurut hari oleh pengguna tak terdaftar')
fig2, ax = plt.subplots(figsize=(20,5))
sns.pointplot(data=data, x='hr', y='casual', hue='weekday', ax=ax)
ax.set(title='Banyak peminjaman sepeda per jam menurut hari oleh pengguna tak terdaftar');
st.pyplot(fig2)

st.subheader('Banyak peminjaman sepeda per jam menurut hari oleh pengguna terdaftar')
fig3, ax = plt.subplots(figsize=(20,5))
sns.pointplot(data=data, x='hr', y='registered', hue='weekday', ax=ax)
ax.set(title='Banyak peminjaman sepeda per jam menurut hari oleh pengguna terdaftar');
st.pyplot(fig3)

st.subheader('Banyak peminjaman sepeda per jam menurut hari oleh pengguna terdaftar')
fig4, ax = plt.subplots(figsize=(20,5))
sns.pointplot(data=data, x='hr', y='cnt', hue='weathersit', ax=ax)
ax.set(title='Banyak peminjaman sepeda pada cuaca yang berbeda');
st.pyplot(fig4)

st.subheader('Banyak peminjaman sepeda pada masing-masing musim')
fig5, ax = plt.subplots(figsize=(20,5))
sns.pointplot(data=data, x='hr', y='cnt', hue='season', ax=ax)
ax.set(title='Banyak peminjaman sepeda pada masing-masing musim');
st.pyplot(fig5)

st.subheader('Banyak peminjaman sepeda pada masing-masing bulan')
fig6, ax = plt.subplots(figsize=(20,5))
sns.barplot(data=data, x='mnth', y='cnt', ax=ax)
ax.set(title='Banyak peminjaman sepeda pada masing-masing bulan');
st.pyplot(fig6)

st.subheader('Perbandingan pengguna terdaftar dan tidak terdaftar')
labels = ["Tidak Terdaftar", "Terdaftar"]
sizes = [data["casual"].sum(), data["registered"].sum()]
fig7, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%');
st.pyplot(fig7)