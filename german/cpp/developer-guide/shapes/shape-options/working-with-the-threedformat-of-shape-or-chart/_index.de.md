---
title: Arbeiten mit der ThreeDFormat von Shape oder Diagramm mit C++
linktitle: Arbeiten mit dem 3D Format von Form oder Diagramm
type: docs
weight: 250
url: /de/cpp/working-with-the-threedformat-of-shape-or-chart/
description: Lernen Sie, wie man das 3D Format von Formen oder Diagrammen mit Aspose.Cells und C++ manipuliert.
---

## **Mögliche Verwendungsszenarien**
Aspose.Cells bietet die [Shape.ThreeDFormat](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getthreedformat/) Eigenschaft zusammen mit der [ThreeDFormat](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/threedformat/) Klasse, um mit dem 3D-Format von Formen oder Diagrammen zu arbeiten. Die [ThreeDFormat](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/threedformat/) Klasse enthält verschiedene Eigenschaften, die gesetzt werden können, um unterschiedliche Ergebnisse je nach Anwendungsanforderung zu erzielen.

## **Arbeiten mit dem ThreeDFormat von Shape oder Diagramm**
Der folgende Beispielcode lädt die [Quelldatei Excel](5115419.xlsx) und greift auf die erste Shape in der ersten Tabelle zu. Es setzt dann die Untereigenschaften der [Shape.ThreeDFormat](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getthreedformat/) Eigenschaft und speichert die Arbeitsmappe in der [Ausgabedatei Excel](5115410.xlsx).

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Load excel file containing a shape
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Apply different three dimensional settings
    ThreeDFormat n3df = sh.GetThreeDFormat();
    n3df.SetContourWidth(17);
    n3df.SetExtrusionHeight(32);

    // Save the output excel file in xlsx format
    wb.Save(outputFilePath);

    std::cout << "3D settings applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
