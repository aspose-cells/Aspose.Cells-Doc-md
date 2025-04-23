---
title: Arbeiten mit dem Glow Effekt von Shape oder Diagramm mit C++
linktitle: Arbeiten mit dem Leuchteffekt von Shape oder Diagramm
type: docs
weight: 240
url: /de/cpp/working-with-the-glow-effect-of-shape-or-chart/
description: Lernen Sie, wie man mit dem Glow Effekt von Formen oder Diagrammen mit Aspose.Cells for C++ arbeitet.
---

## **Mögliche Verwendungsszenarien**
Aspose.Cells bietet die [Shape.Glow](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapepropertycollection/getgloweffect/) Eigenschaft zusammen mit der [GlowEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/) Klasse, um mit dem Glow-Effekt von Shape oder Diagramm zu arbeiten. Die [GlowEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/) Klasse enthält folgende Eigenschaften, die gesetzt werden können, um unterschiedliche Ergebnisse je nach Anwendungsanforderung zu erzielen.

- [GlowEffect.Size](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/getsize/)
- [GlowEffect.Transparency](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/gettransparency/)
- [GlowEffect.Color](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/gloweffect/getcolor/)

## **Arbeiten mit dem Leuchteffekt von Form oder Diagramm**
Der folgende Beispielcode lädt die [Quelldatei Excel](5115407.xlsx) und greift auf die erste Shape in der ersten Tabelle zu, setzt die Untereigenschaften von [Shape.Glow](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapepropertycollection/getgloweffect/) und speichert dann die Arbeitsmappe in der [Ausgabedatei Excel](5115414.xlsx).

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load your source excel file
    Workbook wb(srcDir + u"sample.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Set the glow effect of the shape, Set its Size and Transparency properties
    GlowEffect ge = sh.GetGlow();
    ge.SetSize(30);
    ge.SetTransparency(0.4);

    // Save the workbook in xlsx format
    wb.Save(outDir + u"output_out.xlsx");

    std::cout << "Glow effect applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
