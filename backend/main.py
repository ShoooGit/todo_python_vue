from flask import Flask, render_template
from api import api_bp
from models import get_all, init_db, insert, delete

app = Flask(__name__, static_folder='../frontend/dist/static', template_folder='../frontend/dist')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://{user}:{password}@{host}/{name}'.format(**{
    'user': 'shuto',
    'password': 'shuto',
    'host': '127.0.0.1',
    'name': 'db.postgresql'
})
app.register_blueprint(api_bp)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
  return render_template('index.html')

if __name__ == '__main__':
  with app.app_context():
    init_db(app)
    # delete()
    if not get_all():
      insert('断捨離', 'Todo','2020-12-30', '不要なものを処分する')
      insert('掃除', 'Doing', '2020-12-20', '部屋の掃除をする')
      insert('買い物', 'Done', '2020-12-10', '食料品を買う')
  app.run()