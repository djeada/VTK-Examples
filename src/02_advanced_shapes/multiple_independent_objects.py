import random

import vtk
from vtkmodules.util.numpy_support import vtk_to_numpy


def create_cone(height: float, radius: float, resolution: int) -> vtk.vtkConeSource:
    cone = vtk.vtkConeSource()
    cone.SetHeight(height)
    cone.SetRadius(radius)
    cone.SetResolution(resolution)
    return cone


def create_cube(length: float) -> vtk.vtkCubeSource:
    cube = vtk.vtkCubeSource()
    cube.SetXLength(length)
    cube.SetYLength(length)
    cube.SetZLength(length)
    return cube


def create_sphere(
    radius: float, phi_resolution: int, theta_resolution: int
) -> vtk.vtkSphereSource:
    sphere = vtk.vtkSphereSource()
    sphere.SetRadius(radius)
    sphere.SetPhiResolution(phi_resolution)
    sphere.SetThetaResolution(theta_resolution)
    return sphere


if __name__ == "__main__":
    # define sources
    cone = create_cone(height=5.0, radius=2.0, resolution=10)
    cube = create_cube(length=5.0)
    sphere = create_sphere(radius=3.0, phi_resolution=10, theta_resolution=10)

    sources = (cone, cube, sphere)

    mappers = []
    for source in sources:
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(source.GetOutputPort())
        mappers.append(mapper)

    actors = []
    for mapper in mappers:
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        actors.append(actor)

    renderers = []
    for i, actor in enumerate(actors):
        renderer = vtk.vtkRenderer()
        renderer.AddActor(actor)
        renderer.SetBackground(random.random(), random.random(), random.random())
        renderer.SetViewport(
            0 + i * 1 / len(actors), 0.0, (i + 1) * 1 / len(actors), 1.0
        )  # x, y, width, height
        renderers.append(renderer)

    renderWindow = vtk.vtkRenderWindow()
    renderWindow.SetSize(800, 400)

    for renderer in renderers:
        renderWindow.AddRenderer(renderer)

    interactor = vtk.vtkRenderWindowInteractor()
    interactor.SetRenderWindow(renderWindow)
    interactor.Initialize()
    interactor.Start()
