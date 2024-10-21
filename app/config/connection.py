from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

# Parâmetros de conexão com MySQL.
db_user = "user"
db_password = "user_password"
db_host = "localhost"
db_port = "3306"
db_name = "meu_banco"
# URL de conexão para BD MySQL . 
DATABASE_URL = f"mysql+pymsql://(db_user):(db_password)@(db_host):(db_port)/(db_name)"

#Conectando ao banco de dados.
db = create_engine(DATABASE_URL)
Session = sessionmaker(bind=db)
session = Session()

@contextmanager
def get_db():
    db = Session()
    try:
        yield db # Caso a sessão realize todas as tarefas, salva a operação.
        db.commit()
    except Exception as erro:
        db.rollback() # Desfaz todas as alterações em caso de erro em alguma operação.
        raise erro # Lanca uma exception.
    finally:
        db.close() # Fecha conexão com banco de dados.
