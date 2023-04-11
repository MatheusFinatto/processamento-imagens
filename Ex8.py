import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import cv2

# Variáveis para armazenar as imagens escolhidas
img_p_arr = None
img_q_arr = None

# Define a função para escolher a imagem P
def escolher_imagem_p():
    global img_p_arr
    
    # Abre o diálogo para escolher o arquivo
    arquivo = filedialog.askopenfilename(filetypes=[('Imagens', '*.png;*.jpg;*.bmp')])
    
    # Carrega a imagem e transforma em um array numpy
    img_p = Image.open(arquivo)
    img_p_arr = np.array(img_p)
    
    # Exibe a imagem escolhida na janela
    img_p_tk = ImageTk.PhotoImage(img_p)
    imagem_p.config(image=img_p_tk)
    imagem_p.image = img_p_tk

# Define a função para escolher a imagem Q
def escolher_imagem_q():
    global img_q_arr
    
    # Abre o diálogo para escolher o arquivo
    arquivo = filedialog.askopenfilename(filetypes=[('Imagens', '*.png;*.jpg;*.bmp')])
    
    # Carrega a imagem e transforma em um array numpy
    img_q = Image.open(arquivo)
    img_q_arr = np.array(img_q)
    
    # Exibe a imagem escolhida na janela
    img_q_tk = ImageTk.PhotoImage(img_q)
    imagem_q.config(image=img_q_tk)
    imagem_q.image = img_q_tk

# Define a função para calcular a operação escolhida
def calcular_operacao(operacao):
    global img_p_arr, img_q_arr

    # Verifica se as imagens foram escolhidas
    if img_p_arr is None or img_q_arr is None:
        messagebox.showerror('Erro', 'As imagens P e Q devem ser escolhidas')
        return

    # Verifica se as imagens têm as mesmas dimensões
    if img_p_arr.shape != img_q_arr.shape:
        messagebox.showerror('Erro', 'As imagens devem ter as mesmas dimensões')
        return


    # Calcula a operação escolhida
    if operacao == 'Soma':
        altura, largura = img_p_arr.shape
        img_r_arr = np.zeros((altura, largura), dtype=np.uint8)
        for i in range(altura):
            for j in range(largura):
                    img_r_arr[i, j] = img_p_arr[i, j] + img_q_arr[i, j]

    elif operacao == 'Subtração':
        altura, largura = img_p_arr.shape
        img_r_arr = np.zeros((altura, largura), dtype=np.uint8)
        for i in range(altura):
            for j in range(largura):
                    img_r_arr[i, j] = img_p_arr[i, j] - img_q_arr[i, j]

    elif operacao == 'Multiplicação':
        altura, largura = img_p_arr.shape
        img_r_arr = np.zeros((altura, largura), dtype=np.uint8)
        for i in range(altura):
            for j in range(largura):
                    img_r_arr[i, j] = img_p_arr[i, j] * img_q_arr[i, j]
    elif operacao == 'Divisão':
        altura, largura = img_p_arr.shape
        img_r_arr = np.zeros((altura, largura), dtype=np.uint8)
        for i in range(altura):
            for j in range(largura):
                    img_r_arr[i, j] = img_p_arr[i, j] + img_q_arr[i, j]        
        img_r_arr = np.clip(np.round(img_r_arr), 0, 255).astype(np.uint8)

    elif operacao == 'Blending':
        img_r_arr = cv2.addWeighted(img_p_arr, 0.5, img_q_arr, 0.5, 0)

    elif operacao == 'AND':
        img_r_arr = cv2.bitwise_and(img_p_arr, img_q_arr)

    elif operacao == 'OR':
        img_r_arr = cv2.bitwise_or(img_p_arr, img_q_arr)

    elif operacao == 'XOR':
        img_r_arr = cv2.bitwise_xor(img_p_arr, img_q_arr)
        
    elif operacao == 'NOT':
        img_r_arr = cv2.bitwise_not(img_p_arr)
    else:
        return

    # Transforma o array de volta em uma imagem
    img_r = Image.fromarray(img_r_arr)
    img_r = img_r.convert('L')

    # Exibe a imagem resultante na janela
    img_r_tk = ImageTk.PhotoImage(img_r)
    imagem_r.config(image=img_r_tk)
    imagem_r.image = img_r_tk
   
    
    # Verifica se as imagens foram escolhidas
    if img_p_arr is None or img_q_arr is None:
        messagebox.showerror('Erro', 'As imagens P e Q devem ser escolhidas')
        return
    
    # Verifica se as imagens têm as mesmas dimensões
    if img_p_arr.shape != img_q_arr.shape:
        messagebox.showerror('Erro', 'As imagens devem ter as mesmas dimensões')
        return
    
    # Transforma o array de volta em uma imagem
    img_r = Image.fromarray(img_r_arr)
    img_r = img_r.convert('L')
    
    # Exibe a imagem resultante na janela
    img_r_tk = ImageTk.PhotoImage(img_r)
    imagem_r.config(image=img_r_tk)
    imagem_r.image = img_r_tk

# Cria a janela principal
janela = tk.Tk()
janela.title('Operações com imagens')

# Cria o menu de operações
menu_operacoes = ttk.Combobox(janela, values=['Soma', 'Subtração', 'Multiplicação', 'Divisão', 'Blending', 'AND', 'OR', 'XOR', 'NOT'])

menu_operacoes.grid(row=0, column=0)

# Cria os botões para escolher as imagens
botao_escolher_p = tk.Button(janela, text='Escolher imagem P', command=escolher_imagem_p)
botao_escolher_p.grid(row=1, column=0, padx=10, pady=10)

botao_escolher_q = tk.Button(janela, text='Escolher imagem Q', command=escolher_imagem_q)
botao_escolher_q.grid(row=1, column=1, padx=10, pady=10)

# Cria o botão para calcular a operação escolhida
botao_calcular = tk.Button(janela, text='Calcular', command=lambda: calcular_operacao(menu_operacoes.get()))
botao_calcular.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Cria as labels para exibir as imagens escolhidas e resultante
imagem_p = tk.Label(janela)
imagem_p.grid(row=3, column=0)

imagem_q = tk.Label(janela)
imagem_q.grid(row=3, column=1)

imagem_r = tk.Label(janela)
imagem_r.grid(row=3, column=2)

# Configura a janela principal
janela.geometry('800x600')
janela.mainloop()
