---
title: Zeitleiste mit C++ rendern
type: docs
weight: 40
url: /de/cpp/rendering-timeline/
description: Verwalten Sie Zeitleisten von Excel Dateien mit Aspose.Cells für C++.
keywords: Zeitachse rendern ohne Office 2013, Office 2016, Office 2019 und Office 365
---

## **Mögliche Verwendungsszenarien**
Aspose.Cells unterstützt das Rendern von Zeitachseformen, ohne Office 2013, Office 2016, Office 2019 und Office 365 zu verwenden. Wenn Sie Ihr Arbeitsblatt in ein Bild konvertieren oder Ihre Arbeitsmappe in den Formaten PDF oder HTML speichern, sehen Sie, dass die Zeitachsen ordnungsgemäß gerendert werden.

## **Zeitachse rendern**
Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](input.xlsx) mit einer vorhandenen Zeitachse. Rufen Sie das Formobjekt entsprechend dem Namen der Zeitachse ab und rendern Sie es dann in ein Bild mit der Methode Shape.ToImage(). Das folgende Bild ist das [Ausgabebild](out.png), das die gerenderte Zeitachse zeigt. Wie Sie sehen können, wurde die Zeitachse korrekt gerendert und sieht genauso aus wie in der Beispiel-Excel-Datei.

![todo:image_alt_text](out.png)
### **Beispielcode**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing timeline.
    Workbook workbook(u"input.xlsx");

    // Access second worksheet.
    Worksheet sheet = workbook.GetWorksheets().Get(1);

    // Access the first Timeline inside the worksheet.
    Timeline timeline = sheet.GetTimelines().Get(0);

    ImageOrPrintOptions options;
    options.SetImageType(ImageType::Png);

    // Get timeline shape object by timeline's name
    Shape timeLineShape = sheet.GetShapes().Get(timeline.GetName());

    // Save the timeline as an image
    timeLineShape.ToImage(u"out.png", options);

    std::cout << "Timeline image saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
