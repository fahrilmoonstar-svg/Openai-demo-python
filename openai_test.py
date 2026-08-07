# ============================================
# OpenAI API - Demo Text Completion
# ============================================
from openai import OpenAI

# Inisialisasi client OpenAI
# Pastikan API Key sudah diset di environment variable OPENAI_API_KEY
# atau bisa langsung dimasukkan di sini: OpenAI(api_key="sk-...")
client = OpenAI()

# Mengirim permintaan ke model text-davinci-003
# CATATAN: Model ini sudah usang (deprecated). 
# OpenAI sekarang menggunakan model gpt-3.5-turbo atau gpt-4.
response = client.completions.create(
    model="text-davinci-003",             # Engine/model yang dipakai
    prompt="What is my size of",          # Pertanyaan atau awalan kalimat
    max_tokens=60                         # Panjang jawaban maksimal
)

# Mencetak hasil jawaban dari AI
# response.choices[0].text mengambil teks jawaban pertama
print(response.choices[0].text.strip())