---
title: Ocultar y mostrar filas y columnas con C++
linktitle: Ocultar y Mostrar Filas y Columnas
type: docs
weight: 60
url: /es/cpp/hiding-and-showing-rows-and-columns/
description: Aprenda cómo ocultar y mostrar filas y columnas en archivos de Excel mediante programación usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

A veces, tiene sentido ocultar ciertas filas o columnas en una hoja de cálculo y mostrarlas más tarde. Microsoft Excel ofrece esta función, y también Aspose.Cells.

{{% /alert %}}

## **Controlar la Visibilidad de Filas y Columnas**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene un [**WorksheetCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) que permite a los desarrolladores acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) proporciona una colección [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) que representa todas las celdas de la hoja de cálculo. La colección [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) proporciona varios métodos para gestionar filas o columnas en una hoja de cálculo. Algunos de ellos se discuten a continuación.

### **Ocultar Filas y Columnas**

Los desarrolladores pueden ocultar una fila o columna llamando a los métodos [**HideRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hiderow/) y [**HideColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hidecolumn/) de la colección [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) respectivamente. Ambos métodos toman el índice de fila y columna como parámetro para ocultar la fila o columna específica.

```c++
#include <iostream>
#include <memory>
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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the 3rd row of the worksheet
    worksheet.GetCells().HideRow(2);

    // Hide the 2nd column of the worksheet
    worksheet.GetCells().HideColumn(1);

    // Save the modified Excel file
    U16String outputFilePath = outDir + u"output.out.xls";
    workbook.Save(outputFilePath);

    std::cout << "Rows and columns hidden successfully. File saved to: " << outputFilePath.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

También es posible ocultar una fila o columna estableciendo la altura de la fila o el ancho de la columna en 0, respectivamente.

{{% /alert %}}

### **Mostrar Filas y Columnas**

Los desarrolladores pueden mostrar cualquier fila o columna oculta llamando a los métodos [**UnhideRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhiderow/) y [**UnhideColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhidecolumn/) de la colección [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) respectivamente. Ambos métodos toman dos parámetros:

- **Índice de fila o columna** - el índice de una fila o columna que se utiliza para mostrar la fila o columna específica.
- **Altura de fila o ancho de columna** - la altura de fila o el ancho de columna asignados a la fila o columna después de desocultar.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Unhide the 3rd row and set its height to 13.5
    worksheet.GetCells().UnhideRow(2, 13.5);

    // Unhide the 2nd column and set its width to 8.5
    worksheet.GetCells().UnhideColumn(1, 8.5);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    workbook.Save(outputFilePath);

    Aspose::Cells::Cleanup();

    std::cout << "File modified and saved successfully!" << std::endl;

    return 0;
}
```

{{% alert color="primary" %}}

Al hacer visible una columna oculta, si necesita restaurarla a su ancho asignado previamente o a su ancho original, por favor desoculte la columna con un ancho negativo. Por ejemplo: `worksheet.Cells.UnhideColumn(5, -1)`

{{% /alert %}}

### **Ocultar Múltiples Filas y Columnas**

Los desarrolladores pueden ocultar múltiples filas o columnas a la vez llamando a los métodos [**HideRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hiderows/) y [**HideColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hidecolumns/) de la colección [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) respectivamente. Ambos métodos toman el índice de la fila o columna inicial y el número de filas o columnas que se deben ocultar como parámetros.

```cpp
#include <iostream>
#include <memory>
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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide 3, 4, and 5 rows in the worksheet (zero-based index)
    worksheet.GetCells().HideRows(2, 3);

    // Hide 2 and 3 columns in the worksheet (zero-based index)
    worksheet.GetCells().HideColumns(1, 2);

    // Save the modified Excel file
    workbook.Save(outDir + u"outputxls");

    std::cout << "Rows and columns hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

También es posible usar los métodos [**UnhideRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhiderows/) y [**UnhideColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhidecolumns/) de la clase [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) para hacer varias filas y columnas visibles.

{{% /alert %}}
