---
title: Datenquelle für das Diagramm mit C++ festlegen
linktitle: Datenquelle
type: docs
weight: 10
url: /de/cpp/data-formatting-in-charts/
description: Erfahren Sie mehr über die verschiedenen Datenquellen, die von Aspose.Cells for C++ unterstützt werden. Unser Leitfaden führt Sie durch die verfügbaren Datentypen und zeigt, wie Sie eine Verbindung herstellen und Daten daraus abrufen, um Ihre Arbeitsblätter zu füllen.
keywords: Aspose.Cells for C++, Diagrammerstellung, Datenformatierung, Labels, Farben, Schriftarten, Erscheinungsbild, Benutzerfreundlichkeit.
---

In unseren vorherigen Themen haben wir bereits viele Beispiele gezeigt, um zu demonstrieren, wie Sie eine Datenquelle für Ihr Diagramm festlegen können. In diesem Thema werden wir weitere Details zu den Arten von Daten bereitstellen, die für ein Diagramm festgelegt werden können.

## **Festlegen von Diagrammdaten**

Es gibt zwei Arten von Daten, mit denen Sie beim Arbeiten an Diagrammen mit Aspose.Cells umgehen können:

- Diagrammdaten.
- Kategoriedaten.

### **Diagrammdaten**

Diagrammdaten sind die Daten, die wir als Datenquelle für unsere Diagramme verwenden. Wir können einen Bereich der Zellen (die Diagrammdaten enthalten) hinzufügen, indem wir die [**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/)-Methode des Objekts [**Add**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/add/) aufrufen.

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

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Excel object
    int sheetIndex = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Adding sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(170);
    worksheet.GetCells().Get(u"A4").PutValue(300);
    worksheet.GetCells().Get(u"B1").PutValue(160);
    worksheet.GetCells().Get(u"B2").PutValue(32);
    worksheet.GetCells().Get(u"B3").PutValue(50);
    worksheet.GetCells().Get(u"B4").PutValue(40);

    // Adding sample values to cells as category data
    worksheet.GetCells().Get(u"C1").PutValue(u"Q1");
    worksheet.GetCells().Get(u"C2").PutValue(u"Q2");
    worksheet.GetCells().Get(u"C3").PutValue(u"Y1");
    worksheet.GetCells().Get(u"C4").PutValue(u"Y2");

    // Adding a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Accessing the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
    chart.GetNSeries().Add(u"A1:B4", true);

    // Saving the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "Chart added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Kategoriedaten**

Kategoriedaten werden zur Beschriftung von Diagrammdaten verwendet und können [**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/) mithilfe seiner [**GetCategoryData()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/getcategorydata/)-Eigenschaft hinzugefügt werden. Ein vollständiges Beispiel ist unten gegeben, um die Verwendung von Diagramm- und Kategoriedaten zu demonstrieren. Nach Ausführung des obigen Beispielcodes wird ein Säulendiagramm zu dem Arbeitsblatt hinzugefügt, wie unten gezeigt.

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

    // Get the reference of the newly added worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(10);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(170);
    worksheet.GetCells().Get(u"A4").PutValue(200);
    worksheet.GetCells().Get(u"B1").PutValue(120);
    worksheet.GetCells().Get(u"B2").PutValue(320);
    worksheet.GetCells().Get(u"B3").PutValue(50);
    worksheet.GetCells().Get(u"B4").PutValue(40);

    // Add sample values to cells as category data
    worksheet.GetCells().Get(u"C1").PutValue(u"Q1");
    worksheet.GetCells().Get(u"C2").PutValue(u"Q2");
    worksheet.GetCells().Get(u"C3").PutValue(u"Y1");
    worksheet.GetCells().Get(u"C4").PutValue(u"Y2");

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Access the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Add SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
    chart.GetNSeries().Add(u"A1:B4", true);

    // Set the data source for the category data of SeriesCollection
    chart.GetNSeries().SetCategoryData(u"C1:C4");

    // Save the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "Chart added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Fortgeschrittene Themen**
- [Ändern der Datenquelle des Diagramms zur Zieltabelle beim Kopieren von Zeilen oder Bereichen](/cells/de/cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Dynamische Diagramme erstellen](/cells/de/cpp/create-dynamic-charts/)
- [Einfacher Weg zur Diagrammeinrichtung mit der Methode Chart.SetChartDataRange](/cells/de/cpp/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Typen von X- und Y-Werten von Punkten in Diagrammserien herausfinden](/cells/de/cpp/find-type-of-x-and-y-values-of-points-in-chart-series/)
{{< app/cells/assistant language="cpp" >}}
