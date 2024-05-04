from diagrams import Node


class StartEnd(Node):
    def __init__(self, label: str = ""):

        attrs = {"shape": "ellipse", "style": "filled",
                 "fixedsize": "false", "fillcolor": "lightskyblue",
                 "fontcolor": "black", "labelloc": "c",
                 "fontname": "MS UI Gothic", "color": "darkgray"}
        super().__init__(label=label, nodeid=None, **attrs)


class Action(Node):
    def __init__(self, label: str = ""):

        attrs = {"shape": "box", "style": "filled",
                 "fixedsize": "false", "fillcolor": "lightskyblue",
                 "fontcolor": "black", "labelloc": "c",
                 "fontname": "MS UI Gothic", "color": "darkgray"}
        super().__init__(label=label, nodeid=None, **attrs)


class Decision(Node):
    def __init__(self, label: str = ""):

        attrs = {"shape": "diamond", "style": "filled",
                 "fixedsize": "false", "fillcolor": "lightskyblue",
                 "fontcolor": "black", "labelloc": "c",
                 "fontname": "MS UI Gothic", "color": "darkgray"}
        super().__init__(label=label, nodeid=None, **attrs)


class InLoop(Node):
    def __init__(self, label: str = ""):

        attrs = {"shape": "trapezium", "style": "filled",
                 "fixedsize": "false", "fillcolor": "lightskyblue",
                 "fontcolor": "black", "labelloc": "c",
                 "fontname": "MS UI Gothic", "xlabel": "loopid=1",
                 "color": "darkgray"}
        super().__init__(label=label, nodeid=None, **attrs)


class Outloop(Node):
    def __init__(self, label: str = ""):

        attrs = {"shape": "invtrapezium", "style": "filled",
                 "fixedsize": "false", "fillcolor": "lightskyblue",
                 "fontcolor": "black", "labelloc": "c",
                 "fontname": "MS UI Gothic", "height": "0.75", "xlabel": "loopid=1",
                 "color": "darkgray"}
        super().__init__(label=label, nodeid=None, **attrs)
