---
title: Arbeiten mit dem Reflection Effekt von Shape oder Diagramm mit C++
linktitle: Arbeiten mit dem Spiegeleffekt von Form oder Diagramm
type: docs
weight: 210
url: /de/cpp/working-with-the-reflection-effect-of-shape-or-chart/
description: Lernen Sie, wie man mit dem Reflection Effekt von Formen oder Diagrammen mit Aspose.Cells und C++ arbeitet.
---

## **Mögliche Verwendungsszenarien**
Aspose.Cells bietet die [Shape.Reflection](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getreflection/) Eigenschaft zusammen mit der [ReflectionEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/) Klasse, um mit dem Reflection-Effekt von Shape oder Diagramm zu arbeiten. Die [ReflectionEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/) Klasse enthält folgende Eigenschaften, die gesetzt werden können, um unterschiedliche Ergebnisse je nach Anwendungsanforderung zu erzielen.

- [Unschärfe](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getblur/)
- [Richtung](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getdirection/)
- [Entfernung](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getdistance/)
- [Verblassenrichtung](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getfadedirection/)
- [Mit Form drehen](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getrotwithshape/)
- [Größe](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getsize/)
- [Transparenz](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/gettransparency/)
- [Typ](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/gettype/)

## **Arbeiten mit dem Spiegeleffekt von Form oder Diagramm**
Der folgende Beispielcode lädt die [Quelldatei Excel](5115424.xlsx) und greift auf die erste Shape im Standardarbeitsblatt zu, setzt verschiedene Eigenschaften der [Shape.Reflection](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getreflection/) Klasse und speichert dann die Arbeitsmappe in der [Ausgabedatei Excel](5115423.xlsx).

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

    // Load your source excel file
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Set the reflection effect of the shape, set its Blur, Size, Transparency and Distance properties
    ReflectionEffect re = sh.GetReflection();
    re.SetBlur(30);
    re.SetSize(90);
    re.SetTransparency(0);
    re.SetDistance(80);

    // Save the workbook in xlsx format
    wb.Save(outputFilePath);

    std::cout << "Reflection effect applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
