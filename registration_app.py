# import os
# import flet as ft

# def main(page: ft.Page):
#     page.title = "Registration Form"
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER
#     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

#     # Create TextFields
#     name_field = ft.TextField(label="Name")
#     email_field = ft.TextField(label="Email")
#     password_field = ft.TextField(label="Password", password=True)

#     # Initialize client storage
#     page.client_storage.set("registered_name", "")

#     def register(e):
#         name = name_field.value
#         email = email_field.value
#         password = password_field.value

#         if not name or not email or not password:
#             page.snack_bar = ft.SnackBar(content=ft.Text("Please fill in all fields"))
#             page.snack_bar.open = True
#             page.update()
#             return

#         # Store the name so we can use it later
#         page.client_storage.set("registered_name", name)

#         # Simulate registration process
#         print(f"Registration successful. Name: {name}, Email: {email}, Password: {password}")
#         page.go("/success")

#     def route_change(e):
#         page.clean()
#         if e.route == "/success":
#             # Fetch stored name
#             registered_name = page.client_storage.get("registered_name") or "User"

#             page.add(
#                 ft.Column(
#                     [
#                         ft.Text(f"🎉 Registration successful!\nWelcome {registered_name}!", size=30, weight="bold"),
#                         ft.ElevatedButton("Back to Form", on_click=lambda _: page.go("/")),
#                     ],
#                     alignment=ft.MainAxisAlignment.CENTER,
#                     horizontal_alignment=ft.CrossAxisAlignment.CENTER,
#                 )
#             )
#         else:
#             page.add(
#                 ft.Column(
#                     [
#                         ft.Text("Registration Form", size=30, weight="bold"),
#                         name_field,
#                         email_field,
#                         password_field,
#                         ft.ElevatedButton("Register", on_click=register),
#                     ],
#                     alignment=ft.MainAxisAlignment.CENTER,
#                     horizontal_alignment=ft.CrossAxisAlignment.CENTER,
#                 )
#             )
#         page.update()

#     page.on_route_change = route_change
#     page.go(page.route)

# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 8080))  # <--- Heroku provides PORT
#     ft.app(target=main, port=port, view=ft.WEB_BROWSER)
import os
import flet as ft

def main(page: ft.Page):
    page.title = "Registration Form"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Create TextFields
    name_field = ft.TextField(label="Name",width=500)
    email_field = ft.TextField(label="Email",width=500)
    password_field = ft.TextField(label="Password", password=True,width=500)

    def register(e):
        name = name_field.value
        email = email_field.value
        password = password_field.value

        if not name or not email or not password:
            page.snack_bar = ft.SnackBar(content=ft.Text("Please fill in all fields"))
            page.snack_bar.open = True
            page.update()
            return

        # Store the name so we can use it later
        page.client_storage.set("registered_name", name)

        # Simulate registration process
        print(f"Registration successful. Name: {name}, Email: {email}, Password: {password}")
        page.go("/success")

    def route_change(e):
        page.clean()
        if e.route == "/success":
            # Fetch stored name
            registered_name = page.client_storage.get("registered_name") or "User"

            page.add(
                ft.Column(
                    [
                        ft.Text(f"🎉 Registration successful!\nWelcome {registered_name}!", size=30, weight="bold"),
                        ft.ElevatedButton("Back to Form", on_click=lambda _: page.go("/")),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    width=450,  # The Column itself will wrap contents if they exceed this width
                )
            )
        else:
            page.add(
                ft.Column(
                    [
                        ft.Text("Registration Form", size=30, weight="bold"),
                        name_field,
                        email_field,
                        password_field,
                        ft.ElevatedButton("Register", on_click=register),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )
        page.update()

    page.on_route_change = route_change
    page.go(page.route)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Heroku provides PORT
    ft.app(target=main, port=port, view=ft.WEB_BROWSER)
