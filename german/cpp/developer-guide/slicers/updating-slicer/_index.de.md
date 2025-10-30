---
title: Aktualisieren des Slicers mit C++
linktitle: Slicer aktualisieren
type: docs
weight: 50
url: /de/cpp/updating-slicer/
description: Dieser Artikel zeigt, wie man verbundene Pivot Tabellen durch Aktualisieren des Slicers mit der API Aspose.Cells for C++ aktualisiert.
keywords: Aspose.Cells C++ Aktualisierung des Slicers, C++ wie man den Slicer ändert, wie man den Slicer in C++ anpasst, wie man die Elemente des Slicers auswählt oder deselectiert.
---

## **Mögliche Verwendungsszenarien**

Wenn Sie einen Slicer in Microsoft Excel aktualisieren möchten, wählen Sie seine Elemente aus oder deselectieren Sie sie, dann aktualisiert sich die Slicer-Tabelle oder Pivot-Tabelle entsprechend. Verwenden Sie [**Slicer.GetSlicerCacheItems()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicercache/getslicercacheitems/), um die Elemente des Slicers mit Aspose.Cells auszuwählen oder zu deselectieren, und rufen Sie dann die [**Slicer.Refresh()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/refresh/)-Methode auf, um die Slicer-Tabelle oder Pivot-Tabelle zu aktualisieren.

## **Wie man den Slicer aktualisiert**

Der folgende Beispielscode lädt die [Beispiel-Excel-Datei](67338475.xlsx), die einen vorhandenen Slicer enthält. Es entwählt die 2. und 3. Elemente des Slicers und aktualisiert den Slicer. Anschließend speichert es die Arbeitsmappe unter [Ausgabe-Excel-Datei](67338476.xlsx). Der folgende Screenshot zeigt die Auswirkung des Beispielscodes auf die Beispiel-Excel-Datei. Wie Sie auf dem Screenshot sehen können, wurde durch das Aktualisieren des Slicers mit ausgewählten Elementen auch die Pivot-Tabelle entsprechend aktualisiert.

![todo:image_alt_text](updating-slicer_1.png)

## **Beispielcode**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing slicer.
    U16String inputFilePath = u"sampleUpdatingSlicer.xlsx";
    Workbook wb(inputFilePath);

    // Access first worksheet.
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access the first slicer inside the slicer collection.
    Slicer slicer = ws.GetSlicers().Get(0);

    // Access the slicer items.
    SlicerCacheItemCollection scItems = slicer.GetSlicerCache().GetSlicerCacheItems();

    SlicerCacheItemCollection items = slicer.GetSlicerCache().GetSlicerCacheItems();

    for (int i = 0; i < items.GetCount(); ++i)
    {
        SlicerCacheItem item = items.Get(i);
        if (item.GetValue() == u"Pink" || item.GetValue() == u"Green")
        {
            item.SetSelected(false);
        }
    }

    slicer.Refresh();

    // Save the modified workbook.
    U16String outputFilePath = u"out.xlsx";
    wb.Save(outputFilePath);

    std::cout << "Slicer updated and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
