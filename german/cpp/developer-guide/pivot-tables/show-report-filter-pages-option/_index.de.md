---
title: Berichtsfilterseiten Option mit C++ anzeigen
linktitle: Option zum Anzeigen der Berichtfilterseiten
type: docs
weight: 110
url: /de/cpp/show-report-filter-pages-option/
description: Erfahren Sie, wie Sie die Option "Berichtfilterseiten anzeigen" in Pivot Tabellen mit Aspose.Cells for C++ aktivieren.
---

## **Option zum Anzeigen der Berichtfilterseiten**
Excel unterstützt das Erstellen von Pivot-Tabellen, das Hinzufügen von Berichtsfiltern und das Aktivieren der Option "Berichtfilterseiten anzeigen". Aspose.Cells unterstützt dieses Feature ebenfalls, um die Option "Berichtfilterseiten anzeigen" auf der erstellten Pivot-Tabelle zu aktivieren. Unten ist ein Screenshot, der die Option "Berichtfilterseiten anzeigen" in Excel zeigt.

![todo:image_alt_text](show-report-filter-pages-option_1.png)

Die Beispieldatei und die Ausgabedateien können von hier heruntergeladen werden, um den Beispielcode zu testen:

[Quelldatei Excel](81920786.xlsx) 

[Ausgabedatei Excel](81920787.xlsx)

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

    // Load template file
    Workbook wb(srcDir + u"samplePivotTable.xlsx");

    // Get first pivot table in the worksheet
    PivotTable pt = wb.GetWorksheets().Get(1).GetPivotTables().Get(0);

    // Set pivot field
    pt.ShowReportFilterPage(pt.GetPageFields().Get(0));

    // Set position index for showing report filter pages
    pt.ShowReportFilterPageByIndex(pt.GetPageFields().Get(0).GetPosition());

    // Set the page field name
    pt.ShowReportFilterPageByName(pt.GetPageFields().Get(0).GetName());

    // Save the output file
    wb.Save(outDir + u"outputSamplePivotTable.xlsx");

    std::cout << "Pivot table report filter pages set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
