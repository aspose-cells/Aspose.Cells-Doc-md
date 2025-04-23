---
title: Konvertieren Sie das Smart Art in Gruppierungsform mit C++
linktitle: Konvertieren Sie die SmartArt in eine Gruppenform
type: docs
weight: 200
url: /de/cpp/convert-the-smart-art-to-group-shape/
description: Erfahren Sie, wie Sie Smart Art Shape mit Aspose.Cells for C++ in Gruppierungsformen umwandeln und einzelne Teile der Gruppe zugreifen.
---

## **Mögliche Verwendungsszenarien**

Sie können eine SmartArt-Form in eine Gruppenform mit der Methode [**Shape::GetResultOfSmartArt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getresultofsmartart/) umwandeln. Dadurch können Sie die SmartArt-Form wie eine Gruppenform behandeln. Somit haben Sie Zugriff auf die einzelnen Teile oder Formen der Gruppenform.

## **Konvertieren des SmartArt in Gruppenform**

Der folgende Beispielcode lädt die [Beispieldatei Excel](55541793.xlsx), die eine Smart Art Shape enthält, wie in diesem Screenshot gezeigt. Anschließend wandelt er die Smart Art Shape in eine Gruppierungsform um und gibt die Shape::IsGroup-Eigenschaft aus. Bitte beachten Sie die Konsolenausgabe des Beispielcodes unten.

![todo:image_alt_text](convert-the-smart-art-to-group-shape_1.png)

## **Beispielcode**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Load the sample smart art shape - Excel file
    U16String inputFilePath(u"sampleSmartArtShape_GetResultOfSmartArt.xlsx");
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Determine if shape is smart art
    std::cout << "Is Smart Art Shape: " << sh.IsSmartArt() << std::endl;

    // Determine if shape is group shape
    std::cout << "Is Group Shape: " << sh.IsGroup() << std::endl;

    // Convert smart art shape into group shape
    std::cout << "Is Group Shape: " << sh.GetResultOfSmartArt().IsGroup() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Konsolenausgabe**

{{< highlight java >}}

Is Smart Art Shape: True

Is Group Shape: False

Is Group Shape: True

{{< /highlight >}}
