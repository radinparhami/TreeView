# Python Flet TreeView

> ## [main.py](/main.py)
```python
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
```

## Code preview:
![2024-08-13_20-57-22](https://github.com/user-attachments/assets/00f866d1-d4b3-493f-903c-7d5b78543c6b)

https://github.com/flet-dev/flet/issues/961
This feature seems to be lacking, I'm here to help ❤️
