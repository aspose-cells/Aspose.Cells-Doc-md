---
title: Herausfinden, ob das Arbeitsblatt ein Dialogblatt mit C++ ist
linktitle: Feststellen, ob das Arbeitsblatt ein Dialogblatt ist
type: docs
weight: 90
url: /de/cpp/find-if-the-worksheet-is-dialog-sheet/
description: Dialogblatt ist ein altes Format des Blattes. Dieser Artikel liefert Instruktionen und Beispielcode, um programmgesteuert zu bestimmen, ob ein Excel Arbeitsblatt ein Dialogblatt ist, mit C++ API.
keywords: Excel Arbeitsblatt Dialogtyp mit C++ finden
---

## **Mögliche Verwendungsszenarien**

Ein Dialogblatt ist ein altes Format eines Arbeitsblatts mit einem Dialogfeld. Ein solches Blatt könnte von einer älteren Version von Microsoft Excel, z. B. 2003, wie in diesem Screenshot gezeigt, eingefügt werden. Es kann auch mit VBA in neueren Versionen wie Microsoft Excel 2016 eingefügt werden.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Sie können mit Hilfe der [**Worksheet.GetType()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettype/) Eigenschaft von Aspose.Cells herausfinden, ob das Blatt ein Dialogblatt oder ein anderer Typ ist. Wenn es den Enumerationswert [**SheetType.Dialog**](https://reference.aspose.com/cells/cpp/aspose.cells/sheettype/) zurückgibt, bedeutet dies, dass Sie es mit einem Dialogblatt zu tun haben.

## **Feststellen, ob das Arbeitsblatt ein Dialogblatt ist**

Das folgende Beispiel lädt die [Beispiel-Excel-Datei](64716820.xlsx), die ein Dialogblatt enthält. Es überprüft die [**Worksheet.GetType()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettype/) Eigenschaft, vergleicht sie mit [**SheetType.Dialog**](https://reference.aspose.com/cells/cpp/aspose.cells/sheettype/) und gibt dann die Nachricht aus. Bitte sehen Sie sich den Konsolenausgang des Beispielcodes unten für weitere Hilfe an.

## **Beispielcode**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load Excel file containing Dialog Sheet
    Workbook workbook(u"sampleFindIfWorksheetIsDialogSheet.xlsx");

    // Access first worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);

    // Find if the sheet type is dialog and print the message
    if (ws.GetType() == SheetType::Dialog)
    {
        std::cout << "Worksheet is a Dialog Sheet." << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

## **Konsolenausgabe**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
