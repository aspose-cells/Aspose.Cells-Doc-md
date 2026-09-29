---
title: Formato de tabla dinámica con C++
linktitle: Dar formato a la tabla dinámica
type: docs
weight: 10
url: /es/cpp/formatting-pivot-table/
description: Aprende cómo personalizar la apariencia de las tablas dinámicas usando Aspose.Cells for C++.
---

## **Apariencia de la tabla dinámica**

Cómo crear una tabla dinámica explica cómo crear una tabla dinámica simple. Este artículo describe cómo personalizar la apariencia de una tabla dinámica estableciendo diversas propiedades:

- Opciones de formato de tabla dinámica
- Opciones de formato de campos de tabla dinámica
- Opciones de formato de campos de datos

### **Configuración de opciones de formato de tabla dinámica**

La clase [**PivotTable**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/) controla la tabla dinámica general y se puede formatear de varias maneras.

#### **Establecer el tipo de autoformato**

Microsoft Excel ofrece varias configuraciones de formato preestablecidas para informes. Aspose.Cells también soporta estas opciones de formato. Para acceder a ellas:

1. Establezca [**PivotTable.IsAutoFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/isautoformat/) en **verdadero**.
1. Asignar una opción de formato de la enumeración [**PivotTableAutoFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottableautoformattype/).

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Load a template file
    Workbook workbook(inputFilePath);

    int pivotindex = 0;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Accessing the PivotTable
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotindex);

    // Setting the PivotTable report is automatically formatted
    pivotTable.SetIsAutoFormat(true);

    // Setting the PivotTable autoformat type
    pivotTable.SetAutoFormatType(PivotTableAutoFormatType::Report5);

    // Saving the Excel file
    workbook.Save(outputFilePath);

    std::cout << "PivotTable formatted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Configuración de opciones de formato**

El siguiente ejemplo de código muestra cómo formatear la tabla dinámica para mostrar totales generales para filas y columnas, y cómo establecer el orden de los campos del informe. También muestra cómo establecer una cadena personalizada para valores nulos.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Load a template file
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    int pivotindex = 0;

    // Accessing the PivotTable
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotindex);

    // Setting the PivotTable report shows grand totals for rows.
    pivotTable.SetShowRowGrandTotals(true);

    // Setting the PivotTable report shows grand totals for columns.
    pivotTable.SetShowColumnGrandTotals(true);

    // Setting the PivotTable report displays a custom string in cells that contain null values.
    pivotTable.SetDisplayNullString(true);
    pivotTable.SetNullString(u"null");

    // Setting the PivotTable report's layout
    pivotTable.SetPageFieldOrder(PrintOrderType::DownThenOver);

    // Saving the Excel file
    workbook.Save(outputFilePath);

    std::cout << "PivotTable settings applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Dar formato manualmente al aspecto visual**

Para formatear manualmente la apariencia del informe de tabla dinámica, en lugar de usar formatos predefinidos, utiliza los métodos [**PivotTable.Format()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/format/) y [**PivotTable.FormatAll()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/formatall/). Crea un objeto de estilo para tu formato deseado, por ejemplo:

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
    U16String inputFilePath = srcDir + u"Book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Load a template file
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    auto pivot = worksheet.GetPivotTables().Get(0);

    // Set pivot table style
    pivot.SetPivotTableStyleType(PivotTableStyleType::PivotTableStyleDark1);

    // Create a new style
    Style style = workbook.CreateStyle();
    style.GetFont().SetName(u"Arial Black");
    style.SetForegroundColor(Color::Yellow());
    style.SetPattern(BackgroundType::Solid);

    // Apply style to pivot table
    pivot.FormatAll(style);

    // Save the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Pivot table style applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Configuración de opciones de formato de campo de tabla dinámica**

La clase [**PivotField**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfield/) representa un campo en una tabla dinámica y se puede formatear de varias formas. El ejemplo de código a continuación muestra cómo:

- Acceder a los campos de fila.
- Establecer subtotales.
- Establecer orden automático.
- Establecer autover.

#### **Configuración de formato de campos de fila/columna/página**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load a template file
    Workbook workbook(srcDir + u"Book1.xls");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    int pivotindex = 0;

    // Accessing the PivotTable
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotindex);

    // Setting the PivotTable report shows grand totals for rows.
    pivotTable.SetShowRowGrandTotals(true);

    // Accessing the row fields.
    PivotFieldCollection pivotFields = pivotTable.GetRowFields();

    // Accessing the first row field in the row fields.
    PivotField pivotField = pivotFields.Get(0);

    // Setting Subtotals.
    pivotField.SetSubtotals(PivotFieldSubtotalType::Sum, true);
    pivotField.SetSubtotals(PivotFieldSubtotalType::Count, true);

    // Setting autosort options.
    // Setting the field auto sort.
    pivotField.SetIsAutoSort(true);

    // Setting the field auto sort ascend.
    pivotField.SetIsAscendSort(true);

    // Setting the field auto sort using the field itself.
    pivotField.SetAutoSortField(-5);

    // Setting autoShow options.
    // Setting the field auto show.
    pivotField.SetIsAutoShow(true);

    // Setting the field auto show ascend.
    pivotField.SetIsAscendShow(false);

    // Setting the auto show using field(data field).
    pivotField.SetAutoShowField(0);

    // Saving the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "PivotTable settings applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Configuración de formato de campos de datos**

El ejemplo de código a continuación muestra cómo establecer formatos de visualización y formato numérico para los campos de datos.

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

    // Load a template file
    U16String inputFilePath = srcDir + u"Book1.xls";
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    int pivotindex = 0;

    // Accessing the PivotTable
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotindex);

    // Accessing the data fields
    PivotFieldCollection pivotFields = pivotTable.GetDataFields();

    // Accessing the first data field in the data fields
    PivotField pivotField = pivotFields.Get(0);

    // Setting data display format
    pivotField.GetShowValuesSetting().SetCalculationType(PivotFieldDataDisplayFormat::PercentageOf);

    // Setting the base field
    pivotField.GetShowValuesSetting().SetBaseFieldIndex(1);

    // Setting the base item
    pivotField.GetShowValuesSetting().SetBaseItemPositionType(PivotItemPositionType::Next);

    // Setting number format
    pivotField.SetNumber(10);

    // Saving the Excel file
    U16String outputFilePath = outDir + u"output.xls";
    workbook.Save(outputFilePath);

    std::cout << "Pivot table settings applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Borrado de campos de tabla dinámica**

La clase [**PivotFieldCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfieldcollection/) tiene un método llamado [**Clear()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfieldcollection/clear/) que te permite borrar campos de tabla dinámica. Úsalo cuando quieras borrar todos los campos de tabla dinámica en las áreas, por ejemplo, página, columna, fila o datos.
El ejemplo de código a continuación muestra cómo borrar todos los campos de tabla dinámica en un área de datos.

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
    U16String inputFilePath = srcDir + u"Book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Load a template file
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get the pivot tables in the sheet
    PivotTableCollection pivotTables = sheet.GetPivotTables();

    // Get the first PivotTable
    PivotTable pivotTable = pivotTables.Get(0);

    // Clear all the data fields
    pivotTable.GetDataFields().Clear();

    // Add new data field
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Betrag Netto FW");

    // Set the refresh data flag off
    pivotTable.SetRefreshDataFlag(false);

    // Refresh and calculate the pivot table data
    pivotTable.RefreshData();
    pivotTable.CalculateData();

    // Saving the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Pivot table updated and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
