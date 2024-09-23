import flet as ft
import asyncio
import os

def main(page: ft.Page):
    # Definindo o título e as propriedades da janela
    page.title = "Soma dos Números"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.theme_mode = ft.ThemeMode.DARK

    # Setando altura e largura da janela
    page.window_width = 450  # Largura da janela
    page.window_height = 1000  # Altura da janela

    page.update()
    



    # Adicionando AppBar
    page.appbar = ft.AppBar(
        title=ft.Text("Roleta Soma"),
        center_title=True,
        bgcolor=ft.colors.PINK_500,
       
    )

    # Função para calcular os resultados da subtração
    def calcular_resultados(numero):
        return {valor: numero - valor for valor in [8, 9, 11, 12, 13, 14, 15, 16]}
        

    # Função para determinar a cor com base no valor
    def obter_cor(valor):
        if valor in [8, 9]:
            return ft.colors.GREEN
        elif valor in [11, 12, 13]:
            return ft.colors.BLUE
        elif valor in [14, 15, 16]:
            return ft.colors.RED
        return ft.colors.GRAY

    # Função para filtrar a tabela com base no número digitado
    def filtrar_tabela(numero):
        for row in tabela.controls:
            if row.controls[0].value == str(numero) or numero == "":
                row.visible = True
            else:
                row.visible = False
        tabela.update()

    # Função para atualizar a interface com os resultados
    def atualizar_resultados(e):
        try:
            numero = int(campo_numero.value)
            if numero < 0:
                texto_erro.value = "Por favor, insira um número positivo."
                texto_erro.color = ft.colors.RED
                caixas_resultado.controls.clear()
            else:
                resultados = calcular_resultados(numero)
                caixas_resultado.controls.clear()
                display_numero.value = ""
                display_numero.color = ft.colors.WHITE
                for valor, resultado in resultados.items():
                    caixas_resultado.controls.append(
                        ft.Container(
                            content=ft.Text(f"{valor} = {resultado}", size=15, color=ft.colors.WHITE),
                            padding=2,
                            height=55,
                            width=50,
                            bgcolor=obter_cor(valor),
                            expand=True,
                            margin=3,
                            border_radius=100,
                            alignment=ft.alignment.center,
                        )
                    )
                filtrar_tabela(numero)
                texto_erro.value = ""
        except ValueError:
            texto_erro.value = "Insira um número válido." ,
            texto_erro.color = ft.colors.WHITE
            caixas_resultado.controls.clear()
        page.update()

    # Função para limpar rapidamente a interface ao pressionar "Backspace"
    async def teclado_evento(e: ft.KeyboardEvent):
        if e.key == "Backspace":
            campo_numero.value = ""
            caixas_resultado.controls.clear()
            texto_erro.value = ""
            display_numero.value = ""
            filtrar_tabela("")
            texto_erro.value = "Campo limpo!"
            texto_erro.color = ft.colors.GREEN
            await asyncio.sleep(10)
            texto_erro.value = ""
            page.update()

    # Inicializando a variável de controle de visibilidade
    resultados_visiveis = True

    # Função para alternar a visibilidade dos resultados
    def alternar_resultados(e):
        nonlocal resultados_visiveis
        resultados_visiveis = not resultados_visiveis
        caixas_resultado.visible = resultados_visiveis
        titulo_resultados.visible = resultados_visiveis
        botao_alternar_resultados.icon = ft.icons.VISIBILITY if resultados_visiveis else ft.icons.VISIBILITY_OFF
        page.update()

    # Widgets da interface
    campo_numero = ft.TextField(
        label="Digite o último número que saiu",
        width=2, 
        height=40,
        expand=True, # 20% da largura da janela
        on_change=atualizar_resultados,
        on_submit=atualizar_resultados,
        autofocus=True
    )

    # Adicionando um Container para o campo com a cor de fundo
    container_campo_numero = ft.Container(
        content=campo_numero,
        width=2,
        height=50,
        bgcolor=ft.colors.BLUE_GREY_900,
        padding=3,
        border_radius=8,
        expand=True  # Expande para ocupar o espaço disponível
    )

    display_numero = ft.Text(value="", size=56, weight="bold", color=ft.colors.BLACK87)
    texto_erro = ft.Text(value="", size=10, bgcolor=ft.colors.BLUE)
    caixas_resultado = ft.Row(visible=True, spacing=10, expand=True)

    # Adicionando o título da seção de resultados
    titulo_resultados = ft.Container(
        content=ft.Text("Resultados da Subtração", size=24, weight="bold", color=ft.colors.WHITE),
        padding=1,
        border_radius=8,
        expand=True,
        visible=True
    )

    # Criando a tabela manualmente com Row e adicionando um fundo (bgcolor)
    tabela_dados = [
        ("0", "12, (18), 14, (1), 4, (17), 13, (11)"),
        ("1", "5, (30), 27, (34), 9, (7), 3, (0)"),
        ("2", "15, (3), 7, (18), 6, (11), 10, (23)"),
        ("3", "7, (9), 1, (16), 15, (2), 34, (13)"),
        ("4", "0, (12), 18, (9), 17, (13), 8, (10)"),
        ("5", "30, (27), 25, (21), 1, (9), 7, (12)"),
        ("6", "2, (15), 3, (12), 11, (10), 33, (20)"),
        ("7", "9, (1), 5, (23), 3, (15), 2, (17)"),
        ("8", "13, (17), 4, (15), 24, (20), 22, (29)"),
        ("9", "1, (5), 30, (36), 7, (3), 15, (4)"),
        ("10", "11, (6), 2, (19), 33, (31), 29, (28)"),
        ("11", "6, (2), 15, (0), 10, (33), 31, (22)"),
        ("12", "18, (14), 16, (5), 0, (4), 17, (6)"),
        ("13", "17, (4), 0, (3), 8, (24), 20, (31)"),
        ("14", "16, (23), 36, (27), 18, (12), 0, (15)"),
        ("15", "3, (7), 9, (14), 2, (6), 11, (8)"),
        ("16", "23, (36), 34, (25), 14, (18), 12, (3)"),
        ("17", "4, (0), 12, (7), 13, (8), 24, (33)"),
        ("18", "14, (16), 23, (30), 12, (0), 4, (2)"),
        ("19", "26, (28), 22, (31), 25, (27), 30, (23)"),
        ("20", "24, (8), 13, (6), 22, (28), 26, (32)"),
        ("21", "32, (35), 29, (22), 34, (36), 23, (5)"),
        ("22", "20, (24), 8, (11), 28, (26), 19, (21)"),
        ("23", "36, (34), 21, (19), 16, (14), 18, (7)"),
        ("24", "8, (13), 17, (2), 20, (22), 28, (35)"),
        ("25", "19, (26), 28, (29), 27, (30), 5, (16)"),
        ("26", "28, (22), 20, (33), 19, (25), 27, (36)"),
        ("27", "25, (19), 26, (35), 30, (5), 1, (14)"),
        ("28", "22, (20), 24, (10), 26, (19), 25, (34)"),
        ("29", "31, (33), 10, (8), 35, (32), 21, (25)"),
        ("30", "27, (25), 19, (32), 5, (1), 9, (18)"),
        ("31", "33, (10), 11, (13), 29, (35), 32, (19)"),
        ("32", "35, (29), 31, (20), 21, (34), 36, (30)"),
        ("33", "10, (11), 6, (17), 31, (29), 35, (26)"),
        ("34", "21, (32), 35, (28), 36, (23), 16, (1)"),
        ("35", "29, (31), 33, (24), 32, (21), 34, (27)"),
        ("36", "34, (21), 32, (26), 23, (16), 14, (9)"),
    ]

    # Adicionando o título da tabela
    titulo_tabela = ft.Container(
        content=ft.Text("Tabela de Números", size=24,  weight="bold", color=ft.colors.WHITE),
        padding=10,
        width=500,
        height=300,
        expand=True,
    )

    # Criando o conteúdo da tabela
    tabela = ft.Column(expand=True)
    for dado in tabela_dados:
        numeros = dado[1].split(",")
        tabela.controls.append(
            ft.Row(
                controls=[
                    ft.Text(dado[0], size=30,  color=ft.colors.RED, width=50),
                    ft.Row(
                        controls=[
                            ft.Container(
                                content=ft.Text(
                                    num.strip(),
                                    size=15,
                                    expand=True,
                                    color=ft.colors.WHITE if "(" in num and ")" in num else ft.colors.WHITE
                                ),
                                bgcolor=ft.colors.RED if "(" in num and ")" in num else ft.colors.BLUE,
                                padding=2,
                                width=40,
                                height=30,
                                border_radius=10,
                                expand=True,
                                alignment=ft.alignment.center
                            ) for num in numeros
                        ],
                        spacing=5,
                    )
                ],
                spacing=1,
                alignment=ft.MainAxisAlignment.START
            )
        )

    # Encapsulando a tabela dentro de um Container com cor de fundo
    container_tabela = ft.Container(
        content=ft.Column([titulo_tabela, tabela], expand=True),  # Adiciona o título da tabela junto da tabela
        bgcolor=ft.colors.BLACK12,
        padding=ft.Padding(10, 10, 10, 10),
        border_radius=20,
        expand=True  # Expande o container para ocupar o espaço disponível
    )

    # Adicionando o botão para ativar/desativar resultados
    botao_alternar_resultados = ft.IconButton(
        icon=ft.icons.VISIBILITY if resultados_visiveis else ft.icons.VISIBILITY_OFF,
        on_click=alternar_resultados,
        tooltip="Mostrar/Ocultar Resultados da Subtração",
        icon_color=ft.colors.WHITE,
    )

    # Widgets de interface adicionais
    conteudo = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    controls=[container_campo_numero, display_numero],
                    spacing=30,
                    width=200,

                    alignment=ft.MainAxisAlignment.START,
                    expand=True
                ),
                texto_erro,
                ft.Row(
                    controls=[botao_alternar_resultados, titulo_resultados],
                    spacing=10,
                    alignment=ft.MainAxisAlignment.START,
                    expand=True
                ),
                caixas_resultado,
                container_tabela
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.START,
            expand=True
        ),
        alignment=ft.alignment.center,
        expand=True
    )

    # Verifique se a imagem existe
    imagem_path = os.path.join(os.getcwd(), "cassino.jpg")
    if not os.path.isfile(imagem_path):
        texto_erro.value = f"Imagem de fundo não encontrada em: {imagem_path}"
        texto_erro.color = ft.colors.RED
    else:
        # Adicionando a imagem de fundo com opacidade de 20%
        background = ft.Image(
            src=imagem_path,
            fit=ft.ImageFit.COVER,
            width=1920,
            height=1080,
            opacity=0.2,
            border_radius=10,
            expand=True
        )

        # Criando um Stack com a imagem de fundo e o conteúdo
        stack = ft.Stack(
            [
                background,
                conteudo
            ],
            expand=True  # Expande o Stack para ocupar o espaço disponível
        )

        # Adiciona o Stack à página
        page.add(stack)

    page.on_keyboard_event = teclado_evento
    page.update()

ft.app(target=main)   
