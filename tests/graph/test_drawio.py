import xml.etree.ElementTree as Et
from pathlib import Path

import pytest

from flowchart_explorer.graph.drawio import Drawio


@pytest.fixture()
def drawio():
    drawio = Drawio(Path("./charts/testchart.drawio"))
    return drawio


class TestDrawio:
    def test_init(self, drawio):
        assert isinstance(drawio.root, Et.Element)
        # TODO: FileNotFoundErrorを出力

        with pytest.raises(FileNotFoundError) as e:
            _ = Drawio(Path("./charts/err.drawio"))
        assert str(e.value) == "File not exits."

    def test_get_nodes_and_edges(self, drawio):
        nodes, edges, sources, targets = drawio._get_nodes_and_edges()
        assert isinstance(nodes, dict)
        assert isinstance(edges, dict)

    def test_get_start_node(self, drawio):
        nodes, edges, sources, targets = drawio._get_nodes_and_edges()
        start_node = drawio._get_start_node(nodes, sources, targets)
        assert isinstance(start_node, dict)
        assert start_node["id"] == "10"

        # error pattern
        err_drawio = Drawio(Path("./charts/testerrchart.drawio"))
        nodes, edges, sources, targets = err_drawio._get_nodes_and_edges()
        with pytest.raises(AttributeError) as e:
            err_drawio._get_start_node(nodes, sources, targets)
        assert str(e.value) == "Start Node is not only one."

    def test_get_graph(self, drawio):
        graph = drawio.get_graph()
        keys = set(graph.keys())
        assert keys == {"start_node", "edges", "nodes", "loops"}

    def test_assert_error_check_loops(self):
        err_drawio = Drawio(Path("./charts/test-drawio/error-loop-pair.drawio"))
        with pytest.raises(AssertionError) as e:
            err_drawio.get_graph()
        assert str(e.value) == "There are places where in-loop and out-loop do not form a pair."

    def test_check_same_source_target_edges(self):
        err_drawio = Drawio(Path("./charts/test-drawio/error-double-edge.drawio"))
        with pytest.raises(AssertionError) as e:
            err_drawio.get_graph()
        assert str(e.value) == "There exists one or more edges where the source node and target node are the same."
