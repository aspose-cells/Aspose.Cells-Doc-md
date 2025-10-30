---
title: Bestimmen, ob Shape eine Smart Art Shape ist mit C++
linktitle: Bestimmen, ob es sich um eine SmartArt Form handelt
type: docs
weight: 400
url: /de/cpp/determine-if-shape-is-smart-art-shape/
description: Erfahren Sie, wie Sie mit Aspose.Cells for C++ feststellen, ob eine Shape eine Smart Art Shape ist.
---

## **Mögliche Verwendungsszenarien**

SmartArt-Formen sind spezielle Formen in Microsoft Excel, die es ermöglichen, automatisch komplexe Diagramme zu erstellen. Sie können feststellen, ob es sich um eine SmartArt-Form oder um eine normale Form handelt, indem Sie die Eigenschaft [**Shape.IsSmartArt**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/issmartart/) verwenden.

## **Feststellen, ob eine Form ein SmartArt-Form ist**

Der folgende Beispielcode lädt die [Beispieldatei Excel](55541792.xlsx), die eine SmartArt-Form enthält, wie in diesem Screenshot gezeigt. Anschließend wird der Wert der [**Shape.IsSmartArt**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/issmartart/)-Eigenschaft der ersten Form ausgegeben. Bitte beachten Sie die Konsolenausgabe des folgenden Beispielcodes.

![todo:image_alt_text](determine-if-shape-is-smart-art-shape_1.png)

## **Beispielcode**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Load the sample smart art shape - Excel file
    U16String inputFilePath(u"sampleSmartArtShape.xlsx");
    Workbook wb(inputFilePath);

    // Access first worksheet
    WorksheetCollection sheets = wb.GetWorksheets();
    Worksheet ws = sheets.Get(0);

    // Access first shape
    ShapeCollection shapes = ws.GetShapes();
    Shape sh = shapes.Get(0);

    // Determine if shape is smart art
    std::cout << "Is Smart Art Shape: " << sh.IsSmartArt() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Konsolenausgabe**

{{< highlight java >}}

Is Smart Art Shape: True

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
