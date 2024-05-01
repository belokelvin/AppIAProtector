import flet as ft
from controle import Configuracao


def main(page):

    page.adaptive = True
    file_picker = ft.FilePicker()
    page.overlay.append(file_picker)
    page.scroll = ft.ScrollMode.ALWAYS

    

    page.appbar = ft.AppBar(
        title=ft.Text("Marca d'água imperceptível"),
        center_title=True,
        bgcolor=ft.colors.with_opacity(
            0.04, ft.cupertino_colors.SYSTEM_BACKGROUND),
    )


# - -------- menu lateral
    page.drawer = ft.NavigationDrawer(
        controls=[
            ft.Container(height=12),
            ft.NavigationDrawerDestination(
                label="Item 1",
                icon=ft.icons.DOOR_BACK_DOOR_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.DOOR_BACK_DOOR),
            ),
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.MAIL_OUTLINED),
                label="Item 2",
                selected_icon=ft.icons.MAIL,
            ),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.PHONE_OUTLINED),
                label="Item 3",
                selected_icon=ft.icons.PHONE,
            ),
        ],
    )

    def show_drawer(e):
        page.drawer.open = True
        page.drawer.update()

    page.horizontal_alignment = page.vertical_alignment = "center"
    page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.CHECK)
    page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED

    page.bottom_appbar = ft.BottomAppBar(
        bgcolor=ft.colors.BLUE,
        shape=ft.NotchShape.CIRCULAR,
        content=ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.MENU,
                              icon_color=ft.colors.WHITE, on_click=show_drawer),
                ft.Container(expand=True),
                ft.IconButton(icon=ft.icons.CANCEL,
                              icon_color=ft.colors.WHITE),
            ]
        ),
    )

    app = Configuracao(ft.UserControl)
    app1 = app.txtChave()
    app2 = app.Mascara()
    app3 = app.ImgUpload(page)
    page.add(
        ft.Row([
                app1
        ]),
        ft.Divider(height=9, thickness=3),
        ft.Row([
                app2
        ]),
        ft.Divider(height=9, thickness=3),
        ft.Row([
                app3
        ])

            )


ft.app(target=main)
