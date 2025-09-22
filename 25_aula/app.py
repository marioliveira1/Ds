
from flask import Flask, render_template, request, redirect, url_for
from modelos import *

# --- Inicialização da aplicação Flask ---
app = Flask(__name__)

minha_estante = Estante()
# --- ROTAS DA APLICAÇÃO ---


@app.route('/')
def pagina_inicial():
    """
    Rota principal. Exibe a estante de livros.
    """
    # Acessa a propriedade do objeto para pegar a lista de livros
    livros_na_estante = minha_estante.livros

    # Renderiza o template HTML 'estante.html', passando a lista de livros
    return render_template('estante.html', livros=livros_na_estante)

@app.route('/adicionar', methods=['POST'])
def adicionar_livro():
    """
    Rota que recebe os dados do formulário para adicionar um novo livro.
    Esta rota só aceita requisições POST.
    """
    # 1. Pega os dados enviados pelo formulário
    titulo = request.form['titulo']
    autor = request.form['autor']

    # 2. Cria um NOVO OBJETO 'Livro' com esses dados
    novo_livro = Livro(titulo=titulo, autor=autor)
    
    # 3. Usa o MÉTODO do objeto 'Estante' para adicionar o novo livro
    minha_estante.adicionar_livro(novo_livro)

    # 4. Redireciona o usuário de volta para a página inicial
    return redirect(url_for('pagina_inicial'))

# --- RODA O SERVIDOR DE DESENVOLVIMENTO ---
if __name__ == '__main__':
    # O modo 'debug=True' permite recarregamento automático do servidor
    # e exibe informações detalhadas de erro no navegador.
    app.run(debug=True)
