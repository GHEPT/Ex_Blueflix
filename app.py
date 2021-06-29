from flask import Flask, Blueprint, render_template

app = Flask(__name__)
bp = Blueprint('app', __name__)#é o nome da nossa aplicação.

filmes = [
    {
        "id": 1,
        "nome": "Orgulho e Preconceito",
        "imagem_url": "https://br.web.img3.acsta.net/c_310_420/medias/nmedia/18/87/84/14/20028635.jpg"
    },
    {
        "id": 2,
        "nome": "Tróia",
        "imagem_url": "https://br.web.img3.acsta.net/c_310_420/medias/nmedia/18/90/43/26/20096298.jpg"
    },
    {
        "id": 3,
        "nome": "Príncipe da Pérsia",
        "imagem_url": "https://upload.wikimedia.org/wikipedia/pt/7/7d/Prince_of_Persia_The_Forgotten_Sands_Capa.jpg"
    },
    {
        "id": 4,
        "nome": "A Origem",
        "imagem_url": "https://upload.wikimedia.org/wikipedia/pt/8/84/AOrigemPoster.jpg"
    },
    {
        "id": 5,
        "nome": "Meninas Malvadas",
        "imagem_url": "https://br.web.img3.acsta.net/pictures/210/087/21008705_20130527194056821.jpg"
    },
    {
        "id": 6,
        "nome": "Click",
        "imagem_url": "https://images-na.ssl-images-amazon.com/images/I/51qq%2B12klKL._AC_.jpg"
    }
]

@bp.route('/')#bp é de Blueprint
def index():
    return render_template('index.html')

@bp.route('/read')
def listar_filmes():
    return render_template('listar_filmes.html', filmes=filmes)#passando pra dentro do meu HTML a minha listagem de filmes. O primeiro nome eu uso dentro do HTML. O segundo nome é minha lista de dict.

@bp.route('/read/<filme_id>')
def lista_detalhe_filme(filme_id):
    return 'Página em construção para o filme com ID -> ' + filme_id

app.register_blueprint(bp)# é pra pegar os dados da nossa aplicação (nome do app e as rotas) e registrar dentro do app do Flask

if __name__ == '__main__':
    app.run(debug=True)