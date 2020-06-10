from mongoengine import connect


def global_init():
    # Which database which we're registering to. Core is master
    db = '*****'
    username = '******'
    password = '******'
    host = 'mongodb+srv://'+username+':'+password+'@cluster0-mjpd7.azure.mongodb.net/'+db+'?retryWrites=true&w=majority'
    alias = 'core'
    connect(
        db=db,
        username=username,
        password=password,
        host=host,
        alias=alias,
    )
