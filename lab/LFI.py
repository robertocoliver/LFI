import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def listar_arquivos():
    # Obtém o nome do diretório a ser listado a partir da query string
    diretorio = request.args.get('params', default='.', type=str)

    # Obtém o caminho absoluto do diretório a ser listado
    caminho_absoluto = os.path.abspath(diretorio)

    # Verifica se o caminho absoluto pertence ao diretório raiz do projeto
    pasta_raiz = os.path.abspath(os.path.dirname(__file__))
    if not caminho_absoluto.startswith(pasta_raiz):
        return 'Acesso negado!'
    else:
	      return 'Acesso permitido!'

if __name__ == '__main__':
    app.run(debug=True)
