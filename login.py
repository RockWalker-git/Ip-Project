from tkinter import ttk, messagebox,font
import tkinter as t
window = t.Tk()
style = ttk.Style()

def validate_login(username, password):
    # Adding validation logic here
    if username == "admin" and password == "12345":
        messagebox.showinfo("Login info", "Welcome Admin!")
        return True
    else:
        messagebox.showinfo("Login info", "Incorrect credentials")
        window.destroy()
        return False
    

def resize(event):
    # Calculate new font size based on window size
    new_size = max(8, min(int(event.width / 50), int(event.height / 30)))
    style.configure("TButton", font=("Rockwell", new_size))
    style.configure("TEntry", font=("Rockwell", new_size))

window.bind('<Configure>', resize)   

def create_login_window():
    window.title("Login Screen")
    window.geometry('800x600') 
    window.resizable(True, True)
    # background color
    window.configure(bg='#61A0AF')

    # style creation
    style = ttk.Style()
    style.configure("TEntry",
                    foreground="#F06C9B",
                    fieldbackground="#F06C9B",
                    bordercolor="#F06C9B",
                    lightcolor="#F06C9B",
                    darkcolor="#F06C9B",
                    borderwidth=20,
                    relief="groove",
                    font=("Rockwell", 14))

    style.configure("TButton",
                    background="#F5D491",
                    foreground="black",
                    borderwidth=20,
                    relief="groove",
                    font=("Rockwell", 14))

    username_label = ttk.Label(window, text="Username", font=("Rockwell", 14), background='#61A0AF', foreground="blue",anchor='center', justify='center')
    username_label.pack(fill=t.BOTH, expand=1)
    username_entry = ttk.Entry(window,style='TEntry')
    username_entry.pack(fill=t.BOTH, expand=1)

    password_label = ttk.Label(window, text="Password",font=("Rockwell", 14), background='#61A0AF', foreground="blue",anchor='center', justify='center')
    password_label.pack(fill=t.BOTH, expand=1)
    password_entry = ttk.Entry(window,style="TEntry",show="*")
    password_entry.pack(fill=t.BOTH, expand=1)

    submit_button = ttk.Button(window, text="Login",style="TButton", command=lambda: validate_login(username_entry.get(), password_entry.get()))
    submit_button.pack(fill=t.BOTH, expand=1)
    window.mainloop()
    
 