---
title: Text aus SmartArt Shape vom Getriebetyp mit C++ extrahieren
linktitle: Extrahieren Sie Text aus der SmartArt Form des Zahnradtyps
type: docs
weight: 500
url: /de/cpp/extract-text-from-the-gear-type-smartart-shape/
description: Erfahren Sie, wie Sie mit Aspose.Cells for C++ Text aus SmartArt Shapes vom Getriebetyp in Excel extrahieren, inklusive Schritt für Schritt Anleitung und Codebeispielen.
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells for C++ kann Text aus SmartArt Shape vom Getriebetyp extrahieren. Folgen Sie dazu diesen Schritten:
1. Konvertieren Sie SmartArt Shape mit der Methode [**Shape::GetResultOfSmartArt()**](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.shape/#a0b6c1c2e57f8f1d83a4b8e4f4c4e4f4) in eine Gruppierungsform.
2. Rufen Sie alle einzelnen Formen ab, die die Gruppierungsform bilden, mit der Methode [**GroupShape::GetGroupedShapes()**](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.group_shape/#a8d1a5a5b3a4a7a9a7a9a7a9a7a9a7a).
3. Durchlaufen Sie jede einzelne Form und extrahieren Sie Text mit der Methode [**GetText()**](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.shape/#a8d1a5a5b3a4a7a9a7a9a7a9a7a9a).

## **Text aus dem SmartArt-Form 'Zahnräder' extrahieren**

Der folgende Beispielcode lädt eine [Beispieldatei Excel](67338483.xlsx), die eine Smart Art Shape vom Getriebetyp enthält, und extrahiert Text aus ihren einzelnen Formen. Die Ergebnisse sind in der untenstehenden Konsolenausgabe ersichtlich.

## **Beispielcode**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing gear type smart art shape
    U16String inputFile(u"sampleExtractTextFromGearTypeSmartArtShape.xlsx");
    Workbook wb(inputFile);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Get SmartArt result as group shape
    GroupShape gs = sh.GetResultOfSmartArt();

    // Get grouped shapes collection
    Vector<Shape> shps = gs.GetGroupedShapes();

    // Iterate through shapes and check gear types
    for (int i = 0; i < shps.GetLength(); i++)
    {
        Shape s = shps[i];
        AutoShapeType shapeType = s.GetType();

        if (shapeType == AutoShapeType::Gear9 || shapeType == AutoShapeType::Gear6)
        {
            std::cout << "Gear Type Shape Text: " << s.GetText().ToUtf8() << std::endl;
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Konsolenausgabe**

{{< highlight java >}}
Gear Type Shape Text: Nice
Gear Type Shape Text: Good
Gear Type Shape Text: Excellent
{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
