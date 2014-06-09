"""Modulo che implementa il servizio unificato.

Carica una lista dei negozi aderenti all'iniziativa,
cerca di connettervisi,
si mette a rispondere alle query.

"""


from flask import Flask
from flask import render_template

import query

app = Flask(__name__)

@app.route('/index') #@app.route('/cane/?<query>')
def service():
    rv = query.get_records();
    return render_template('service.html', rv=rv)

if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) #[0] is __name__
    
    app.debug = True
    app.run(port=port)