from PIL import Image, ImageTk, ImageChops
import tkinter.messagebox as messagebox
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk


def abrir_imagem1():
    global imagem1, imagem1_tk
    caminho_imagem1 = filedialog.askopenfilename()
    if caminho_imagem1:
        imagem1 = Image.open(caminho_imagem1)
        imagem1_tk = ImageTk.PhotoImage(imagem1)
        botao_imagem1.config(text="Imagem 1 selecionada: " + caminho_imagem1)
        label_imagem1.config(image=imagem1_tk)


def abrir_imagem2():
    global imagem2, imagem2_tk
    caminho_imagem2 = filedialog.askopenfilename()
    if caminho_imagem2:
        imagem2 = Image.open(caminho_imagem2)
        imagem2_tk = ImageTk.PhotoImage(imagem2)
        botao_imagem2.config(text="Imagem 2 selecionada: " + caminho_imagem2)
        label_imagem2.config(image=imagem2_tk)


def somar_imagens():
    global imagem1, imagem2, resultado, resultado_tk
    if imagem1 and imagem2:  # verifica se as duas imagens foram selecionadas
        if imagem1.size == imagem2.size:  # verifica se as imagens têm o mesmo tamanho
            # cria uma imagem vazia com o mesmo modo e tamanho das imagens originais
            resultado = Image.new(imagem1.mode, imagem1.size)
            if imagem1.mode == 'RGB' or imagem1.mode == 'RGBA':  # se a imagem for RGB
                for i in range(imagem1.width):
                    for j in range(imagem1.height):
                        # obtém o pixel da imagem 1 na posição (i,j)
                        pixel1 = imagem1.getpixel((i, j))
                        # obtém o pixel da imagem 2 na posição (i,j)
                        pixel2 = imagem2.getpixel((i, j))
                        # somar os valores dos canais RGB individualmente, com checagem de truncamento
                        novo_pixel = (min(pixel1[0] + pixel2[0], 255),
                                      min(pixel1[1] + pixel2[1], 255),
                                      min(pixel1[2] + pixel2[2], 255),)
                        # atribui o novo pixel à imagem resultante na posição (i,j)
                        resultado.putpixel((i, j), novo_pixel)
            elif imagem1.mode == 'L':  # se a imagem for escala de cinza
                for i in range(imagem1.width):
                    for j in range(imagem1.height):
                        # obtém o pixel da imagem 1 na posição (i,j)
                        pixel1 = imagem1.getpixel((i, j))
                        # obtém o pixel da imagem 2 na posição (i,j)
                        pixel2 = imagem2.getpixel((i, j))
                        # somar os valores dos canais de escala de cinza, com checagem de truncamento
                        novo_pixel = min(pixel1 + pixel2, 255)
                        # atribui o novo pixel à imagem resultante na posição (i,j)
                        resultado.putpixel((i, j), novo_pixel)
            else:
                messagebox.showerror(
                    "Erro", "O modo da imagem não é suportado.")  # exibe uma mensagem de erro se o modo da imagem não for suportado
                return
            # cria uma nova imagem Tkinter com a imagem resultante
            resultado_tk = ImageTk.PhotoImage(resultado)
            # exibe uma mensagem de sucesso
            messagebox.showinfo("Sucesso", "Imagens somadas com sucesso.")
            # exibe a imagem resultante no widget Label
            label_resultado.config(image=resultado_tk)
        else:
            messagebox.showerror(
                "Erro", "As imagens precisam ter o mesmo tamanho.")  # exibe uma mensagem de erro se as imagens não tiverem o mesmo tamanho
    else:
        # exibe uma mensagem de erro se as imagens não foram selecionadas
        messagebox.showerror("Erro", "Selecione duas imagens.")


def subtrair_imagens():
    global imagem1, imagem2, resultado, resultado_tk
    if imagem1 and imagem2:  # verifica se as duas imagens foram selecionadas
        if imagem1.size == imagem2.size:  # verifica se as imagens têm o mesmo tamanho
            # cria uma imagem vazia com o mesmo modo e tamanho das imagens originais
            resultado = Image.new(imagem1.mode, imagem1.size)
            if imagem1.mode == 'RGB' or imagem1.mode == 'RGBA':  # se a imagem for RGB
                for i in range(imagem1.width):
                    for j in range(imagem1.height):
                        # obtém o pixel da imagem 1 na posição (i,j)
                        pixel1 = imagem1.getpixel((i, j))
                        # obtém o pixel da imagem 2 na posição (i,j)
                        pixel2 = imagem2.getpixel((i, j))
                        # subtrai os valores dos canais RGB individualmente
                        novo_pixel = (max(pixel1[0] - pixel2[0], 0),
                                      max(pixel1[1] - pixel2[1], 0),
                                      max(pixel1[2] - pixel2[2], 0),)
                        # atribui o novo pixel à imagem resultante na posição (i,j)
                        resultado.putpixel((i, j), novo_pixel)
            elif imagem1.mode == 'L':  # se a imagem for escala de cinza
                for i in range(imagem1.width):
                    for j in range(imagem1.height):
                        # obtém o pixel da imagem 1 na posição (i,j)
                        pixel1 = imagem1.getpixel((i, j))
                        # obtém o pixel da imagem 2 na posição (i,j)
                        pixel2 = imagem2.getpixel((i, j))
                        # subtrai os valores dos canais de escala de cinza
                        novo_pixel = max(pixel1 - pixel2, 0)
                        # atribui o novo pixel à imagem resultante na posição (i,j)
                        resultado.putpixel((i, j), novo_pixel)
            else:
                messagebox.showerror(
                    "Erro", "O modo da imagem não é suportado.")  # exibe uma mensagem de erro se o modo da imagem não for suportado
                return
            # cria uma nova imagem Tkinter com a imagem resultante
            resultado_tk = ImageTk.PhotoImage(resultado)
            # exibe uma mensagem de sucesso
            messagebox.showinfo("Sucesso", "Imagens subtraídas com sucesso.")
            # exibe a imagem resultante no widget Label
            label_resultado.config(image=resultado_tk)
        else:
            messagebox.showerror(
                "Erro", "As imagens precisam ter o mesmo tamanho.")  # exibe uma mensagem de erro se as imagens não tiverem o mesmo tamanho
    else:
        # exibe uma mensagem de erro se as imagens não foram selecionadas
        messagebox.showerror("Erro", "Selecione duas imagens.")


def multiplicar_imagens():
    global imagem1, imagem2, resultado, resultado_tk
    if imagem1 and imagem2:  # verifica se as duas imagens foram selecionadas
        if imagem1.size == imagem2.size:  # verifica se as imagens têm o mesmo tamanho
            # cria uma imagem vazia com o mesmo modo e tamanho das imagens originais
            resultado = Image.new(imagem1.mode, imagem1.size)
            if imagem1.mode == 'RGB' or imagem1.mode == 'RGBA':  # se a imagem for RGB
                for i in range(imagem1.width):
                    for j in range(imagem1.height):
                        # obtém o pixel da imagem 1 na posição (i,j)
                        pixel1 = imagem1.getpixel((i, j))
                        # obtém o pixel da imagem 2 na posição (i,j)
                        pixel2 = imagem2.getpixel((i, j))
                        # multiplica os valores dos canais RGB individualmente
                        novo_pixel = (min(pixel1[0] * pixel2[0], 255),
                                      min(pixel1[1] * pixel2[1], 255),
                                      min(pixel1[2] * pixel2[2], 255),)
                        # atribui o novo pixel à imagem resultante na posição (i,j)
                        resultado.putpixel((i, j), novo_pixel)
            elif imagem1.mode == 'L':  # se a imagem for escala de cinza
                for i in range(imagem1.width):
                    for j in range(imagem1.height):
                        # obtém o pixel da imagem 1 na posição (i,j)
                        pixel1 = imagem1.getpixel((i, j))
                        # obtém o pixel da imagem 2 na posição (i,j)
                        pixel2 = imagem2.getpixel((i, j))
                        # multiplica os valores dos canais de escala de cinza
                        novo_pixel = min(pixel1 * pixel2, 255)
                        # atribui o novo pixel à imagem resultante na posição (i,j)
                        resultado.putpixel((i, j), novo_pixel)
            else:
                messagebox.showerror(
                    "Erro", "O modo da imagem não é suportado.")  # exibe uma mensagem de erro se o modo da imagem não for suportado
                return
            # cria uma nova imagem Tkinter com a imagem resultante
            resultado_tk = ImageTk.PhotoImage(resultado)
            # exibe uma mensagem de sucesso
            messagebox.showinfo(
                "Sucesso", "Imagens multiplicadas com sucesso.")
            # exibe a imagem resultante no widget Label
            label_resultado.config(image=resultado_tk)
        else:
            messagebox.showerror(
                "Erro", "As imagens precisam ter o mesmo tamanho.")  # exibe uma mensagem de erro se as imagens não tiverem o mesmo tamanho
    else:
        # exibe uma mensagem de erro se as imagens não foram selecionadas
        messagebox.showerror("Erro", "Selecione duas imagens.")


def dividir_imagens():
    global imagem1, imagem2, resultado, resultado_tk
    if imagem1 and imagem2:  # verifica se as duas imagens foram selecionadas
        if imagem1.size == imagem2.size:  # verifica se as imagens têm o mesmo tamanho
            # cria uma imagem vazia com o mesmo modo e tamanho das imagens originais
            resultado = Image.new(imagem1.mode, imagem1.size)
            if imagem1.mode == 'RGB' or imagem1.mode == 'RGBA':  # se a imagem for RGB
                for i in range(imagem1.width):
                    for j in range(imagem1.height):
                        # obtém o pixel da imagem 1 na posição (i,j)
                        pixel1 = imagem1.getpixel((i, j))
                        # obtém o pixel da imagem 2 na posição (i,j)
                        pixel2 = imagem2.getpixel((i, j))
                        # divide os valores dos canais RGB individualmente, mas verifica se o valor do divisor é zero para evitar divisão por zero
                        novo_pixel = (pixel1[0] // max(pixel2[0], 1),
                                      pixel1[1] // max(pixel2[1], 1),
                                      pixel1[2] // max(pixel2[2], 1))
                        # atribui o novo pixel à imagem resultante na posição (i,j)
                        resultado.putpixel((i, j), novo_pixel)
            elif imagem1.mode == 'L':  # se a imagem for escala de cinza
                for i in range(imagem1.width):
                    for j in range(imagem1.height):
                        # obtém o pixel da imagem 1 na posição (i,j)
                        pixel1 = imagem1.getpixel((i, j))
                        # obtém o pixel da imagem 2 na posição (i,j)
                        pixel2 = imagem2.getpixel((i, j))
                        # divide os valores dos canais de escala de cinza, mas verifica se o valor do divisor é zero para evitar divisão por zero
                        novo_pixel = pixel1 // max(pixel2, 1)
                        # atribui o novo pixel à imagem resultante na posição (i,j)
                        resultado.putpixel((i, j), novo_pixel)
            else:
                messagebox.showerror(
                    "Erro", "O modo da imagem não é suportado.")  # exibe uma mensagem de erro se o modo da imagem não for suportado
                return
            # cria uma nova imagem Tkinter com a imagem resultante
            resultado_tk = ImageTk.PhotoImage(resultado)
            # exibe uma mensagem de sucesso
            messagebox.showinfo("Sucesso", "Imagens divididas com sucesso.")
            # exibe a imagem resultante no widget Label
            label_resultado.config(image=resultado_tk)
        else:
            messagebox.showerror(
                "Erro", "As imagens precisam ter o mesmo tamanho.")  # exibe uma mensagem de erro se as imagens não tiverem o mesmo tamanho
    else:
        # exibe uma mensagem de erro se as imagens não foram selecionadas
        messagebox.showerror("Erro", "Selecione duas imagens.")


def salvar_resultado():
    global resultado
    if resultado:
        caminho_salvar = filedialog.asksaveasfilename(
            filetypes=[("Imagens", "*.jpg;*.png")], defaultextension=".png")
        if caminho_salvar:
            resultado.save(caminho_salvar)
            messagebox.showinfo("Sucesso", "Resultado salvo com sucesso.")
    else:
        messagebox.showerror(
            "Erro", "Some as imagens antes de salvar o resultado.")


imagem1 = None
imagem2 = None
resultado = None
imagem1_tk = None
imagem2_tk = None
resultado_tk = None

root = Tk()
root.title("Somador de imagens")

# Criar um Canvas com barras de rolagem
container1 = Frame(root)
container1.pack()

botao_imagem1 = Button(
    container1, text="Selecionar imagem 1", command=abrir_imagem1)
botao_imagem1.pack(side=LEFT)

botao_imagem2 = Button(
    container1, text="Selecionar imagem 2", command=abrir_imagem2)
botao_imagem2.pack(side=LEFT)

container2 = Frame(root)
container2.pack(pady=10)

botao_somar = Button(container2, text="Somar", command=somar_imagens)
botao_somar.pack(side=LEFT)

botao_subtrair = Button(container2, text="Subtrair", command=subtrair_imagens)
botao_subtrair.pack(side=LEFT)

botao_multiplicar = Button(
    container2, text="Multiplicar", command=multiplicar_imagens)
botao_multiplicar.pack(side=LEFT)

botao_dividir = Button(container2, text="Dividir", command=dividir_imagens)
botao_dividir.pack(side=RIGHT)

container4 = Frame(root)
container4.pack()

botao_salvar = Button(container4, text="Salvar resultado",
                      command=salvar_resultado)
botao_salvar.pack(side=TOP)

container3 = Frame(root)
container3.pack(pady=10, fill=BOTH, expand=True)

label_imagem1 = Label(container3)
label_imagem1.pack(side=LEFT, padx=10)

label_imagem2 = Label(container3)
label_imagem2.pack(side=LEFT, padx=10)

label_resultado = Label(root)
label_resultado.pack(pady=10)


root.mainloop()
