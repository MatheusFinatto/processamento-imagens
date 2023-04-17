from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk


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

container4 = Frame(root)
container4.pack()

campo_alpha = Entry(container4)
campo_alpha.pack(side=LEFT)

botao_blend = Button(container4, text="Blend",
                     command=lambda: operar_imagens("blend"))
botao_blend.pack()

container6 = Frame(root)
container6.pack()
botao_salvar = Button(container6, text="Salvar resultado",
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


root.mainloop()
