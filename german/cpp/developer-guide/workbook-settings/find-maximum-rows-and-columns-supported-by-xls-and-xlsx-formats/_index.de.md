---
title: Maximale Zeilen und Spalten in XLS und XLSX Formaten mit C++ finden
linktitle: Maximale Zeilen und Spalten finden
type: docs
weight: 20
url: /de/cpp/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
description: Erfahren Sie, wie Sie die maximale Zeilen und Spaltenzahl der XLS und XLSX Formate mit Aspose.Cells for C++ ermitteln.
---

## **Mögliche Verwendungsszenarien**

Es gibt unterschiedliche Zeilen- und Spaltenzahlen, die von Excel-Formaten unterstützt werden. Zum Beispiel unterstützt XLS 65536 Zeilen und 256 Spalten, während XLSX 1048576 Zeilen und 16384 Spalten unterstützt. Wenn Sie wissen möchten, wie viele Zeilen und Spalten ein bestimmtes Format unterstützt, können Sie die Eigenschaften [**GetMaxRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxrow/) und [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxcolumn/) verwenden.

## **Suchen Sie die maximale Anzahl von Zeilen und Spalten, die von den XLS- und XLSX-Formaten unterstützt werden**

Der folgende Beispielcode erstellt zunächst eine Arbeitsmappe im XLS-Format und anschließend im XLSX-Format. Nach der Erstellung werden die Werte der Eigenschaften [**GetMaxRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxrow/) und [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxcolumn/) ausgegeben. Bitte siehe die Konsolenausgabe des unten angegebenen Codes zu Ihrer Referenz.

## **Beispielcode**

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

## **Konsolenausgabe**

{{< highlight java >}}

Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
