---
title: Drei Methoden zum Filtern von Diagrammdaten mit C++
linktitle: Drei Methoden zum Filtern von Diagrammdaten
description: Erfahren Sie, wie Sie Diagramme in Excel mit Aspose.Cells for C++ filtern. Unser umfassender Leitfaden zeigt, wie Filter auf Diagramme angewandt, Diagrammelemente angepasst und Datenanalyse Tools für bessere Einblicke und fundierte Entscheidungen verwendet werden.
keywords: Aspose.Cells for C++, Diagramme in Excel filtern, Datenanalyse, Entscheidungsfindung, Visualisierung.
type: docs
weight: 2210
url: /de/cpp/filtering-charts-in-excel/
---


## **1. Herausfiltern von Reihen, um ein Diagramm zu rendern**

### **Schritte zum Filtern von Reihen aus einem Diagramm in Excel**
In Excel können wir bestimmte Serien aus einem Diagramm herausfiltern, sodass diese gefilterten Serien im Diagramm nicht angezeigt werden. Das Originaldiagramm ist in **Abbildung 1** dargestellt. Wenn wir jedoch **Testseries2** und **Testseries4** herausfiltern, erscheint das Diagramm wie in **Abbildung 2**.

In Aspose.Cells können wir eine ähnliche Operation durchführen. Für eine [Beispieldatei](seriesFiltered.xlsx) wie diese, wenn wir **Testseries2** und **Testseries4** filtern wollen, führen wir den folgenden Code aus. Außerdem verwalten wir zwei Listen: eine ([GetNSeries()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getnseries/)), um alle ausgewählten Serien zu speichern, und eine ([GetFilteredNSeries](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getfilterednseries/)), um die gefilterten Serien zu speichern.

Bitte **beachten** Sie, dass im Code, wenn wir **chart->GetNSeries()->Get(0)->SetIsFiltered(true);** setzen, die erste Serie in [GetNSeries()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getnseries/) entfernt wird und an der entsprechenden Stelle in [GetFilteredNSeries](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getfilterednseries/) eingefügt wird. Danach wird das vorherige **NSeries[1]** das neue erste Element in der Liste, und alle folgenden Serien verschieben sich um eine Position. Das bedeutet, wenn wir dann **chart->GetNSeries()->Get(1)->SetIsFiltered(true);** ausführen, wird die ursprüngliche dritte Serie entfernt. Dieser Vorgang kann manchmal verwirrend sein, daher empfehlen wir, die Operation im Code zu befolgen, die Serien vom Ende zum Anfang löscht.

![todo:image_alt_text](Figure1.png)

![todo:image_alt_text](Figure2.png)

### **Beispielcode**
Der folgende Beispielcode lädt die [Beispieldatei Excel](seriesFiltered.xlsx).

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of existing Workbook
    Workbook workbook(u"seriesFiltered.xlsx");

    // Get filtered series list
    SeriesCollection nSeriesFiltered = workbook.GetWorksheets().Get(0).GetCharts().Get(u"Chart 1").GetFilteredNSeries();

    // Get selected series list
    SeriesCollection nSeries = workbook.GetWorksheets().Get(0).GetCharts().Get(u"Chart 1").GetNSeries();

    // Should be 0
    std::cout << "Filtered Series count: " << nSeriesFiltered.GetCount() << std::endl;

    // Should be 6
    std::cout << "Visible Series count: " << nSeries.GetCount() << std::endl;

    // Process from the end to the beginning
    nSeries.Get(1).SetIsFiltered(true);
    nSeries.Get(0).SetIsFiltered(true);

    // Should be 2
    std::cout << "Filtered Series count: " << nSeriesFiltered.GetCount() << std::endl;

    // Should be 4
    std::cout << "Visible Series count: " << nSeries.GetCount() << std::endl;

    // Save the workbook
    workbook.Save(u"seriesFiltered-out.xlsx");

    // Reload the workbook
    workbook = Workbook(u"seriesFiltered-out.xlsx");

    // Should be 2
    std::cout << "Filtered Series count: " << nSeriesFiltered.GetCount() << std::endl;

    // Should be 4
    std::cout << "Visible Series count: " << nSeries.GetCount() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **2. Filtern Sie die Daten und lassen Sie das Diagramm sich ändern**

Das Filtern Ihrer Daten ist eine großartige Möglichkeit, mit Diagrammfiltern bei großen Datenmengen umzugehen. Wenn Sie die Daten filtern, ändert sich das Diagramm. Ein Problem, das wir lösen müssen, ist sicherzustellen, dass das Diagramm auf dem Bildschirm bleibt. Beim Filtern werden versteckte Zeilen angezeigt, und manchmal befindet sich das Diagramm in diesen versteckten Zeilen.

![todo:image_alt_text](Figure3.png)

### **Schritte zum Verwenden von Datenfiltern zum Ändern des Diagramms in Excel**

1. Klicken Sie innerhalb Ihres Datenbereichs.
2. Klicken Sie auf die Registerkarte **Daten** und aktivieren Sie Filter, indem Sie auf Filter klicken. Ihre Kopfzeile wird Dropdown-Pfeile haben.
3. Erstellen Sie ein Diagramm, indem Sie zum **Einfügen**-Tab gehen und ein Säulendiagramm auswählen.
4. Filtern Sie nun Ihre Daten mithilfe der Dropdown-Pfeile in den Daten. Verwenden Sie nicht die Diagrammfilter.

### **Beispielcode**
Der folgende Beispielcode zeigt die gleiche Funktion mit Aspose.Cells.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main() {
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook;

    // Get the First sheet.
    Worksheet sheet = workbook.GetWorksheets().Get(u"Sheet1");

    // Add data into details cells.
    sheet.GetCells().Get(0, 0).PutValue(u"Fruits Name");
    sheet.GetCells().Get(0, 1).PutValue(u"Fruits Price");
    sheet.GetCells().Get(1, 0).PutValue(u"Apples");
    sheet.GetCells().Get(2, 0).PutValue(u"Bananas");
    sheet.GetCells().Get(3, 0).PutValue(u"Grapes");
    sheet.GetCells().Get(4, 0).PutValue(u"Oranges");
    sheet.GetCells().Get(1, 1).PutValue(5);
    sheet.GetCells().Get(2, 1).PutValue(2);
    sheet.GetCells().Get(3, 1).PutValue(1);
    sheet.GetCells().Get(4, 1).PutValue(4);

    // Add a chart to the worksheet
    int chartIndex = sheet.GetCharts().Add(ChartType::Column, 7, 7, 15, 15);

    // Access the instance of the newly added chart
    Chart chart = sheet.GetCharts().Get(chartIndex);

    // Set data range
    chart.SetChartDataRange(u"A1:B5", true);

    // Set AutoFilter range
    sheet.GetAutoFilter().SetRange(u"A1:B5");

    // Add filters for a filter column.
    sheet.GetAutoFilter().AddFilter(0, u"Bananas");
    sheet.GetAutoFilter().AddFilter(0, u"Oranges");

    // Apply the filters
    sheet.GetAutoFilter().Refresh();

    // Save the chart as an image
    chart.ToImage(u"Autofilter.png");

    // Save the workbook
    workbook.Save(u"Autofilter.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **3. Filtern Sie die Daten mithilfe einer Tabelle und lassen Sie das Diagramm sich ändern.**

Die Verwendung einer Tabelle ist ähnlich wie Methode 2, die Verwendung eines Bereichs, aber Sie haben mit Tabellen Vorteile gegenüber Bereichen. Wenn Sie Ihren Bereich in eine Tabelle ändern und Daten hinzufügen, wird das Diagramm automatisch aktualisiert. Mit einem Bereich müssten Sie die Datenquelle ändern.

### **Als Tabelle formatieren in Excel**

Klicken Sie in Ihre Daten und verwenden Sie **STRG + T** oder gehen Sie zum Register **Start**, **Als Tabelle formatieren**

![todo:image_alt_text](Figure4.png)

### **Beispielcode**
Der folgende Beispielcode lädt die [Beispiel Excel-Datei](TableFilters.xlsx) und zeigt die gleiche Funktion mit Aspose.Cells.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Tables;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook
    Workbook workbook(u"TableFilters.xlsx");

    // Access first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Access the instance of the newly added chart
    int chartIndex = sheet.GetCharts().Add(ChartType::Column, 7, 7, 15, 15);
    Chart chart = sheet.GetCharts().Get(chartIndex);

    // Set data range
    chart.SetChartDataRange(u"A1:B7", true);

    // Convert the chart to image
    chart.ToImage(u"TableFilters.before.png");

    // Add a new List Object to the worksheet
    ListObject listObject = sheet.GetListObjects().Get(sheet.GetListObjects().Add(u"A1", u"B7", true));

    // Add default style to the table
    listObject.SetTableStyleType(TableStyleType::TableStyleMedium10);

    // Show Total
    listObject.SetShowTotals(false);

    // Add filters for a filter column
    listObject.GetAutoFilter().AddFilter(0, u"James");

    // Apply the filters
    listObject.GetAutoFilter().Refresh();

    // After adding new value the chart will change
    listObject.PutCellValue(7, 0, Object(u"Me"));
    listObject.PutCellValue(7, 1, Object(1000));

    // Check the changed images
    chart.ToImage(u"TableFilters.after.png");

    // Saving the Excel file
    workbook.Save(u"TableFilter.out.xlsx");

    Aspose::Cells::Cleanup();
}
```
