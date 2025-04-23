---
title: Text mit Shape innerhalb des Arbeitsblatts mit C++ drehen
linktitle: Text mit Shape drehen
type: docs
weight: 1300
url: /de/cpp/rotate-text-with-shape-inside-the-worksheet/
description: Lernen Sie, wie Sie die Textrotation mit Shapes in Excel Tabellen mit Aspose.Cells for C++ steuern.
---

## **Mögliche Verwendungsszenarien**

Sie können Text in jeder Form mit Microsoft Excel hinzufügen. Wenn Sie eine Form mit der sehr alten Microsoft Excel 2003-Version hinzufügen, dreht sich der Text nicht mit der Form. Wenn Sie jedoch eine Form mit neueren Versionen von Microsoft Excel hinzufügen, wie 2007, 2010, 2013 oder 2016, dreht sich der Text mit der Form. Sie können steuern, ob der Text mit der Form drehen soll oder nicht, mit der [**ShapeTextAlignment.GetRotateTextWithShape()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getrotatetextwithshape/)-Eigenschaft. Der Standardwert dieser Eigenschaft ist **true**, was bedeutet, dass sich der Text mit der Form dreht. Wenn Sie ihn auf **false** setzen, dreht sich der Text nicht mit der Form.

## **Text mit Form im Arbeitsblatt drehen**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](64716896.xlsx), die eine Dreieckform enthält und deren Text sich mit der Form dreht. Wenn Sie die Beispiel-Excel-Datei in Microsoft Excel öffnen und das Dreieck drehen, dreht sich auch der Text mit. Der Code setzt dann die [**ShapeTextAlignment.GetRotateTextWithShape()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getrotatetextwithshape/)-Eigenschaft auf **false** und speichert sie als [Ausgabedatei](64716897.xlsx). Wenn Sie die Ausgabedatei in Microsoft Excel öffnen und das Dreieck drehen, dreht sich der Text nicht mit. Bitte sehen Sie sich den folgenden Screenshot an, der die Wirkung des Codes auf die Beispiel-Excel-Datei zeigt.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Beispielcode**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Drawing::Texts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load sample Excel file
    Workbook wb(srcDir + u"sampleRotateTextWithShapeInsideWorksheet.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell B4 and add message inside it
    Cell b4 = ws.GetCells().Get(u"B4");
    b4.PutValue(u"Text is not rotating with shape because RotateTextWithShape is false.");

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Access shape text alignment
    ShapeTextAlignment shapeTextAlignment = sh.GetTextBody().GetTextAlignment();

    // Do not rotate text with shape by setting RotateTextWithShape as false
    shapeTextAlignment.SetRotateTextWithShape(false);

    // Save the output Excel file
    wb.Save(outDir + u"outputRotateTextWithShapeInsideWorksheet.xlsx");

    Aspose::Cells::Cleanup();
}
```
