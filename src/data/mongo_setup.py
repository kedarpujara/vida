import mongoengine
from mongoengine import connect


def global_init():
    # Which database which we're registering to. Core is master?
    # alias_core = 'core'
    # db_name = 'vida'
    # data = {}
    # mongoengine.register_connection(alias=alias_core, name=db_name, data=data)
    init_db()


def init_db():
    db = 'Cluster0'
    username = 'kedarpujara'
    password = '***********'
    host = 'mongodb+srv://'+username+':'+password+'@cluster0-mjpd7.azure.mongodb.net/'+db+'?retryWrites=true&w=majority'
    print(host)
    connect(
        db=db,
        username=username,
        password=password,
        host=host,
        alias='core',
    )
