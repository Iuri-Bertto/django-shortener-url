# 1 - Instale o Python 3
https://www.python.org/downloads/

# 2 - Instalação de ambiente virtual
Acesse a diretório do projeto "tiny_url" e rode o comando "python -m venv venv" ou "python3 -m venv venv"

# 3 - Ativação do ambiente virtual
No diretório do projeto rodar o comando:

MacOS/Linux: source venv/bin/activate
ou
Windows: venv\Scripts\activate

# 4 - Instale os requirements com o ambiente virtual ativado
pip install -r requirements.txt

# 5 - Subindo o serviço
python manage.py runserver

# 6 - Acessar painel administrativo
http://127.0.0.1:8000/admin/

Usuário: admin
Senha: admin

# 7 - URL's API
COLLECTION POSTMAN: https://www.getpostman.com/collections/529cffc0d55fa003cfae


GET http://127.0.0.1:8000/api/shortener/tiny_url/ => Listar URLS (TINYURL) <br>
POST http://127.0.0.1:8000/api/shortener/tiny_url/ => Encurtar URLS (TINYURL) <br>
BODY -> RAW -> JSON: {
    "original_url": "https://g1.globo.com/sp/vale-do-paraiba-regiao/noticia/2021/05/02/ponto-turistico-em-santo-antonio-do-pinhal-pico-agudo-registra-aglomeracao-de-turistas.ghtml"
}


GET http://127.0.0.1:8000/api/shortener/offline_url/ => Listar URLS (OFFLINE URL) <br>
POST http://127.0.0.1:8000/api/shortener/tiny_url/ => Encurtar URLS (OFFLINE URL) <br>
BODY -> RAW -> JSON: {
    "original_url": "https://g1.globo.com/sp/vale-do-paraiba-regiao/noticia/2021/05/02/ponto-turistico-em-santo-antonio-do-pinhal-pico-agudo-registra-aglomeracao-de-turistas.ghtml"
}

POST http://127.0.0.1:8000/api/shortener/tiny_url/ => Encurtar URLS COM NOME OPCIONAL (OFFLINE URL) <br>
BODY -> RAW -> JSON: {
    "original_url": "https://stackoverflow.com/questions/54642671/a-clear-step-by-step-process-for-running-a-periodic-task-in-a-django-applicaon",
    "opcional_path": "blabla"
}