---
title: Crear, manipular o eliminar escenarios en hojas de cálculo con C++
linktitle: Gestionar Escenarios
type: docs
weight: 190
url: /es/cpp/create-manipulate-or-remove-scenarios-from-worksheets/
description: En este artículo, aprenderás cómo crear, manipular o eliminar escenarios de las hojas de Excel programáticamente usando la biblioteca C++ con Aspose.Cells API.
keywords: crear escenario hoja de cálculo c++, eliminar escenario hoja de cálculo c++, manipular escenario hoja de cálculo c++
---

{{% alert color="primary" %}}

A veces, necesitas crear, manipular o eliminar escenarios en hojas de cálculo. Un escenario es un modelo de 'qué pasaría si' que incluye celdas de entrada variables vinculadas por una o más fórmulas. Antes de crear un escenario, diseña la hoja de cálculo para que contenga al menos una fórmula que dependa de celdas en las que se puedan insertar diferentes valores. El siguiente ejemplo muestra cómo crear y eliminar escenarios de una hoja de cálculo en un libro mediante las API de Aspose.Cells.

{{% /alert %}}

Aspose.Cells ofrece algunas clases útiles, por ejemplo, [**ScenarioCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/scenariocollection/), [**Scenario**](https://reference.aspose.com/cells/cpp/aspose.cells/scenario/), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/scenarioinputcellcollection/) y [**ScenarioInputCell**](https://reference.aspose.com/cells/cpp/aspose.cells/scenarioinputcell/). También proporciona la propiedad [**Worksheet.GetScenarios()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getscenarios/). El código de ejemplo a continuación abre un archivo XLSX que contiene algunos escenarios y elimina un escenario existente. También añade un nuevo escenario en la hoja de cálculo antes de guardar el archivo Excel. El ejemplo usa un archivo de plantilla muy simple que contiene un escenario.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load input Excel file
    Workbook workbook(srcDir + u"aspose-sample.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access scenarios collection
    ScenarioCollection scenarios = worksheet.GetScenarios();
    if (scenarios.GetCount() > 0)
    {
        // Create new scenario and configure
        int32_t scenarioIndex = scenarios.Add(u"MyScenario");
        Scenario scenario = scenarios.Get(scenarioIndex);
        scenario.SetComment(u"Test scenario is created.");

        // Add input cell to scenario
        ScenarioInputCellCollection inputCells = scenario.GetInputCells();
        inputCells.Add(3, 1, u"1100000"); // Cell B4 (0-based)

        // Save modified workbook
        U16String outputPath = outDir + u"outBk_scenarios1.out.xlsx";
        workbook.Save(outputPath);

        std::cout << "\nProcess completed successfully.\nFile saved at " << outputPath.ToUtf8() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
