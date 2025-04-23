---
title: Función de Consolidación con C++
linktitle: Función de consolidación
type: docs
weight: 20
url: /es/cpp/consolidation-function/
description: Aprende cómo aplicar la Función de Consolidación a los campos de datos de una tabla dinámica usando Aspose.Cells con C++.
---

## **Función de consolidación**

Aspose.Cells se puede utilizar para aplicar la Función de Consolidación a los campos de datos (o campos de valor) de la tabla dinámica. En Microsoft Excel, puedes hacer clic derecho en el campo de valor y luego seleccionar la opción **Configuración del campo de valor...**, y luego seleccionar la pestaña **Resumir valores mediante**. Desde allí, puedes seleccionar cualquier Función de Consolidación de tu elección, como Suma, Conteo, Promedio, Máx, Mín, Producto, Conteo único, etc.

Aspose.Cells proporciona la enumeración [**ConsolidationFunction**](https://reference.aspose.com/cells/cpp/aspose.cells/consolidationfunction/) para admitir las siguientes funciones de consolidación.

- ConsolidationFunction::Average
- ConsolidationFunction::Count
- ConsolidationFunction::CountNums
- ConsolidationFunction::DistinctCount
- ConsolidationFunction::Max
- ConsolidationFunction::Min
- ConsolidationFunction::Product
- ConsolidationFunction::StdDev
- ConsolidationFunction::StdDevp
- ConsolidationFunction::Sum
- ConsolidationFunction::Var
- ConsolidationFunction::Varp

### **Aplicar la función de consolidación a los campos de datos de la tabla dinámica**

El siguiente código aplica la función de consolidación **Promedio** al primer campo de datos (o campo de valor) y la función de consolidación **Conteo de valores distintos** al segundo campo de datos (o campo de valor).

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xlsx";

    // Create workbook from source excel file
    Workbook workbook(inputFilePath);

    // Access the first worksheet of the workbook
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first pivot table of the worksheet
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    // Apply Average consolidation function to first data field
    pivotTable.GetDataFields().Get(0).SetFunction(ConsolidationFunction::Average);

    // Apply DistinctCount consolidation function to second data field
    pivotTable.GetDataFields().Get(1).SetFunction(ConsolidationFunction::DistinctCount);

    // Calculate the data to make changes affect
    pivotTable.CalculateData();

    // Saving the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Pivot table updated and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

La función de consolidación Recuento único es compatible solo con Microsoft Excel 2013.

{{% /alert %}}
