---
title: Benutzerdefinierte Slice oder Sektorfärbung in Tortendiagramm mit C++
linktitle: Benutzerdefinierte Slice oder Sektorenfarben in einem Tortendiagramm
description: Lernen Sie, wie man Aspose.Cells for C++ verwendet, um die Farben von Sektoren und Segmenten in einem Tortendiagramm anzupassen. Unser Leitfaden zeigt, wie man jeder Scheibe, jedem Sektor oder Segment eine einzigartige Farbe zuweist, um die visuelle Attraktivität und die Datenpräsentation zu verbessern.
keywords: Aspose.Cells for C++, Tortendiagramm, Benutzerdefinierte Segmentfarben, Benutzerdefinierte Sektorfarbe, Visueller Reiz, Datenpräsentation.
type: docs
weight: 60
url: /de/cpp/custom-slice-or-sector-colors-in-pie-chart/
---

{{% alert color="primary" %}}

In diesem Artikel wird erläutert, wie benutzerdefinierte Farben zu Tortendiagrammslices/Sektoren hinzugefügt werden. Standardmäßig verwenden Tortendiagramme die Microsoft Excel-Standardvorlage. Um andere Farben zu verwenden, definieren Sie die Farben im Diagramm neu.

{{% /alert %}}

Um eine benutzerdefinierte Farbe für die einzelnen Slices oder Sektoren eines Tortendiagramms festzulegen:

1. Greifen Sie auf das [**Series**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/)-Objekt's [**ChartPoint**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartpoint/) zu.
1. Weisen Sie die Farbe Ihrer Wahl mit der [**ChartPoint.GetForegroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/area/getforegroundcolor/)-Eigenschaft zu.

In diesem Artikel wird auch erläutert, wie:

- Die Kategoriedaten eines Diagramms.
- Ein Diagrammtitel, der mit einer Zelle verknüpft ist.
- Die Schriftarteinstellungen des Diagrammtitels.
- Die Position der Legende.

{{% alert color="primary" %}}

[**ChartPoint.GetForegroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/area/getforegroundcolor/) ist nicht spezifisch für Tortendiagramme, kann aber für alle Arten von Diagrammen verwendet werden.

{{% /alert %}}

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

    // Create a workbook object
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put the sample values used in a pie chart
    worksheet.GetCells().Get(u"C3").PutValue(u"India");
    worksheet.GetCells().Get(u"C4").PutValue(u"China");
    worksheet.GetCells().Get(u"C5").PutValue(u"United States");
    worksheet.GetCells().Get(u"C6").PutValue(u"Russia");
    worksheet.GetCells().Get(u"C7").PutValue(u"United Kingdom");
    worksheet.GetCells().Get(u"C8").PutValue(u"Others");

    // Put the sample values used in a pie chart
    worksheet.GetCells().Get(u"D2").PutValue(u"% of world population");
    worksheet.GetCells().Get(u"D3").PutValue(25);
    worksheet.GetCells().Get(u"D4").PutValue(30);
    worksheet.GetCells().Get(u"D5").PutValue(10);
    worksheet.GetCells().Get(u"D6").PutValue(13);
    worksheet.GetCells().Get(u"D7").PutValue(9);
    worksheet.GetCells().Get(u"D8").PutValue(13);

    // Create a pie chart with desired length and width
    int pieIdx = worksheet.GetCharts().Add(ChartType::Pie, 1, 6, 15, 14);

    // Access the pie chart
    Chart pie = worksheet.GetCharts().Get(pieIdx);

    // Set the pie chart series
    pie.GetNSeries().Add(u"D3:D8", true);

    // Set the category data
    pie.GetNSeries().SetCategoryData(u"=Sheet1!$C$3:$C$8");

    // Set the chart title that is linked to cell D2
    pie.GetTitle().SetLinkedSource(u"D2");

    // Set the legend position at the bottom
    pie.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Set the chart title's font name and color
    pie.GetTitle().GetFont().SetName(u"Calibri");
    pie.GetTitle().GetFont().SetSize(18);

    // Access the chart series
    Series srs = pie.GetNSeries().Get(0);

    // Color the individual points with custom colors
    srs.GetPoints().Get(0).GetArea().SetForegroundColor(Color{0, 246, 22, 219});
    srs.GetPoints().Get(1).GetArea().SetForegroundColor(Color{0, 51, 34, 84});
    srs.GetPoints().Get(2).GetArea().SetForegroundColor(Color{0, 46, 74, 44});
    srs.GetPoints().Get(3).GetArea().SetForegroundColor(Color{0, 19, 99, 44});
    srs.GetPoints().Get(4).GetArea().SetForegroundColor(Color{0, 208, 223, 7});
    srs.GetPoints().Get(5).GetArea().SetForegroundColor(Color{0, 222, 69, 8});

    // Autofit all columns
    worksheet.AutoFitColumns();

    // Save the workbook
    U16String outputPath = outDir + u"output.out.xlsx";
    workbook.Save(outputPath, SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
}
```
