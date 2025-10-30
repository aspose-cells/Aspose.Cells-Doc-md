---
title: Wie erstellt man ein Gantt Diagramm mit C++
linktitle: So erstellen Sie ein Gantt Diagramm
type: docs
weight: 72
url: /de/cpp/how-to-create-gantt-chart/
description: Erfahren Sie, wie Sie mit der API Aspose.Cells for C++ ein Gantt Diagramm erstellen.
keywords: C++ Gantt Diagramm erstellen, Gantt Diagramm hinzufügen, Gantt Diagramm einfügen
---

## **Was ist ein Gantt-Diagramm?**

Ein Gantt-Diagramm ist eine Art Balkendiagramm, das einen Projektzeitplan veranschaulicht. Es zeigt die Anfangs- und Enddaten der verschiedenen Elemente eines Projekts. Jede Aufgabe oder Aktivität wird durch einen Balken dargestellt, dessen Länge ihrer Dauer entspricht. Gantt-Diagrams zeigen auch Abhängigkeiten zwischen Aufgaben, sodass Projektmanager die Reihenfolge der Aufgaben visualisieren können. Sie werden häufig im Projektmanagement verwendet, um Projekte effektiv zu planen, zu planen und zu verfolgen.

## **So erstellen Sie ein Gantt-Diagramm in Excel**

Sie können in Excel ein Gantt-Diagramm erstellen, indem Sie diese Schritte befolgen:
1. Fügen Sie einige Daten für das Gantt-Diagramm hinzu. 
<br>
<img src="00.png" width=50% />
1. Wählen Sie die Daten aus und gehen Sie zu Einfügen --> Diagramme --> Säulen- oder Balkendiagramm einfügen --> Gestapeltes Balkendiagramm. In unserem Beispiel sind das B1:B7, dann fügen Sie ein **Gestapeltes Balken**-Diagramm ein.
<br>
<img src="1.png" width=50% />

1. Wählen Sie das Diagramm aus, **Daten auswählen**->**Hinzufügen**, setzen Sie den **Seriennamen** und die **Serienwerte** wie folgt.
<br>
<img src="2.png" width=50% />

1. Wählen Sie das Diagramm aus, bearbeiten Sie die **Horizontalen (Kategorie) Achsenbeschriftungen**.
<br>
<img src="3.png" width=50% />

1. **Achse formatieren** des Y-Achse, wählen Sie **Kategorien umkehren**.
1. Wählen Sie die **Blaue Serie** aus und setzen Sie die **Füllung->Keine Füllung**.
1. **Achse formatieren** für die x-Achse, setzen Sie die **Minimal- und Maximalwerte** (01.05.2019:43470, 30.01.2019:43494).
<br>
<img src="4.png" width=50% />

1. **Datenbeschriftungen hinzufügen** für das Diagramm, jetzt erhalten Sie ein Gantt-Diagramm.
<br>
<img src="0.png" width=50% />


## **So fügen Sie ein Gantt-Diagramm in Aspose.Cells hinzu**
Bitte sehen Sie sich den folgenden Beispielcode an. Es lädt die [Beispiel-Excel-Datei](sample.xlsx), die einige Beispieldaten enthält. Anschließend erstellt es das gestapelte Balkendiagramm basierend auf den Anfangsdaten und setzt die entsprechenden Eigenschaften. Schließlich speichert es die Arbeitsmappe im [Ausgabe XLSX-Format](result.xlsx). Der folgende Screenshot zeigt das von Aspose.Cells erstellte Gantt-Diagramm in der Ausgabedatei.
<br>
<img src="5.png" width=60% />

### **Beispielcode**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"sample.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create BarStacked Chart
    int32_t chartIndex = worksheet.GetCharts().Add(ChartType::BarStacked, 5, 6, 20, 15);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Set the chart title name
    chart.GetTitle().SetText(u"Gantt Chart");

    // Set the chart title visibility
    chart.GetTitle().SetIsVisible(true);

    // Set data range
    chart.SetChartDataRange(u"B1:B6", true);

    // Add series data range
    chart.GetNSeries().Add(u"C2:C6", true);

    // No fill for one series
    chart.GetNSeries().Get(0).GetArea().GetFillFormat().SetFillType(FillType::None);

    // Set the Horizontal(Category) Axis
    chart.GetNSeries().SetCategoryData(u"A2:A6");

    // Reverse the Horizontal(Category) Axis
    chart.GetCategoryAxis().SetIsPlotOrderReversed(true);

    // Set the value axis's MinValue and MaxValue
    chart.GetValueAxis().SetMinValue(worksheet.GetCells().Get(u"B2").GetValue());
    chart.GetValueAxis().SetMaxValue(worksheet.GetCells().Get(u"D6").GetValue());

    // Set the PlotArea with no fill
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Show the DataLabels
    chart.GetNSeries().Get(1).GetDataLabels().SetShowValue(true);

    // Disable the Legend
    chart.SetShowLegend(false);

    // Save the result
    workbook.Save(u"result.xlsx");

    Aspose::Cells::Cleanup();
}
```

{{< app/cells/assistant language="cpp" >}}
