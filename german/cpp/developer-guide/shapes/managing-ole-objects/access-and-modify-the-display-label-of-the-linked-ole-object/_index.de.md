---
title: Zugriff und Änderung des Anzeige Labels des verbundenen OLE Objekts mit C++
linktitle: Auf das Anzeigen des verknüpften Ole Objekts zugreifen und es ändern
type: docs
weight: 100
url: /de/cpp/access-and-modify-the-display-label-of-the-linked-ole-object/
description: Lernen Sie, wie Sie den Anzeige Label verbundener OLE Objekte in Excel Dateien mit Aspose.Cells for C++ zugreifen und diesen ändern.
---

## **Mögliche Verwendungsszenarien**

Microsoft Excel erlaubt es, das Anzeige-Label des OLE-Objekts zu ändern, wie im folgenden Screenshot gezeigt. Sie können auch das Anzeige-Label des OLE-Objekts mit den APIs von Aspose.Cells und den Methoden [**GetLabel()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getlabel/) und [**SetLabel(const U16String\& value)**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/setlabel/) zugreifen oder ändern.

![todo:image_alt_text](access-and-modify-the-display-label-of-the-linked-ole-object_1.png)

## **Auf das Anzeigen des verknüpften Ole-Objekts zugreifen und es ändern**

Bitte sehen Sie sich den folgenden Beispielcode an. Es lädt die [Beispieldatei Excel](64716810.xlsx), die das Ole-Objekt enthält. Der Code ruft das Ole-Objekt auf und ändert sein Label von 'Sample APIs' in 'Aspose APIs'. Bitte sehen Sie sich die unten angezeigte Konsolenausgabe an, die die Auswirkung des Beispielcodes auf die Beispieldatei Excel zeigt.

## **Beispielcode**

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Load the sample Excel file
    U16String inputFilePath = u"sampleAccessAndModifyLabelOfOleObject.xlsx";
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first Ole Object
    OleObject oleObject = ws.GetOleObjects().Get(0);

    // Display the Label of the Ole Object
    std::cout << "Ole Object Label - Before: " << oleObject.GetLabel().ToUtf8() << std::endl;

    // Modify the Label of the Ole Object
    oleObject.SetLabel(u"Aspose APIs");

    // Save workbook to memory stream
    auto ms = wb.SaveToStream();

    // Set the workbook reference to null
    wb = Workbook();

    // Load workbook from memory stream
    wb = Workbook(ms);

    // Access first worksheet
    ws = wb.GetWorksheets().Get(0);

    // Access first Ole Object
    oleObject = ws.GetOleObjects().Get(0);

    // Display the Label of the Ole Object that has been modified earlier
    std::cout << "Ole Object Label - After: " << oleObject.GetLabel().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Konsolenausgabe**

{{< highlight java >}}

Ole Object Label - Before: Sample APIs

Ole Object Label - After: Aspose APIs

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
