---
title: Bereich von Zellen in einem Arbeitsblatt mit C++ verschieben
linktitle: Bereich von Zellen in einem Arbeitsblatt verschieben
type: docs
weight: 370
url: /de/cpp/move-range-of-cells-in-a-worksheet/
description: Lernen Sie, wie Sie einen Zellbereich in einem Arbeitsblatt mit Aspose.Cells und C++ verschieben.
---

{{% alert color="primary" %}}

In diesem Artikel wird gezeigt, wie man einen Bereich von Zellen in einem Arbeitsblatt verschiebt.

{{% /alert %}}

## **Bereich von Zellen in einem Arbeitsblatt verschieben**
Der Beispielcode verwendet eine Vorlagendatei, um die Aufgabe zu demonstrieren.

**Die Eingabedatei**

![todo:image_alt_text](move-range-of-cells-in-a-worksheet_1.png)

Bitte sehen Sie die folgende generierte Datei mit dem Bereich A1:B5, der nach C1:D5 verschoben wurde.

**Die Ausgabedatei**

![todo:image_alt_text](move-range-of-cells-in-a-worksheet_2.png)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate the workbook object. Open the Excel file
    U16String inputFilePath = u"book1.xlsx";
    Workbook workbook(inputFilePath);

    // Access the first worksheet and its cells
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Create a range from A1 to B5
    Range range = cells.CreateRange(u"A1", u"B5");

    // Move the range to the right by 2 columns
    range.MoveTo(0, 2);

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
