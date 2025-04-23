---
title: Bild als Hintergrundfüllung im Diagramm mit C++ festlegen
linktitle: Setzen Sie ein Bild als Hintergrundfüllung im Diagramm
description: Lernen Sie, wie Sie ein Bild als Hintergrundfüllung in einem Diagramm mit Aspose.Cells for C++ festlegen. Unser Leitfaden zeigt Ihnen, wie Sie das Bild importieren und positionieren, seine Größe und Farbe anpassen und Formatierungsoptionen anwenden, um das Aussehen Ihres Diagramms zu verbessern.
keywords: Aspose.Cells for C++, Diagrammerstellung, Hintergrundfüllung, Bild, Import, Positionierung, Größe, Farbe, Formatierung.
type: docs
weight: 30
url: /de/cpp/set-picture-as-background-fill-in-the-chart/
---

{{% alert color="primary" %}}

Aspose.Cells ermöglicht es Ihnen, einen Farbverlauf, eine Textur, ein Muster oder ein Bild als Fülleffekte für verschiedene Objekte festzulegen, z.B. den Plot-Bereich, den Diagrammbereich oder die Legendenbox eines Diagramms. Dieses Dokument zeigt, wie man ein Bild zum Hintergrund eines Diagramms hinzufügt.

{{% /alert %}}

Um dies zu erreichen, bietet Aspose.Cells die Eigenschaft [**Chart.GetImageData()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/getimagedata/). Das folgende Beispiel zeigt die Verwendung der Eigenschaft [**Chart.GetImageData()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/getimagedata/), um ein Bild als Hintergrundfüllung im Diagramm festzulegen.

## C++-Code zum Festlegen des Hintergrundbilds im Diagramm

```cpp
#include <iostream>
#include <fstream>
#include <vector>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main() {
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    sheet.SetName(u"Data");

    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Region");
    cells.Get(u"A2").PutValue(u"France");
    cells.Get(u"A3").PutValue(u"Germany");
    cells.Get(u"A4").PutValue(u"England");
    cells.Get(u"A5").PutValue(u"Sweden");
    cells.Get(u"A6").PutValue(u"Italy");
    cells.Get(u"A7").PutValue(u"Spain");
    cells.Get(u"A8").PutValue(u"Portugal");
    cells.Get(u"B1").PutValue(u"Sale");
    cells.Get(u"B2").PutValue(70000);
    cells.Get(u"B3").PutValue(55000);
    cells.Get(u"B4").PutValue(30000);
    cells.Get(u"B5").PutValue(40000);
    cells.Get(u"B6").PutValue(35000);
    cells.Get(u"B7").PutValue(32000);
    cells.Get(u"B8").PutValue(10000);

    int sheetIndex = workbook.GetWorksheets().Add(SheetType::Chart);
    sheet = workbook.GetWorksheets().Get(sheetIndex);
    sheet.SetName(u"Chart");

    int chartIndex = sheet.GetCharts().Add(ChartType::Column, 1, 1, 25, 10);
    Chart chart = sheet.GetCharts().Get(chartIndex);

    std::ifstream fs((srcDir + u"aspose.png").ToUtf8(), std::ios::binary);
    std::vector<uint8_t> data((std::istreambuf_iterator<char>(fs)), std::istreambuf_iterator<char>());
    Aspose::Cells::Vector<uint8_t> asposeData(data.data(), data.size());

    chart.GetPlotArea().GetArea().GetFillFormat().SetImageData(asposeData);
    chart.GetPlotArea().GetBorder().SetIsVisible(false);

    chart.GetTitle().SetText(u"Sales By Region");
    chart.GetTitle().GetFont().SetColor(Color::Blue());
    chart.GetTitle().GetFont().SetIsBold(true);
    chart.GetTitle().GetFont().SetSize(12);

    chart.GetNSeries().Add(u"Data!B2:B8", true);
    chart.GetNSeries().SetCategoryData(u"Data!A2:A8");
    chart.GetNSeries().SetIsColorVaried(true);

    Legend legend = chart.GetLegend();
    legend.SetPosition(LegendPositionType::Top);

    workbook.Save(outDir + u"column_chart_out.xls");
    Aspose::Cells::Cleanup();
    return 0;
}
```
