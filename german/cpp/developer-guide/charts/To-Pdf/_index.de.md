---
title: Diagramm nach PDF mit C++
linktitle: Diagramm in PDF umwandeln
description: Lernen Sie, wie Sie Aspose.Cells for C++ verwenden, um ein Diagramm in ein PDF Dokument zu konvertieren. Unser Leitfaden zeigt, wie man ein Diagramm aus Microsoft Excel exportiert und als PDF für weitere Verteilung und Archivierung speichert.
keywords: Aspose.Cells for C++, Diagramm zu PDF, Microsoft Excel, PDF Konvertierung, Export, Verteilung, Archivierung.
type: docs
weight: 47
url: /de/cpp/chart-to-pdf/
---

## **Diagramm in PDF umwandeln**

Um das Diagramm ins PDF-Format zu rendern, haben die Aspose.Cells APIs die [**Chart::ToPdf**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/topdf/)-Methode bereitgestellt, mit der das resultierende PDF auf einem Disc-Pfad oder Stream gespeichert werden kann.

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

    // Obtain the reference of the newly added worksheet by passing its index to WorksheetCollection
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(4);
    worksheet.GetCells().Get(u"B2").PutValue(20);
    worksheet.GetCells().Get(u"B3").PutValue(50);

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Access the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Add Series Collection (chart data source) to the chart ranging from "A1" cell to "B3"
    chart.GetNSeries().Add(u"A1:B3", true);

    // Convert chart to PDF
    chart.ToPdf(outDir + u"chartPDF_out.pdf");

    std::cout << "Chart converted to PDF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Erstellen Sie ein Diagramm-PDF mit gewünschter Seitengröße**
Sie können Diagramm-PDFs mit Ihrer gewünschten Seitengröße erstellen, indem Sie Aspose.Cells verwenden und angeben, wie Sie das Diagramm innerhalb der Seite ausrichten möchten, z.B. oben, unten, zentriert, links, rechts usw. Außerdem kann das Ausgabediagramm in einem Stream oder auf der Festplatte erstellt werden. Bitte sehen Sie sich den folgenden Beispielcode an, der die [Beispiel-Excel-Datei](64716906.xlsx) lädt, auf das erste Diagramm im Arbeitsblatt zugreift und es dann in ein [Ausgabepdf](64716907.pdf) mit der gewünschten Seitengröße konvertiert. Das folgende Screenshot zeigt, dass die Seitengröße im Ausgabepdf 7x7 beträgt, wie im Code angegeben, und das Diagramm sowohl horizontal als auch vertikal zentriert ausgerichtet ist.

![todo:image_alt_text](create-chart-pdf-with-desired-page-size_1.png)

## **Beispielcode**
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load sample Excel file containing the chart
    Workbook wb(srcDir + u"sampleCreateChartPDFWithDesiredPageSize.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first chart inside the worksheet
    Chart ch = ws.GetCharts().Get(0);

    // Create chart pdf with desired page size
    ch.ToPdf(outDir + u"outputCreateChartPDFWithDesiredPageSize.pdf", 7, 7, PageLayoutAlignmentType::Center, PageLayoutAlignmentType::Center);

    std::cout << "Chart PDF created successfully with desired page size!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
