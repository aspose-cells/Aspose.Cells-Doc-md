---
title: Titel in Excel Diagrammen mit C++ verwalten
linktitle: Titel
description: Lernen Sie, wie Sie Aspose.Cells for C++ verwenden, um Diagramm und Achsentitel in Microsoft Excel hinzuzufügen und zu formatieren. Unser Leitfaden zeigt, wie man unterschiedliche Titelformate einstellt, deren Aussehen anpasst und Achsentitel für eine bessere Datenvisualisierung und Klarheit ändert.
keywords: Aspose.Cells for C++, Diagrammtitel, Achsentitel, Microsoft Excel, Datenvisualisierung, Erscheinungsbild.
type: docs
weight: 50
url: /de/cpp/chart-and-axis-titles/
---

{{% alert color="primary" %}}

In Excel-Diagrammen gibt es 2 Arten von Titeln:
1. Diagrammtitel 
1. Achsentitel

{{% /alert %}}

## **Titeloptionen**
Aspose.Cells ermöglicht es auch, Diagrammtitel zur Laufzeit zu verwalten. Mit dem [Title](https://reference.aspose.com/cells/cpp/aspose.cells.charts/title/) -Objekt können Sie Text, Schriftart und Füllformat für Titel ändern.

|![todo:image_alt_text](chart_title.png)|

## **Einstellen der Titel von Diagrammen oder Achsen**
Sie können Microsoft Excel verwenden, um Titel für ein Diagramm und seine Achsen in einer WYSIWYG-Umgebung festzulegen. Aspose.Cells ermöglicht es Entwicklern auch, die Titel eines Diagramms und seiner Achsen zur Laufzeit zu setzen. Alle Diagramme und ihre Achsen enthalten eine [Title](https://reference.aspose.com/cells/cpp/aspose.cells.charts/title/)-Eigenschaft, mit der ihre Titel festgelegt werden können, wie im folgenden Beispiel gezeigt.

 Das folgende Code-Snippet zeigt, wie man Titel für Diagramme und Achsen festlegt.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    int sheetIndex = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Adding sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(60);
    worksheet.GetCells().Get(u"B2").PutValue(32);
    worksheet.GetCells().Get(u"B3").PutValue(50);

    // Adding a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Accessing the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
    chart.GetNSeries().Add(u"A1:B3", true);

    // Setting the foreground color of the plot area
    chart.GetPlotArea().GetArea().SetForegroundColor(Color::Blue());

    // Setting the foreground color of the chart area
    chart.GetChartArea().GetArea().SetForegroundColor(Color::Yellow());

    // Setting the foreground color of the 1st SeriesCollection area
    chart.GetNSeries().Get(0).GetArea().SetForegroundColor(Color::Red());

    // Setting the foreground color of the area of the 1st SeriesCollection point
    chart.GetNSeries().Get(0).GetPoints().Get(0).GetArea().SetForegroundColor(Color::Cyan());

    // Filling the area of the 2nd SeriesCollection with a gradient
    chart.GetNSeries().Get(1).GetArea().GetFillFormat().SetOneColorGradient(Color::Lime(), 1, GradientStyleType::Horizontal, 1);

    // Setting the title of a chart
    chart.GetTitle().SetText(u"Title");

    // Setting the font color of the chart title to blue
    chart.GetTitle().GetFont().SetColor(Color::Blue());

    // Setting the title of category axis of the chart
    chart.GetCategoryAxis().GetTitle().SetText(u"Category");

    // Setting the title of value axis of the chart
    chart.GetValueAxis().GetTitle().SetText(u"Value");

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Erweiterte Themen**
- [Diagramm-Untertitel aus ODS-Datei lesen](/cells/de/cpp/read-chart-subtitle-from-ods-file/)
