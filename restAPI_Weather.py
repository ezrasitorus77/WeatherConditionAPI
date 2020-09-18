import requests # import modul

cityName = input("Masukkan nama kota : ") # input user
req = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid=b943055fdc1d454ed6e882f43fb83df2&lang=id") # request dengan query kota berdasar input user

while req.status_code == 404: # kondisi didasarkan pada status code, dimana bila yang didapat adalah 404 maka input user tidak terdaftar
    cityName = input("Kota yang Anda masukkan tidak terdaftar. Mohon periksa kembali penulisan Anda. \n Silahkan masukkan kembali : ")
    req = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid=b943055fdc1d454ed6e882f43fb83df2&lang=id") # define request sebagai varibael baru berdasar input user yang terbaru

if req.status_code == 200: # akses dan hasil berhasil di dapat
    req = req.json()
    # variabel - variabel di bawah sesuai dengan ketentuan soal
    temp = round((req["main"]["temp"] - 273.15), 2)
    weatherCon = [req["weather"][0]["main"], req["weather"][0]["description"]]
    cityCoord = [req["coord"]["lon"], req["coord"]["lat"]]
    humidityLvl = req["main"]["humidity"]
    windSpeed = req["wind"]["speed"] * 3.6

    # menampilkan sesuai ketentuan soal
    print(f'''Kota yang Anda pilih : {cityName.capitalize()}
Koordinat kota : {str(cityCoord[0]) + " BT" if cityCoord[0] > 0 else str(cityCoord[0]) + " BB"}, {str(cityCoord[1]) + " LU" if cityCoord[1] > 0 else str(cityCoord[1]) + " LS"}
Suhu terkini : {temp}\N{DEGREE SIGN}C
Kondisi cuaca terkini : {weatherCon[0]}, dengan kecenderungan {weatherCon[1]}
Tingkat kelembapan : {humidityLvl}%
Kecepatan angin : {windSpeed} km/jam''')

else: # jika status code diluar 200 atau 404, misal 502 Bad Gateway, maka diasumsikan terjadi kesalahan jaringan
    print("Terjadi kesalahan pada jaringan. Silahkan ulangi kembali dalam beberapa waktu atau hubungi penyedia layanan.")