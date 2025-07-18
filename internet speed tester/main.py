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


