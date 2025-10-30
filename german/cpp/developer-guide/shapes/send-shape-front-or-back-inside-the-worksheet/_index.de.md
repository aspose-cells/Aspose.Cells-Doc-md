---
title: Formen in Arbeitsblättern mit C++ nach vorne oder nach hinten senden
linktitle: Form vorwärts oder rückwärts innerhalb des Arbeitsblatts senden
type: docs
weight: 3400
url: /de/cpp/send-shape-front-or-back-inside-the-worksheet/
description: Lernen Sie, wie Sie die Z Order Position von Formen in einem Arbeitsblatt mit Aspose.Cells for C++ ändern.
---

## **Mögliche Verwendungsszenarien**

Wenn mehrere Formen am selben Ort vorhanden sind, wird ihre Sichtbarkeit durch ihre Z-Reihenfolge-Positionen bestimmt. Aspose.Cells bietet die [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/tofrontorback/) Methode, die die Z-Orders-Position der Form ändert. Wenn Sie eine Form nach hinten schicken möchten, verwenden Sie eine negative Zahl wie -1, -2, -3 usw. Wenn Sie eine Form nach vorne bringen möchten, verwenden Sie eine positive Zahl wie 1, 2, 3 usw.

## **Form nach vorn oder hinten im Arbeitsblatt senden**

Der folgende Beispielcode zeigt die Verwendung der [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/tofrontorback/) Methode. Bitte sehen Sie sich die [Beispiel-Excel-Datei](50528330.xlsx) an, die im Code verwendet wird, sowie die [Ausgabe-Excel-Datei](50528331.xlsx), die daraus erzeugt wurde. Der Screenshot zeigt die Wirkung des Codes auf die Beispiel-Excel-Datei nach der Ausführung.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Beispielcode**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load source Excel file
    Workbook wb(srcDir + u"sampleToFrontOrBack.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first and fourth shape
    Shape sh1 = ws.GetShapes().Get(0);
    Shape sh4 = ws.GetShapes().Get(3);

    // Print the Z-Order position of the shape
    std::cout << "Z-Order Shape 1: " << sh1.GetZOrderPosition() << std::endl;

    // Send this shape to front
    sh1.ToFrontOrBack(2);

    // Print the Z-Order position of the shape
    std::cout << "Z-Order Shape 4: " << sh4.GetZOrderPosition() << std::endl;

    // Send this shape to back
    sh4.ToFrontOrBack(-2);

    // Save the output Excel file
    wb.Save(outDir + u"outputToFrontOrBack.xlsx");

    std::cout << "Shapes reordered successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
