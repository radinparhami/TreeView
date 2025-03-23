# Python Flet TreeView [1.5]

> ## [main.py](/main.py)
```python
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

    segment_2_1.append(ft.Text("2.1.1(This is text!)", weight=ft.FontWeight.BOLD))
    segment_2_1.append(ft.Checkbox("2.1.2"))
    segment_2_1.append(ft.Text("2.1.3(This is text!)", weight=ft.FontWeight.BOLD))

    page.add(root)


ft.app(target=main)

```

## Code preview:
![2024-08-13_20-57-22](https://github.com/user-attachments/assets/00f866d1-d4b3-493f-903c-7d5b78543c6b)

https://github.com/flet-dev/flet/issues/961
This feature seems to be lacking, I'm here to help ❤️
