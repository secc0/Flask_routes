from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="formulario_db",  # Substitua pelo nome do seu banco de dados
        user="postgres",           # Seu usuário PostgreSQL
        password="Joao2504."       # Sua senha PostgreSQL
    )
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM comentarios')
    comentarios = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', comentarios=comentarios)


@app.route("/formulario")
def sobre():
    return render_template('formulario.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        nome = request.form['nome']
        comentario = request.form['comentario']
        
        # Inserir os dados no banco de dados
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO comentarios (nome, comentario) VALUES (%s, %s)',
                    (nome, comentario))
        conn.commit()
        cur.close()
        conn.close()

        return redirect(url_for('index'))


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
        nome = request.form['nome']
        comentario = request.form['comentario']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('UPDATE comentarios SET nome = %s, comentario = %s WHERE id = %s',
                    (nome, comentario, id))
        conn.commit()
        cur.close()
        conn.close()

        return redirect(url_for('index'))
    
@app.route('/excluir/<int:id>', methods=['GET'])
def excluir(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM comentarios WHERE id = %s', (id,))
    conn.commit()
    cur.close()
    conn.close()

    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)