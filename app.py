import csv

leitura_dados = None
linhas = []

with open('dados.csv', newline='', encoding='utf-8') as dados:
  leitura_dados = csv.reader(dados)

  for linha in leitura_dados:
    linhas.append(linha)

linhas.pop(0)

for linha in linhas:
  for key, l in enumerate(linha):
    if key < 2:
      linha[key] = str(l).strip()
    if key == 2 and (l == '' or l == ' ' or l == None):
      linha[key] = 0
    if key == 1 and (l == '' or l == ' ' or l == None):
      linha[key] = 0
    if key == 0 and (l == '' or l == ' ' or l == None):
      linha[key] = 0

    if key == 0 and 'historia' in l.lower():
      linha[key] = 'História'

    if key == 0 and 'historias' in l.lower():
      linha[key] = 'Histórias'

    if key == 2 and not l.isnumeric():
      numeros = []
      numero_final = ''
      for c in l:
        if str(c).isnumeric():
          numeros.append(str(c))

      for n in numeros:
        numero_final += n 
      
      try:
        linha[key] = int(numero_final)
      except Exception:
        print(f'Não consegui converter o número na linha {linha}')


with open('SQL_CODES.txt', 'w') as sql:
  for linha in linhas:
    sql.write(f'INSERT INTO livros_livro (titulo, autor, quantidade) VALUES ("{str(linha[0]).strip()}", "{str(linha[1]).strip()}", {linha[2]});\n')