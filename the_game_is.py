import pandas as pd
import string
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error
)
import joblib

#1. Data ingestion -> ngumpulin data dari berbagai sumber

#buat variable df source nya dari filex
#buka file x dengan pandas

#2. Data preprocessing -> pembersihan dan transformasi data, kek ngilangin koma, pecah kalimat jadi kata kata

#cleaning, same formatting
#null data filling -> data hilang harus isi, cek rata rata untuk isi data yang hilang. intinya perlu diisi, entah pake media, avg, atau 0. The data filling affects the model's result
#outlier cleaning
#correlation searching
#encode -> normalize min max scalar

#3. Model Training & Evaluation -> fase belajar modelnya dari feed data kita, dia bakal cari pola 

#train_test_split -> misaghin 80% data untuk latihan, 20% untuk test. analoginya kek guru kasih kisi-kisi
#model_selection -> pilih otak dari algoritmanya, linear regression buat tebak angka, Clustering, Classifier, RandomForest 
#model fit -> suruh budak nelen data terus cari pattern
#model predict -> nebak hasil ujiannya, ini yang 20% itu bestiku
#model evaluation -> budak ini dievaluasi akurasinya berapa dengan cara dicocokin sama kunci jawaban aslinya
#tuning -> kalo akurasinya jelek (misal cuma 50%), ubah settingan algoritmanya atau balik lagi ke Step 2 buat beresin datanya.

#4. Deployment -> hasilnya udah ada, terus dia kirim ke backend pake API

#model_export -> simpan model yang udah dilatih pake file .pkl
#api_setup -> bikin wadah connect ke FastAPI
#model_loading -> load file .pkl di server FastAPI
#route_binding -> bikin route untuk rest method
#data_parsing -> passing data ke route binding dari JSON laravel ke format array yang dimngerti AI
#inference_execution -> masukin data tadi ke dalam model.predict
#response_formatting -> setelah ditebak datanya, dibungkus dalam JSON dan dilempar lagi ke Laravel


#5. Integration -> sambungin ai pipeline ini ke dalam sebuah proses bisnis
# request_trigger -> user ngelakuin aksi di frontend (misal isi form atau klik tombol), request masuk ke controller Laravel.
# payload_preparation -> Laravel ngambil data user dari database (Postgres), dibungkus rapi jadi format JSON.
# microservice_call -> Laravel nembak API endpoint FastAPI yang udah lu bikin di tahap 4 (misal pake Guzzle atau Http::post di Laravel).
# async_handling -> (Opsional) kalo AI-nya butuh waktu mikir agak lama, lempar tugas nembak API ini ke Queue/Redis biar user nggak kena loading screen kelamaan.
# database_update -> FastAPI balikin hasil tebakannya. Laravel nerima data itu, dan langsung nyimpen hasilnya ke Postgres (misal update status transaksi jadi "Aman" atau "Fraud").
# user_feedback -> Laravel ngasih tau frontend kalo prosesnya udah kelar, dan tampilin hasilnya ke user.


#Data Ingestion using simple Pandas
df = pd.read_csv("books.csv")
clean_price = df['Price'].str.replace("£", "").astype(float).to_frame()

#Data Preprocess
scaler = MinMaxScaler()
price_column = scaler.fit_transform(clean_price)
df['Rating'] = np.random.randint(1, 6, size=len(df))

#Model Training
x1 = price_column
y1 = df['Rating']

X_train, X_test, y_train, y_test = train_test_split(x1, y1, test_size=0.2, random_state=10)

model = LinearRegression()

model.fit(X_train, y_train)
price_prediction = model.predict(X_test)

#Model Evaluation
mse = mean_squared_error(y_test, price_prediction)
mae = mean_absolute_error(y_test, price_prediction)

joblib.dump(mse, "price_prediction_with_mse.csv")
joblib.dump(mae, "price_prediction_with_mae.csv")
