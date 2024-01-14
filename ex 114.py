import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.mercadolivre.com.br')
except urllib.error.URLError:
    print('O site Mercado Livre não está acessível no momento!')
else:
    print('Conseguiu acessar o site Mercado Livre com sucesso!')
    #print(site.read())
