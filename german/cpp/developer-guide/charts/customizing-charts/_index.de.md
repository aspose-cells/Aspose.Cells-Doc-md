---
title: Anpassen von Diagrammen mit C++
linktitle: Diagramme anpassen
description: Erfahren Sie, wie Sie Diagramme in Aspose.Cells for C++ anpassen können. Unser Leitfaden zeigt Ihnen, wie Sie Diagrammlayouts ändern, Datenreihen hinzufügen und formatieren, Achsen anpassen und verschiedene Formatierungsoptionen anwenden, um das Aussehen und die Benutzerfreundlichkeit Ihrer Diagramme zu verbessern.
keywords: Aspose.Cells for C++, Diagrammerstellung, Anpassung, Layouts, Datenreihen, Achsen, Formatierung, Erscheinungsbild, Benutzerfreundlichkeit.
type: docs
weight: 40
url: /de/cpp/customizing-charts/
---

{{% alert color="primary" %}}

## **Erstellen von benutzerdefinierten Diagrammen**

Bisher haben wir bei der Diskussion über Diagramme standardisierte Diagramme mit ihren Standardformatierungseinstellungen betrachtet. Wir definieren nur die Datenquelle, setzen einige Eigenschaften und das Diagramm wird mit den Standardformatierungen erstellt. Aber Aspose.Cells APIs unterstützen auch die Erstellung von benutzerdefinierten Diagrammen, die es Entwicklern ermöglichen, Diagramme mit eigenen Formatierungseinstellungen zu erstellen.

Entwickler können benutzerdefinierte Diagramme zur Laufzeit mithilfe von Aspose.Cells erstellen.

Ein Diagramm besteht aus einer Datenreihe. Jede Datenreihe in Aspose.Cells wird durch ein [**Series**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/)-Objekt repräsentiert, während ein [**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/)-Objekt als Sammlung von [**Series**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/)-Objekten dient. Beim Erstellen eines benutzerdefinierten Diagramms haben Entwickler die Freiheit, verschiedene Diagrammtypen für verschiedene Datenreihen (gesammelt im [**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/)-Objekt) zu verwenden.

Der nachstehende Beispielcode zeigt, wie benutzerdefinierte Diagramme erstellt werden können. In diesem Beispiel verwenden wir ein Säulendiagramm für die erste Datenreihe und ein Liniendiagramm für die zweite Reihe. Das Ergebnis ist, dass wir ein Säulendiagramm, kombiniert mit einem Liniendiagramm, dem Arbeitsblatt hinzufügen.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int sheetIndex = workbook.GetWorksheets().Add();

    // Obtain the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"A4").PutValue(110);
    worksheet.GetCells().Get(u"B1").PutValue(260);
    worksheet.GetCells().Get(u"B2").PutValue(12);
    worksheet.GetCells().Get(u"B3").PutValue(50);
    worksheet.GetCells().Get(u"B4").PutValue(100);

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Access the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Add NSeries (chart data source) to the chart ranging from "A1" cell to "B4"
    chart.GetNSeries().Add(u"A1:B4", true);

    // Set the chart type of 2nd NSeries to display as line chart
    chart.GetNSeries().Get(1).SetType(ChartType::Line);

    // Save the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "Chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Derzeit unterstützt Aspose.Cells nur benutzerdefinierte Diagramme, die Kreis-, Linien-, Säulen- und Säulenstapel-Diagramme kombinieren, aber in zukünftigen Versionen werden weitere Diagrammtypen unterstützt.

{{% /alert %}}
