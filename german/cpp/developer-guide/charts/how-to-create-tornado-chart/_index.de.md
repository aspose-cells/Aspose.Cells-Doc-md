---
title: Wie erstellt man ein Tornado Diagramm mit C++
linktitle: Tornado Diagramm erstellen
type: docs
weight: 73
url: /de/cpp/create-tornado-chart/
description: Erfahren Sie, wie Sie mit der API Aspose.Cells for C++ ein Tornado Diagramm erstellen.
keywords: C++ Tornado Diagramm erstellen, Tornado Diagramm hinzufügen, Tornado Diagramm einfügen
---

## **Einführung**
Ein Tornado-Diagramm, auch als Tornado-Diagramm oder Tornado-Grafik bekannt, ist eine Art der Datendarstellung, die oft für die Sensitivitätsanalyse in Excel verwendet wird. Es hilft Ihnen, den Einfluss von sich ändernden Variablen auf ein bestimmtes Ergebnis oder Resultat zu verstehen.

## **Wie man ein Tornado-Diagramm in Excel erstellt**
Sie können ein Tornado-Diagramm in Excel erstellen, indem Sie diesen Schritten folgen:
1. Wählen Sie die Daten aus und gehen Sie zu Einfügen --> Diagramme --> Säulen- oder Balkendiagramm einfügen --> Gestapeltes Balkendiagramm. Klicken Sie darauf.
<br>
<img src="1.png" width=70% />
2. Ändern Sie die Y-Achse: Klicken Sie mit der rechten Maustaste auf die y-Achse. Klicken Sie auf Achsenformat. Klicken Sie in Beschriftungen auf das Dropdown-Menü für die Position der Beschriftung und wählen Sie Niedrigstes Element aus.
<br>
<img src="2.png" width=70% />
3. Wählen Sie eine beliebige Leiste aus und gehen Sie zur Formatierung. Legen Sie einen geeigneten Abstand fest.
<br>
<img src="3.png" width=70% />
4. Entfernen wir das Minuszeichen (-) aus dem Tornado-Diagramm. Wählen Sie die x-Achse aus. Gehen Sie zur Formatierung. Klicken Sie in den Achsenoptionen auf die Nummer. Wählen Sie in der Kategorie Benutzerdefiniert aus. Im Formatcode schreiben Sie ###0,###0. Klicken Sie auf Hinzufügen.
<br>
<img src="4.png" width=70% />
5. Klicken Sie auf die y-Achse und gehen Sie zu den Achsenoptionen. In den Achsenoptionen aktivieren Sie Kategorien in umgekehrter Reihenfolge.
<br>
<img src="5.png" width=70% />

## **Wie man ein Tornado-Diagramm in Aspose.Cells hinzufügt**
Bitte sehen Sie sich den folgenden Beispielcode an. Es lädt die [Beispieldatei Excel](sample.xlsx), die einige Beispieldaten enthält. Danach erstellt es das gestapelte Balkendiagramm basierend auf den Anfangsdaten und setzt relevante Eigenschaften. Schließlich speichert es die Arbeitsmappe im [Ausgabe-XLSX-Format](out.xlsx). Der folgende Screenshot zeigt das von Aspose.Cells erstellte Tornado-Diagramm in der Ausgabe-Excel-Datei.
<br>
<img src="6.png" width=70% />

### **Beispielcode**

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"out.xlsx";

    // Create workbook
    Workbook wb(inputFilePath);

    // Get the first worksheet
    Worksheet sheet = wb.GetWorksheets().Get(0);

    // Get the chart collection from the worksheet
    ChartCollection charts = sheet.GetCharts();

    // Add a bar chart
    int index = charts.Add(ChartType::BarStacked, 8, 1, 24, 8);
    Chart chart = charts.Get(index);

    // Set data for the bar chart
    chart.SetChartDataRange(u"A1:C7", true);

    // Set properties for the bar chart
    chart.GetTitle().SetText(u"Tornado chart");
    chart.SetStyle(2);
    chart.GetPlotArea().GetArea().SetForegroundColor(Color::White());
    chart.GetPlotArea().GetBorder().SetColor(Color::White());
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Set properties for the category axis
    chart.GetCategoryAxis().SetTickLabelPosition(TickLabelPositionType::Low);
    chart.GetCategoryAxis().SetIsPlotOrderReversed(true);

    // Set gap width
    chart.SetGapWidth(10);

    // Set properties for the value axis
    Axis valueAxis = chart.GetValueAxis();
    valueAxis.GetTickLabels().SetNumberFormat(u"#,##0;#,##0");

    // Save the workbook
    wb.Save(outputFilePath);

    std::cout << "Chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
