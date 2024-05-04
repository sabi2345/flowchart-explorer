from flowchart_explorer.methods import get_logger

logger = get_logger(__name__)


class Draw:

    def __init__(self, max_recursion: int = 1000):
        self._max_recursion = max_recursion

    def draw(self, flow_path: dict[int, list[str]], graph: dict):
        print(graph)
