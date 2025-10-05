import tkinter as tk
from tkinter import messagebox
import settings.universal as univ
import firebase_admin
from firebase_admin import credentials, auth
import requests, json

root = tk.Tk()
root.title("PyProfile")
root.geometry("400x600")
root.resizable(False, False)

if not firebase_admin._apps:
    cred = credentials.Certificate("data/serviceAccountKey.json")
    firebase_admin.initialize_app(cred)

def login_page(event=None):
    showPass = "*"
    def tooglePass(event):
        nonlocal showPass
        if showPass == "*":
            showPass = ""
            print("Show Pass")
        else:
            showPass = "*"
            print("Hide Pass")
        
        pass_input.config(show=showPass)
        passBtn.config(text="Show" if showPass == "*" else "Hide")
    print("login")
    univ.clear(root)
    univ.backBtn(tk, root, main_page)

    title = tk.Label(root, text="Login", font=("Arial", 40, "bold"))
    title.pack(pady=(10, 0))
    subtitle = tk.Label(root, text="Log back into your existing profile", font=("Arial", 16), fg="#808080")
    subtitle.pack()

    email_frame = tk.Frame(root, width=400, height=100)
    email_frame.pack(fill="x", pady=(100, 0))
    email_text = tk.Label(email_frame, text="Email:        ", font=("Arial", 15))
    email_text.pack(side="left", padx=(65, 0))
    email_input = tk.Entry(email_frame, width=30)
    email_input.pack(side="right", padx=(0, 65))

    pass_frame = tk.Frame(root, width=400, height=100)
    pass_frame.pack(fill="x")
    pass_text = tk.Label(pass_frame, text="Password: ", font=("Arial", 15))
    pass_text.pack(side="left", padx=(65, 0))
    passBtn = tk.Label(pass_frame, text=("Show" if showPass == "*" else "Hide"), cursor=univ.cursor_style)
    passBtn.pack(side="right", padx=(0, 65))
    passBtn.bind("<Button-1>", tooglePass)
    pass_input = tk.Entry(pass_frame, width=30, show="*")
    pass_input.pack(side="right")

    def loginacc(event):
        email = email_input.get()
        password = pass_input.get()
        url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={univ.API_KEY}"
        payload = {
            "email": email,
            "password": password,
            "returnSecureToken": True
        }

        res = requests.post(url, json=payload)
        data = res.json()
        if "idToken" in data:
            tokenData = {"loginToken": data["refreshToken"]}
            with open("data/account.json", 'w', encoding='utf-8') as f:
                json.dump(tokenData, f, ensure_ascii=False, indent=4)
            account_page()
        else:
            print("Login Failed")

    loginBtn = tk.Label(root, text="Login", font=("Arial", 18, "bold"), cursor=univ.cursor_style)
    loginBtn.pack(pady=(20, 0))
    loginBtn.bind("<Button-1>", loginacc)

    root.update_idletasks()

def signup_page(event=None):
    showPass = "*"
    def tooglePass(event):
        nonlocal showPass
        if showPass == "*":
            showPass = ""
            print("Show Pass")
        else:
            showPass = "*"
            print("Hide Pass")
        
        pass_input.config(show=showPass)
        passBtn.config(text="Show" if showPass == "*" else "Hide")
    print("signup")
    univ.clear(root)
    univ.backBtn(tk, root, main_page)

    title = tk.Label(root, text="Signup", font=("Arial", 40, "bold"))
    title.pack(pady=(10, 0))
    subtitle = tk.Label(root, text="Create an account to... have a profile", font=("Arial", 16), fg="#808080")
    subtitle.pack()

    name_frame = tk.Frame(root, width=400, height=100)
    name_frame.pack(fill="x", pady=(100, 0))
    name_text = tk.Label(name_frame, text="Full Name: ", font=("Arial", 15))
    name_text.pack(side="left", padx=(65, 0))
    name_input = tk.Entry(name_frame, width=30)
    name_input.pack(side="right", padx=(0, 65))

    email_frame = tk.Frame(root, width=400, height=100)
    email_frame.pack(fill="x")
    email_text = tk.Label(email_frame, text="Email:        ", font=("Arial", 15))
    email_text.pack(side="left", padx=(65, 0))
    email_input = tk.Entry(email_frame, width=30)
    email_input.pack(side="right", padx=(0, 65))

    pass_frame = tk.Frame(root, width=400, height=100)
    pass_frame.pack(fill="x")
    pass_text = tk.Label(pass_frame, text="Password: ", font=("Arial", 15))
    pass_text.pack(side="left", padx=(65, 0))
    passBtn = tk.Label(pass_frame, text=("Show" if showPass == "*" else "Hide"), cursor=univ.cursor_style)
    passBtn.pack(side="right", padx=(0, 65))
    passBtn.bind("<Button-1>", tooglePass)
    pass_input = tk.Entry(pass_frame, width=30, show="*")
    pass_input.pack(side="right")

    def createacc(event):
        name = name_input.get()
        email = email_input.get()
        password = pass_input.get()

        user = auth.create_user(
            email=email,
            password=password,
            display_name=name
        )

        url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={univ.API_KEY}"
        payload = {
            "email": email,
            "password": password,
            "returnSecureToken": True
        }

        res = requests.post(url, json=payload)
        data = res.json()

        tokenData = {"loginToken": data["refreshToken"]}
        with open("data/account.json", 'w', encoding='utf-8') as f:
            json.dump(tokenData, f, ensure_ascii=False, indent=4)
        
        account_page()

    createBtn = tk.Label(root, text="Create Account", font=("Arial", 18, "bold"), cursor=univ.cursor_style)
    createBtn.pack(pady=(20, 0))
    createBtn.bind("<Button-1>", createacc)

    root.update_idletasks()
 
def main_page(event=None):
    univ.clear(root)

    title = tk.Label(root, text="PyProfile", font=("Arial", 40, "bold"))
    title.pack(pady=(10, 0))
    subtitle = tk.Label(root, text="Where you can't really do much but have a profile", font=("Arial", 16), fg="#808080")
    subtitle.pack()

    loginBtn = tk.Label(root, text="Login", font=("Arial", 24, "bold"), cursor=univ.cursor_style)
    loginBtn.pack(pady=(100, 0))
    loginBtn.bind("<Button-1>", login_page)

    signupBtn = tk.Label(root, text="Signup", font=("Arial", 24, "bold"), cursor=univ.cursor_style)
    signupBtn.pack(pady=(20, 0))
    signupBtn.bind("<Button-1>", signup_page)

    quitBtn = tk.Label(root, text="Quit", font=("Arial", 24, "bold"), cursor=univ.cursor_style)
    quitBtn.pack(pady=(20, 0))
    quitBtn.bind("<Button-1>", quit)

    root.mainloop()

def account_page(event=None):
    print("account")
    univ.clear(root)

    with open("data/account.json", "r") as f:
        accData = json.load(f)
    refresh_token = accData["loginToken"]

    url = f"https://securetoken.googleapis.com/v1/token?key={univ.API_KEY}"
    payload = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token
    }

    res = requests.post(url, data=payload)
    new_data = res.json()
    uid = new_data["user_id"]

    user = auth.get_user(uid)

    title = tk.Label(root, text=f"Welcome, {user.display_name.split()[0]}", font=("Arial", 30, "bold"))
    title.pack(pady=(10, 0))
    subtitle = tk.Label(root, text=f"Logged in with email: {user.email}", font=("Arial", 12), fg="#808080")
    subtitle.pack()

    def logout(event):
        logout = messagebox.askokcancel("Logout", "Are you sure you want to log out of your account?")
        if logout:
            tokenData = {"loginToken": ""}
            with open("data/account.json", 'w', encoding='utf-8') as f:
                json.dump(tokenData, f, ensure_ascii=False, indent=4)
            
            univ.clear(root)
            main_page()
        else:
            pass

    logoutBtn = tk.Label(root, text="Logout", font=("Arial", 24, "bold"), cursor=univ.cursor_style)
    logoutBtn.pack(pady=(100, 0))
    logoutBtn.bind("<Button-1>", logout)

    def delete(event):
        delete = messagebox.askokcancel("Delete Account", "Are you sure you want to delete your account? This action cannot be undone.")
        if delete:
            tokenData = {"loginToken": ""}
            with open("data/account.json", 'w', encoding='utf-8') as f:
                json.dump(tokenData, f, ensure_ascii=False, indent=4)
            auth.delete_user(user.uid)
            univ.clear(root)
            main_page()
        else:
            pass
    
    deleteBtn = tk.Label(root, text="Delete Account", font=("Arial", 24, "bold"), cursor=univ.cursor_style)
    deleteBtn.pack(pady=(20, 0))
    deleteBtn.bind("<Button-1>", delete)

    root.mainloop()

if __name__ == "__main__":
    main_page()