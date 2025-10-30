---
title: Trabajando con formatos de visualización de datos en DataField en tablas dinámicas con C++
linktitle: Trabajando con formatos de visualización de datos en DataField en tablas dinámicas
type: docs
weight: 140
url: /es/cpp/working-with-data-display-formats-of-datafield-in-pivot-table/
description: Aprende cómo trabajar con los formatos de visualización de datos en DataField en tablas dinámicas usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells admite todos los formatos de visualización de datos de DataField.

{{% /alert %}}

## **Opción de formato de visualización "Clasificación de menor a mayor" y "Clasificación de mayor a menor"**

Aspose.Cells proporciona la capacidad de configurar la opción de formato de visualización para campos pivote. Para esto, la API ofrece la propiedad [**PivotField.GetCalculationType()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotshowvaluessetting/getcalculationtype/). Para clasificar de mayor a menor, puedes establecer la propiedad [**PivotField.GetCalculationType()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotshowvaluessetting/getcalculationtype/) a [**PivotFieldDataDisplayFormat.RankLargestToSmallest**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfielddatadisplayformat/). El siguiente fragmento de código muestra cómo establecer las opciones de formato de visualización.

Los archivos de origen y salida de muestra se pueden descargar desde aquí para probar el código de muestra:

[Archivo Excel de origen](101089332.xlsx)

[Archivo Excel de salida](101089333.xlsx)

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load a template file
    Workbook workbook(srcDir + u"PivotTableSample.xlsx");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    int pivotIndex = 0;

    // Accessing the PivotTable
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    // Accessing the data fields
    PivotFieldCollection pivotFields = pivotTable.GetDataFields();

    // Accessing the first data field in the data fields
    PivotField pivotField = pivotFields.Get(0);

    // Setting data display format
    pivotField.GetShowValuesSetting().SetCalculationType(PivotFieldDataDisplayFormat::RankLargestToSmallest);

    // Calculate data
    pivotTable.CalculateData();

    // Saving the Excel file
    workbook.Save(outDir + u"PivotTableDataDisplayFormatRanking_out.xlsx");

    std::cout << "PivotTable data display format ranking applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
