---
title: Automatisches Ausfüllen eines Bereichs in Excel mit C++
linktitle: Autoausfüllbereich
type: docs
weight: 105
url: /de/cpp/autofill-ranges/
description: Erfahren Sie, wie Sie eine Autofill Operation in einem bestimmten Bereich einer Excel Datei mit Aspose.Cells und C++ durchführen.
---

## **Automatisches Ausfüllen im angegebenen Bereich in Excel**

Wählen Sie in Excel einen Bereich aus, bewegen Sie die Maus in die rechte untere Ecke und ziehen Sie das "+"-Symbol, um die Daten automatisch auszufüllen.

## **Auto Fill-Bereiche mit Aspose.Cells**

Das folgende Beispiel zeigt, wie ein AutoFill in einem Bereich durchgeführt wird. Hier ist die Beispiel-Datei, die zum Testen dieser Funktion heruntergeladen werden kann:

[range_autofill.xlsx](range_autofill.xlsx)

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook
    Workbook workbook(u"range_autofill.xlsx");

    // Get Cells
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Create Range
    Range src = cells.CreateRange(u"C3:C4");
    Range dest = cells.CreateRange(u"C5:C10");

    // AutoFill
    src.AutoFill(dest, AutoFillType::Series);

    // Save the Workbook
    workbook.Save(u"range_autofill_result.xlsx");

    std::cout << "Range auto-filled successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
