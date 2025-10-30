---
title: Hitta maximala rader och kolumner som stöds av XLS och XLSX format med C++
linktitle: Hitta maximala rader och kolumner
type: docs
weight: 20
url: /sv/cpp/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
description: Lär dig hur man hittar de maximala raderna och kolumnerna som stöds av XLS och XLSX format med hjälp av Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

Det finns olika antal rader och kolumner som stöds av Excel-format. Till exempel stöder XLS 65536 rader och 256 kolumner, medan XLSX stöder 1048576 rader och 16384 kolumner. Om du vill veta hur många rader och kolumner som stöds av ett givet format kan du använda [**GetMaxRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxrow/) och [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxcolumn/) egenskaper.

## **Hitta maxrader och maxkolumner som stöds av XLS och XLSX-format**

Följande exempel skapar först en arbetsbok i XLS-format och sedan i XLSX-format. Efter skapandet skriver den ut värdena för [**GetMaxRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxrow/) och [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxcolumn/) egenskaperna. Vänligen se konsolutmatningen av koden nedan för referens.

## **Exempelkod**

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

## **Konsoloutput**

{{< highlight java >}}

Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
