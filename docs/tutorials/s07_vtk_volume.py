import vtk
import os
import dash
import dash_vtk
from dash_vtk.utils import to_volume_state
from dash import html

repo_path = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))
head_vti = os.path.join(repo_path, 'demos', 'data', 'head.vti')

# Load dataset from dist
reader = vtk.vtkXMLImageDataReader()
reader.SetFileName(head_vti)
reader.Update()

# Get mesh to dash_vtk
volume_state = to_volume_state(reader.GetOutput())

content = dash_vtk.View([
    dash_vtk.VolumeRepresentation([
        dash_vtk.VolumeController(),
        dash_vtk.Volume(state=volume_state)
    ]),
])

# Dash setup
app = dash.Dash(__name__)
server = app.server
app.layout = html.Div(
    style={"width": "100%", "height": "calc(100vh - 15px)"},
    children=[content],
)

if __name__ == "__main__":
    app.run_server(debug=True)
