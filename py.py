import tkinter as tk
from tkinter import messagebox
import speedtest

def run_speedtest():
    try:
        st = speedtest.Speedtest()
        st.download()  # Testa a velocidade de download
        st.upload()  # Testa a velocidade de upload
        ping = st.results.ping  # Obtém o valor do ping

        # Formata os resultados
        download_speed = st.results.download / 1_000_000  # Mbps
        upload_speed = st.results.upload / 1_000_000  # Mbps

        # Atualiza os rótulos com os resultados
        download_label.config(text=f"Velocidade de Download: {download_speed:.2f} Mbps")
        upload_label.config(text=f"Velocidade de Upload: {upload_speed:.2f} Mbps")
        ping_label.config(text=f"Ping: {ping:.2f} ms")
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível realizar o teste de velocidade: {e}")

# Configuração da janela principal
root = tk.Tk()
root.title("Teste de Velocidade de Internet")
root.geometry("300x200")

# Rótulos para exibir os resultados
download_label = tk.Label(root, text="Velocidade de Download: - Mbps")
download_label.pack(pady=10)

upload_label = tk.Label(root, text="Velocidade de Upload: - Mbps")
upload_label.pack(pady=10)

ping_label = tk.Label(root, text="Ping: - ms")
ping_label.pack(pady=10)

# Botão para iniciar o teste
test_button = tk.Button(root, text="Iniciar Teste de Velocidade", command=run_speedtest)
test_button.pack(pady=20)

# Inicia o loop da interface gráfica
root.mainloop()
