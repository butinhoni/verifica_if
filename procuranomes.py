import pandas as pd
from pypdf import PdfReader
from getmatriculas import getPlanilha

accent_map = {
    'á': 'a', 'à': 'a', 'ã': 'a', 'â': 'a', 'ä': 'a',
    'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
    'í': 'i', 'ì': 'i', 'î': 'i', 'ï': 'i',
    'ó': 'o', 'ò': 'o', 'õ': 'o', 'ô': 'o', 'ö': 'o',
    'ú': 'u', 'ù': 'u', 'û': 'u', 'ü': 'u',
    'ç': 'c', 'ñ': 'n',
    'Á': 'A', 'À': 'A', 'Ã': 'A', 'Â': 'A', 'Ä': 'A',
    'É': 'E', 'È': 'E', 'Ê': 'E', 'Ë': 'E',
    'Í': 'I', 'Ì': 'I', 'Î': 'I', 'Ï': 'I',
    'Ó': 'O', 'Ò': 'O', 'Õ': 'O', 'Ô': 'O', 'Ö': 'O',
    'Ú': 'U', 'Ù': 'U', 'Û': 'U', 'Ü': 'U',
    'Ç': 'C', 'Ñ': 'N'
}

def replace_acento(variavel):
    result = variavel
    for accented_char, unaccented_char in accent_map.items():
        result = result.replace(accented_char, unaccented_char)
    return result


matriculas = getPlanilha()

def getText(path):
    reader = PdfReader(path)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return text

texto = getText('pdfteste.pdf')
texto = replace_acento(texto)

with open('teste.txt','w') as f:
    f.write(texto)

lista = {
    'nomeLista':[],
    'nomeMatricula': [],
    'probabilidade':[],
    'certeza': []
}

matriculas['Nome'] = matriculas['Nome'].apply(lambda x: replace_acento(x))

for name in matriculas['Nome']:
    #pra cada um dos nomes na matricula
    nomes_grandes = []
    #separa nome/sobrenome
    nomes = name.split(' ')
    #separa só nomes com mais de 3 caracteres
    for nome in nomes:
        if len(nome) > 3:
            nomes_grandes.append(nome)
    
    #passa procurando os nomes um por um

    for line in open('teste.txt'):
        count = 0
        for nome in nomes_grandes:
            if nome in line:
                count += 1
        if count > 0:
            lista['nomeLista'].append(line)
            lista['nomeMatricula'].append(name)
            lista['probabilidade'].append(count/len(nomes_grandes))
            lista['certeza'].append('sim' if name.upper() in line.upper() else 'não')



df = pd.DataFrame(lista)
df = df.sort_values('probabilidade', ascending=False)
print(df)
df.to_csv('tabela.csv')