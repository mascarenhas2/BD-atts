from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.connection import Session
import os

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    #Criando um usuário.
    service.criar_usuario("Marta","marta@gmail.com","123")

    #Listando todos os usuários.
    print("\nListando os usuários.")
    lista_usuarios = service.listar_todos_usuarios()
    for usuario in lista_usuarios:
        print(f"{usuario.id} - {usuario.nome} - {usuario.email} - {usuario.senha}")

os.system("cls || clear")
if __name__ == "__main__":
    main()