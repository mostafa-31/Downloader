import yt_dlp
import tkinter as tk
import pyperclip
from tkinter import messagebox, ttk


def paste_link():
    link_entry.delete(0, tk.END)
    link_entry.insert(0, pyperclip.paste())


def fetch_formats():
    url = link_entry.get().strip()
    if not url:
        messagebox.showerror("Error", "Please enter a video link.")
        return

    try:
        with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
            info = ydl.extract_info(url, download=False)
            formats = info.get('formats', [])
            format_options = []
            format_map.clear()

            for fmt in formats:
                if 'format_id' in fmt and 'ext' in fmt:
                    resolution = fmt.get('resolution', 'Unknown')
                    desc = f"{resolution} ({fmt['ext']})"
                    format_options.append(desc)
                    format_map[desc] = fmt['format_id']

            format_dropdown['values'] = format_options
            if format_options:
                format_dropdown.current(0)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch formats!\n{e}")


def progress_hook(d):
    if d['status'] == 'downloading':
        downloaded = d.get('downloaded_bytes', 0) / (1024 * 1024)  # Convert to MB
        total = d.get('total_bytes', 1) / (1024 * 1024)  # Convert to MB
        percent = d.get('_percent_str', '0%').strip()
        eta = d.get('eta', 0)

        progress_label.config(text=f"Progress: {percent}")
        size_label.config(text=f"Size: {downloaded:.2f}MB / {total:.2f}MB")
        eta_label.config(text=f"ETA: {eta}s")

        root.update_idletasks()

    elif d['status'] == 'finished':
        progress_label.config(text="Download Completed!")


def download_video():
    url = link_entry.get().strip()
    selected_format = format_var.get()

    if not url:
        messagebox.showerror("Error", "Please enter a video link.")
        return
    if not selected_format:
        messagebox.showerror("Error", "Please select a format.")
        return

    format_id = format_map.get(selected_format, 'best')

    try:
        ydl_opts = {
            'format': format_id,
            'outtmpl': '%(title)s.%(ext)s',
            'quiet': False,
            'progress_hooks': [progress_hook]
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", "Download Completed!")
    except Exception as e:
        messagebox.showerror("Error", f"Download Failed!\n{e}")


# Create GUI window
root = tk.Tk()
root.title("Video Downloader")
root.geometry("470x280")
root.resizable(False, False)

style = ttk.Style()
style.configure("TButton", padding=5, font=("Arial", 10))
style.configure("TLabel", font=("Arial", 10))
style.configure("TEntry", padding=5, font=("Arial", 10))
style.configure("TCombobox", padding=5, font=("Arial", 10))

frame = ttk.Frame(root, padding=10)
frame.pack(fill="both", expand=True)

format_map = {}

# Input field
link_label = ttk.Label(frame, text="Video URL:")
link_label.grid(row=0, column=0, sticky="w", pady=5)

link_entry = ttk.Entry(frame, width=40)
link_entry.grid(row=0, column=1, pady=5)

paste_button = ttk.Button(frame, text="Paste", command=paste_link)
paste_button.grid(row=0, column=2, padx=5, pady=5)

# Fetch Formats Button
fetch_button = ttk.Button(frame, text="Fetch Formats", command=fetch_formats)
fetch_button.grid(row=1, column=1, pady=5)

# Format Selection Dropdown
format_label = ttk.Label(frame, text="Select Quality:")
format_label.grid(row=2, column=0, sticky="w", pady=5)

format_var = tk.StringVar()
format_dropdown = ttk.Combobox(frame, textvariable=format_var, state="readonly", width=38)
format_dropdown.grid(row=2, column=1, pady=5)

# Download Button
download_button = ttk.Button(frame, text="Download", command=download_video)
download_button.grid(row=3, column=1, pady=10)

# Progress Labels
progress_label = ttk.Label(frame, text="Progress: 0%", font=("Arial", 10))
progress_label.grid(row=4, column=1, pady=2)

size_label = ttk.Label(frame, text="Size: 0.00MB / 0.00MB", font=("Arial", 10))
size_label.grid(row=5, column=1, pady=2)

eta_label = ttk.Label(frame, text="ETA: --s", font=("Arial", 10))
eta_label.grid(row=7, column=1, pady=2)

root.mainloop()
