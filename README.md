

# 🎥 Video Downloader with Real-Time Progress

A **Python GUI-based video downloader** using `yt-dlp` and `Tkinter`, with **real-time download progress updates** including:  
✅ **Download percentage**  
✅ **Downloaded size / Total size**  
✅ **Estimated time remaining (ETA)**  

## 🚀 Features

- Fetch available video formats from a given URL  
- Choose video quality before downloading  
- Displays real-time **download progress**  
- Shows **downloaded size vs total size**  
- Provides **ETA (estimated time remaining)**  

## 🛠️ Requirements

Ensure you have **Python 3.8+** installed. Then install the dependencies:

```sh
pip install yt-dlp tkinter pyperclip
```

## 📜 Usage

1️⃣ **Run the script**  

```sh
python video_downloader.py
```

2️⃣ **Paste the video URL** in the input box.  

3️⃣ Click **"Fetch Formats"** to load available quality options.  

4️⃣ Select the preferred **video quality** from the dropdown.  

5️⃣ Click **"Download"** to start downloading.  

🟢 **Progress updates** will appear below the button.  

## 📸 Screenshot

![App Screenshot](screenshot.png)  

## 🛠️ Technologies Used

- **Python**  
- **yt-dlp** (for downloading videos)  
- **Tkinter** (for GUI)  
- **Pyperclip** (for clipboard functionality)  

## 📜 License

This project is **open-source** under the **MIT License**.


# 📥 Universal Video Downloader - Chrome Extension

A powerful Chrome extension that allows users to download videos from **YouTube, Facebook, Instagram, and other websites** with multiple quality options.

---

## **🚀 Features**  
✅ Supports **YouTube, Facebook, Instagram, and other websites**  
✅ **Fetch video formats** before downloading  
✅ **Select video quality** from a dropdown  
✅ **Paste button** to quickly insert copied links  
✅ **Progress bar** with real-time percentage, speed, and estimated time  
✅ **Saves latest download at the top** in the **Downloads** folder  
✅ **Runs automatically** (No need to manually start the server)  

---

## **🛠 Installation**  

### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/mostafa-31/Downloader.git
cd Downloader
```

### **2️⃣ Install Python Dependencies**  
Make sure you have **Python 3+** installed. Then, install the required modules:  
```sh
pip install yt-dlp flask pyperclip
```

### **3️⃣ Run the Server (Only Once to Set Up)**  
```sh
python server.py
```
*(Alternatively, set it to run automatically at startup – see below.)*  

---

## **🖥 Chrome Extension Setup**  

### **1️⃣ Open Chrome Extensions Page**  
1. Open Chrome and go to:  
   ```plaintext
   chrome://extensions/
   ```
2. Enable **Developer Mode** (top-right corner).  

### **2️⃣ Load the Extension**  
1. Click **"Load unpacked"**  
2. Select the `extension/` folder from the repository  

Now, you’ll see a **new video downloader icon** in your Chrome toolbar! 🎉  

---

## **🔄 Auto-Start the Server**  
To avoid manually running `server.py` every time, follow one of these options:  

### **Option 1: Windows Task Scheduler (Recommended)**
1. Open **Task Scheduler** (`Win + R`, then type `taskschd.msc`).  
2. Create a new task → Set it to **"Run at logon"**.  
3. Select **server.exe** as the program.  
4. Add `"C:\path\to\server.py"` in the **arguments** field.  

### **Option 2: Run as Windows Service** (Advanced Users)  
Use **NSSM** to install `server.py` as a background service.  
```sh
nssm install VideoDownloader python "C:\path\to\server.py"
```
*(More details in the documentation.)*  

---

## **📸 Screenshot (UI Preview)**  
![image](https://github.com/user-attachments/assets/d176a2fc-d91d-4285-8ede-cef8b1875374)


---

## **⚡ Usage**  
1️⃣ Copy a **video link** from YouTube, Facebook, Instagram, or any supported site.  
2️⃣ Click on the **extension icon** and paste the link.  
3️⃣ Click **"Fetch Formats"** to see available resolutions.  
4️⃣ Select your desired quality and click **"Download"**.  
5️⃣ Watch the real-time progress bar and enjoy your video! 🎥  

---

## **📜 License**  
This project is **open-source** under the **MIT License**. Feel free to contribute and improve it!  

---

## **🛠 Contributing**  
Pull requests are welcome! If you want to add new features, create a new issue first.  

---

## **📧 Contact**  
For any issues or suggestions, feel free to reach out:  
📩 **Email:** shiahidmostafa@gmail.com  
🌐 **GitHub:** [mostafa-31](https://github.com/mostafa-31)  

