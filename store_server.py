# import logging
# logging.basicConfig(level=logging.DEBUG)
# logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)
# logging.getLogger('sqlalchemy.engine.base.Engine').setLevel(logging.DEBUG)

from flask import Flask
from flask.ext.spyne import Spyne

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

from spyne.error import InternalError, ResourceNotFoundError
from spyne.model.primitive import UnsignedInteger32, Unicode
from spyne.model.complex import Iterable, ComplexModelBase, ComplexModelMeta
from spyne.model.fault import Fault
from spyne.protocol.soap import Soap11
from spyne.decorator import rpc, srpc
from spyne.service import ServiceBase
from spyne.application import Application
from spyne.server.wsgi import WsgiApplication

app = Flask(__name__) 
spyne = Spyne(app)

db = create_engine('sqlite:///records.db')
Session = sessionmaker(bind=db)

import logging
h = logging.StreamHandler()
rl = logging.getLogger()
rl.setLevel(logging.DEBUG)
rl.addHandler(h)

class TableModel(ComplexModelBase):
    __metaclass__ = ComplexModelMeta
    __metadata__ = MetaData(bind=db)

class Record(TableModel):
    __tablename__ = 'record'
    __namespace__ = 'recordstorecoop'
    __table_args__= {"sqlite_autoincrement": True}

    id = UnsignedInteger32(pk=True)
    title = Unicode
    author = Unicode
    genre = Unicode
    year = UnsignedInteger32
    thumbnail_url = Unicode
    description = Unicode
    quantity = UnsignedInteger32
    price = UnsignedInteger32

class RecordStoreService(ServiceBase):
    
    __service_url_path__ = '/soapservice'
    __in_protocol__ = Soap11(validator='lxml')
    __out_protocol__ = Soap11()

    @rpc(Record, _returns=Iterable(Record))
    def get_records(ctx, rq=None):
        """rq stands for Record query, for matching"""
        q = ctx.udc.session.query(Record)
        if rq:
            for val in ('title', 'author', 'genre', 'year'):
                if rq.__getattribute__(val):
                    q = q.filter_by(**{val: rq.__getattribute__(val)})
        for record in q:
            yield record

@app.route('/index')
def index():
    return "hello world!"
# class UserDefinedContext(object):
#     """Immagino si possa usare per limitare i privilegi. Inutile qui."""
#     def __init__(self):
#         self.session = Session()

# def _on_method_call(ctx):
#     ctx.udc = UserDefinedContext()

# def _on_method_context_closed(ctx):
#     if ctx.udc is not None:
#         ctx.udc.session.commit()
#         ctx.udc.session.close()

# class MyApplication(Application):
#     def __init__(self, services, tns, name=None, in_protocol=None, out_protocol=None):
#         super(MyApplication, self).__init__(services, tns, name, in_protocol, out_protocol)

#         self.event_manager.add_listener('method_call', _on_method_call)
#         self.event_manager.add_listener("method_context_closed", _on_method_context_closed)

#     def call_wrapper(self, ctx):
#         try:
#             return ctx.service_class.call_wrapper(ctx)
#         except NoResultFound:
#             raise ResourceNotFoundError(ctx.in_object)
#         except Fault, e:
#             logging.error(e)
#             raise
#         except Exception, e:
#             logging.exception(e)
#             raise InternalError(e)

if __name__=='__main__':
    import sys
    
    #from wsgiref.simple_server import make_server
    
    if len(sys.argv) == 1: #no args passed: sys.argv[0] is __name__
        port = 8000
    else:
        port = int(sys.argv[1])
    #app = MyApplication([RecordStoreService], 'recordstorecoop', in_protocol=Soap11(validator='lxml'), out_protocol=Soap11())
    #wsgi_app = WsgiApplication(app)
    #server = make_server('localhost', port, wsgi_app)

    TableModel.Attributes.sqla_metadata.create_all()
    
    # logging.info("listening to http://localhost:{}".format(port))
    # logging.info("wsdl is at: http://localhost:{}/?wsdl".format(port))

    #server.serve_forever()
    app.run(port=port,debug = True)