---
title: Rand eines Bereichs mit C++ festlegen
type: docs
weight: 600
url: /de/cpp/set-range-border/
description: Lernen Sie, wie Sie mit Aspose.Cells und C++ Ränder eines Bereichs festlegen.
---

## **Mögliche Verwendungsszenarien**
Wenn Sie den Rand für einen Bereich festlegen möchten, müssen Sie nicht jede Zelle einzeln einstellen. Sie können den Rand für den gesamten Bereich festlegen. Aspose.Cells bietet diese Funktion. Dieser Artikel enthält einen Beispielcode, der zeigt, wie man mit Aspose.Cells den Bereichsrand setzt.

## **Bereichsgrenze in Excel festlegen**
Um die Grenze eines Bereichs in Excel festzulegen, befolgen Sie diese Schritte:
1. Wählen Sie den Zellenbereich aus, für den Sie die Grenze festlegen möchten.
2. Suchen Sie im Register „Start“ in der Gruppe „Schriftart“.
3. Klicken Sie in der Gruppe „Schriftart“ auf die Schaltfläche „Rahmen“.
<br>
<img src="border.png" />
4. Wählen Sie den zu verwendenden Randtyp aus den Optionen im Dropdown-Menü aus. Sie können aus voreingestellten Rahmenstilen wählen oder Ihren eigenen Rahmen anpassen.
5. Sobald Sie den gewünschten Rahmenstil ausgewählt haben, wird der Rahmen auf den ausgewählten Zellenbereich angewendet.

## **Bereichsgrenze mit Aspose.Cells festlegen**
Dieses Beispiel zeigt, wie Sie:

1. Ein Arbeitsbuch erstellen.
2. Daten in die Zellen des ersten Arbeitsblatts einfügen.
3. Erstellen Sie ein [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range).
4. Inneren Rand des Bereichs einstellen.
5. Äußeren Rand des Bereichs einstellen.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new Workbook object
    Workbook workbook;

    // Obtain the reference of the newly added worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Setting the value to the cells
    Cell cell = cells.Get("A1");
    cell.PutValue(u"Fruit");
    cell = cells.Get("B1");
    cell.PutValue(u"Count");
    cell = cells.Get("C1");
    cell.PutValue(u"Price");

    cell = cells.Get("A2");
    cell.PutValue(u"Apple");
    cell = cells.Get("A3");
    cell.PutValue(u"Mango");
    cell = cells.Get("A4");
    cell.PutValue(u"Blackberry");
    cell = cells.Get("A5");
    cell.PutValue(u"Cherry");

    cell = cells.Get("B2");
    cell.PutValue(5);
    cell = cells.Get("B3");
    cell.PutValue(3);
    cell = cells.Get("B4");
    cell.PutValue(6);
    cell = cells.Get("B5");
    cell.PutValue(4);

    cell = cells.Get("C2");
    cell.PutValue(5);
    cell = cells.Get("C3");
    cell.PutValue(20);
    cell = cells.Get("C4");
    cell.PutValue(30);
    cell = cells.Get("C5");
    cell.PutValue(60);

    // Create a range (A1:C5)
    Range range = cells.CreateRange(u"A1", u"C5");

    // Set inner border of range
    CellsColor innerColor = workbook.CreateCellsColor();
    innerColor.SetColor(Color::Red());
    range.SetInsideBorders(BorderType::Vertical, CellBorderType::Thin, innerColor);
    innerColor.SetColor(Color::Green());
    range.SetInsideBorders(BorderType::Horizontal, CellBorderType::Thin, innerColor);

    // Set outer border of range
    CellsColor outerColor = workbook.CreateCellsColor();
    outerColor.SetColor(Color::Blue());
    range.SetOutlineBorders(CellBorderType::Thin, outerColor);

    // Save the Workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
