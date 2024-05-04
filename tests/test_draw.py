from pathlib import Path

from flowchart_explorer.chartpath import FlowChartPath
from flowchart_explorer.explorer import Explorer
from flowchart_explorer.graph.drawio import Drawio


class TestDrawFlowPath:

    def test_draw(self):
        drawio = Drawio(Path("./charts/test-explorer/simple_double_loop_chart.drawio"))
        graph = drawio.get_graph()
        explorer = Explorer()
        key, flow_path = explorer.run(graph)

        drawpath = FlowChartPath()
        drawpath.draw(flow_path=flow_path, graph=graph)
