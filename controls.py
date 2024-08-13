from typing import Dict, Union
from flet import (
    Control,
    Column,
    Row,
    Container,
    padding,
    Checkbox,
    ControlEvent,
)


NestedControl = Dict[Control, Union["NestedControl", Control]]


class TreeView(Container):
    def __init__(
        self,
        tree_controls: NestedControl,
        depth: int = 30,
        first_title_spacing: int = 20,
        segment_spacing: int = 5,
        title_spacing: int = 0,
        column_spacing: int = 0,
        set_on_change: bool = False,
    ):
        super().__init__()
        self.controls = tree_controls
        self.content: Column = Column([], spacing=column_spacing)
        self.first_title_spacing: int = first_title_spacing
        self.segment_spacing: int = segment_spacing
        self.title_spacing: int = title_spacing
        self.depth: int = depth

        self.set_on_change = set_on_change

        self._last_depth: bool = False
        self._last_depth_num: int = 0
        self._traverse_dict(self.controls)

    def _add_control(
        self,
        control,
        depth,
    ):
        p_top, p_left = 0, self.depth * depth
        if control != list(self.controls.keys())[0]:  # first control
            if depth == 0:
                p_top += self.first_title_spacing

            if self._last_depth_num != depth:
                if self._last_depth:
                    p_top += self.segment_spacing
                if depth != 0:
                    p_top += self.title_spacing

        self._last_depth = False
        self._last_depth_num = depth
        self.content.controls.append(
            Row(
                controls=[
                    Container(
                        control,
                        padding=padding.only(top=p_top, left=p_left),
                    )
                ]
            )
        )

    def _traverse_dict(self, d, depth=0):
        for key, value in d.items():
            self._add_control(control=key, depth=depth)

            if self.set_on_change and isinstance(key, Checkbox):
                if value != {}:
                    if key.on_change is None:
                        key.on_change = self._update

                    if key.value is False:
                        continue

            if isinstance(value, dict):
                self._traverse_dict(value, depth + 1)
            self._last_depth = True

    def _update(self, e: ControlEvent):
        self.content.controls.clear()
        self._traverse_dict(self.controls)
        e.page.update()
