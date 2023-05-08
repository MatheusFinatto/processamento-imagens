from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import numpy as np
from PIL import ImageEnhance


def abrir_imagem1():
    global imagem1, imagem1_tk
    caminho_imagem1 = filedialog.askopenfilename()
    if caminho_imagem1:
        imagem1 = Image.open(caminho_imagem1)

        # Obtém as dimensões da imagem original
        largura_original, altura_original = imagem1.size

        # Define a largura máxima desejada para o widget Label
        largura_maxima = 300

        # Calcula o fator de escala necessário para redimensionar a imagem
        fator_escala = min(1.0, largura_maxima / largura_original)

        # Calcula as novas dimensões da imagem
        largura_nova = int(largura_original * fator_escala)
        altura_nova = int(altura_original * fator_escala)

        # Redimensiona a imagem com o fator de escala calculado
        imagem1 = imagem1.resize((largura_nova, altura_nova))

        # Converte a imagem redimensionada em um objeto PhotoImage do Tkinter
        imagem1_tk = ImageTk.PhotoImage(imagem1)
        botao_imagem1.config(text="Imagem 1 selecionada: " + caminho_imagem1)
        label_imagem1.config(image=imagem1_tk)


def abrir_imagem2():
    global imagem2, imagem2_tk
    caminho_imagem2 = filedialog.askopenfilename()
    if caminho_imagem2:
        imagem2 = Image.open(caminho_imagem2)

        # Obtém as dimensões da imagem original
        largura_original, altura_original = imagem2.size

        # Define a largura máxima desejada para o widget Label
        largura_maxima = 300

        # Calcula o fator de escala necessário para redimensionar a imagem
        fator_escala = min(1.0, largura_maxima / largura_original)

        # Calcula as novas dimensões da imagem
        largura_nova = int(largura_original * fator_escala)
        altura_nova = int(altura_original * fator_escala)

        # Redimensiona a imagem com o fator de escala calculado
        imagem2 = imagem2.resize((largura_nova, altura_nova))

        # Converte a imagem redimensionada em um objeto PhotoImage do Tkinter
        imagem2_tk = ImageTk.PhotoImage(imagem2)
        botao_imagem2.config(text="Imagem 2 selecionada: " + caminho_imagem2)
        label_imagem2.config(image=imagem2_tk)


def operar_imagens(operacao):

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

                        # realiza a operação matemática com os valores dos canais RGB individualmente
                        if operacao == 'toGray':
                            gray_pixel = int(
                                0.2989 * pixel1[0] + 0.5870 * pixel1[1] + 0.1140 * pixel1[2])
                            novo_pixel = (gray_pixel, gray_pixel, gray_pixel)

                        if operacao == 'soma':
                            novo_pixel = (min(pixel1[0] + pixel2[0], 255),
                                          min(pixel1[1] + pixel2[1], 255),
                                          min(pixel1[2] + pixel2[2], 255),)

                        elif operacao == 'subtracao':
                            novo_pixel = (max(pixel1[0] - pixel2[0], 0),
                                          max(pixel1[1] - pixel2[1], 0),
                                          max(pixel1[2] - pixel2[2], 0),)

                        elif operacao == 'multiplicacao':
                            novo_pixel = (min(pixel1[0] * pixel2[0], 255),
                                          min(pixel1[1] * pixel2[1], 255),
                                          min(pixel1[2] * pixel2[2], 255),)

                        elif operacao == 'divisao':
                            novo_pixel = (pixel1[0] // max(pixel2[0], 1),
                                          pixel1[1] // max(pixel2[1], 1),
                                          pixel1[2] // max(pixel2[2], 1))

                        elif operacao == 'and':
                            novo_pixel = (pixel1[0] & pixel2[0],
                                          pixel1[1] & pixel2[1],
                                          pixel1[2] & pixel2[2])

                        elif operacao == 'or':
                            novo_pixel = (pixel1[0] | pixel2[0],
                                          pixel1[1] | pixel2[1],
                                          pixel1[2] | pixel2[2])

                        elif operacao == 'xor':
                            novo_pixel = (pixel1[0] ^ pixel2[0],
                                          pixel1[1] ^ pixel2[1],
                                          pixel1[2] ^ pixel2[2])

                        elif operacao == 'media':
                            novo_pixel = ((pixel1[0] + pixel2[0]) // 2,
                                          (pixel1[1] + pixel2[1]) // 2,
                                          (pixel1[2] + pixel2[2]) // 2)

                        elif operacao == 'blend':
                            alpha = float(campo_alpha.get())
                            novo_pixel = (
                                int(alpha * pixel1[0] +
                                    (1 - alpha) * pixel2[0]),
                                int(alpha * pixel1[1] +
                                    (1 - alpha) * pixel2[1]),
                                int(alpha * pixel1[2] +
                                    (1 - alpha) * pixel2[2])
                            )

                        else:
                            messagebox.showerror(
                                "Erro", "Operação inválida.")  # exibe uma mensagem de erro se a operação for inválida
                            return

                        # atribui o novo pixel à imagem resultante na posição (i,j)
                        resultado.putpixel((i, j), novo_pixel)

            elif imagem1.mode == 'L':  # se a imagem for escala de cinza
                for i in range(imagem1.width):
                    for j in range(imagem1.height):

                        # obtém o pixel da imagem 1 na posição (i,j)
                        pixel1 = imagem1.getpixel((i, j))

                        # obtém o pixel da imagem 2 na posição (i,j)
                        pixel2 = imagem2.getpixel((i, j))

                        # realiza a operação matemática com os valores dos canais de escala de cinza
                        if operacao == 'soma':
                            novo_pixel = min(pixel1 + pixel2, 255)

                        elif operacao == 'subtracao':
                            novo_pixel = max(pixel1 - pixel2, 0)

                        elif operacao == 'multiplicacao':
                            novo_pixel = min(pixel1 * pixel2, 255)

                        elif operacao == 'divisao':
                            novo_pixel = pixel1 // max(pixel2, 1)

                        elif operacao == 'and':
                            novo_pixel = pixel1 & pixel2

                        elif operacao == 'or':
                            novo_pixel = pixel1 | pixel2

                        elif operacao == 'xor':
                            novo_pixel = pixel1 ^ pixel2

                        elif operacao == 'media':
                            novo_pixel = (pixel1 + pixel2) // 2

                        elif operacao == 'blend':
                            alpha = float(campo_alpha.get())
                            novo_pixel = int(alpha*pixel1 + (1-alpha)*pixel2)

                        else:
                            messagebox.showerror(
                                "Erro", "Operação inválida.")  # exibe uma mensagem de erro se a operação for inválida
                            return

                        # atribui o novo pixel à imagem resultante na posição (i,j)
                        resultado.putpixel((i, j), novo_pixel)

            else:
                messagebox.showerror(
                    "Erro", "O modo da imagem não é suportado.")  # exibe uma mensagem de erro se o modo da imagem não for suportado
                return

            # cria uma nova imagem Tkinter com a imagem resultante
            resultado_tk = ImageTk.PhotoImage(resultado)

            # exibe uma mensagem de sucesso
            messagebox.showinfo("Sucesso", "Operação realizada com sucesso.")

            # exibe a imagem resultante no widget Label
            label_resultado.config(image=resultado_tk)

        else:
            messagebox.showerror(
                "Erro", "As imagens precisam ter o mesmo tamanho.")  # exibe uma mensagem de erro se as imagens não tiverem o mesmo tamanho

    else:
        # exibe uma mensagem de erro se as imagens não foram selecionadas
        messagebox.showerror("Erro", "Selecione duas imagens.")


def not_image():
    global imagem1, resultado, resultado_tk
    if imagem1:  # verifica se a imagem foi selecionada

        # cria uma imagem vazia com o mesmo modo e tamanho da imagem original
        resultado = Image.new(imagem1.mode, imagem1.size)

        if imagem1.mode == 'RGB' or imagem1.mode == 'RGBA':  # se a imagem for RGB
            for i in range(imagem1.width):
                for j in range(imagem1.height):

                    # obtém o pixel da imagem 1 na posição (i,j)
                    pixel1 = imagem1.getpixel((i, j))

                    # realiza a operação "not" em cada canal de cor individualmente
                    novo_pixel = (
                        255 - pixel1[0], 255 - pixel1[1], 255 - pixel1[2])
                    # atribui o novo pixel à imagem resultante na posição (i,j)
                    resultado.putpixel((i, j), novo_pixel)

        elif imagem1.mode == 'L':  # se a imagem for escala de cinza
            for i in range(imagem1.width):
                for j in range(imagem1.height):

                    # obtém o pixel da imagem 1 na posição (i,j)
                    pixel1 = imagem1.getpixel((i, j))

                    # realiza a operação "not" no pixel
                    novo_pixel = 255 - pixel1

                    # atribui o novo pixel à imagem resultante na posição (i,j)
                    resultado.putpixel((i, j), novo_pixel)

        else:
            messagebox.showerror(
                "Erro", "O modo da imagem não é suportado.")  # exibe uma mensagem de erro se o modo da imagem não for suportado
            return

        # cria uma nova imagem Tkinter com a imagem resultante
        resultado_tk = ImageTk.PhotoImage(resultado)

        # exibe uma mensagem de sucesso
        messagebox.showinfo("Sucesso", "Imagem invertida com sucesso.")

        # exibe a imagem resultante no widget Label
        label_resultado.config(image=resultado_tk)

    else:
        # exibe uma mensagem de erro se a imagem não foi selecionada
        messagebox.showerror("Erro", "Selecione uma imagem.")


def multiplicar_por_fator():
    global imagem1, resultado, resultado_tk
    if imagem1:  # verifica se a imagem foi selecionada

        # cria uma imagem vazia com o mesmo modo e tamanho da imagem original
        resultado = Image.new(imagem1.mode, imagem1.size)

        if imagem1.mode == 'RGB' or imagem1.mode == 'RGBA':  # se a imagem for RGB
            for i in range(imagem1.width):
                for j in range(imagem1.height):

                    # obtém o pixel da imagem 1 na posição (i,j)
                    pixel1 = imagem1.getpixel((i, j))

                    # realiza a operação "not" em cada canal de cor individualmente
                    fator = float(campo_multiplicacao.get())
                    novo_pixel = (int(min(pixel1[0] * fator, 255)),
                                  int(min(pixel1[1] * fator, 255)),
                                  int(min(pixel1[2] * fator, 255)))
                    # atribui o novo pixel à imagem resultante na posição (i,j)
                    resultado.putpixel((i, j), novo_pixel)

        elif imagem1.mode == 'L':  # se a imagem for escala de cinza
            for i in range(imagem1.width):
                for j in range(imagem1.height):

                    # obtém o pixel da imagem 1 na posição (i,j)
                    pixel1 = imagem1.getpixel((i, j))

                    # realiza a operação "not" no pixel
                    fator = float(campo_multiplicacao.get())
                    novo_pixel = (min(pixel1 * fator, 255))
                    # atribui o novo pixel à imagem resultante na posição (i,j)
                    resultado.putpixel((i, j), novo_pixel)

        else:
            messagebox.showerror(
                "Erro", "O modo da imagem não é suportado.")  # exibe uma mensagem de erro se o modo da imagem não for suportado
            return

        # cria uma nova imagem Tkinter com a imagem resultante
        resultado_tk = ImageTk.PhotoImage(resultado)

        # exibe uma mensagem de sucesso
        messagebox.showinfo("Sucesso", "Imagem multiplicada com sucesso.")

        # exibe a imagem resultante no widget Label
        label_resultado.config(image=resultado_tk)

    else:
        # exibe uma mensagem de erro se a imagem não foi selecionada
        messagebox.showerror("Erro", "Selecione uma imagem.")


def dividir_por_fator():
    global imagem1, resultado, resultado_tk
    if imagem1:  # verifica se a imagem foi selecionada

        # cria uma imagem vazia com o mesmo modo e tamanho da imagem original
        resultado = Image.new(imagem1.mode, imagem1.size)

        if imagem1.mode == 'RGB' or imagem1.mode == 'RGBA':  # se a imagem for RGB
            for i in range(imagem1.width):
                for j in range(imagem1.height):

                    # obtém o pixel da imagem 1 na posição (i,j)
                    pixel1 = imagem1.getpixel((i, j))

                    # realiza a operação "not" em cada canal de cor individualmente
                    fator = float(campo_divisao.get())
                    novo_pixel = (int(max(pixel1[0] / fator, 1)),
                                  int(max(pixel1[1] / fator, 1)),
                                  int(max(pixel1[2] / fator, 1)))
                    # atribui o novo pixel à imagem resultante na posição (i,j)
                    resultado.putpixel((i, j), novo_pixel)

        elif imagem1.mode == 'L':  # se a imagem for escala de cinza
            for i in range(imagem1.width):
                for j in range(imagem1.height):

                    # obtém o pixel da imagem 1 na posição (i,j)
                    pixel1 = imagem1.getpixel((i, j))

                    # realiza a operação "not" no pixel
                    fator = float(campo_divisao.get())
                    novo_pixel = int((max(pixel1 / fator, 0)))

                    # atribui o novo pixel à imagem resultante na posição (i,j)
                    resultado.putpixel((i, j), novo_pixel)

        else:
            messagebox.showerror(
                "Erro", "O modo da imagem não é suportado.")  # exibe uma mensagem de erro se o modo da imagem não for suportado
            return

        # cria uma nova imagem Tkinter com a imagem resultante
        resultado_tk = ImageTk.PhotoImage(resultado)

        # exibe uma mensagem de sucesso
        messagebox.showinfo("Sucesso", "Imagem dividida com sucesso.")

        # exibe a imagem resultante no widget Label
        label_resultado.config(image=resultado_tk)

    else:
        # exibe uma mensagem de erro se a imagem não foi selecionada
        messagebox.showerror("Erro", "Selecione uma imagem.")


def somar_por_fator():
    global imagem1, resultado, resultado_tk
    if imagem1:  # verifica se a imagem foi selecionada

        # cria uma imagem vazia com o mesmo modo e tamanho da imagem original
        resultado = Image.new(imagem1.mode, imagem1.size)

        if imagem1.mode == 'RGB' or imagem1.mode == 'RGBA':  # se a imagem for RGB
            for i in range(imagem1.width):
                for j in range(imagem1.height):

                    # obtém o pixel da imagem 1 na posição (i,j)
                    pixel1 = imagem1.getpixel((i, j))

                    # realiza a operação "not" em cada canal de cor individualmente
                    fator = float(campo_somar_fator.get())
                    novo_pixel = (int(min(pixel1[0] + fator, 255)),
                                  int(min(pixel1[1] + fator, 255)),
                                  int(min(pixel1[2] + fator, 255)))
                    # atribui o novo pixel à imagem resultante na posição (i,j)
                    resultado.putpixel((i, j), novo_pixel)

        elif imagem1.mode == 'L':  # se a imagem for escala de cinza
            for i in range(imagem1.width):
                for j in range(imagem1.height):

                    # obtém o pixel da imagem 1 na posição (i,j)
                    pixel1 = imagem1.getpixel((i, j))

                    # realiza a operação "not" no pixel
                    fator = float(campo_somar_fator.get())
                    novo_pixel = (min(pixel1 + fator, 255))

                    # atribui o novo pixel à imagem resultante na posição (i,j)
                    resultado.putpixel((i, j), novo_pixel)

        else:
            messagebox.showerror(
                "Erro", "O modo da imagem não é suportado.")  # exibe uma mensagem de erro se o modo da imagem não for suportado
            return

        # cria uma nova imagem Tkinter com a imagem resultante
        resultado_tk = ImageTk.PhotoImage(resultado)

        # exibe uma mensagem de sucesso
        messagebox.showinfo("Sucesso", "Imagem dividida com sucesso.")

        # exibe a imagem resultante no widget Label
        label_resultado.config(image=resultado_tk)

    else:
        # exibe uma mensagem de erro se a imagem não foi selecionada
        messagebox.showerror("Erro", "Selecione uma imagem.")


def subtrair_por_fator():
    global imagem1, resultado, resultado_tk
    if imagem1:  # verifica se a imagem foi selecionada

        # cria uma imagem vazia com o mesmo modo e tamanho da imagem original
        resultado = Image.new(imagem1.mode, imagem1.size)

        if imagem1.mode == 'RGB' or imagem1.mode == 'RGBA':  # se a imagem for RGB
            for i in range(imagem1.width):
                for j in range(imagem1.height):

                    # obtém o pixel da imagem 1 na posição (i,j)
                    pixel1 = imagem1.getpixel((i, j))

                    # realiza a operação "not" em cada canal de cor individualmente
                    fator = float(campo_subtracao.get())
                    novo_pixel = (int(max(pixel1[0] - fator, 0)),
                                  int(max(pixel1[1] - fator, 0)),
                                  int(max(pixel1[2] - fator, 0)))
                    # atribui o novo pixel à imagem resultante na posição (i,j)
                    resultado.putpixel((i, j), novo_pixel)

        elif imagem1.mode == 'L':  # se a imagem for escala de cinza
            for i in range(imagem1.width):
                for j in range(imagem1.height):

                    # obtém o pixel da imagem 1 na posição (i,j)
                    pixel1 = imagem1.getpixel((i, j))

                    # realiza a operação "not" no pixel
                    fator = float(campo_subtracao.get())
                    novo_pixel = int((max(pixel1 - fator, 0)))

                    # atribui o novo pixel à imagem resultante na posição (i,j)
                    resultado.putpixel((i, j), novo_pixel)

        else:
            messagebox.showerror(
                "Erro", "O modo da imagem não é suportado.")  # exibe uma mensagem de erro se o modo da imagem não for suportado
            return

        # cria uma nova imagem Tkinter com a imagem resultante
        resultado_tk = ImageTk.PhotoImage(resultado)

        # exibe uma mensagem de sucesso
        messagebox.showinfo("Sucesso", "Imagem dividida com sucesso.")

        # exibe a imagem resultante no widget Label
        label_resultado.config(image=resultado_tk)

    else:
        # exibe uma mensagem de erro se a imagem não foi selecionada
        messagebox.showerror("Erro", "Selecione uma imagem.")


def RGBtoGray():
    global imagem1, resultado, resultado_tk
    if imagem1:  # verifica se a imagem foi selecionada

        # cria uma imagem vazia com o mesmo modo e tamanho da imagem original
        resultado = Image.new(imagem1.mode, imagem1.size)

        if imagem1.mode == 'RGB' or imagem1.mode == 'RGBA':  # se a imagem for RGB
            for i in range(imagem1.width):
                for j in range(imagem1.height):

                    # obtém o pixel da imagem 1 na posição (i,j)
                    pixel1 = imagem1.getpixel((i, j))

                    # realiza a operação "not" em cada canal de cor individualmente
                    gray_pixel = int(
                        0.2989 * pixel1[0] + 0.5870 * pixel1[1] + 0.1140 * pixel1[2])
                    novo_pixel = (gray_pixel, gray_pixel, gray_pixel)

                    # atribui o novo pixel à imagem resultante na posição (i,j)
                    resultado.putpixel((i, j), novo_pixel)

        else:
            messagebox.showerror(
                "Erro", "O modo da imagem não é suportado.")  # exibe uma mensagem de erro se o modo da imagem não for suportado
            return

        # cria uma nova imagem Tkinter com a imagem resultante
        resultado_tk = ImageTk.PhotoImage(resultado)

        # exibe uma mensagem de sucesso
        messagebox.showinfo("Sucesso", "Imagem dividida com sucesso.")

        # exibe a imagem resultante no widget Label
        label_resultado.config(image=resultado_tk)

    else:
        # exibe uma mensagem de erro se a imagem não foi selecionada
        messagebox.showerror("Erro", "Selecione uma imagem.")


def RGBtoBinary():
    global imagem1, resultado, resultado_tk
    if imagem1:  # verifica se a imagem foi selecionada

        # cria uma imagem vazia com o mesmo tamanho da imagem original
        resultado = Image.new('1', imagem1.size)

        if imagem1.mode == 'RGB' or imagem1.mode == 'RGBA':  # se a imagem for RGB
            for i in range(imagem1.width):
                for j in range(imagem1.height):

                    # obtém o valor de escala de cinza do pixel da imagem 1 na posição (i,j)
                    pixel1 = imagem1.getpixel((i, j))
                    gray_pixel = int(
                        0.2989 * pixel1[0] + 0.5870 * pixel1[1] + 0.1140 * pixel1[2])

                    # aplica a limiarização para transformar em imagem binária
                    if gray_pixel > 128:
                        novo_pixel = 255
                    else:
                        novo_pixel = 0

                    # define o novo pixel na imagem de resultado
                    resultado.putpixel((i, j), novo_pixel)

        else:
            messagebox.showerror(
                "Erro", "O modo da imagem não é suportado.")  # exibe uma mensagem de erro se o modo da imagem não for suportado
            return

        # cria uma nova imagem Tkinter com a imagem resultante
        resultado_tk = ImageTk.PhotoImage(resultado)

        # exibe uma mensagem de sucesso
        messagebox.showinfo("Sucesso", "Imagem convertida com sucesso.")

        # exibe a imagem resultante no widget Label
        label_resultado.config(image=resultado_tk)

    else:
        # exibe uma mensagem de erro se a imagem não foi selecionada
        messagebox.showerror("Erro", "Selecione uma imagem.")


def equalize_histogram():
    global imagem1, resultado, resultado_tk, resultado_tk_norm
    if imagem1:  # verifica se a imagem foi selecionada

        # calcula o histograma da imagem
        hist = imagem1.histogram()

        # cria um vetor para armazenar a função de distribuição cumulativa do histograma
        cdf = [sum(hist[:i+1]) for i in range(len(hist))]

        # normaliza a função de distribuição cumulativa
        cdf = [round((cdf[i] - cdf[0]) * 255 / (imagem1.width *
                     imagem1.height - cdf[0])) for i in range(len(cdf))]

        # cria uma imagem vazia com o mesmo tamanho e modo da imagem original
        resultado = Image.new(imagem1.mode, imagem1.size)

        # aplica a função de distribuição cumulativa aos valores de pixel da imagem original
        for i in range(imagem1.width):
            for j in range(imagem1.height):

                # obtém o pixel da imagem 1 na posição (i,j)
                pixel1 = imagem1.getpixel((i, j))

                # calcula o novo valor de pixel usando a função de distribuição cumulativa
                novo_pixel = tuple(cdf[pixel1[k]] for k in range(len(pixel1)))

                # atribui o novo pixel à imagem resultante na posição (i,j)
                resultado.putpixel((i, j), novo_pixel)

        # cria uma nova imagem Tkinter com a imagem resultante
        resultado_tk = ImageTk.PhotoImage(resultado)

        # exibe uma mensagem de sucesso
        messagebox.showinfo("Sucesso", "Histograma equalizado com sucesso.")

        # exibe a imagem resultante no widget Label
        label_resultado.config(image=resultado_tk)

    else:
        # exibe uma mensagem de erro se a imagem não foi selecionada
        messagebox.showerror("Erro", "Selecione uma imagem.")


# create a global variable to hold the reference to the ImageTk object
resultado_tk_norm = None


def histogram():
    global imagem1, resultado, resultado_tk, resultado_tk_norm
    if imagem1:  # verifica se a imagem foi selecionada

        # cria um array para armazenar as contagens do histograma
        hist = np.array([0] * 256)

        # percorre cada pixel na imagem e incrementa o bin correspondente no histograma
        for pixel in imagem1.convert('L').getdata():
            hist[pixel] += 1

        # cria um array de bordas de bin
        bins = list(range(257))

        # cria uma nova figura do Matplotlib
        fig = plt.figure(figsize=(4, 3))

        # plota o histograma na figura
        plt.plot(hist)

        # configura os eixos da figura
        plt.xlim([0, 256])
        plt.ylim([0, max(hist) * 1.1])

        # salva a figura em um arquivo temporário
        fig.savefig('histogram.png')

        # carrega a nova imagem a partir do arquivo temporário
        resultado = Image.open('histogram.png')

        # cria uma nova imagem Tkinter com a imagem resultante
        resultado_tk = ImageTk.PhotoImage(resultado)

        # exibe a imagem resultante no widget Label
        histograma.config(image=resultado_tk)

        # calcula o histograma normalizado
        hist_norm = hist / float(imagem1.size[0] * imagem1.size[1])
        bins_norm = np.arange(0, 257) / 256

        # cria uma nova figura do Matplotlib
        fig_norm = plt.figure(figsize=(4, 3))

        # plota o histograma normalizado na figura
        plt.plot(bins_norm[:-1], hist_norm)

        # configura os eixos da figura
        plt.xlim([0, 1])
        plt.ylim([0, max(hist_norm) * 1.1])

        # salva a figura normalizada em um arquivo temporário
        fig_norm.savefig('histogram_norm.png')

        # carrega a nova imagem a partir do arquivo temporário
        resultado_norm = Image.open('histogram_norm.png')

        # cria uma nova imagem Tkinter com a imagem resultante
        resultado_tk_norm = ImageTk.PhotoImage(resultado_norm)

        # exibe a imagem resultante no widget Label
        histograma_norm.config(image=resultado_tk_norm)

        # equalize_histogram()

    else:
        # exibe uma mensagem de erro se a imagem não foi selecionada
        messagebox.showerror("Erro", "Selecione uma imagem.")


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


def realce_max():
    global imagem1_tk
    imagem_realce_maximo = ImageEnhance.Brightness(imagem1).enhance(1.5)
    imagem1_tk = ImageTk.PhotoImage(imagem_realce_maximo)
    label_imagem1.config(image=imagem1_tk)


def realce_medio():
    global imagem1_tk
    imagem_realce_medio = ImageEnhance.Brightness(imagem1).enhance(1.2)
    imagem1_tk = ImageTk.PhotoImage(imagem_realce_medio)
    label_imagem1.config(image=imagem1_tk)


def realce_min():
    global imagem1_tk
    imagem_realce_minimo = ImageEnhance.Brightness(imagem1).enhance(0.8)
    imagem1_tk = ImageTk.PhotoImage(imagem_realce_minimo)
    label_imagem1.config(image=imagem1_tk)


imagem1 = None
imagem2 = None
resultado = None
imagem1_tk = None
imagem2_tk = None
resultado_tk = None

root = Tk()
root.title("Operações com imagens")

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

botao_somar = Button(container2, text="Somar",
                     command=lambda: operar_imagens("soma"))
botao_somar.pack(side=LEFT)

botao_subtrair = Button(container2, text="Subtrair",
                        command=lambda: operar_imagens("subtracao"))
botao_subtrair.pack(side=LEFT)

botao_multiplicar = Button(
    container2, text="Multiplicar", command=lambda: operar_imagens("multiplicacao"))
botao_multiplicar.pack(side=LEFT)

botao_dividir = Button(container2, text="Dividir",
                       command=lambda: operar_imagens("divisao"))
botao_dividir.pack(side=RIGHT)

botao_media = Button(container2, text="Media",
                     command=lambda: operar_imagens("media"))
botao_media.pack(side=RIGHT)


container4 = Frame(root)
container4.pack()

botao_MAX = Button(container4, text="MAX",
                   command=lambda: realce_max())
botao_MAX.pack(side=RIGHT)
botao_MEDIA = Button(container4, text="MEDIA",
                     command=lambda: realce_medio())
botao_MEDIA.pack(side=RIGHT)
botao_MIN = Button(container4, text="MIN",
                   command=lambda: realce_min())
botao_MIN.pack(side=RIGHT)

container5 = Frame(root)
container5.pack()

botao_and = Button(container5, text="and",
                   command=lambda: operar_imagens("and"))
botao_and.pack(side=RIGHT)

botao_or = Button(container5, text="or", command=lambda: operar_imagens("or"))
botao_or.pack(side=RIGHT)

botao_xor = Button(container5, text="xor",
                   command=lambda: operar_imagens("xor"))
botao_xor.pack(side=RIGHT)

botao_not = Button(container5, text="not", command=not_image)
botao_not.pack(side=RIGHT)

botao_togray = Button(container5, text="RGB -> Cinza",
                      command=RGBtoGray)
botao_togray.pack(side=RIGHT)

botao_toRGB = Button(container5, text="RGB -> Binário",
                     command=RGBtoBinary)
botao_toRGB.pack(side=RIGHT)

botao_histogram = Button(container5, text="Gerar histogramas",
                         command=histogram)
botao_histogram.pack(side=RIGHT)


container8 = Frame(root)
container8.pack()

# criação do frame esquerdo
frame_esquerdo = Frame(container8)
frame_esquerdo.pack(side=LEFT)

campo_somar_fator = Entry(frame_esquerdo, width=10)
campo_somar_fator.pack(side=RIGHT)

botao_somar_fator = Button(frame_esquerdo, text="Somar por fator",
                           command=lambda: somar_por_fator())
botao_somar_fator.pack(side=LEFT)

# criação do frame direito
frame_direito = Frame(container8)
frame_direito.pack(side=RIGHT)

campo_multiplicacao = Entry(frame_direito, width=10)
campo_multiplicacao.pack(side=RIGHT)

botao_multiplicacao_fator = Button(frame_direito, text="Multiplicar por fator",
                                   command=lambda: multiplicar_por_fator())
botao_multiplicacao_fator.pack(side=RIGHT)

botao_somar_fator.pack()

container6 = Frame(root)
container6.pack()

center_frame = Frame(container6)
center_frame.pack(side=TOP)

campo_subtracao = Entry(center_frame, width=10)
campo_subtracao.pack(side=RIGHT)

botao_subtracao_fator = Button(center_frame, text="Subtracao por fator",
                               command=lambda: subtrair_por_fator())
botao_subtracao_fator.pack()

left_frame = Frame(container6)
left_frame.pack(side=LEFT)

campo_divisao = Entry(left_frame, width=10)
campo_divisao.pack(side=RIGHT)

botao_divisao_fator = Button(left_frame, text="Divisao por fator",
                             command=lambda: dividir_por_fator())
botao_divisao_fator.pack()

right_frame = Frame(container6)
right_frame.pack(side=RIGHT)

campo_alpha = Entry(right_frame, width=10)
campo_alpha.pack(side=RIGHT)

botao_blend = Button(right_frame, text="Blend",
                     command=lambda: operar_imagens("blend"))
botao_blend.pack()


container7 = Frame(root)
container7.pack()

botao_salvar = Button(container7, text="Salvar resultado",
                      command=salvar_resultado)
botao_salvar.pack()

container3 = Frame(root)
container3.pack(pady=10, fill=BOTH, expand=True)


label_imagem1 = Label(container3)
label_imagem1.pack(side=LEFT, padx=10)


label_imagem2 = Label(container3)
label_imagem2.pack(side=LEFT, padx=10)


label_resultado = Label(container3)
label_resultado.pack(pady=10)

container8 = Frame(root)
container8.pack()

histograma = Label(container8)
histograma.pack(side='left', padx=10, pady=10)

histograma_norm = Label(container8)
histograma_norm.pack(side='left', padx=10, pady=10)


root.mainloop()
