from classes import Usuario as us
from controllers import usuario_controller as uc

continuar : str

try:
    while True:
        u = us.Usuario(
            str(input("Nome: ")),
            str(input("Email: ")),
            str(input("Tel: ")),
            str(input("gen: "))
        )
        
        if uc.add_usuario(u):
            print("Usuário adicionado com sucesso!")
        else:
            print("Não foi possível adicionar o usuário pois ele já existe!")
        
        continuar = str(input("Deseja continuar(S/N)?\n"))
        if continuar in "Nn":
            break
    
    for u in uc.retornar_usuarios():
        print(f"Nome: {u.nome} | Email: {u.email} | Tel: {u.telefone} | gen: {u.genero}")
except ValueError as err:
    print(err)
    
    