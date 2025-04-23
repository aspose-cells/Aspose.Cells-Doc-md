---
title: Encontrar el máximo de filas y columnas soportadas por los formatos XLS y XLSX con C++
linktitle: Encontrar el máximo de filas y columnas
type: docs
weight: 20
url: /es/cpp/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
description: Aprende cómo encontrar el máximo de filas y columnas soportadas por los formatos XLS y XLSX usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

Hay diferentes números de filas y columnas soportadas por los formatos de Excel. Por ejemplo, XLS soporta 65536 filas y 256 columnas mientras que XLSX soporta 1048576 filas y 16384 columnas. Si deseas saber cuántas filas y columnas soporta un formato dado, puedes usar las propiedades [**GetMaxRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxrow/) y [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxcolumn/).

## **Encontrar el número máximo de filas y columnas admitidas por los formatos XLS y XLSX**

El siguiente código de ejemplo crea un libro de trabajo primero en formato XLS y luego en XLSX. Después de la creación, imprime los valores de las propiedades [**GetMaxRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxrow/) y [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxcolumn/). Por favor, consulta la salida de la consola del código a continuación para tu referencia.

## **Código de muestra**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Print message about XLS format.
    std::cout << "Maximum Rows and Columns supported by XLS format." << std::endl;

    // Create workbook in XLS format.
    Workbook wb(FileFormatType::Excel97To2003);

    // Print the maximum rows and columns supported by XLS format.
    int maxRows = wb.GetSettings().GetMaxRow() + 1;
    int maxCols = wb.GetSettings().GetMaxColumn() + 1;
    std::cout << "Maximum Rows: " << maxRows << std::endl;
    std::cout << "Maximum Columns: " << maxCols << std::endl;
    std::cout << std::endl;

    // Print message about XLSX format.
    std::cout << "Maximum Rows and Columns supported by XLSX format." << std::endl;

    // Create workbook in XLSX format.
    wb = Workbook(FileFormatType::Xlsx);

    // Print the maximum rows and columns supported by XLSX format.
    maxRows = wb.GetSettings().GetMaxRow() + 1;
    maxCols = wb.GetSettings().GetMaxColumn() + 1;
    std::cout << "Maximum Rows: " << maxRows << std::endl;
    std::cout << "Maximum Columns: " << maxCols << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Salida de la consola**

{{< highlight java >}}

Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
