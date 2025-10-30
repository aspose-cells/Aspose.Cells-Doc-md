---
title: Bereich der Zellen mit C++ abrufen
linktitle: Holen Sie sich den Zellenbereich
type: docs
weight: 600
url: /de/cpp/get-cells-range/
description: Lernen Sie, wie Sie den Zellenbereich mithilfe der Aspose.Cells for C++ API abrufen.
keywords: Höchsten Anzeigebereich von Zellen erhalten, Höchste Zeile von Zellen erhalten, Höchste Dat Zeile von Zellen erhalten, Höchste Spalte von Zellen erhalten, Höchste Datenspalte von Zellen erhalten.
---

## **Mögliche Verwendungsszenarien**
Wenn Sie nur einige Daten im Arbeitsblatt bearbeiten müssen, müssen Sie den Datenbereich des gesamten Arbeitsblatts kennen. Aspose.Cells bietet diese Funktion an. Aspose.Cells stellt die folgenden Eigenschaften und Methoden zur Verfügung, um Ihre Ziele zu erreichen.
- [**Cells.GetMaxDisplayRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdisplayrange/)
- [**Cells.GetMaxRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxrow/)
- [**Cells.GetMaxDataRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatarow/)
- [**Cells.GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxcolumn/)
- [**Cells.GetMaxDataColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatacolumn/)

## **Holen Sie sich den Zellenbereich mit Aspose.Cells**
Dieses Beispiel zeigt, wie Sie:

1. Ein Arbeitsbuch erstellen.
1. Daten zu Zellen im ersten Arbeitsblatt hinzufügen.
1. Zellen abrufen [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/).

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

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

    cell = cells.Get(u"E10");
    Style temp = workbook.CreateStyle();
    temp.GetFont().SetColor(Color::Red());
    cell.SetStyle(temp);

    Range range = cells.GetMaxDisplayRange();

    std::cout << cells.GetMaxRow() << std::endl;
    std::cout << cells.GetMaxDataRow() << std::endl;
    std::cout << cells.GetMaxColumn() << std::endl;
    std::cout << cells.GetMaxDataColumn() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
