# Cria a aplicação Flask
 app = Flask(__name__) 

 # --- PONTO CRÍTICO DA ORIENTAÇÃO A OBJETOS ---
 # É criada UMA ÚNICA instância da Estante.
 # Este objeto 'minha_estante' vai persistir enquanto o app estiver rodando. 
 # É ele que vai carregar os livros do arquivo e manter a lista em memória.
 # minha_estante = Estante()
 # ---------------------------------------------

@app.route('/') 
 def pagina_inicial():
     """ Rota principal. Exibe a estante de livros."""
 # Acessa a propriedade do objeto para pegar a lista de livros
  livros_na_estante = minha_estante.livros

 # Renderiza o HTML, passando a lista de livros para o template 
 return render_template('estante.html', livros=livros_na_estante)
 @app.route('/adicionar', methods=['POST']) 
 def adicionar_livro():
      """ Rota que recebe os dados do formulário para adicionar um novo livro."""
    
    titulo = request.form['titulo'] 
    autor = request.form['autor']
    novo_livro = Livro(titulo=titulo, autor=autor)
    minha_estante.adicionar_livro(novo_livro)
    return redirect(url_for('pagina_inicial'))

    # Roda o servidor de desenvolvimento 
    if __name__ == '__main__': 
        app.run(debug=True)