import tkinter as tk
from PIL import ImageTk
from urllib.request import urlopen
from tkinter import Canvas
import paramiko
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

def executar_comando_ssh(comando):
    # Configuração das informações de conexão SSH
    host = '192.168.0.164'  # Substitua pelo endereço IP ou hostname do seu servidor Debian
    username = 'kali'
    password = 'kali'

    # Criação de uma instância SSHClie
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Conexão SSH
        ssh.connect(host, username=username, password=password)

        # Execução do comando remoto
        stdin, stdout, stderr = ssh.exec_command(comando)

        # Captura da saída do comando
        resultado = stdout.read().decode("utf-8")

        return resultado
    except Exception as e:
        return f"Erro na conexão SSH: {str(e)}"
    finally:
        # Fecha a conexão SSH
        ssh.close()

def on_button_click():
    comando = entry_comando.get()
    resultado = executar_comando_ssh(comando)
    text_resultado.delete(1.0, tk.END)  # Limpa o resultado anterior
    text_resultado.insert(tk.END, resultado)

root = tk.Tk()
root.title("DEDSEC - TOOLS")
root.geometry("338x602")
root.resizable(False, False)

URL = "https://github.com/campoix/WebApp.Organizacao/blob/main/the-matrix-digital-rain.jpg?raw=True"
carregar_image = urlopen(URL)
raw_data = carregar_image.read()
carregar_image.close()
foto = ImageTk.PhotoImage(data=raw_data)
label_image = tk.Label(root, image=foto)
label_image.image = foto
label_image.place(relx=1.0, rely=0.0, anchor="ne")

canvas1 = Canvas(root, width=400, height=400)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(0, 0, image=foto, anchor="nw")

# Entrada para o comando
entry_comando = tk.Entry(root, width=50)
entry_comando.pack(pady=10)

# Botão para executar o comando remoto
btn_executar = tk.Button(root, text="Executar Comando Remoto", command=on_button_click)
btn_executar.pack(pady=10)

# Resultado da execução do comando
text_resultado = tk.Text(root, height=10, width=50)
text_resultado.pack(pady=10)

root.mainloop()