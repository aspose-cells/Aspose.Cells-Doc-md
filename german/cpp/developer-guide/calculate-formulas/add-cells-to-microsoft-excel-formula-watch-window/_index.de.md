---
title: Cells zum Microsoft Excel Formel Watch Fenster mit C++ hinzufügen
linktitle: Zellen zum Formelausblick Fenster hinzufügen
description: Lernen Sie, wie man mit Aspose.Cells for C++ Zellen zum Formelausblick Fenster in Excel hinzufügt. Laden oder erstellen Sie eine Excel Datei, manipulieren Sie Zellen, setzen Sie Formeln, und speichern Sie die modifizierte Datei.
keywords: Aspose.Cells, Excel, Formel Watch Fenster, Zellen, Hinzufügen, C++
type: docs
weight: 60
url: /de/cpp/add-cells-to-microsoft-excel-formula-watch-window/
---

## **Mögliche Verwendungsszenarien**

Das Microsoft Excel Watch Window ist ein nützliches Tool, um die Zellwerte und deren Formeln bequem in einem Fenster zu überwachen. Sie können das *Watch Window* in Microsoft Excel öffnen, indem Sie *Formeln > Watch Window* klicken. Es gibt eine *Add Watch*-Schaltfläche, mit der Sie Zellen zur Überwachung hinzufügen können. Ebenso können Sie die [**Worksheet.CellWatches.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells/cellwatchcollection/add/)-Methode verwenden, um Zellen mit Aspose.Cells API zum *Watch Window* hinzuzufügen.

## **Zellen zur Microsoft Excel-Formelüberwachung hinzufügen**

Der folgende Beispielcode setzt die Formel der Zellen C1 und E1 und fügt beide zum Watch Window hinzu. Danach speichert es die Arbeitsmappe als eine [Ausgabedatei](67338481.xlsx). Wenn Sie die Ausgabedatei öffnen und das *Watch Window* ansehen, sehen Sie beide Zellen wie in diesem Screenshot dargestellt.

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Beispielcode**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create empty workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Put some integer values in cell A1 and A2
    ws.GetCells().Get(u"A1").PutValue(10);
    ws.GetCells().Get(u"A2").PutValue(30);

    // Access cell C1 and set its formula
    Cell c1 = ws.GetCells().Get(u"C1");
    c1.SetFormula(u"=Sum(A1,A2)");

    // Add cell C1 into cell watches by name
    ws.GetCellWatches().Add(c1.GetName());

    // Access cell E1 and set its formula
    Cell e1 = ws.GetCells().Get(u"E1");
    e1.SetFormula(u"=A2*A1");

    // Add cell E1 into cell watches by its row and column indices
    ws.GetCellWatches().Add(e1.GetRow(), e1.GetColumn());

    // Save workbook to output XLSX format
    wb.Save(u"outputAddCellsToMicrosoftExcelFormulaWatchWindow.xlsx", SaveFormat::Xlsx);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
