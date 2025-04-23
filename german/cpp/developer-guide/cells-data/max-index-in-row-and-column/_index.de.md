---
title: Maximale Spaltenindex in einer Zeile und maximaler Zeilenindex in einer Spalte mit C++
linktitle: Maximalen Spaltenindex in Zeile und maximalen Zeilenindex in Spalte erhalten
type: docs
weight: 600
url: /de/cpp/get-max-index-in-row-and-column/
description: Lernen Sie, wie man den maximalen Spaltenindex in einer Zeile und den maximalen Zeilenindex in einer Spalte über die API Aspose.Cells for C++ erhält.
keywords: Holen Sie sich den Max Spaltenindex in Zeile, holen Sie sich den Max Zeilenindex in Spalte, holen Sie sich den Max Data Spaltenindex in Zeile, holen Sie sich den Max Data Zeilenindex in Spalte.
---

## **Mögliche Verwendungsszenarien**
Wenn Sie nur einige Daten in den Zeilen oder Spalten manipulieren müssen, ist es wichtig, den Datenbereich der Zeilen und Spalten zu kennen. Aspose.Cells bietet diese Funktion. Um den maximalen Spaltenindex in einer Zeile zu erhalten, können Sie die Eigenschaften [Row.GetLastCell()](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastcell/) und [Row.GetLastDataCell()](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastdatacell/) verwenden und dann die Eigenschaft [Cell.GetColumn()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/) nutzen, um den maximalen Spaltenindex und den maximalen Daten-Spaltenindex zu bestimmen. Um aber den maximalen Zeilenindex und den maximalen Zeilendatenindex in einer Spalte zu erhalten, müssen Sie einen Bereich in der Spalte erstellen, diesen Bereich durchlaufen, um die letzte Zelle zu finden, und schließlich das Attribut [Cell.GetRow()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/) der Zelle verwenden.

Aspose.Cells bietet die folgenden Eigenschaften und Methoden, um Ihnen bei Ihren Zielen zu helfen.
- [**Row.GetLastCell()**](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastcell/)
- [**Row.GetLastDataCell()**](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastdatacell/)
- [**Cell.GetColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/)
- [**Cell.GetRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/)

## **Holen Sie sich den Max-Spaltenindex in Zeile und den Max-Zeilenindex in Spalte mit Aspose.Cells**
Dieses Beispiel zeigt, wie Sie:

1. Laden Sie die [Beispieldatei](sample.xlsx).
1. Die Zeile abrufen, für die der maximale Spaltenindex und der maximale Daten-Spaltenindex benötigt werden.
1. Holen Sie das [Cell.GetColumn()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/) Attribut der Zelle.
1. Basierend auf der Spalte einen Bereich erstellen.
1. Iterator abrufen und den Bereich durchlaufen.
1. Holen Sie das [Cell.GetRow()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/) Attribut der Zelle.

```c++
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String filePath = srcDir + u"sample.xlsx";

    Workbook workbook(filePath);
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    Row row = cells.CheckRow(1);
    if (row)
    {
        std::cout << "Max column index in row: " << row.GetLastCell().GetColumn() << std::endl;
        std::cout << "Max data column index in row: " << row.GetLastDataCell().GetColumn() << std::endl;
    }

    Range columnRange = cells.CreateRange(1, 1, true);
    auto colIter = columnRange.GetEnumerator();

    int maxRow = 0;
    int maxDataRow = 0;

    while (colIter.MoveNext())
    {
        Cell currCell = colIter.GetCurrent();
        if (!currCell.GetStringValue().IsEmpty())
        {
            maxDataRow = currCell.GetRow();
        }
        if (!currCell.GetStringValue().IsEmpty() || currCell.GetHasCustomStyle())
        {
            maxRow = currCell.GetRow();
        }
    }

    std::cout << "Max row index in Column: " << maxRow << std::endl;
    std::cout << "Max data row index in Column: " << maxDataRow << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
