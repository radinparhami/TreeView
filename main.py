import flet as ft

from custom_controls import TreeView


def main(page: ft.Page):
    page.title = "TreeView"

    root = TreeView(auto_collapse=True)
    root.append(ft.Checkbox("1"))
    segment_2 = root.append(ft.Checkbox("2", value=True))
    root.append(ft.Checkbox("3"))

    segment_2_1 = segment_2.append(ft.Checkbox("2.1", value=True))
    segment_2.append(ft.Checkbox("2.2"))

    segment_2_1.append(ft.Text("2.1.1(This is a text!)", weight=ft.FontWeight.BOLD))
    segment_2_1.append(ft.Checkbox("2.1.2"))
    segment_2_1.append(ft.Text("2.1.3(This is a text!)", weight=ft.FontWeight.BOLD))

    page.add(root)


ft.app(target=main)
