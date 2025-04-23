---
title: Convertir texto a columnas usando Aspose.Cells con C++
linktitle: Convertir texto en columnas
type: docs
weight: 30
url: /es/cpp/convert-text-to-columns-using-aspose-cells/
description: Aprenda cómo convertir texto en columnas en archivos de Excel usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

Puedes convertir tu Texto a Columnas utilizando Microsoft Excel. Esta característica está disponible en *Herramientas de Datos* bajo la pestaña *Datos*. Para dividir el contenido de una columna en varias columnas, los datos deben contener un delimitador específico como una coma (u otro carácter) en función del cual Microsoft Excel dividirá el contenido de una celda en varias celdas. Aspose.Cells también proporciona esta característica a través del método [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/texttocolumns/).

## **Convertir Texto en Columnas usando Aspose.Cells**

El siguiente código de ejemplo explica cómo usar el método [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/texttocolumns/). Primero añade algunos nombres de personas en la columna A de la primera hoja de cálculo. El nombre y el apellido están separados por un espacio. Luego aplica el método [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/texttocolumns/) en la columna A y lo guarda como un archivo Excel de salida. Si abre el [archivo Excel de salida](25395213.xlsx), verá que los nombres van en la columna A y los apellidos en la columna B, como se muestra en esta captura de pantalla.

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)

## **Código de muestra**

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

    // Create a workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Add people name in column A. Fast name and Last name are separated by space.
    ws.GetCells().Get(u"A1").PutValue(u"John Teal");
    ws.GetCells().Get(u"A2").PutValue(u"Peter Graham");
    ws.GetCells().Get(u"A3").PutValue(u"Brady Cortez");
    ws.GetCells().Get(u"A4").PutValue(u"Mack Nick");
    ws.GetCells().Get(u"A5").PutValue(u"Hsu Lee");

    // Create text load options with space as separator
    TxtLoadOptions opts;
    opts.SetSeparator(u' ');

    // Split the column A into two columns using TextToColumns() method
    // Now column A will have first name and column B will have second name
    ws.GetCells().TextToColumns(0, 0, 5, opts);

    // Save the workbook in xlsx format
    wb.Save(outDir + u"outputTextToColumns.xlsx");

    std::cout << "Text to columns conversion completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
