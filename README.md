# StegaPro

Este é um programa simples em Python que permite esconder e extrair textos nos bytes de imagens.
### Esconder Texto na Imagem:

1. O texto desejado para ocultação é convertido para uma sequência de bytes usando a codificação UTF-8 e, em seguida, é codificado em base64 para representação binária.
2. A imagem de entrada é tratada como uma sequência de bytes.
3. Marcas de início e fim são adicionadas para identificar o início e o fim do texto codificado.
4. Se as marcas já existirem na imagem, são removidas.
5. O texto codificado é anexado à sequência de bytes da imagem.
6. A imagem resultante, agora contendo o texto oculto, é salva em um novo arquivo.

### Extrair Texto da Imagem:

1. A imagem é lida como uma sequência de bytes.
2. As marcas de início e fim são localizadas na sequência de bytes.
3. O texto codificado entre essas marcas é extraído.
4. O texto é decodificado usando base64 para recuperar o texto original.
5. O texto decodificado é salvo em um arquivo chamado "extração.txt".
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
