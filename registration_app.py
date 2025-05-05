import os
import flet as ft

def main(page: ft.Page):
    page.title = "Registration Form"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Create TextFields
    std_id_field = ft.TextField(label="Student ID", width=500)
    name_field = ft.TextField(label="Name", width=500)
    email_field = ft.TextField(label="Email", width=500)
    password_field = ft.TextField(label="Password", password=True, width=500)

    # Sex checkboxes
    male_checkbox = ft.Checkbox(label="Male")
    female_checkbox = ft.Checkbox(label="Female")

    # Mutually exclusive logic for sex
    def on_male_change(e):
        if male_checkbox.value:
            female_checkbox.value = False
        page.update()

    def on_female_change(e):
        if female_checkbox.value:
            male_checkbox.value = False
        page.update()

    male_checkbox.on_change = on_male_change
    female_checkbox.on_change = on_female_change

    # Status dropdown
    status_dropdown = ft.Dropdown(
        label="Status",
        width=500,
        options=[
            ft.dropdown.Option("Single"),
            ft.dropdown.Option("Married"),
            ft.dropdown.Option("Comflicated"),
            ft.dropdown.Option("prefer not to tell"),
        ]
    )

    # Create SnackBar
    snack = ft.SnackBar(content=ft.Text(""))
    page.overlay.append(snack)  # <<-- IMPORTANT: Add to overlay!
    page.snack_bar = snack

    def register(e):
        stdid = std_id_field.value
        name = name_field.value
        email = email_field.value
        password = password_field.value
        sex = "Male" if male_checkbox.value else "Female" if female_checkbox.value else None
        status = status_dropdown.value

        if not stdid or not name or not email or not password or not sex or not status:
            page.snack_bar.content = ft.Text("Please fill in all fields", color="white")
            page.snack_bar.bgcolor = "red"
            page.snack_bar.open = True
            page.update()
            return

        # Store the form data
        page.client_storage.set("registered_id", stdid)
        page.client_storage.set("registered_name", name)
        page.client_storage.set("registered_email", email)
        page.client_storage.set("registered_sex", sex)
        page.client_storage.set("registered_status", status)

        print(f"Registration successful. Name: {name}, Email: {email}, Password: {password}")
        page.go("/success")

    def route_change(e):
        page.clean()
        if e.route == "/success":
            registered_id = page.client_storage.get("registered_id") or "User"
            registered_name = page.client_storage.get("registered_name") or "User"
            registered_email = page.client_storage.get("registered_email") or "User"
            registered_sex = page.client_storage.get("registered_sex") or "User"
            registered_status = page.client_storage.get("registered_status") or "User"

            page.add(
                ft.Column(
                    [
                        ft.Text(f"Registration successful!\nWelcome {registered_name}!\n\nHere is your profile info:\nID number: {registered_id}\nName: {registered_name}\nEmail: {registered_email}\nSex: {registered_sex}\nStatus: {registered_status}", size=30, weight="bold"),
                        ft.ElevatedButton("Back to Form", on_click=lambda _: page.go("/")),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )
        else:
            page.add(
                ft.Column(
                    [
                        ft.Text("Registration Form", size=30, weight="bold"),
                        std_id_field,
                        name_field,
                        ft.Row([
                            ft.Text("Sex:"),
                            male_checkbox,
                            female_checkbox
                        ] ,alignment=ft.MainAxisAlignment.START,width=500),
                        status_dropdown,
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
    port = int(os.environ.get("PORT", 8180))  # Heroku provides PORT
    ft.app(target=main, port=port, view=ft.WEB_BROWSER)
