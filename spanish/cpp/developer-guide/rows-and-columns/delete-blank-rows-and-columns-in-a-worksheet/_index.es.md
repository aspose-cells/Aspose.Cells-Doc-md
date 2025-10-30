---
title: Eliminar filas y columnas en blanco en una hoja de cálculo con C++
linktitle: Eliminar Filas y Columnas en Blanco en una Hoja de Cálculo
type: docs
weight: 300
url: /es/cpp/delete-blank-rows-and-columns-in-a-worksheet/
description: Eliminar filas y columnas vacías en una hoja de cálculo usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Es posible eliminar todas las filas y columnas en blanco de una hoja de cálculo. Esto es útil cuando, por ejemplo, se genera un archivo PDF a partir de un archivo de Microsoft Excel y se desea convertir solo filas y columnas que contienen datos u objetos relacionados.

Use los siguientes métodos de Aspose.Cells para eliminar filas y columnas vacías:

1. Para eliminar filas en blanco, utilice el método [**Cells.DeleteBlankRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleteblankrows/). Tenga en cuenta que, para las filas en blanco que se eliminarán, no solo es necesario que [**Row.IsBlank**](https://reference.aspose.com/cells/cpp/aspose.cells/row/isblank/) sea verdadero, sino que también no debe haber comentarios visibles definidos para ninguna celda en esas filas, y no debe haber una tabla dinámica cuyo rango se interseque con ellas.
2. Para eliminar columnas en blanco, use el método [**Cells.DeleteBlankColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleteblankcolumns/).

{{% /alert %}}

## Código C++ para eliminar filas en blanco

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Open an existing Excel file
    U16String inputFilePath = srcDir + u"SampleInput.xlsx";
    Workbook workbook(inputFilePath);

    // Create a Worksheets object with reference to the sheets of the Workbook
    WorksheetCollection sheets = workbook.GetWorksheets();

    // Get the first Worksheet from WorksheetCollection
    Worksheet sheet = sheets.Get(0);

    // Delete the Blank Rows from the worksheet
    sheet.GetCells().DeleteBlankRows();

    // Save the Excel file
    U16String outputFilePath = outDir + u"mybook.out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Blank rows deleted and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## Código C++ para eliminar columnas en blanco

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"SampleInput.xlsx";

    // Create a smart pointer to a new Workbook instance
    std::unique_ptr<Workbook> wb = std::make_unique<Workbook>(inputFilePath);

    // Create a Worksheets object with reference to the sheets of the Workbook
    WorksheetCollection sheets = wb->GetWorksheets();

    // Get the first Worksheet from WorksheetCollection
    Worksheet sheet = sheets.Get(0);

    // Delete the blank columns from the worksheet
    sheet.GetCells().DeleteBlankColumns();

    // Save the excel file
    U16String outputFilePath = srcDir + u"mybook.out.xlsx";
    wb->Save(outputFilePath);

    std::cout << "Blank columns deleted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
