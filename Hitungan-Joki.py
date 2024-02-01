import streamlit as st

# Constants
# singkat = {"B5": "Bronze 5", "B4": "Bronze 4", "B3": "Bronze 3", "B2": "Bronze 2", "B1": "Bronze 1",
#            "S5": "Silver 5", "S4": "Silver 4", "S3": "Silver 3", "S2": "Silver 2", "S1": "Silver 1",
#            "G5": "Gold 5", "G4": "Gold 4", "G3": "Gold 3", "G2": "Gold 2", "G1": "Gold 1",
#            "P5": "Platinum 5", "P4": "Platinum 4", "P3": "Platinum 3", "P2": "Platinum 2", "P1": "Platinum 1",
#            "D5": "Diamond 5", "D4": "Diamond 4", "D3": "Diamond 3", "D2": "Diamond 2", "D1": "Diamond 1",
#            "C5": "Crown 5", "C4": "Crown 4", "C3": "Crown 3", "C2": "Crown 2", "C1": "Crown 1",
#            "A": "Ace", "A1": "Ace 1", "A2": "Ace 2", "A3": "Ace 3", "A4": "Ace 4", "A5": "Ace 5"}

isi = {"Bronze 5": 1, "Bronze 4": 2, "Bronze 3": 3, "Bronze 2": 4, "Bronze 1": 5,
       "Silver 5": 6, "Silver 4": 7, "Silver 3": 8, "Silver 2": 9, "Silver 1": 10,
       "Gold 5": 11, "Gold 4": 12, "Gold 3": 13, "Gold 2": 14, "Gold 1": 15,
       "Platinum 5": 16, "Platinum 4": 17, "Platinum 3": 18, "Platinum 2": 19, "Platinum 1": 20,
       "Diamond 5": 21, "Diamond 4": 22, "Diamond 3": 23, "Diamond 2": 24, "Diamond 1": 25,
       "Crown 5": 26, "Crown 4": 27, "Crown 3": 28, "Crown 2": 29, "Crown 1": 30,
       "Ace": 31, "Ace 1": 32, "Ace 2": 33, "Ace 3": 34, "Ace 4": 35, "Ace 5": 36}

list_harga = [10, 10, 10, 10, 10, 15, 15, 15, 15, 15, 20, 20, 20, 20, 20, 25, 25, 25, 25, 25, 30, 30, 30, 30, 30, 40, 40, 40,
              40, 40, 50, 80, 80, 80, 80, 80]

# Input
st.set_page_config(layout='wide', page_title='Perkiraan KD Joki')
st.title('Perkiraan KDA dan Harga Joki')

st.text('''
Program ini dibuat untuk memperkirakan K/D pada jasa joki kami
Perkiraan KD dari kami 3-6, tidak termasuk KD sebelumnya
Owner: @rayhan.kurniawan / 0821-5758-1260
Instagram: @jasa.joki.pubgmobile
WhatsApp: 0857-5078-3967
''')

st.text('''===PERKIRAAN KD JOKI===
Instagram: @jasa.joki.pubgmobile
WhatsApp: 0857-5078-3967
''')

awal = st.selectbox("Masukkan Tier Awal:", list(isi.keys()))
tujuan_options = [tier for tier in list(isi.keys()) if isi[tier] > isi[awal]]
tujuan = st.selectbox("Masukkan Tier Tujuan:", tujuan_options)
ms = st.number_input("Masukkan Jumlah Match Sebelumnya: ", step=1)
ks = st.number_input("Masukkan Jumlah Kill Sebelumnya: ", step=1)

# Logic
a = isi[awal]
b = isi[tujuan]
harga = sum(list_harga[a:b])

st.text(f'Perkiraan match yang cocok sekitar {int(harga / 10)} match')

if (awal[0] == "B" or awal[0] == "S" or awal[0] == "G") and tujuan == "A":
    harga = 450
elif awal[0] == "P" and tujuan == "A":
    harga = 350
elif awal[0] == "D" and tujuan == "A":
    harga = 250

# Output
st.text(f"Harga= {harga}K")
match= int(harga / 10)
tm = st.number_input('Masukkan Jumlah Match yang akan dimainkan: ', value = match, step=1)
kd3 = tm * 3
kdr = tm * 4.5
kd6 = tm * 6

hasil3 = (ks + kd3) / (ms + tm)
hasilr = (ks + kdr) / (ms + tm)
hasil6 = (ks + kd6) / (ms + tm)

kom1 = round(harga * (2 / 3))
kom2 = round(harga * (3 / 4))

st.text('''
===Catatan Penjoki:===''')
st.text(f'Komisi Anda {kom1}K hingga {kom2}K')
st.text(f'Komisi Saya {harga - kom2}K hingga {harga - kom1}K')

if harga >= 150:
    st.text(f'Waktu pengerjaan sekitar {round(harga / 100 + 1)} sampai {round(harga / 50)} Hari')
else:
    st.text(f'Waktu pengerjaan sekitar {round(harga / 100)} sampai {round(harga / 50 + 1)} Hari')

st.text(f'Permainan sekitar {tm} Match, harus mengumpulkan {round(kdr)} Kill, dengan rate {kd3}-{kd6} Kill')
st.text(f'''
===STATISTIK===')
st.text(f"Tier Awal= {awal}")
st.text(f"Tier Tujuan= {tujuan}")
st.text(f"Harga= {harga}K")
st.text(f"Jumlah Match: {ms}")
st.text(f"Jumlah Kill: {ks}")
''')

if ms == 0:
    st.text('KD: 0')
else:
    st.text(f'KD: {round(ks / ms, 2)}')

st.text('===================')
st.text('''Note:
Perkiraan KD dari kami 3-6, tidak termasuk KD sebelumnya
KD Rata-Rata sekitar 4.5''')
st.text(f'Perkiraan match yang dimainkan sekitar {tm} match')

if harga >= 150:
    st.text(f'Waktu pengerjaan sekitar {round(harga / 100 + 1)} sampai {round(harga / 50)} Hari')
else:
    st.text(f'Waktu pengerjaan sekitar {round(harga / 100)} sampai {round(harga / 50 + 1)} Hari')

st.text('===================')
st.text('=*Perkiraan Hasil Setelah Dimainkan*=')
st.text(f'Total Match: {ms + tm}')
st.text(f'Total Kill: {ks + kd3}-{ks + kd6}')
st.text(f'Total Kill Rata-Rata: {round(ks + kdr)}')
st.text(f'KD: {round(hasil3, 2)}-{round(hasil6, 2)}')
st.text(f'KD Rata-Rata: {round(hasilr, 2)}')
