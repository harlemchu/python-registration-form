import flet as ft

def main(page: ft.Page):
    page.title = "Registration Form"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    name_field = ft.TextField(label="Name")
    email_field = ft.TextField(label="Email")
    password_field = ft.TextField(label="Password", password=True)

    def register(e):
        if not name_field.value or not email_field.value or not password_field.value:
            page.snack_bar = ft.SnackBar(ft.Text("Please fill in all fields"))
            page.snack_bar.open = True
            page.update()
            return

        page.clean()
        page.add(ft.Text(f"Registration successful!\nWelcome, {name_field.value}!"))

    page.add(
        ft.Column(
            [
                name_field,
                email_field,
                password_field,
                ft.ElevatedButton("Register", on_click=register),
            ],
            width=400,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main, view=ft.WEB_BROWSER)
