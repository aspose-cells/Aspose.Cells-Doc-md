---
title: Wie setzt man einen Punkt als Total mit C++
linktitle: So setzen Sie einen Punkt als Gesamtwert
description: In einigen Excel Diagrammen, z.B. WaterFall Diagrammen, ist es notwendig, Punkte als Total zu setzen. Dieser Artikel beschreibt, wie man Aspose.Cells mit C++ dazu nutzt.
keywords: WaterFall Diagramm, Punkt, als Total setzen.
type: docs
weight: 72
url: /de/cpp/how-to-set-point-as-total/
---

## Was bedeutet "Punkt als Gesamtwert setzen" in Excel-Diagrammen

In einigen Excel-Diagrammen, z.B. WaterFall-Diagrammen, sind einige Punkdaten die Summe der vorherigen Punkte. Sie müssen eventuell den Punkt als Gesamtwert "setzen". Das Beispiel zeigt den Code und die Illustrationen.

## Für ein WaterFall-Diagramm muss man den Punkt "Als Total setzen" 

![todo:image_alt_text](set-as-total1.png)

Dieses Bild zeigt ein Wasserfall-Diagramm in Excel. Wir können sehen, dass es vier Datenpunkte gibt, die mit "Total" beginnen, und sie werden verwendet, um alle vorherigen Datenpunkte zu zählen.
In diesem Bild sind die Einstellungen nicht ganz richtig. Wenn wir einen Punkt "Total 2024" auswählen, sehen wir, dass die Option "Als Total setzen" in Excel nicht aktiviert ist.
Unten ist die [Beispieldatei Excel](SampleSheet.xlsx), die geändert werden muss, und wir werden Aspose.Cells verwenden, um sie korrekt einzurichten.

## Verwendung von Aspose.Cells zum "Setzen des Punkts als Total" 

Wir verwenden den folgenden Code, um die Datei richtig einzurichten:

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Initialize file path
    U16String filePath(u"");

    // Load the workbook
    Workbook wb(filePath + u"SampleSheet.xlsx");

    // Get the first worksheet
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // Get the chart by name
    Chart chart = worksheet.GetCharts().Get(u"Graphiq5");

    // Set some points as total column
    // In this example, we set points 0, 4, 8, 12 as total
    Vector<int32_t> subtotals = {0, 4, 8, 12};
    chart.GetNSeries().Get(0).GetLayoutProperties().SetSubtotals(subtotals);

    // Save the workbook
    wb.Save(filePath + u"output.xlsx");

    std::cout << "Chart subtotals set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Sie können die folgende korrekte [Ausgabedatei](output.xlsx) herunterladen

Wie im untenstehenden Bild gezeigt, sind die vier "Total"-Datenpunkte korrekt eingestellt, und Sie können den Unterschied zum vorherigen Diagramm erkennen.

![todo:image_alt_text](set-as-total2.png)
{{< app/cells/assistant language="cpp" >}}
