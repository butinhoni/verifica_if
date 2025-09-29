import requests
from bs4 import BeautifulSoup as bs
import time
from sendmail import sendmail
import segredos

#coisas estáticas
procurado = 3118
ultima_coisa = 'LISTAGEM PRELIMINAR DE INSCRITOS NA AMPLA CONCORRÊNCIA'

#loop eterno
while True:
    response = requests.get('https://seletivo.ifmt.edu.br/edital/visualizar/119/')

    soup = bs(response.content, 'html.parser')

    content_div = soup.find('div', class_ = 'even')

    text = soup.prettify()


    if text.find(ultima_coisa) != procurado:
        fim = text.find(ultima_coisa)
        novidade = text[3118:]
        novidadeFim = novidade.find('\n')
        novidade = novidade[:novidadeFim]
        print(novidade)
        corpo = f"""
                <html>
                <head></head>
                    <body>
                    Olá amigos, passando pra informar vocês que o seguinte arquivo foi disponibilizado no site do edital do IF:
                    <br>
                    <br>
                    <b>{novidade}</b>
                    <br>
                    <br>
                    Atenciosamente, seu amigo virtual.
                    </body>
                </html>
                """
        sendmail(login=segredos.login, sender=segredos.login, senha=segredos.senha_mail, corpo=str(corpo))
        ultima_coisa = novidade
        resposta = 'teve alteração'
    else:
        resposta = 'nada mudou :('
    print(resposta)
    time.sleep(600)