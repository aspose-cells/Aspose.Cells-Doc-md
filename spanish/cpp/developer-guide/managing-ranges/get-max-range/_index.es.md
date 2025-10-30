---
title: Obtener el rango máximo en una hoja de cálculo con C++
linktitle: Obtener el rango máximo en una hoja de cálculo
type: docs
weight: 360
url: /es/cpp/get-max-range-in-a-worksheet/
description: Este artículo describe cómo obtener el rango máximo, rango de datos máximo y rango de visualización máximo de archivos de Excel con la biblioteca Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Al leer datos de la hoja de cálculo, necesitamos conocer el área máxima.

Al copiar todos los datos de una hoja de cálculo, necesitamos conocer el área máxima.

Al exportar un área específica a HTML y PDF, debemos conocer el área máxima.

Aspose.Cells for C++ contiene diferentes formas de encontrar el rango máximo en una hoja de cálculo. 

{{% /alert %}} 

## **Obteniendo el rango máximo**
En Aspose.Cells, si los objetos [**Row**](https://reference.aspose.com/cells/cpp/aspose.cells/row/) y [**Column**](https://reference.aspose.com/cells/cpp/aspose.cells/column/) están inicializados, estas filas y columnas se contarán hasta el área máxima, incluso si no hay datos en filas o columnas vacías.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook object and open the Excel file
    Workbook workbook(u"Book1.xlsx");

    // Get all the worksheets in the workbook
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet sheet = worksheets.Get(0);

    // Get the max data range
    int maxRow = sheet.GetCells().GetMaxRow();
    int maxColumn = sheet.GetCells().GetMaxColumn();

    // Create a range from A1 to the max data range
    Range range = sheet.GetCells().CreateRange(0, 0, maxRow + 1, maxColumn + 1);

    // Set a null value in cell A10
    sheet.GetCells().Get(u"A10").PutValue(nullptr);

    // Update the max data range after modifying the sheet
    maxRow = sheet.GetCells().GetMaxRow();
    maxColumn = sheet.GetCells().GetMaxColumn();

    // Update the range to include the new data
    range = sheet.GetCells().CreateRange(0, 0, maxRow + 1, maxColumn + 1);

    Aspose::Cells::Cleanup();
}
```

## **Obteniendo el rango máximo de datos**
En la mayoría de los casos, solo necesitamos obtener todos los rangos que contienen todos los datos, incluso si las celdas vacías fuera del rango están formateadas.
Y la configuración sobre formas, tablas y tablas dinámicas se ignorará.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    Workbook workbook(u"Book1.xlsx");

    // Get all the worksheets in the book
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet sheet = worksheets.Get(0);

    // Gets the max data range
    int maxRow = sheet.GetCells().GetMaxDataRow();
    int maxColumn = sheet.GetCells().GetMaxDataColumn();

    // The range is A1:B3
    Range range = sheet.GetCells().CreateRange(0, 0, maxRow + 1, maxColumn + 1);

    // Put null value in cell A10
    sheet.GetCells().Get(u"A10").PutValue(nullptr);

    // Update max data range after modification
    maxRow = sheet.GetCells().GetMaxDataRow();
    maxColumn = sheet.GetCells().GetMaxDataColumn();

    // The range is still A1:B3
    range = sheet.GetCells().CreateRange(0, 0, maxRow + 1, maxColumn + 1);

    Aspose::Cells::Cleanup();
}
```

## **Obteniendo el rango máximo de visualización**
Cuando exportamos todos los datos de la hoja de cálculo a HTML, PDF o imágenes, necesitamos obtener un área que contenga todos los objetos visibles, incluidos los datos, estilos, gráficos, tablas y tablas dinámicas.
Los siguientes códigos muestran cómo renderizar el rango de visualización máxima a HTML:

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"html.html";

    // Instantiate a new Workbook
    Workbook workbook(inputFilePath);

    // Get all the worksheets in the book
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the max display range of the first worksheet
    Range range = worksheets.Get(0).GetCells().GetMaxDisplayRange();

    // Create HtmlSaveOptions to configure the export
    HtmlSaveOptions saveOptions;
    saveOptions.SetExportActiveWorksheetOnly(true);

    // Set the export area to the range of the first worksheet
    CellArea exportArea = CellArea::CreateCellArea(range.GetFirstRow(), range.GetFirstColumn(), 
                                                   range.GetFirstRow() + range.GetRowCount() - 1, 
                                                   range.GetFirstColumn() + range.GetColumnCount() - 1);
    saveOptions.SetExportArea(exportArea);

    // Save the range to HTML
    workbook.Save(outputFilePath, saveOptions);

    std::cout << "Range saved to HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Aquí está el [archivo de excel fuente](Book1.xlsx).
{{< app/cells/assistant language="cpp" >}}
