from flowchart_explorer.methods import get_logger

logger = get_logger(__name__)


class FlowChartPath:

    def __init__(self):
        pass

    def draw(self, flow_path: dict[int, list[str]], graph: dict):
        print(graph)
