import flet as ft
from flet import Column, ElevatedButton, Text, Image, FilePicker
import base64


class Configuracao(ft.UserControl):
    def txtChave(self):
        self.tasks = ft.Column()

        return ft.Column(
            scroll=ft.ScrollMode.ALWAYS,
            expand=True,
            controls=[
                ft.Text("Texto chave:"),
                ft.TextField(keyboard_type=ft.KeyboardType.TEXT)
            ]
        )

    def Mascara(self):

        self.tasks = ft.Column()
        dd = ft.Dropdown(
            label="Mascara",
            hint_text="Escolha a mascara de proteção",
            options=[
                ft.dropdown.Option("Red"),
                ft.dropdown.Option("Green"),
                ft.dropdown.Option("Blue"),
            ],
            autofocus=True,
        )
        return ft.Column([
                ft.Text("Escolha uma mascara de ocultação"),
                ft.Divider(),
                dd
                    ])

    def ImgUpload(self, page):
        file_picker = FilePicker()
        page.overlay.append(file_picker)
        self.tasks = ft.Column()
        self.selected_image = None

        def pick_files_result(e: ft.FilePickerResultEvent):
            if e.files:
                self.selected_image = e.files[0]
                selected_image_text.value = f"Imagem Selecionada: {self.selected_image.name}"
                image_display.src = self.selected_image.path
                image_display.update()

            else:
                selected_image_text.value = "Nenhuma imagem selecionada"
                image_display.src = ""
                image_display.update()

            with open( self.selected_image .path, "rb") as image_file:
                        encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
                        

        pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
        selected_image_text = Text(
            "Imagem Selecionada:",
            size=20,
            color=ft.colors.BLUE_700,
            weight=ft.FontWeight.BOLD,
            italic=True,
        )
        image_display = Image(src="C:/Users/Kelvin/Documents/Projetos/i.a/vazio.gif", height=500)
        page.overlay.append(pick_files_dialog)

        return ft.Column(
            [
                ft.ElevatedButton(
                    "Escolher Imagem",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        allow_multiple=False
                    ),
                ),
                selected_image_text,
                image_display,
            ]
        )