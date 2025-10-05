import os, platform, subprocess

API_KEY = "YOUR API KEY GOES HERE"

if platform.system() == "Darwin":
    cursor_style = "pointinghand"

    try:
        output = subprocess.check_output(
            ["defaults", "read", "-g", "AppleInterfaceStyle"],
            stderr=subprocess.DEVNULL
        ).decode().strip()
        theme = "dark"
    except subprocess.CalledProcessError:
        theme = "light"
else:
    cursor_style = "hand2" 

def clear(container):
    for widget in container.winfo_children():
        widget.destroy()

def backBtn(tk, container, page):
    backBtn = tk.Label(container, text="<", font=("Arial", 24, "bold"), cursor=cursor_style)
    backBtn.place(x=15, y=10)
    backBtn.bind("<Button-1>", page)