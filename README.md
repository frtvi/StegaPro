# StegaPro

Este é um programa simples em Python que permite esconder e extrair textos nos bytes de imagens.

O texto que você deseja ocultar é convertido para uma sequência de bytes usando a codificação UTF-8 e, em seguida, é codificado em base64. Isso é feito para garantir que o texto possa ser representado como uma sequência de bytes, o que é essencial para a ocultação.
A imagem de entrada é lida como uma sequência de bytes.
Uma marca de início e uma marca de fim são adicionadas para identificar o início e o fim do texto codificado.
Se a marcação de início e fim já existir na imagem, ela é removida.
O texto codificado é então anexado à sequência de bytes da imagem.
A imagem resultante, agora contendo o texto oculto, é salva em um novo arquivo.
Extrair Texto da Imagem:

A imagem é lida como uma sequência de bytes.
As marcas de início e fim são localizadas na sequência de bytes.
O texto codificado entre essas marcas é extraído.
O texto é decodificado usando base64 para recuperar o texto original.
O texto decodificado é salvo em um arquivo chamado "extração.txt".
Interface Gráfica (GUI):

Uma interface gráfica é criada usando a biblioteca Tkinter.
Dois botões são fornecidos na GUI: um para esconder o texto na imagem e outro para extrair o texto de uma imagem.
A função on_esconder_click é chamada quando o botão "Esconder Texto na Imagem" é pressionado, e a função on_extrair_click é chamada quando o botão "Extrair Texto" é pressionado.

## Requisitos

Certifique-se de ter o Python instalado em seu sistema. Além disso, instale as dependências usando:

```bash
pip install pillow
```
# Como Usar
Execute o script ```python3 stegapro.py```.<br>
Insira o texto na caixa de texto.<br>
Pressione o botão "Esconder Texto na Imagem" para esconder o texto em uma imagem selecionada.<br>
Pressione o botão "Extrair Texto" para extrair o texto da imagem selecionada.<br>
O texto extraído será salvo automaticamente no arquivo extração.txt.<br>

# Nota Legal

Este programa é fornecido apenas para fins educacionais e demonstrativos. O desenvolvedor não se responsabiliza pelo uso indevido deste software para atividades maliciosas ou ilegais. É estritamente proibido utilizar este programa para ocultar arquivos ou realizar qualquer outra atividade que viole a lei ou a ética.

O desenvolvedor não endossa ou encoraja qualquer forma de atividade maliciosa, invasiva ou prejudicial. A utilização deste software está sujeita à legislação aplicável e às políticas éticas. Certifique-se de compreender e cumprir as leis e regulamentações locais antes de utilizar este programa.

Este projeto é fornecido "como está", sem garantias expressas ou implícitas. O desenvolvedor não assume qualquer responsabilidade por danos diretos, indiretos, incidentais, especiais, exemplares ou consequenciais resultantes do uso deste software.

Ao utilizar este programa, você concorda em aceitar todos os termos e condições estabelecidos nesta nota legal.

---
