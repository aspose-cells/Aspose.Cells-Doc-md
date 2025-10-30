---
title: Ställ in texten för diagramlegendens fält till None med C++
linktitle: Ställ in texten för diagramlegendens fält till None
description: Lär dig hur du använder Aspose.Cells for C++ för att ställa in texten för ett diagramlegenden fält till ingen. Vår guide visar hur man ändrar fyllfärgen på legendsfält i Microsoft Excel diagram för bättre visualisering och anpassning.
keywords: Aspose.Cells for C++, Diagramlegendens fält, Microsoft Excel, Visualisering, Anpassning.
type: docs
weight: 320
url: /sv/cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/
---

{{% alert color="primary" %}}

Om du vill ställa in texten för diagrammets legendpostfyllnad till none så att den inte ska visas i diagrammets legend, ställ in [**LegendEntry.IsTextNoFill**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/legendentry/istextnofill/) till **true**.

{{% /alert %}}

Följande exempelkod ställer in texten för diagrammets andra legendpostfyllnad till none. Vänligen ladda ner den [exempelfil för Excel](5115219.xlsx) som används i denna kod och den [utfärdade Excelfilen](5115217.xlsx) som genererats av den som referens.

Följande skärmdump belyser effekten av denna kod på [exempelfilen för Excel](5115219.xlsx).

![todo:image_alt_text](set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells_1.png)

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Sample.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"ChartLegendEntry_out.xlsx";

    // Open the template file
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Access the first chart inside the sheet
    Chart chart = sheet.GetCharts().Get(0);

    // Set text of second legend entry fill to none
    chart.GetLegend().GetLegendEntries().Get(1).SetIsTextNoFill(true);

    // Save the workbook in xlsx format
    workbook.Save(outputFilePath, SaveFormat::Xlsx);

    std::cout << "Chart legend entry modified successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
