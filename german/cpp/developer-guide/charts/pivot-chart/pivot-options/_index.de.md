---
title: Verwaltung von PivotCharts mit PivotOptions in C++
linktitle: Pivot Optionen
type: docs
weight: 10
url: /de/cpp/how-to-manage-pivotchart-with-pivotoptions/
description: Verwaltung von PivotCharts mit PivotOptions unter Verwendung von C++.
keywords: PivotChart
---

## Was ist ein PivotChart

Ein PivotChart in Excel ist eine grafische Darstellung von Daten, die aus einer PivotTable erstellt wird. Es ermöglicht Benutzern, Daten dynamisch zu visualisieren und zu analysieren, indem Informationen in Diagrammform zusammengefasst und angezeigt werden. PivotCharts sind interaktiv und können leicht modifiziert werden, um verschiedene Perspektiven der Daten zu zeigen, was es zu einem leistungsstarken Werkzeug für die Datenanalyse und Präsentation in Excel macht.

## Wie man PivotChart mit PivotOptions verwaltet

Mit Aspose.Cells können Sie [**PivotOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/pivotoptions/) verwenden, um PivotChart zu verwalten.

Beispiel-Datei und Code:  
[Beispiel-Datei](Sample.xlsx)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Path for the sample Excel file
    U16String path = u"..\\Data\\01_SourceDirectory\\";

    // Create a Workbook object from the sample file
    Workbook book(path + u"Sample.xlsx");

    // Get the first chart from the first worksheet
    Chart chart = book.GetWorksheets().Get(0).GetCharts().Get(0);

    // Get the PivotOptions from the chart
    PivotOptions opt = chart.GetPivotOptions();

    // Hide ZoneFilter in PivotChart
    opt.SetDropZoneFilter(false); // HideZoneFilter

    // You can set more properties, try them!
    // opt.SetDropZoneCategories(false);  // HideZoneCategories
    // opt.SetDropZoneData(false);        // HideZoneData
    // opt.SetDropZoneSeries(false);      // HideZoneSeries
    // opt.SetDropZonesVisible(false);    // Hide All

    // Save the modified file to see the effect
    book.Save(path + u"HideZoneFilter.xlsx");

    std::cout << "Pivot chart updated and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Mit dem obigen Beispielcode können Sie die Ergebnisdatei mit folgender Wirkung überprüfen, wie im Bild gezeigt:

**![Ergebnis](Output.png)**
