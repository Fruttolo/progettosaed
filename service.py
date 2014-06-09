"""Modulo che implementa il servizio unificato.

Carica una lista dei negozi aderenti all'iniziativa,
cerca di connettervisi,
si mette a rispondere alle query.

"""


from flask import Flask
from flask import render_template

import query

app = Flask(__name__)

@app.route('/cane') #@app.route('/cane/?<query>')
def cane():
    rv = query.get_all_records();
    return render_template('service.html', rv=rv)

if __name__ == '__main__':
    app.debug = True
    app.run(port = 5000)