import flet as ft
import pygame


def main(page: ft.Page):
    def playAudio(e=None,arquivo=None):
        pygame.mixer.init()
        pygame.mixer.music.load(arquivo)
        pygame.mixer.music.play()

    def naoLagosta(e=None):
        page.title = "Não Lagosta Yupiiiiii!"
        playAudio(arquivo="Knucles.mp3")
        background = ft.Container(
            content=ft.Image(
                src="Knuckles-Approve-Lagosta.jpg",
                fit=ft.ImageFit.COVER
            ),
            width=800,
            height=600
        )

        page.add(
            ft.Stack(
                [background],
                width=800,
                height=600
            )
        )
        page.update()
    def lagosta(e=None):
        page.title = "Oh no! Lagosta detected"
        playAudio(arquivo='lobster-jumpsacre-audio.mp3')
        texto_lagosta = ft.Text(
            "Você é uma lagosta!!!!",
            size=30,
            color=ft.colors.BLACK,
            weight=ft.FontWeight.NORMAL
        )
        background = ft.Container(
            content=ft.Image(
                src="lobster.jpg",
                fit=ft.ImageFit.COVER
            ),
            width=800,
            height=600
        )

        # Adiciona novo conteúdo à página
        page.add(
            ft.Stack(
                [background,
                 ft.Container(
                     content=texto_lagosta,
                     alignment=ft.alignment.center,
                     width=page.width,
                     height=100  # Para garantir que apareça no topo
                 )],
                width=800,
                height=600
            )
        )
        page.update()


    def open_popup(e):
        dialog = ft.AlertDialog(
            title=ft.Text("Verificando"),
            content=ft.Text("Você é uma lagosta?"),
            actions=[
                ft.Container(
                    content=ft.TextButton("Sim",on_click=lambda e: close_dialogAndLagosta()),
                    alignment=ft.alignment.center_left
                ),
                 ft.Container(
                    content=ft.TextButton("Não",on_click=lambda e: close_dialogAndNotLagosta()),
                    alignment=ft.alignment.center_left
                )
            ]
        )
        page.dialog = dialog
        dialog.open = True
        page.update()
    
    def close_dialog():
        page.dialog.open=False
        page.update()
        
    def close_dialogAndLagosta():
        page.clean()
        page.dialog.open=False
        page.update()
        lagosta()
    def close_dialogAndNotLagosta():
        page.clean()
        page.dialog.open=False
        page.update()
        naoLagosta()
        
        
    page.title = "Verificador de Lagosta"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page_width = 800
    page_height = 600
    page.window.width = page_width
    page.window.height = page_height
    page.window.resizable = False
    page.window.maximizable = False
    page.window_borderless = True
    
    
    
    #usar onclick para chamar uma funçao para abrir a outra pagina
    startButton = ft.ElevatedButton(text="Começar",on_click=open_popup,
                            bgcolor=ft.colors.BLACK,
                            color=ft.colors.WHITE, width=130, height=50, 
                            style=ft.ButtonStyle(text_style=ft.TextStyle(size=20), 
                            shape=ft.RoundedRectangleBorder(radius=5)))
    
    texto01 = ft.Text(
                "Teste de lagosticidade",
                size=50,
                color=ft.colors.BLACK,
                weight=ft.FontWeight.NORMAL,
                
            )
    
    background = ft.Container(
            content=ft.Image(
                src="background1.jpg",
                fit=ft.ImageFit.COVER
            ),
            width=800,
            height=600
    )
    page.add(
        ft.Stack(
            [background,
             ft.Container(
            content=texto01,
            alignment=ft.alignment.center,
            width = page.width,
            height=100 # para garantir que apareça no topo
                ),
             ft.Container(
                 content=startButton,
                 left=330,
                 top=300
                 
                 
             )
            ],
            
            width=800,
            height=600
        ),
        
        
    )
    
    
ft.app(target=main)
