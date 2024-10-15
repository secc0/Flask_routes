from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/formulario")
def sobre():
    return render_template('formulario.html')


@app.route('/submit', methods=['POST'])
def submit():
    
    if request.method == 'POST':
        nome = request.form['nome']
        comentario = request.form['comentario']
        return render_template('resultado.html', nome=nome, comentario=comentario), print("formulario enviado")

@app.route('/editar/<int:id>', methods=['GET'])
def editar(id):
    cometario_existente = {
        'id': id,
        'nome': 'João Silva',
        'comentario':'Novo comentário do João'
    }
    return render_template('atualizar_form.html', id=cometario_existente['id'],
                           nome=cometario_existente['nome'],comentario=cometario_existente['comentario'])

@app.route('/atualizar/<int:id>', methods=['POST'])
def atualizar(id):
    if request.method == 'POST':
        nome = request.form['nome'],
        comentario = request.form['comentario']
        return(f"Comentário {id} \n atualizado com sucesso! Novo nome: {nome},\n Novo comentário: {comentario}")

if __name__ == '__main__':
    app.run(debug=True)