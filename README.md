# VTK - Visualization Toolkit Python Examples

VTK examples in Python.
 
![Screenshot from 2024-02-10 21-38-23](https://github.com/djeada/VTK-Examples/assets/37275728/d843d55f-ab7a-4830-a762-34cc71041fdc)

## Overview

- The Visualization Toolkit (VTK) is an advanced 3D graphics and visualization software library.
- It is widely utilized in scientific and data visualization, 3D graphics, and image processing.
- VTK offers a comprehensive suite of tools, including hundreds of algorithms.
- Since its inception in 1993, it has been actively developed and maintained by Kitware Inc.
- The toolkit is open-source, primarily written in C++, and offers bindings for Python, Java, and Tcl.

## Getting Started with VTK

### Installation Guide

- For installation instructions on various platforms such as Windows, Linux, and macOS, please refer to the [official VTK download page](https://vtk.org/download/). Here, you will find platform-specific installation guides and resources.

### Basic Workflow in VTK

1. **Data Input and Representation:** 
   - Begin by selecting the right data structure for your dataset.
2. **Data Manipulation and Processing:** 
   - Apply various filters and algorithms to manipulate and process your data.
3. **Visualization and Rendering:** 
   - Utilize mappers, actors, and renderers for effective data display.
4. **Interaction and Exporting:** 
   - Enhance the visualization with interactive elements and export functionalities as required.

## Repository Structure

- This repository is an extensive collection of Python examples and tutorials for VTK users. 
- It is organized into subdirectories, each focusing on a different topic, complete with relevant code examples.

## Running the Examples

### Setting Up Your Environment

1. **Creating a Virtual Environment:**
   - Use tools like `virtualenv` or `conda` to create a virtual environment for your project.
2. **Activating and Installing Dependencies:**
   - Activate your environment and install required packages:

    ```bash
    pip install -r requirements.txt
    ```

### Executing Scripts

- To run an example script, navigate to the corresponding folder in the `src/` directory and use the command line to execute the script. For example:

    ```bash
    cd src/01_basic_shapes
    python circle.py
    ```

  - This command runs the `circle.py` script, demonstrating a simple circle visualization with VTK.

### Using an Integrated Development Environment (IDE)

- For users preferring IDEs like Visual Studio Code or PyCharm:
  
  1. **Project Setup:**
     - Open your IDE and load the project folder.
  2. **Interpreter Configuration:**
     - Configure the Python interpreter to use the virtual environment you created.
  3. **Running Scripts:**
     - Open and run the desired script using the IDE's tools, such as the "Run" button.
  4. **Debugging:**
     - Use IDE features like breakpoints and step-through debugging for in-depth analysis of the example scripts.

## Basic Shapes

| Number | Description | Link |
| --- | --- | --- |
| 1 | Demonstrates the steps to create a perfectly round circle | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/01_basic_shapes/circle.py) |
| 2 | Describes the process of generating a 3D cone | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/01_basic_shapes/cone.py) |
| 3 | Explore how to make a simple cube in 3D space | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/01_basic_shapes/cube.py) |
| 4 | Learn to draw a cylinder using vtk | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/01_basic_shapes/cylinder.py) |
| 5 | Get started with glyph production in vtk | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/01_basic_shapes/glyph.py) |
| 6 | Tutorial on creating a 2D square | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/01_basic_shapes/square.py) |
| 7 | Guides you through the creation of a simple triangle | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/01_basic_shapes/triangle.py) |

## Advanced Shapes

| Number | Description | Link |
| --- | --- | --- |
| 1 | A detailed example of creating a 3D box that encloses other objects | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/02_advanced_shapes/enclosing_box.py) |
| 2 | Shows how to construct an isosurface in vtk | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/02_advanced_shapes/isosurface.py) |
| 3 | Delves into creating scenes with multiple dependent objects | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/02_advanced_shapes/multiple_dependent_objects.py) |
| 4 | Explores creating complex scenes with multiple independent objects | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/02_advanced_shapes/multiple_independent_objects.py) |
| 5 | Introduction to the creation of streamlines in vtk | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/02_advanced_shapes/streamlines.py) |
| 6 | Teaches you how to use triangulation techniques in vtk | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/02_advanced_shapes/triangulation.py) |
| 7 | Explores the world of volume rendering in vtk | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/02_advanced_shapes/volume_rendering.py) |
| 8 | A comparison of different visualization techniques in vtk | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/02_advanced_shapes/visualization_techniques_comparison.py) |
| 9 | Demonstrates how to visualize flow simulation data | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/02_advanced_shapes/flow_simulation_visualization.py) |

## Structures and Datasets

| Number | Description | Link |
| --- | --- | --- |
| 1 | Shows you how to manipulate points in vtk | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/03_structures_and_datasets/points.py) |
| 2 | Dives into the workings of cells within vtk | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/03_structures_and_datasets/cells.py) |
| 3 | An overview of handling fields in vtk | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/03_structures_and_datasets/fields.py) |
| 4 | Detailed example of working with multiblock datasets | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/03_structures_and_datasets/multiblock_dataset.py) |
| 5 | Covers the basics of poly data structures in vtk | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/03_structures_and_datasets/poly_data.py) |
| 6 | Teaches you how to work with structured grids | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/03_structures_and_datasets/structured_grid.py) |
| 7 | Guides you through the intricacies of unstructured grids | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/03_structures_and_datasets/unstructured_grid.py) |
| 8 | Introduction to structured mesh concepts in vtk | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/03_structures_and_datasets/structured_mesh.py) |
| 9 | Explores the creation and manipulation of unstructured meshes | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/03_structures_and_datasets/unstructured_mesh.py) |

## Input and Output

| Number | Description | Link |
| --- | --- | --- |
| 1 | Introduction to working with OBJ files in vtk | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/04_input_output/io_obj.py) |
| 2 | Learn to read and write STL files with vtk | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/04_input_output/io_stl.py) |
| 3 | Overview of handling VTK file format | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/04_input_output/io_vtk.py) |
| 4 | Guides you through the usage of VTM file format | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/04_input_output/io_vtm.py) |
| 5 | Explores handling VTU file formats with vtk | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/04_input_output/io_vtu.py) |
| 6 | Walkthrough of handling Exodus II files | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/04_input_output/io_exodus_ii.py) |
| 7 | Tutorial on interacting with OpenFOAM files | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/04_input_output/io_openfoam.py) |

## Data Conversion

| Number | Description | Link |
| --- | --- | --- |
| 1 | Interface for data conversion utilities | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/05_data_conversion/converter_interface.py) |
| 2 | Learn to convert between STL and VTK formats | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/05_data_conversion/stl_vtk.py) |
| 3 | Demonstrates conversion between VTK and OBJ formats | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/05_data_conversion/vtk_obj.py) |
| 4 | Teaches conversion between STL and OBJ formats | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/05_data_conversion/stl_obj.py) |
| 5 | Shows you how to convert between VTK and VTM formats | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/05_data_conversion/vtk_vtm.py) |
| 6 | Guides you through the conversion between VTK and VTU formats | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/05_data_conversion/vtk_vtu.py) |
## Visualization Pipeline

| Number | Description | Link |
| --- | --- | --- |
| 1 | Shows handling multiple objects in the actor-mapper setup | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/06_visualization_pipeline/actor_mapper_multiple_objects.py) |
| 2 | Teaches you how to add text labels in your visualization | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/06_visualization_pipeline/adding_text_labels.py) |
| 3 | Demonstrates scalar color mapping in vtk | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/06_visualization_pipeline/scalar_color_mapping.py) |
| 4 | Walks you through creating camera movements | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/06_visualization_pipeline/camera_movement.py) |
| 5 | Shows various filters in action in vtk | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/06_visualization_pipeline/filters_in_action.py) |
| 6 | Guides you through creating lighting and shadows in your visualization | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/06_visualization_pipeline/lighting_and_shadows.py) |
| 7 | Shows you how to animate your visualization pipeline | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/06_visualization_pipeline/pipeline_animation.py) |

## Interactive Widgets

| Number | Description | Link |
| --- | --- | --- |
| 1 | Guides you to use the orientation marker widget | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/07_interactive_widgets/orientation_marker.py) |
| 2 | Tutorial on creating and using sliders in your visualization | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/07_interactive_widgets/slider.py) |
| 3 | Learn how to interact with simple buttons in your visualization | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/07_interactive_widgets/simple_button.py) |
| 4 | Demonstrates creating interactive planes intersection | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/07_interactive_widgets/planes_intersection.py) |

## Integrations with External Tools

| Number | Description | Link |
| --- | --- | --- |
| 1 | Learn to integrate VTK with Qt to create a 3D sphere visualization | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/08_integration_with_ui/qt_sphere.py) |
| 2 | Demonstrates the use of Matplotlib for creating a 3D sphere using VTK | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/08_integration_with_ui/matplotlib_sphere.py) |
| 3 | Shows how to create surface plots using VTK and Matplotlib | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/08_integration_with_ui/matplotlib_surface_plot.py) |

## Computational Fluid Dynamics (CFD)

| Number | Description | Link |
| --- | --- | --- |
| 1 | 1D heat convection problems | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/09_cfd/heat_convection_solver_1d.py) |
| 2 | 1D fixed end heat transfer | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/09_cfd/fixed_end_heat_transfer_1d.py) |
| 3 | 1D convective end heat transfer | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/09_cfd/convective_end_heat_transfer_1d.py) |
| 4 | 1D enhanced heat transfer | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/09_cfd/enhanced_heat_transfer_solver_1d.py) |
| 5 | 2D heat conduction problems | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/09_cfd/heat_conduction_solver_2d.py) |
| 6 | 2D enhanced heat transfer | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/09_cfd/enhanced_heat_transfer_solver_2d.py) |
| 7 | Simple fluid flow | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/09_cfd/fluid_flow_simulator.py) |
| 8 | Fluid flow around an obstacle | [Python](https://github.com/djeada/VTK-Examples/blob/main/src/09_cfd/obstacle_flow_simulation.py) |

## References

* [PyScience: VTK](https://pyscience.wordpress.com/tag/vtk/)
* [Program Creek: VTK](https://www.programcreek.com/python/index/480/vtk)
* [Visualization Course 2014](https://www.cb.uu.se/~aht/Vis2014/)
* [Data Visualization Course, SJTU](https://www.cs.sjtu.edu.cn/~shengbin/course/datavis/)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
