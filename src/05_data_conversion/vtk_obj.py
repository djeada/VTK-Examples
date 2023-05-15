import vtk

from converter_interface import Converter


class VTKtoOBJConverter(Converter):
    def convert(self, input_filename: str, output_filename: str):
        reader = vtk.vtkGenericDataObjectReader()
        reader.SetFileName(input_filename)
        reader.Update()

        writer = vtk.vtkOBJWriter()
        writer.SetFileName(output_filename)
        writer.SetInputConnection(reader.GetOutputPort())
        writer.Write()


class OBJtoVTKConverter(Converter):
    def convert(self, input_filename: str, output_filename: str):
        reader = vtk.vtkOBJReader()
        reader.SetFileName(input_filename)
        reader.Update()

        writer = vtk.vtkDataSetWriter()
        writer.SetFileName(output_filename)
        writer.SetInputConnection(reader.GetOutputPort())
        writer.Write()