import logging
logging.basicConfig(level=logging.DEBUG)
logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)
logging.getLogger('sqlalchemy.engine.base.Engine').setLevel(logging.DEBUG)

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

from spyne.error import InternalError, ResourceNotFoundError

from spyne.model.primitive import Integer, Unicode
from spyne.model.complex import Array, Iterable, ComplexModelBase, ComplexModelMeta
from spyne.model.fault import Fault

from spyne.application import Application
from spyne.protocol.soap import Soap11
from spyne.decorator import rpc
from spyne.server.wsgi import WsgiApplication
from spyne.service import ServiceBase

db = create_engine('sqlite:///prova.db')
Session = sessionmaker(bind=db)

class TableModel(ComplexModelBase):
    __metaclass__ = ComplexModelMeta
    __metadata__ = MetaData(bind=db)

class Record(TableModel):
    __tablename__ = 'record'
    __namespace__ = 'recordstorecoop.record'
    __table_args__= {"sqlite_autoincrement": True}

    id = UnsignedInteger32(pk=True)
    title = Unicode
    author = Unicode
    genre = Unicode
    year = Integer
    thumbnail_url = Unicode
    tracklist = Array(Unicode)

class RecordStoreService(ServiceBase):
    @rpc(Record, _returns=Array(Record))
    def get_record(ctx, rq): #rq stands for record query, a Record instance
        #ctx.udc.session.query(Record).filter_by(id=album_id).one()
        raise ResourceNotFoundError #TODO implement this shit
    
    @rpc(_returns=Array(Record))
    def get_all_records(ctx):
        return ctx.udc.session.query(Record)

class UserDefinedContext(object):
    def __init__(self):
        self.session = Session()

def _on_method_call(ctx):
    ctx.udc = UserDefinedContext()

def _on_method_context_closed(ctx):
    if ctx.udc is not None:
        ctx.udc.session.commit()
        ctx.udc.session.close()

class MyApplication(Application):
    def __init__(self, services, tns, name=None, in_protocol=None, out_protocol=None):
        super(MyApplication, self).__init__(services, tns, name, in_protocol, out_protocol)

        self.event_manager.add_listener('method_call', _on_method_call)
        self.event_manager.add_listener("method_context_closed", _on_method_context_closed)

    def call_wrapper(self, ctx):
        try:
            return ctx.service_class.call_wrapper(ctx)
        except NoResultFound:
            raise ResourceNotFoundError(ctx.in_object)
        except Fault, e:
            logging.error(e)
            raise
        except Exception, e:
            logging.exception(e)
            raise InternalError(e)

if __name__=='__main__':
    import sys
    
    from wsgiref.simple_server import make_server
    
    port = int(sys.argv[1]) #[0] is __name__
    
    app = MyApplication([RecordStoreService], 'recordstorecoop', in_protocol=Soap11(validator='lxml'), out_protocol=Soap11())
    server = make_server('127.0.0.1', port, WsgiApplication(app))

    TableModel.Attributes.sqla_metadata.create_all()
    
    logging.info("listening to http://127.0.0.1:{}".format(port))
    logging.info("wsdl is at: http://127.0.0.1:{}/?wsdl".format(port))

    server.serve_forever()