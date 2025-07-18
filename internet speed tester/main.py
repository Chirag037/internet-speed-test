import tkinter as tk
from tkinter import messagebox
import speedtest
import time 

def test_speed():
    try:
        st = speedtest.Speedtest()

        label_status.config(text="Testing... Please wait...")
        window.update()

        st.get_best_server()
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        upload_speed = st.upload() / 1_000_000
        ping_result = st.results.ping

        label_download.config(text=f"Download Speed: {download_speed:.2f} Mbps")
        label_upload.config(text=f"Upload Speed: {upload_speed:.2f} Mbps")
        label_ping.config(text=f"Ping: {ping_result:.2f} ms")
        label_status.config(text="Test completed ✅")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to test speed:\n{e}")
        label_status.config(text="Test failed ❌")

# GUI Setup
window = tk.Tk()
window.title("Internet Speed Test")
window.geometry("400x300")
window.resizable(False, False)

label_title = tk.Label(window, text="📶 Internet Speed Test", font=("Arial", 16, "bold"))
label_title.pack(pady=10)

btn_test = tk.Button(window, text="Start Test", font=("Arial", 12), command=test_speed, bg="green", fg="white")
btn_test.pack(pady=10)

label_status = tk.Label(window, text="", font=("Arial", 12), fg="blue")
label_status.pack()

label_download = tk.Label(window, text="Download Speed: -- Mbps", font=("Arial", 12))
label_download.pack(pady=5)

label_upload = tk.Label(window, text="Upload Speed: -- Mbps", font=("Arial", 12))
label_upload.pack(pady=5)

label_ping = tk.Label(window, text="Ping: -- ms", font=("Arial", 12))
label_ping.pack(pady=5)

window.mainloop()
