import flet as ft
from controls import TreeView


def main(page: ft.Page):
    page.add(
        TreeView(
            {
                ft.Checkbox("Security"): {
                    ft.Checkbox("Firewall"): {
                        ft.Checkbox("Local"): {},
                        ft.Checkbox("Public"): {},
                    },
                    ft.Checkbox(label="Password Manager"): {},
                    ft.Checkbox("Antivirus"): {},
                },
                ft.Checkbox("Dev", value=True): {
                    ft.Checkbox(
                        label="Show logs", on_change=lambda _: print("This is a test!")
                    ): {},
                    ft.Checkbox("Take Snapshot", value=True): {},
                },
            },
            set_on_change=True,
        )
    )


ft.app(target=main)
