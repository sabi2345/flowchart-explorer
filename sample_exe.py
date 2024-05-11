from pathlib import Path

from flowchart_explorer.chartpath import FlowChartPath
from flowchart_explorer.explorer import Explorer
from flowchart_explorer.graph.drawio import Drawio


def main():
    drawio = Drawio(Path("./charts/sample_chart.drawio"))
    graph = drawio.get_graph()
    explorer = Explorer()
    key, flow_path = explorer.run(graph)
    dir_path = Path("./")
    # dir_path = Path("tests/chart_path/simple_double_loop_chart")
    flowchart = FlowChartPath(dir_path=dir_path)
    flowchart.draw(flow_path=flow_path, graph=graph)


if __name__ == '__main__':
    main()