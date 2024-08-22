from tkinter import *
from tkinter import messagebox, Toplevel
import PIL
from PIL import Image,ImageFilter
import ast

def signin():
    username = user.get()
    password = code.get()

    with open('datasheet.txt', 'r') as file:
        d = file.read()
        r = ast.literal_eval(d)

    if username in r.keys() and password == r[username]:
        root.withdraw()  # Hide the login screen
        screen = Toplevel(root)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg="white")
        Label(screen, text="Working start", bg='#fff', font=('calibri(Body)', 50, 'bold')).pack(expand=True)

        def on_close():
            screen.destroy()
            root.destroy()  # Close the login screen and exit the application

        screen.protocol("WM_DELETE_WINDOW", on_close)
        screen.mainloop()
    else:
        messagebox.showerror('Invalid', 'Invalid username or password')

def signup_command():
    root.withdraw()  # Hide the login screen
    signup_screen()

def signup_screen():
    global img  # Globalize the image variable to ensure it persists
    window = Toplevel()
    window.title('Sign Up')
    window.geometry('925x500+300+200')
    window.configure(bg='#fff')
    window.resizable(False, False)

    def signup():
        username = user.get()
        password = code.get()
        confirm_password = confirm_code.get()

        if password == confirm_password:
            try:
                with open('datasheet.txt', 'r+') as file:
                    d = file.read()
                    r = ast.literal_eval(d)

                    dict2 = {username: password}
                    r.update(dict2)
                    file.seek(0)
                    file.write(str(r))
                    file.truncate()

                messagebox.showinfo('Signup', 'Successfully signed up')

            except:
                with open('datasheet.txt', 'w') as file:
                    pp = str({'username': 'password'})
                    file.write(pp)

        else:
            messagebox.showerror('Invalid', "Both passwords should match")

    def sign():
        window.destroy()  # Destroy the signup screen
        root.deiconify()  # Show the login screen again

    Label(window, image=img, border=0, bg='white').place(x=50, y=90)

    frame = Frame(window, width=350, height=390, bg='white')
    frame.place(x=480, y=50)

    heading = Label(frame, text='Sign Up', fg="#57a1f8", bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
    heading.place(x=100, y=5)

    user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    user.place(x=30, y=80)
    user.insert(0, 'username')
    user.bind("<FocusIn>", lambda e: user.delete(0, 'end'))
    user.bind("<FocusOut>", lambda e: user.insert(0, 'username') if user.get() == '' else None)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

    code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    code.place(x=30, y=150)
    code.insert(0, 'password')
    code.bind("<FocusIn>", lambda e: code.delete(0, 'end'))
    code.bind("<FocusOut>", lambda e: code.insert(0, 'password') if code.get() == '' else None)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

    confirm_code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    confirm_code.place(x=30, y=220)
    confirm_code.insert(0, 'confirm password')
    confirm_code.bind("<FocusIn>", lambda e: confirm_code.delete(0, 'end'))
    confirm_code.bind("<FocusOut>",
                      lambda e: confirm_code.insert(0, 'confirm password') if confirm_code.get() == '' else None)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

    Button(frame, width=39, pady=7, text='Sign Up', bg='#57a1f8', fg='white', border=0, command=signup).place(x=35, y=280)
    label = Label(frame, text='I have an account', fg='black', bg='white', font=('Microsoft Yahei UI Light', 9))
    label.place(x=90, y=340)

    signin = Button(frame, width=6, text='Sign in', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=sign)
    signin.place(x=200, y=340)

root = Tk()
root.title('SMS Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)
# Globalize the img to ensure it persists
global img
img = Image.open("login.png")

re_img = img.resize((100, 225))
re_img.show()

root.mainloop()

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)
heading = Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', lambda e: user.delete(0, 'end'))
user.bind('<FocusOut>', lambda e: user.insert(0, 'Username') if user.get() == '' else None)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

code = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', lambda e: code.delete(0, 'end'))
code.bind('<FocusOut>', lambda e: code.insert(0, 'Password') if code.get() == '' else None)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=signin).place(x=35, y=204)
label = Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=75, y=270)

sign_up = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8',
                 command=signup_command)
sign_up.place(x=215, y=270)

root.mainloop()