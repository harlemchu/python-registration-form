import flet as ft

def main(page: ft.Page):
    page.title = "Registration Form"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Create input fields
    name_field = ft.TextField(label="Name")
    email_field = ft.TextField(label="Email")
    password_field = ft.TextField(label="Password", password=True)

    # Define what happens when the user clicks "Register"
    def register_clicked(e):
        name = name_field.value
        email = email_field.value
        password = password_field.value

        if not name or not email or not password:
            page.snack_bar = ft.SnackBar(ft.Text("Please fill in all fields!"))
            page.snack_bar.open = True
            page.update()
            return
        
        # Successful registration
        page.clean()
        page.add(
            ft.Column(
                [
                    ft.Text(f"✅ Welcome, {name}!", size=30, weight="bold"),
                    ft.Text("You have registered successfully.", size=20),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )

    # --- Now ADD the fields and button to the page directly ---
    page.add(
        ft.Column(
            [
                name_field,
                email_field,
                password_field,
                ft.ElevatedButton("Register", on_click=register_clicked)
            ],
            width=400,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main, view=ft.WEB_BROWSER)
