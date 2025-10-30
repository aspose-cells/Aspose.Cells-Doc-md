---
title: Slicer Eigenschaften mit C++ ändern
linktitle: Slicer Eigenschaften ändern
type: docs
weight: 70
url: /de/cpp/change-slicer-properties/
description: Ändern Sie die Eigenschaften eines Slicers in Excel Dateien mit Aspose.Cells in C++.
---

## **Mögliche Verwendungsszenarien**

Es kann Situationen geben, in denen Sie die Eigenschaften des Slicers wie Platzierung oder Zeilenhöhe ändern möchten. Aspose.Cells bietet Ihnen die Möglichkeit, diese Eigenschaften zu aktualisieren.

## **Slicer-Eigenschaften ändern**

Bitte sehen Sie sich den folgenden Beispielcode an. Er lädt die [Beispieldatei](sampleCreateSlicerToExcelTable.xlsx), die eine Tabelle enthält. Dann erstellt er den Slicer basierend auf der ersten Spalte und ändert dessen Eigenschaften wie Zeilenhöhe, Breite, ist druckbar, Titel, etc. Er speichert die Arbeitsmappe als [Ausgabedatei zum Ändern der Slicer-Eigenschaften.xlsx](outputChangeSlicerProperties.xlsx).

## **Beispielcode**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file containing a table.
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    Workbook workbook(sourceDir + u"sampleCreateSlicerToExcelTable.xlsx");

    // Access first worksheet.
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first table inside the worksheet.
    ListObject table = worksheet.GetListObjects().Get(0);

    // Add slicer
    int32_t idx = worksheet.GetSlicers().Add(table, 0, u"H5");

    Slicer slicer = worksheet.GetSlicers().Get(idx);
    slicer.SetPlacement(PlacementType::FreeFloating);
    slicer.SetRowHeightPixel(50);
    slicer.SetWidthPixel(500);
    slicer.SetTitle(u"Aspose");
    slicer.SetAlternativeText(u"Alternate Text");
    slicer.SetIsPrintable(false);
    slicer.SetIsLocked(false);

    // Refresh the slicer.
    slicer.Refresh();

    // Save the workbook in output XLSX format.
    workbook.Save(outputDir + u"outputChangeSlicerProperties.xlsx", SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
