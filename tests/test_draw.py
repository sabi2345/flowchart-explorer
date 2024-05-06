from pathlib import Path

from flowchart_explorer.chartpath import FlowChartPath
from flowchart_explorer.explorer import Explorer
from flowchart_explorer.graph.drawio import Drawio


class TestDrawFlowPath:

    def test_draw(self, tmp_path):
        drawio = Drawio(Path("./charts/test-explorer/simple_double_loop_chart.drawio"))
        graph = drawio.get_graph()
        explorer = Explorer()
        key, flow_path = explorer.run(graph)
        for key in graph["nodes"].keys():
            print(graph["nodes"][key]["label"])
        dir_path = Path(tmp_path)
        dir_path = Path("tests/chart_path/simple_double_loop_chart")
        drawpath = FlowChartPath(dir_path=dir_path)
        drawpath.draw(flow_path=flow_path, graph=graph)
        # Check if the files are created
        for i in range(1, 20):
            assert (dir_path / f"FlowChart-{i}.png").exists(), f"FlowChart-{i}.png does not exist"
