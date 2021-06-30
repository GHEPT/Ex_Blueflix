from flask import Flask, Blueprint, render_template
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
bp = Blueprint('app', __name__)#é o nome da nossa aplicação.

# Database
user = 'ftmeceao'
password = 'T9lZLHP_lSMbMXIxPjAlekEtoVatjTrx'
host = 'tuffi.db.elephantsql.com'
database = 'ftmeceao'

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}/{database}'
# Variável que contém toda a configuração do PostgreSQL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#Modelo Filmes (cada modelo é uma tabela)
class Filmes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    imagem_url = db.Column(db.String(255), nullable=False) 

    def __init__(self, nome, imagem_url):
        self.nome = nome
        self.imagem_url = imagem_url
    
    @staticmethod
    def read_all():
        #Select * FROM FILMES
        return Filmes.query.order_by(Filmes.id.desc()).all()


@bp.route('/')#bp é de Blueprint
def index():
    return render_template('index.html')

@bp.route('/read')
def read_all():
    filmes = Filmes.read_all()
    return render_template('listar_filmes.html', filmes=filmes)#passando pra dentro do meu HTML a minha listagem de filmes. O primeiro nome eu uso dentro do HTML. O segundo nome é minha lista de dict.

@bp.route('/read/<filme_id>')
def lista_detalhe_filme(filme_id):
    return 'Página em construção para o filme com ID -> ' + filme_id

app.register_blueprint(bp)# é pra pegar os dados da nossa aplicação (nome do app e as rotas) e registrar dentro do app do Flask

if __name__ == '__main__':
    app.run(debug=True)