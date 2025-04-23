---
title: Autoajustar filas y columnas con C++
linktitle: Ajustar automáticamente filas y columnas
type: docs
weight: 20
url: /es/cpp/autofit-rows-and-columns/
description: Este artículo muestra cómo autoajustar filas, columnas, filas de celdas combinadas y filas en un rango de celdas usando la API Aspose.Cells for C++.
keywords: Ajustar automáticamente filas, ajustar automáticamente columnas, ajustar automáticamente fila en un rango de celdas, ajustar automáticamente filas de celdas fusionadas
---

{{% alert color="primary" %}}

Microsoft Excel permite a los usuarios ajustar automáticamente el ancho y la altura de las celdas según su contenido. Esta función también está disponible a través de Aspose.Cells, por lo que los desarrolladores pueden ajustar automáticamente las dimensiones de una celda en tiempo de ejecución.

{{% /alert %}}

## **Ajuste automático**

Aspose.Cells proporciona una clase [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) que permite acceder a cada hoja de cálculo en un archivo Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) ofrece una amplia gama de métodos para gestionar una hoja de cálculo. Este artículo analiza cómo usar la clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) para autoajustar filas o columnas.

### **Ajuste automático de fila - Simple**

El enfoque más sencillo para ajustar automáticamente el ancho y la altura de una fila es llamar al método [**AutoFitRow**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrow/) de la clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). El método [**AutoFitRow**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrow/) toma un índice de fila (de la fila a redimensionar) como parámetro.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Auto-fit the 2nd row (index 1) of the worksheet
    worksheet.AutoFitRow(1);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Row auto-fitted and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Cómo AutoAjustar una Fila en un Rango de Celdas**

Una fila está compuesta por muchas columnas. Aspose.Cells permite a los desarrolladores ajustar automáticamente una fila basada en el contenido en un rango de celdas dentro de la fila llamando a una versión sobrecargada del método [**AutoFitRow**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrow/). Toma los siguientes parámetros:

- **Índice de la fila**, el índice de la fila a ajustar automáticamente.
- **Índice de la primera columna**, el índice de la primera columna de la fila.
- **Índice de la última columna**, el índice de la última columna de la fila.

El método [**AutoFitRow**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrow/) verifica el contenido de todas las columnas en la fila y luego ajusta automáticamente la fila.

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

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xlsx";

    // Open the Excel file
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Auto-fitting the 3rd row of the worksheet
    worksheet.AutoFitRow(1, 0, 5);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Row auto-fitted and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Cómo AutoAjustar una Columna en un Rango de Celdas**

Una columna está compuesta por muchas filas. Es posible ajustar automáticamente una columna según el contenido en un rango de celdas en la columna llamando a una versión sobrecargada del método [**AutoFitColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitcolumn/) que acepta los siguientes parámetros:

- **Índice de columna**, el índice de la columna que se va a ajustar automáticamente.
- **Índice de la primera fila**, el índice de la primera fila de la columna.
- **Índice de la última fila**, el índice de la última fila de la columna.

El método [**AutoFitColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitcolumn/) verifica el contenido de todas las filas en la columna y luego ajusta automáticamente la columna.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Auto-fit the 5th column (index 4) from row 4 to 6
    worksheet.AutoFitColumn(4, 4, 6);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Column auto-fitted and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Cómo AutoAjustar Filas para Celdas Fusionadas**

Con Aspose.Cells, es posible ajustar automáticamente filas incluso para celdas que han sido combinadas usando la API [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/). La clase [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) proporciona la propiedad [**GetAutoFitMergedCellsType()**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getautofitmergedcellstype/) que puede usarse para ajustar filas de celdas combinadas. [**GetAutoFitMergedCellsType()**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getautofitmergedcellstype/) acepta la enumeración [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitmergedcellstype/), que tiene los siguientes miembros:

- Ninguno: Ignora las celdas combinadas.
- PrimeraLinea: Solo expande la altura de la primera fila.
- ÚltimaLinea: Solo expande la altura de la última fila.
- CadaLinea: Solo expande la altura de cada fila.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook wb;

    // Get the first (default) worksheet
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // Create a range A1:B1
    Range range = worksheet.GetCells().CreateRange(0, 0, 1, 2);

    // Merge the cells
    range.Merge();

    // Insert value to the merged cell A1
    worksheet.GetCells().Get(0, 0).SetValue(u"A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end");

    // Create a style object
    Style style = worksheet.GetCells().Get(0, 0).GetStyle();

    // Set wrapping text on
    style.SetIsTextWrapped(true);

    // Apply the style to the cell
    worksheet.GetCells().Get(0, 0).SetStyle(style);

    // Create an object for AutoFitterOptions
    AutoFitterOptions options;

    // Set auto-fit for merged cells
    options.SetAutoFitMergedCellsType(AutoFitMergedCellsType::EachLine);

    // Autofit rows in the sheet (including the merged cells)
    worksheet.AutoFitRows(options);

    // Save the Excel file
    wb.Save(outDir + u"AutofitRowsforMergedCells.xlsx");

    std::cout << "Autofit rows for merged cells completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

También puede intentar usar las versiones sobrecargadas de los métodos [**AutoFitRows**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrows/) y [**AutoFitColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitcolumns/) que aceptan un rango de filas/columnas y una instancia de [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) para ajustar automáticamente las filas/columnas seleccionadas con el [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) deseado.

Las firmas de los métodos mencionados anteriormente son las siguientes:

1. AutoFitRows(int startRow, int endRow, [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) options)
1. AutoFitColumns(int firstColumn, int lastColumn, [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) options)

{{% /alert %}}

## **Importante saber**

{{% alert color="primary" %}}

Si una celda está combinada, entonces los métodos AutoFit no se aplicarán, lo cual es el mismo comportamiento que en Microsoft Excel. Puede solucionar esto usando la API de filtro automático. Además, si el texto en una celda está ajustado, el método [**AutoFitColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitcolumn/) tampoco se aplicará. Otra cosa que debe saber es que los métodos *AutoFit* consumen mucho tiempo. Por lo tanto, debe llamar a estos métodos lo menos posible para garantizar la eficiencia de su aplicación.

{{% /alert %}}

## **Temas Avanzados**
- [Ajustar automáticamente filas para celdas fusionadas](/cells/es/cpp/autofit-rows-for-merged-cells/)
