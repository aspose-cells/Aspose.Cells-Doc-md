---
title: Agrupando y desagrupando filas y columnas con C++
linktitle: Agrupando y Desagrupando Filas y Columnas
type: docs
weight: 50
url: /es/cpp/grouping-and-ungrouping-rows-and-columns/
description: Aprenda cómo agrupar y desagrupar filas y columnas en archivos de Excel usando Aspose.Cells con C++.
---

## **Introducción**

En un archivo de Microsoft Excel, puedes crear un esquema para los datos que te permita mostrar y ocultar niveles de detalle con un solo clic de ratón.

Haz clic en los **Símbolos de Esquema**, 1,2,3, + y - para mostrar rápidamente solo las filas o columnas que proporcionen resúmenes o encabezados para secciones en una hoja de cálculo, o puedes usar los símbolos para ver detalles bajo un resumen o encabezado individual como se muestra a continuación en la figura:

|**Agrupar Filas y Columnas.**|
| :- |
|![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)|

## **Gestión de Agrupación de Filas y Columnas**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una [**WorksheetCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) proporciona una colección [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) que representa todas las celdas en la hoja de cálculo.

La colección [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) proporciona varios métodos para gestionar filas o columnas en una hoja de cálculo, algunos de estos se discuten a continuación con más detalle.

### **Agrupar Filas y Columnas**

Es posible agrupar filas o columnas llamando a los métodos [**GroupRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/grouprows/) y [**GroupColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/groupcolumns/) de la colección [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Ambos métodos toman los siguientes parámetros:

- Índice de la primera fila/columna, la primera fila o columna del grupo.
- Índice de la última fila/columna, la última fila o columna del grupo.
- Está oculto, un parámetro booleano que especifica si ocultar o no filas/columnas después de agrupar.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Group first six rows (from 0 to 5) and make them hidden
    worksheet.GetCells().GroupRows(0, 5, true);

    // Group first three columns (from 0 to 2) and make them hidden
    worksheet.GetCells().GroupColumns(0, 2, true);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    workbook.Save(outputFilePath);

    std::cout << "Rows and columns grouped successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Configuración de Grupo**

Microsoft Excel te permite configurar la configuración de grupo para mostrar:

- Filas resumen debajo del detalle.
- Columnas de resumen a la derecha del detalle.

Los desarrolladores pueden configurar estas configuraciones de grupo usando la propiedad [**GetOutline()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getoutline/) de la clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/).

### **Filas de Resumen Debajo del Detalle**

Es posible controlar si se muestran las filas de resumen debajo del detalle configurando la propiedad [**GetSummaryRowBelow()**](https://reference.aspose.com/cells/cpp/aspose.cells/outline/getsummaryrowbelow/) de la clase [**Outline**](https://reference.aspose.com/cells/cpp/aspose.cells/outline/) en **true** o **false**.

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
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Grouping first six rows and first three columns
    worksheet.GetCells().GroupRows(0, 5, true);
    worksheet.GetCells().GroupColumns(0, 2, true);

    // Setting SummaryRowBelow property to false
    worksheet.GetOutline().SetSummaryRowBelow(false);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file modified and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Columnas Resumen a la Derecha del Detalle**

Los desarrolladores también pueden controlar la visualización de columnas de resumen a la derecha del detalle configurando la propiedad [**GetSummaryColumnRight()**](https://reference.aspose.com/cells/cpp/aspose.cells/outline/getsummarycolumnright/) de la clase [**Outline**](https://reference.aspose.com/cells/cpp/aspose.cells/outline/) en **true** o **false**.

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
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet worksheet = sheets.Get(0);

    // Grouping first six rows and first three columns
    worksheet.GetCells().GroupRows(0, 5, true);
    worksheet.GetCells().GroupColumns(0, 2, true);

    // Set summary column to the right
    worksheet.GetOutline().SetSummaryColumnRight(true);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file modified and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Desagrupando Filas y Columnas**

Para desagrupar filas o columnas agrupadas, llama a los métodos [**UngroupRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungrouprows/) y [**UngroupColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungroupcolumns/) de la colección [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Ambos métodos toman dos parámetros:

- Índice de la primera fila o columna, la primera fila/columna a desagrupar.
- Índice de la última fila o columna, la última fila/columna a desagrupar.

[**UngroupRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungrouprows/) tiene una sobrecarga que toma un tercer parámetro Booleano. Configurándolo en **true** eliminará toda la información agrupada. De lo contrario, solo se eliminará la información de grupo externa.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Ungrouping first six rows (from 0 to 5)
    worksheet.GetCells().UngroupRows(0, 5);

    // Ungrouping first three columns (from 0 to 2)
    worksheet.GetCells().UngroupColumns(0, 2);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    workbook.Save(outputFilePath);

    Aspose::Cells::Cleanup();

    return 0;
}
```
