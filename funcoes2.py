"""
Nome do programa: funcoes2.py
Descricao: Descrever a utilização argumentos de funções em Python
Autor: Evando Chaves
Criado em: 28/07/2024
"""
def loginUsuario(perfil):
    
    if perfil.lower() == 'admin':
        print('Bem-vindo, Administrador')
    
    else:
        print('Bem-vindo, Usuario')

#loginUsuario('Admin')
# loginUsuario('admin')
loginUsuario('User')
#loginUsuario('usuario')