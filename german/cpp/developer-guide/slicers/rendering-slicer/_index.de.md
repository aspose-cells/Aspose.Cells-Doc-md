---
title: Rendering des Slicers mit C++
type: docs
weight: 40
url: /de/cpp/rendering-slicer/
description: Rendern Sie Gliederungsschneider in Excel Dateien mit Aspose.Cells in C++.
---

## **Mögliche Verwendungsszenarien**
Aspose.Cells unterstützt das Rendern von Slicer-Formen. Wenn Sie Ihr Arbeitsblatt in ein Bild konvertieren oder Ihre Arbeitsmappe in den Formaten PDF oder HTML speichern, werden Sie sehen, dass die Slicer ordnungsgemäß gerendert werden.
## **Slicer rendern**
Der folgende Beispielcode lädt die [Beispieldatei Excel](67338479.xlsx), die einen bestehenden Gliederungsschneider enthält. Er wandelt das Arbeitsblatt in ein Bild um, indem er den Druckbereich festlegt, der nur den Gliederungsschneider umfasst. Das folgende Bild zeigt den [Ausgabebild](67338480.png), das den gerenderten Gliederungsschneider zeigt. Wie man sieht, wurde der Gliederungsschneider richtig gerendert und sieht aus wie im Beispiel-Excel.

![todo:image_alt_text](rendering-slicer_1)
## **Beispielcode**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file containing slicer.
    Workbook workbook(u"sampleRenderingSlicer.xlsx");

    // Access first worksheet.
    Worksheet ws = workbook.GetWorksheets().Get(0);

    // Set the print area because we want to render slicer only.
    ws.GetPageSetup().SetPrintArea(u"B15:E25");

    // Specify image or print options, set one page per sheet and only area to true.
    ImageOrPrintOptions imgOpts;
    imgOpts.SetHorizontalResolution(200);
    imgOpts.SetVerticalResolution(200);
    imgOpts.SetImageType(ImageType::Png);
    imgOpts.SetOnePagePerSheet(true);
    imgOpts.SetOnlyArea(true);

    // Create sheet render object and render worksheet to image.
    SheetRender sr(ws, imgOpts);
    sr.ToImage(0, u"outputRenderingSlicer.png");

    Aspose::Cells::Cleanup();
}
```
