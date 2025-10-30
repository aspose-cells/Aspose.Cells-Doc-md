---
title: Zellindex mit C++ abrufen
linktitle: Zellenindex erhalten
type: docs
weight: 600
url: /de/cpp/get-cells-index/
description: Lernen Sie, wie Sie die Zeilen oder Spaltenindex anhand des Namens der Zeile, Spalte oder Zelle ermitteln. Konvertieren Sie den Namen der Zelle mithilfe von Aspose.Cells mit C++ in einen nullbasierten Zeilen und Spaltenindex.
keywords: Zeilen und Spaltenindex nach dem Namen der Zelle erhalten, Spaltenindex nach dem Namen der Spalte erhalten, Zeilenindex nach dem Namen der Zeile erhalten, Index nach dem Namen der Zelle erhalten.
---

{{% alert color="primary" %}}
Die Standardansicht von Excel ist die A1-Referenz. Dabei ist jede Spalte als A, B, C... definiert, und die Zellen sind als A1, B2, C3... benannt.
 Sie möchten vielleicht wissen, in welcher Zeile und Spalte sich diese Zelle befindet.

{{% /alert %}}

## **Mögliche Verwendungsszenarien**
 Wenn Sie nur bestimmte Daten im Arbeitsblatt anhand von Zeilen- und Spaltenindex manipulieren möchten, müssen Sie die Zeilen- und Spaltenindizes dieser speziellen Zelle kennen. 
 Aspose.Cells bietet diese Funktion, um Zeilen- und Spaltenindex anhand des Namens der Zeile, Spalte und Zelle zu ermitteln. 
 Aspose.Cells stellt die folgenden Eigenschaften und Methoden bereit, um Ihre Ziele zu erreichen:
- [**CellsHelper::CellNameToIndex**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellnametoindex/)
- [**CellsHelper::ColumnIndexToName**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/columnindextoname/)
- [**CellsHelper::ColumnNameToIndex**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/columnnametoindex/)
- [**CellsHelper::RowIndexToName**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/rowindextoname/)
- [**CellsHelper::RowNameToIndex**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/rownametoindex/)

Hinweis: Die Indizierung ist nullbasiert in Aspose.Cells for C++, aber die ID der Zeile ist einsbasiert in MS Excel.

## **Zellenindizes mithilfe von Aspose.Cells abrufen**
Dieses Beispiel zeigt, wie Sie:

1. Erstellen Sie ein Arbeitsbuch und fügen Sie einige Daten hinzu.
1. Finden Sie die spezifische Zelle im ersten Arbeitsblatt.
1. Holen Sie sich den Zeilenindex und Spaltenindex nach dem Namen der Zelle.
1. Holen Sie sich den Spaltenindex nach dem Namen der Spalte.
1. Holen Sie sich den Zeilenindex nach dem Namen der Zeile.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Instantiating a Workbook object
    Workbook workbook;

    // Obtaining the reference of the newly added worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Setting the value to the cells
    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Fruit");
    cell = cells.Get(u"B1");
    cell.PutValue(u"Count");
    cell = cells.Get(u"C1");
    cell.PutValue(u"Price");

    cell = cells.Get(u"A2");
    cell.PutValue(u"Apple");
    cell = cells.Get(u"A3");
    cell.PutValue(u"Mango");
    cell = cells.Get(u"A4");
    cell.PutValue(u"Blackberry");
    cell = cells.Get(u"A5");
    cell.PutValue(u"Cherry");

    cell = cells.Get(u"B2");
    cell.PutValue(5);
    cell = cells.Get(u"B3");
    cell.PutValue(3);
    cell = cells.Get(u"B4");
    cell.PutValue(6);
    cell = cells.Get(u"B5");
    cell.PutValue(4);

    cell = cells.Get(u"C2");
    cell.PutValue(5);
    cell = cells.Get(u"C3");
    cell.PutValue(20);
    cell = cells.Get(u"C4");
    cell.PutValue(30);
    cell = cells.Get(u"C5");
    cell.PutValue(60);

    Cell curr = cells.Find(u"Blackberry", nullptr);
    int currRow, currCol;

    // Get row and column index of current cell
    CellsHelper::CellNameToIndex(curr.GetName(), currRow, currCol);
    std::cout << "Row Index: " << currRow << "  Column Index: " << currCol << std::endl;

    // Get column name by column index
    U16String columnName = CellsHelper::ColumnIndexToName(currCol);

    // Get row name by row index
    U16String rowName = CellsHelper::RowIndexToName(currRow);

    std::cout << "Column Name: " << columnName.ToUtf8() << " Row Name: " << rowName.ToUtf8() << std::endl;

    // Get column index by column name
    int columnIndex = CellsHelper::ColumnNameToIndex(columnName);

    // Get row index by row name
    int rowIndex = CellsHelper::RowNameToIndex(rowName);

    std::cout << "Column Index: " << columnIndex << " Row Index: " << rowIndex << std::endl;

    // Assertions
    if (columnIndex != currCol || rowIndex != currRow) {
        std::cerr << "Assertion failed!" << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
