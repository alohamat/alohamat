#  creating a signup and login screen in tkinter
import tkinter as tk

class SignUp():
    def __init__(self, master):
        self.master = master
        self.master.title("Sign in")
        self.master.geometry("250x100")
        self.master.resizable(False, False)

        self.data = {
            'username':None,
            'password':None
        }

        self.h1 = tk.Label(self.master, text="Create your account")
        self.h1.grid(row=0, column=1)

        self.userText = tk.Label(self.master, text="Username:")
        self.userText.grid(row=1, column=0)

        self.passText = tk.Label(self.master, text="Password:")
        self.passText.grid(row=2, column=0)

        self.userEntry = tk.Entry(self.master)
        self.userEntry.grid(row=1, column=1)

        self.passEntry = tk.Entry(self.master, show='*')
        self.passEntry.grid(row=2, column=1)

        self.submitButton = tk.Button(self.master, text='Create', command=self.store)
        self.submitButton.grid(row=3, column=1)

    def store(self):
        username = self.userEntry.get() # Return values from window to variables
        password = self.passEntry.get()
        self.data.update({'username':username, 'password':password}) # Updates the "server" with new data
        self.master.destroy()
        
class Login():
    def __init__(self, master, signInstance):
        self.master = master
        self.signInstance = signInstance
        self.master.title("Login")
        self.master.geometry("250x120")
        self.master.resizable(False, False)

        self.h1 = tk.Label(self.master, text="Login your account")
        self.h1.grid(row=0, column=1)

        self.userText = tk.Label(self.master, text="Username:")
        self.userText.grid(row=1, column=0)

        self.passText = tk.Label(self.master, text="Password:")
        self.passText.grid(row=2, column=0)

        self.userEntry = tk.Entry(self.master)
        self.userEntry.grid(row=1, column=1)

        self.passEntry = tk.Entry(self.master, show='*')    # using 'show' to hide the password
        self.passEntry.grid(row=2, column=1)

        self.h2 = tk.Label(self.master, text='Waiting for data...', width=25)   # using 'width' to avoid unexpected widget repositioning
        self.h2.grid(row=3, column=1)

        self.submitButton = tk.Button(self.master, text="Submit", command=self.check)
        self.submitButton.grid(row=4, column=1)
    
    def check(self):
        username = self.userEntry.get()
        password = self.passEntry.get()
        if username == self.signInstance.data['username'] and password == self.signInstance.data['password']:
            self.h2.config(text='Successfully logged in!', fg='green')
        else:
            self.h2.config(text='Invalid username or password!', fg='red')


if __name__ == "__main__":
    signRoot = tk.Tk()  # Create a Tk instance, that represents main window
    sign_up = SignUp(signRoot)    # Pass main window instance to 'SignUp' class, which configures UI and creates an instance of class (sign_up)
    signRoot.mainloop() # Initiates window loop, which keeps it open

    loginRoot = tk.Tk()
    Login(loginRoot, sign_up)
    loginRoot.mainloop()
