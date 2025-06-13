# 🎬 Film Log App

**Film Log App**, izlediğiniz filmleri aramanıza, derecelendirmenize ve günlüğünü tutmanıza olanak sağlayan Flask tabanlı bir web uygulamasıdır. Uygulama OMDB API üzerinden film bilgilerini çekerek yerel bir veritabanına kaydeder. Geliştiriciler için REST API, SQLAlchemy modelleme ve CRUD işlemleri üzerinde çalışmak için mükemmel bir örnektir.

---

## 📌 Uygulama Amacı

- İzlenen filmlerin arşivlenmesini sağlamak
- Kişisel derecelendirme ve izlenme tarihlerini kayıt altına almak
- Flask + SQLAlchemy + OMDB API gibi teknolojilerle pratik yapmak

---

## 🚀 Özellikler

- 🎞️ OMDB API üzerinden film arama
- 📄 Detaylı film bilgisi gösterimi
- ⭐ Kendi puanınızı vererek film ekleme
- 🗓️ İzlenme tarihi günlüğü tutma (log)
- 🗑️ Film silme
- 🔍 Başlığa göre film listesinde filtreleme
- 📂 SQLite veritabanı desteği

---

## 🧱 Kullanılan Teknolojiler

| Teknoloji     | Açıklama                    |
|---------------|-----------------------------|
| Flask         | Web uygulama çatısı         |
| SQLAlchemy    | ORM (Veritabanı yönetimi)   |
| OMDB API      | Film bilgileri alma         |
| Jinja2        | Şablon motoru               |
| HTML + CSS    | Arayüz                      |

---

## 🧠 Veri Modelleri (models.py)

### 🎬 `Movie`
- `id`, `imdb_id`, `title`, `year`, `genre`, `description`, `poster_url`
- İlişkiler: `logs`, `ratings`

### ⭐ `Rating`
- Bir filme verilen kullanıcı puanını tutar.
- `movie_id`, `rating`

### 🗓️ `Log`
- İzlenme tarihini saklar.
- `movie_id`, `watched_date`

---

## 🏗️ Klasör Yapısı

```
FilmLogApp/
├── app.py              # Ana uygulama
├── models.py           # SQLAlchemy veri modelleri
├── templates/          # HTML şablonları
├── static/             # CSS, JS, görseller
├── movies.db           # SQLite veritabanı
├── requirements.txt    # Gerekli paketler
└── README.md           # Proje dokümantasyonu
```

---

## ⚙️ Kurulum

```bash
# Depoyu klonla
git clone https://github.com/AlihanUral/Film_Log_App.git
cd Film_Log_App

# Sanal ortam oluştur ve aktive et
python3 -m venv venv
source venv/bin/activate        # Windows: .\venv\Scripts\activate

# Bağımlılıkları yükle
pip install -r requirements.txt

# Uygulamayı çalıştır
python app.py
```

🖥️ [http://localhost:5000](http://localhost:5000) üzerinden erişebilirsin.

---

## 🔑 OMDB API Kullanımı

1. [http://www.omdbapi.com/apikey.aspx](http://www.omdbapi.com/apikey.aspx) üzerinden ücretsiz API anahtarı alın.
2. `app.config['OMDB_API_KEY']` satırına kendi anahtarınızı yazın.

---

## 🔧 Geliştirici Rehberi

Yeni bir özellik geliştirmek için:

```bash
git checkout -b yeni-ozellik
# Değişiklikleri yap
git commit -m "Yeni özellik eklendi"
git push origin yeni-ozellik
```

---

## 🤝 Katkı

Pull request’ler açarak katkıda bulunabilirsiniz. Her türlü öneri ve geri bildirime açığız!

---

## 📄 Lisans

MIT Lisansı © 2025 [Alihan Ural](https://github.com/AlihanUral)