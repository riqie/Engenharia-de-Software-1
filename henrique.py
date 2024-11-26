import tkinter as tk
import os
import sys

def desligar_computador():
    
    if sys.platform == "win32":
        os.system("shutdown /s /f /t 0")  
    elif sys.platform == "darwin":
        
        os.system("sudo shutdown -h now")  
    else:
        os.system("shutdown now")  


janela = tk.Tk()
janela.title("henrique")


botao_desligar = tk.Button(janela, text="henrique", command=desligar_computador, font=("Arial", 20), fg="red", bg="black")
botao_desligar.pack(padx=50, pady=50)


janela.mainloop()
