import flet as ft
import requests
from connect import get_livros
from urllib.parse import urlparse, parse_qs

def main(page: ft.Page):
    page.title = 'Cadastro App'
    page.window_width = 400
    


    def home_page():
        nome_input = ft.TextField(label="Nome do Produto", text_align=ft.TextAlign.LEFT)

        streaming_select = ft.Dropdown(
            options=[
                ft.dropdown.Option("AK" ),
                ft.dropdown.Option("F")
            ],
            label="Selecione a Streaming", width=400
        )

        def carregar_livros():
            lista_livros.controls.clear()
            for i in get_livros():
                lista_livros.controls.append(
                    ft.Container(
                        ft.Text(i['nome']),
                        padding=15,
                        alignment=ft.alignment.center,
                        margin=3,
                        border_radius=10,
                        on_click=lambda e, livro_id=i['id']:page.go(f'/review?id={livro_id}')
                    )
                )
            page.update()   
        def cadastrar(e):
            print(f"Nome: {nome_input.value}, Streaming: {streaming_select.value}")
            if not streaming_select.value:
                print("Erro: Nenhuma opção de streaming foi selecionada!")
                return  # Evita enviar uma requisição inválida

            data = {
                'nome': nome_input.value,
                'streaming': streaming_select.value,
                'categoria': [1]
            }
            headers = {"Content-Type": "application/json"}

            response = requests.post('http://127.0.0.1:8000/api/livros/', json= data, headers=headers)
            print("Resposta do servidor:", response.status_code, response.text)
            carregar_livros()


        cadastrar_btn = ft.ElevatedButton("Cadastrar", on_click=cadastrar)

        lista_livros = ft.ListView()

        

            
        carregar_livros()


        page.views.append(
            ft.View(
                '/',
                controls=[
                    nome_input,
                    streaming_select,
                    cadastrar_btn,
                    lista_livros
                ]
            )
        )

    def review_page(livro_id):
        nota_input = ft.TextField(label="Nota (inteiro)", text_align=ft.TextAlign.LEFT, value=0, width=100)
        comentario_input = ft.TextField(label="Comentarios", multiline=True, expand=True)
        
        
        def avaliar(e):
            print("✅ Botão Avaliar foi clicado!")

            data = {
                'nota': int(nota_input.value),
                'comentarios': comentario_input.value
            }

            try:
                headers = {"Content-Type": "application/json"}  
                response = requests.put(
                    f'http://127.0.0.1:8000/api/livros/{livro_id}', 
                    json=data, 
                    headers=headers
                )

                if response.status_code == 200:
                    page.snack_bar = ft.SnackBar(ft.Text(f"Avaliação enviada com sucesso"))
                else:
                    page.snack_bar = ft.SnackBar(
                        ft.Text(f"Erro ao enviar avaliação: {response.status_code} - {response.text}")
                    )

                page.snack_bar.open = True 

            except Exception as e:
                page.snack_bar = ft.SnackBar(ft.Text(f"Erro de conexão: {e}"))
                page.snack_bar.open = True   
            
            print("🔄 Atualizando a página...")

            page.update()


        avaliar_btn = ft.ElevatedButton("Avaliar", on_click=avaliar)
        voltar_btn = ft.ElevatedButton("Voltar", on_click=lambda _: page.go('/'))


        page.views.append(
            ft.View(
                '/review',
                controls=[
                    nota_input,
                    comentario_input,
                    avaliar_btn,
                    voltar_btn
                ]
            )
        )


    def route_chance(e):
        page.views.clear()
        if page.route == '/':  
            home_page()
        elif page.route.startswith('/review'):
            parsed_url = urlparse(page.route)
            query_params = parse_qs(parsed_url.query)
            livro_id = query_params['id'][0]
            review_page(livro_id)

        page.update()        

    page.on_route_change = route_chance
    page.go('/')
ft.app(target=main)    