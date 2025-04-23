---
title: Slicer mit C++ entfernen
linktitle: Slicer entfernen
type: docs
weight: 30
url: /de/cpp/removing-slicer/
description: Erfahren Sie, wie Sie Slicer in Excel Dateien programmatisch mit Aspose.Cells for C++ entfernen.
---

## **Mögliche Verwendungsszenarien**

Wenn Sie einen Slicer in Microsoft Excel entfernen möchten, wählen Sie ihn einfach aus und drücken Sie die *Entfernen*-Taste. Ebenso, wenn Sie ihn programmatisch mit der API von Aspose.Cells entfernen möchten, verwenden Sie die [**Worksheet.Slicers.Remove()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicercollection/remove/)-Methode. Dadurch wird der Slicer aus dem Arbeitsblatt entfernt.

## **Slicer entfernen**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](67338478.xlsx), die einen vorhandenen Slicer enthält. Es greift auf die Slicer zu und entfernt ihn dann. Schließlich speichert er die Arbeitsmappe als [Ausgabe-Excel-Datei](67338477.xlsx). Der folgende Screenshot zeigt den Slicer, der nach der Ausführung des Beispielcodes entfernt wird.

![todo:image_alt_text](removing-slicer_1.png)

## **Beispielcode**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing slicer.
    U16String inputFilePath(u"sampleRemovingSlicer.xlsx");
    Workbook wb(inputFilePath);

    // Access first worksheet.
    WorksheetCollection worksheets = wb.GetWorksheets();
    Worksheet ws = worksheets.Get(0);

    // Access the first slicer inside the slicer collection.
    SlicerCollection slicers = ws.GetSlicers();
    Slicer slicer = slicers.Get(0);

    // Remove slicer.
    slicers.Remove(slicer);

    // Save the workbook in output XLSX format.
    U16String outputFilePath(u"outputRemovingSlicer.xlsx");
    wb.Save(outputFilePath, SaveFormat::Xlsx);

    std::cout << "Slicer removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
