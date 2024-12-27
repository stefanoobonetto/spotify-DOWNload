
# 🎵 Spotify-DOWNload 🎶

A **Python script** to download tracks from a Spotify playlist by fetching YouTube URLs and converting them to MP3 format. 🎧✨

---

## ⚡ Prerequisites

- 🐍 **Python 3.8+** is required.
- 🛠️ Install `venv` if not already installed.

---

## 🚀 Setup

Follow these steps to set up the project and start downloading your favorite tunes:

### 1️⃣ **Clone the Repository** 🖥️

```bash
git clone https://github.com/stefanoobonetto/spotify-DOWNload.git
cd spotify-DOWNload
```

### 2️⃣ **Create a Virtual Environment** 🌐

```bash
python3 -m venv venv
```

### 3️⃣ **Activate the Virtual Environment** 💻

- **On Linux/Mac:**
    ```bash
    source venv/bin/activate
    ```

- **On Windows:**
    ```bash
    venv\Scripts\activate
    ```

### 4️⃣ **Install Requirements** 📦

```bash
pip install -r requirements.txt
```

### 5️⃣ **Install FFmpeg** 🛠️

#### 🐧 **On Linux (Ubuntu/Debian-based systems):**
```bash
sudo apt update
sudo apt install ffmpeg -y
```

#### 🍎 **On macOS (Using Homebrew):**
1. Install Homebrew (if not already installed):
    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```
2. Install FFmpeg:
    ```bash
    brew install ffmpeg
    ```

#### 🪟 **On Windows:**
1. Download FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html) (choose a recommended provider like gyan.dev).
2. Extract the `.zip` file to a folder (e.g., `C:\ffmpeg`).
3. Add `C:\ffmpeg\bin` to your system's PATH:
    - Search for "Environment Variables" in the Start Menu.
    - Under "System Variables," find and edit the `Path` variable.
    - Add the path to `C:\ffmpeg\bin`.
4. Verify the installation:
    ```bash
    ffmpeg -version
    ```

---

## 🛠️ **Usage**

Run the script using:

```bash
python main.py
```

You will be prompted to enter a **Spotify playlist URL**. The tracks will be downloaded and converted to MP3 format.

---

## 📂 **Output**

- The MP3 files will be saved in the `output/<playlist_name>` folder. 🎵
- A `.csv` file with track details will also be temporarily created in the same folder and then deleted after processing.

---

Happy downloading! 🥳✨
