from classes import Usuario as u
from controllers import usuario_controller as uc
import flet as ft

# TESTE
def main(page: ft.Page):
    page.window_left=525
    page.window_resizable=False
    page.window_height=810
    page.window_width=500
    page.horizontal_alignment="CENTER"
    page.vertical_alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    page.title = "CADASTRO DE USUÁRIOS"
    page.padding = 85
    
    
    try:
        def confirmar(e):
            cadastro_modal.open = False
            add_user()
            page.update()
        
        def cancelar(e):
            cadastro_modal.open = False
            alerta_cadastro_feito.open = False
            alert_erro_cadastro.open = False
            page.update()
        
        #? FUNÇÃO PARA RETORNAR OS USUÁRIOS NO PROMPT E LIMPAR TODA A TELA  
        def feedback_usuarios_cli(e):
            print("="*40)
            print("= USUÁRIOS")
            print("="*40)
            for ur in uc.retornar_usuarios():
                print(f"Nome: {ur.nome} | Email: {ur.email} | Telefone: {ur.telefone} | Gênero: {ur.genero}")
            print("="*40)
            page.clean()
            
            
        #? DEFININDO O MODAL DOS CADASTROS
        cadastro_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Por favor confirme o cadastro"),
            content=ft.Text("Deseja fazer o cadastro?"),
            actions=[
                ft.TextButton("Sim", on_click=confirmar,),
                ft.TextButton("Não", on_click=cancelar)
            ],
            actions_alignment=ft.MainAxisAlignment.END
        )
        
        #? DEFININDO O ÍCONE
        icone = ft.Icon(
            name=ft.icons.ACCOUNT_CIRCLE,
            size=95
        )
        
        #? DEFININDO O TEXTO DO CENTRO
        txt_center = ft.Text(
            value = "CADASTRO", 
            size=35, 
            weight=ft.FontWeight.BOLD
        )
        
        #? DEFININDO OS CAMPOS DE TEXTO
        txtField_nome = ft.TextField(
            label="Nome",
            hint_text="Digite seu nome",
            autofocus=True,
            capitalization=ft.TextCapitalization.WORDS,
            keyboard_type=ft.KeyboardType.NAME
        )
        
        txtField_email = ft.TextField(
            label = "Email",
            hint_text="Digite seu email",
            keyboard_type=ft.KeyboardType.EMAIL
            
        )
        
        txtField_tel = ft.TextField(
            label = "Telefone",
            hint_text="Telefone",
            keyboard_type=ft.KeyboardType.PHONE
        )
        
        #? DEFININDO O DROPDOWN DE GÊNEROS
        dropdown_generos = ft.Dropdown(
            label="Gênero",
            hint_text="Escolha seu gênero",
            options=[
                ft.dropdown.Option("Homem"),
                ft.dropdown.Option("Mulher"),
                ft.dropdown.Option("Prefiro não dizer")
            ]
        )
        
        #? ALERTA QUANDO O CADASTRO TEM SUCESSO
        alerta_cadastro_feito = ft.AlertDialog(
                    modal=True,
                    content=ft.Text("Usuário cadastrado com sucesso!"),
                    actions=[
                        ft.TextButton("Ok", on_click=cancelar)
                    ],
                    actions_alignment=ft.MainAxisAlignment.END
                )
        
        #? ALERTA SE HOUVER ERRO
        alert_erro_cadastro = ft.AlertDialog(
            modal=True,
            content=ft.Text("Não foi possível fazer o cadastro."),
            actions=[
                ft.TextButton("Ok", on_click=cancelar)
            ],
            actions_alignment=ft.MainAxisAlignment.END
        )
        
        #? FUNÇÃO PARA ADICIONAR O USUÁRIO A LISTA DE USUÁRIOS
        def add_user():
            user = u.Usuario(
                txtField_nome.value,
                txtField_email.value,
                txtField_tel.value,
                dropdown_generos.value)
            
            if uc.add_usuario(user):
                page.dialog = alerta_cadastro_feito
                alerta_cadastro_feito.open = True
                page.update()
            else:
                page.dialog = alert_erro_cadastro
                alert_erro_cadastro.open = True
                page.update()
        
        
        
        #? FUNÇÃO PARA ABRIR O MODAL E VERIFICAR SE OS CAMPOS ESTÃO COMPLETOS
        def abrir_modal(e):
            if not txtField_nome.value:
                txtField_nome.error_text = "Por favor digite seu nome"
                page.update()
            if not txtField_email.value:
                txtField_email.error_text = "Por favor digite seu email"
                page.update()
            if not txtField_tel.value:
                txtField_tel.error_text = "Por favor digite seu telefone"
                page.update()
            if not dropdown_generos.value:
                dropdown_generos.error_text = "Por favor escolha seu gênero"
                page.update()
            else:
                page.dialog = cadastro_modal
                cadastro_modal.open = True
                page.update()

                
            
        #? DEFININDO O BOTÃO DE CADASTRO
        
        botao_cadastro = ft.ElevatedButton(
            "CADASTRAR", 
            on_click=abrir_modal,
            scale=1.5
            
        )
        
        #? DEFININDO O BOTÃO PARA MOSTRAR OS USUÁRIOS NO PROMPT
        botao_mostrar_usuarios = ft.ElevatedButton(
            "MOSTRAR USUÁRIOS",
            on_click= feedback_usuarios_cli,
            scale=1.5
        )
        
        
        page.add(txt_center,
                icone, 
                txtField_nome, 
                txtField_email,
                txtField_tel,
                dropdown_generos,
                botao_cadastro,
                botao_mostrar_usuarios)
        page.update()
    except ValueError as error:
        print(f"Erro: {error}")

ft.app(target=main)