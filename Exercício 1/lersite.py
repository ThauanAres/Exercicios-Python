# Exercício para acessar um site e ler seu conteúdo.

import urllib.request

try:
    site = urllib.request.urlopen('http://www.google.com.br/')
except urllib.error.URLError:
    print('\033[31mNão foi possível acessar o seu site!\033[m')
else:
    print('\033[32mConsegui acessar o seu site com sucesso!\033[m')
    html = site.read().decode('utf-8', errors='replace')
    print(html[:500])

