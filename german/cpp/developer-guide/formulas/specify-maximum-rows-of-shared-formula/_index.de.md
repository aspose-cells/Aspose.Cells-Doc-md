---
title: Maximale Zeilen der gemeinsamen Formel mit C++ angeben
linktitle: Maximale Zeilen der gemeinsamen Formel angeben
type: docs
weight: 40
url: /de/cpp/specify-maximum-rows-of-shared-formula/
description: Erfahren Sie, wie Sie die maximale Zeilenzahl der gemeinsamen Formel in Excel Dateien mit Aspose.Cells for C++ angeben.
---

## **Mögliche Verwendungsszenarien**

Die standardmäßige maximale Zeilenzahl der gemeinsamen Formel ist 64. Es kann jede Zahl sein, z.B. 1000. Die Leistung der gemeinsamen Formel ändert sich mit einer unterschiedlichen Zeilenzahl. Daher bietet Aspose.Cells die Eigenschaft [**GetMaxRowsOfSharedFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxrowsofsharedformula/), die verwendet werden kann, um die maximale Zeilenzahl der gemeinsamen Formel anzugeben. Die gemeinsame Formel wird in mehreren gemeinsamen Formeln aufgeteilt, wenn die Gesamtzahl der Zeilen größer ist, wie im folgenden Screenshot gezeigt.

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)

## **Maximale Zeilen der gemeinsamen Formel angeben**

Der folgende Beispielcode erklärt die Verwendung der Eigenschaft [**GetMaxRowsOfSharedFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxrowsofsharedformula/). Er setzt die maximale Zeilenzahl der gemeinsamen Formel auf 5 und fügt die gemeinsame Formel in Zelle D1 für 100 Zeilen ein und speichert sie in [Ausgabedatei Excel](61767856.xlsx). Wenn Sie die Inhalte der Ausgabedatei extrahieren und *sheet1.xml* prüfen, sehen Sie, dass die gemeinsame Formel alle 5 Zeilen aufgeteilt wird, wie im obigen Screenshot hervorgehoben.

## **Beispielcode**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook wb;

    // Set the max rows of shared formula to 5
    wb.GetSettings().SetMaxRowsOfSharedFormula(5);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell D1
    Cell cell = ws.GetCells().Get(u"D1");

    // Set the shared formula in 100 rows
    cell.SetSharedFormula(u"=Sum(A1:A2)", 100, 1);

    // Save the output Excel file
    wb.Save(u"outputSpecifyMaximumRowsOfSharedFormula.xlsx");

    std::cout << "Shared formula set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
