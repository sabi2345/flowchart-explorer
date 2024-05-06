from pathlib import Path

import pytest

from flowchart_explorer.explorer import Explorer
from flowchart_explorer.graph.drawio import Drawio


@pytest.fixture()
def drawio_graph():
    drawio = Drawio(Path("./charts/test-explorer/simple_chart.drawio"))
    return drawio.get_graph()


class TestExploler:
    def test_run_simple_graph(self):
        drawio = Drawio(Path("./charts/test-explorer/simple_chart.drawio"))
        graph = drawio.get_graph()
        explorer = Explorer()
        key, flow_path = explorer.run(graph)
        assert key == 4
        assert flow_path[1] == ["2", "3", "5", "7"]

    def test_run_simple_loop(self):
        drawio = Drawio(Path("./charts/test-explorer/simple_loop_chart.drawio"))
        graph = drawio.get_graph()
        explorer = Explorer()
        key, flow_path = explorer.run(graph)
        assert key == 4
        assert flow_path[1] == ["2", "17", "18", "20", "22", "17", "18", "20", "22", "24", "26"]

    def test_run_double_loop(self):
        drawio = Drawio(Path("./charts/test-explorer/simple_double_loop_chart.drawio"))
        graph = drawio.get_graph()
        explorer = Explorer()
        key, flow_path = explorer.run(graph)
        assert len(flow_path.keys()) == 19

    def test_run_triple_loop(self):
        drawio = Drawio(Path("./charts/test-explorer/triple_loop.drawio"))
        graph = drawio.get_graph()
        explorer = Explorer()
        key, flow_path = explorer.run(graph)
        assert key == 3
