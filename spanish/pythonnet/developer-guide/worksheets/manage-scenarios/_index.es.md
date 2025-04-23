---
title: Crear, manipular o eliminar escenarios de hojas con Python via .NET
linktitle: Gestionar Escenarios
type: docs
weight: 190
url: /es/python-net/create-manipulate-or-remove-scenarios-from-worksheets/
description: Aprende cómo crear, modificar y eliminar escenarios en hojas de Excel programáticamente usando la API de Aspose.Cells para Python via .NET.
keywords: Escenarios de Excel en Python, gestionar escenarios de hojas de trabajo en Python, agregar escenario en Python, eliminar escenario en Excel Python, modificar escenarios en Python
---

{{% alert color="primary" %}}

A veces necesitas crear, manipular o eliminar escenarios en hojas de cálculo. Un escenario es un modelo '¿qué pasaría si?' nombrado que incluye celdas de entrada variables vinculadas por una o más fórmulas. Antes de crear un escenario, diseña la hoja de cálculo para que contenga al menos una fórmula que dependa de celdas que puedan aceptar diferentes valores. Este ejemplo demuestra cómo gestionar escenarios en hojas usando Aspose.Cells para Python via .NET.

{{% /alert %}}

Aspose.Cells proporciona varias clases para trabajar con escenarios:
- [**ScenarioCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/scenariocollection/)
- [**Scenario**](https://reference.aspose.com/cells/python-net/aspose.cells/scenario/)
- [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/scenarioinputcellcollection/)
- [**ScenarioInputCell**](https://reference.aspose.com/cells/python-net/aspose.cells/scenarioinputcell/)

Usa la propiedad [**Worksheet.scenarios**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/scenarios/) para acceder a los escenarios. El siguiente código demuestra cómo:
1. Abrir un archivo de Excel que contenga escenarios
2. Eliminar un escenario existente
3. Agregar un nuevo escenario

4. Guardar el libro modificado

```python
import os
from aspose.cells import Workbook

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
# The path to the documents directory.
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Instantiate the Workbook and load an Excel file
workbook = Workbook(os.path.join(data_dir, "aspose-sample.xlsx"))
# Access first worksheet
worksheet = workbook.worksheets[0]

if len(worksheet.scenarios) > 0:
    # Remove the existing first scenario from the sheet
    worksheet.scenarios.remove_at(0)

    # Create a scenario
    i = worksheet.scenarios.add("MyScenario")
    # Get the scenario
    scenario = worksheet.scenarios[i]
    # Add comment to it
    scenario.comment = "Test sceanrio is created."
    # Get the input cells for the scenario
    sic = scenario.input_cells
    # Add the scenario on B4 (as changing cell) with default value
    sic.add(3, 1, "1100000")

    output_path = os.path.join(data_dir, "outBk_scenarios1.out.xlsx")

    # Save the Excel file
    workbook.save(output_path)
    print(f"\nProcess completed successfully.\nFile saved at {output_path}")
```

