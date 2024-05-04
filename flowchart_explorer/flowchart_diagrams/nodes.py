from diagrams import Node


class StartEnd(Node):
    def __init__(self, label: str = ""):

        attrs = {"shape": "ellipse", "style": "filled",
                 "fixedsize": "false", "fillcolor": "#354093:#354093",
                 "fontcolor": "white", "labelloc": "c",
                 "fontname": "Meiryo UI"}
        super().__init__(label=label, nodeid=None, **attrs)
