<h1>Calculadora de imagens</h1>

Esta é uma aplicação GUI em Python que permite selecionar duas imagens e realizar operações matemáticas entre elas. As operações disponíveis são soma, subtração, multiplicação, divisão, AND, OR, XOR, média e blend. O blend é uma operação que realiza uma combinação linear das duas imagens, controlada por um valor de alpha. A aplicação utiliza a biblioteca Pillow para manipulação de imagens e a biblioteca Tkinter para criar a interface gráfica.

<h2>Como usar</h2>
Para usar a aplicação, execute o arquivo Ex8.py. A interface gráfica será aberta. Em seguida, siga os passos abaixo:

<ol>

<li>
Clique no botão "Selecionar Imagem 1" e escolha uma imagem no formato suportado pela biblioteca Pillow (JPEG, BMP, PNG, entre outros).
</li>

<li>
Clique no botão "Selecionar Imagem 2" e escolha outra imagem no mesmo formato e com o mesmo tamanho da primeira imagem.
</li>

<li>
Selecione uma operação matemática na caixa de seleção "Operação".
</li>

<li>
Se desejar, ajuste o valor de alpha no campo de entrada "Alpha" para a operação blend.
</li>

<li>
Clique no botão correspondente à operação matemática desejada para realizar a operação entre as duas imagens.
</li>

<li>
O resultado da operação será exibido na janela.
</li>

</ol>

<h2>Dependências</h2>
A aplicação utiliza as seguintes bibliotecas Python:

<ul>

<li>
Pillow
</li>

<li>
Tkinter
</li>

</ul>

Para instalar as dependências, execute o comando "pip install -r requirements.txt" no terminal.

<h2>Descrição técnica</h2>
A aplicação é implementada sem o auxílio de funções externas, pixel a pixel, no baixo nível, utilizando apenas as bibliotecas Pillow e Tkinter. As imagens são carregadas como objetos Image da biblioteca Pillow e suas matrizes de pixels são acessadas diretamente para realizar as operações matemáticas. Para a operação blend, é feita uma combinação linear de cada pixel das duas imagens, ponderada pelo valor de alpha, utilizando a fórmula (1 - alpha) _ pixel_imagem_1 + alpha _ pixel_imagem_2. A imagem resultante é então convertida de volta para um objeto Image e exibida na janela.
