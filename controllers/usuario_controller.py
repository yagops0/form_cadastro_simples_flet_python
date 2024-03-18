from classes import Usuario


lista_usuarios = []

#? FUNÇÕES

def existe_usuario(nome : str):
    for u in lista_usuarios:
        if u.nome == nome:
            return True
    return False

def add_usuario(u : Usuario):
    if existe_usuario(u.nome):
        return False
    else:
        lista_usuarios.append(u)
        return True
    
def retornar_usuarios():
    return lista_usuarios



