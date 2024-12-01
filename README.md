# **udownload**

U-Download is a Django-based web application that allows users to download YouTube videos in various formats and resolutions. The app is designed to provide a simple, intuitive interface for video downloading while leveraging Django's robust backend capabilities.

---

## **Features**

- 🎥 **Download YouTube Videos**: Supports downloading videos in different resolutions (1080p, 720p, etc.).
- 🎶 **Audio Extraction**: Option to download only the audio as MP3.
- 🚀 **Fast and Reliable**: Built using Django for efficient backend processing.
- 🌍 **User-Friendly Interface**: Clean, responsive UI for easy navigation and usage.
- 🔒 **Safe and Secure**: Does not store any user data.

---

## **Installation**

Follow these steps to set up and run the project locally.

### **1. Clone the Repository**
```bash
git clone https://github.com/BlackCoder56/u-dowload.git
cd u-download


```
### **2. Set Up Virtual Enviroment ***
```bash
    python -m venv venv
    source venv/bin/activate  # For Linux/macOS
    venv\Scripts\activate     # For Windows

```
### **3. Install Dependencies ***
```bash
    pip install -r requirements.txt

```
### **4. Configure the Environment ***
```env
    SECRET_KEY=your-django-secret-key
    DEBUG=True
    ALLOWED_HOSTS=localhost, 127.0.0.1

```
### **5. Run Migrations ***
```bash
    python manage.py migrate

```
### **6. Start the Development Server**
```bash
    python manage.py runserver

```
### ***7. Access the App**
```arduino
    http://127.0.0.1:8000

```
### ***Usage**
    1.Enter the URL of the YouTube video you want to download.
    2. Select the format (video or audio) and resolution.
    3. Click "Download" to start the process.

### ***Technologies Used**
    Backend: Django
    Frontend: HTML, CSS, Bootstrap
    API: pytube for interacting with YouTube
    Database: SQLite (default, replaceable with PostgreSQL/MySQL)

### ***Project Structure**
    u-download/
    │
    ├── manage.py
    ├── requirements.txt
    ├── .env
    ├── .gitignore
    ├── README.md
    ├── downloader/
    │   ├── migrations/
    │   ├── templates/
    │   │   └── app/
    │   │       └── index.html
    │   ├── static/
    │   │   ├── css/
    │   │   ├── js/
    │   │   └── images/
    │   ├── views.py
    │   ├── urls.py
    │   ├── models.py
    │   └── admin.py
    └── settings/
        ├── base.py
        ├── development.py
        └── production.py

### ***Future Enhancements**
    ✅ Add a download queue for batch downloads.
    ✅ Support downloading entire YouTube playlists.
    ✅ Allow users to choose custom file names for downloads.
    ✅ Improve download speed with server-side optimizations.

### ***License**
    This project is licensed under the MIT License. See the LICENSE file for details.

### ***Contributing**
We welcome contributions! If you'd like to contribute to this project, please follow these steps:
    1. Fork the repository.
    2. Create a new branch (feature-name).
    3. Commit your changes.
    4. Push your branch and open a pull request.

### ***Contact**
    Developer: Elisha alias BlackCoder56
    Email: blackcoda56@gmail.com
    GitHub: BlackCoder56

