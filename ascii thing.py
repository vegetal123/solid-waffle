import tkinter as tk

def encrypt_input():
    user_input = entry.get()
    ascii_codes = [ord(char) for char in user_input]
    encrypted_chars = [chr(code - 1) for code in ascii_codes]
    
    ascii_str = ' '.join(str(code) for code in ascii_codes)
    encrypted_str = ''.join(encrypted_chars)
    
    ascii_label.config(text=f"ASCII Code: {ascii_str}")
    encrypted_label.config(text=f"Encrypted String: {encrypted_str}")

root = tk.Tk()
root.title("ASCII Encryption Tool")
root.geometry("400x200")
root.configure(bg='lightblue')

entry = tk.Entry(root)
entry.place(x=150, y=20)

ascii_label = tk.Label(root, text="ASCII Code: ", bg='lightblue')
ascii_label.place(x=20, y=80)
encrypted_label = tk.Label(root, text="Encrypted String: ", bg='lightblue')
encrypted_label.place(x=20, y=120)

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_input, fg='white', bg='black')
encrypt_button.place(x=170, y=50)

root.mainloop()
s