import flet as ft


class TreeView(ft.ListView):
    def __init__(
        self,
        depth: int = 0,
        parent_obj: ft.Control = None,
        parent: "TreeView" = None,
        spacing: int = 0,
        # -- roots(parent) --
        root_top: int = 20,
        # -- segments(child) --
        segment_left: int = 30,
        segment_top: int = 5,
        segment_first_top: int = 0,
        # other
        auto_collapse: bool = False,
        expand: bool = False,
        visible: bool = True,
    ):
        super().__init__()

        assert isinstance(parent, None | TreeView)
        self.parent_obj: ft.Container = parent_obj
        self.parent: TreeView = parent

        self.spacing = spacing
        self.root_top = root_top
        self.segment_left = segment_left
        self.segment_top = segment_top
        self.segment_first_top = segment_first_top

        self.auto_collapse = self.parent.auto_collapse if self.parent else auto_collapse
        self.expand = expand

        self.__is_first_control = True
        self.__depth = depth
        self.__controls = []
        self.__visibility = visible

    @property
    def visible(self):
        return self.__visibility

    @visible.setter
    def visible(self, value):
        self.__visibility = value

    def append(self, control: ft.Control):
        # if the control has parent so thats a child(segment) else its the
        if self.parent:
            padding = ft.padding.only(left=self.segment_left * self.__depth)
            if self.__is_first_control:
                padding.top = self.segment_top
            else:
                # segment first row top padding size
                padding.top = self.segment_first_top
        else:
            padding = ft.padding.only()
            if self.__is_first_control:
                padding.top = self.root_top

        res_control = self.__customize_control(control, padding)

        res_obj = TreeView(
            depth=self.__depth + 1,
            parent=self.parent or self,
            parent_obj=res_control,
        )
        res_control.data = res_obj

        if self.auto_collapse and isinstance(control, ft.Checkbox):
            control.data = res_obj
            last_func = control.on_change
            if last_func:
                control.on_change = lambda e: (
                    self.__parent_on_click(e),
                    last_func(e),
                )
            else:
                control.on_change = self.__parent_on_click

        self.__controls.append(res_control)
        self.__is_first_control = False

        return res_obj

    def before_update(self):
        if isinstance(self.parent, TreeView):
            return

        self.sorted = []
        self.__sort(self.__controls)
        self.controls = self.sorted
        del self.sorted

    def __customize_control(self, control: ft.Control, padding: ft.padding):
        visible = True
        if (
            self.parent
            and self.auto_collapse
            and self.parent_obj.content.value is False
        ):
            visible = False

        return ft.Container(
            control,
            padding=padding,
            visible=visible,
        )

    def __sort(self, controls: list):
        for control in controls:
            obj = self.__check_control(control)
            if obj.__visibility:
                self.sorted.append(control)
            if obj.__controls:
                self.__sort(obj.__controls)

    def __parent_on_click(self, e: ft.ControlEvent):
        obj = self.__check_control(e.control)
        self.__set_visibility(obj.__controls, e.control.value)
        e.page.update()

    def __set_visibility(self, controls: list, value: bool):
        for control in controls:
            obj = self.__check_control(control)
            obj.__visibility = value
            if len(obj.__controls) > 0:
                self.__set_visibility(obj.__controls, value)

    def __check_control(self, control: ft.Control) -> "TreeView":
        if not isinstance(control.data, TreeView):
            raise ValueError("Control.data must be an instance of TreeView")
        return control.data
