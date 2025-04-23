---
title: Konvertera diagram till bild i SVG format med C++
linktitle: Konvertera diagram till bild i SVG format
type: docs
weight: 240
url: /sv/cpp/converting-chart-to-image-in-svg-format/
description: Lär dig hur du konverterar diagram till SVG bilder med Aspose.Cells och C++.
---

{{% alert color="primary" %}}

Scalable Vector Graphics (SVG) är ett XML-baserat vektorbildformat för tvådimensionell grafik som också stöder interaktivitet och animation. SVG-specifikationen är en öppen standard som utvecklats av World Wide Web Consortium (W3C) sedan 1999.

SVG-bilder och deras beteenden definieras i XML-textfiler. Detta innebär att de kan sökas, indexeras, skriptas och komprimeras. Som XML-filer kan SVG-bilder skapas och redigeras med vilken textredigerare som helst, men skapas oftare med ritprogram.

Aspose.Cells kan spara diagram i bilder i olika format som BMP, JPEG, PNG, GIF, SVG med flera. Den här artikeln förklarar hur man sparar ett diagram i SVG-format.

{{% /alert %}}

Följande exempelkod förklarar hur man använder Aspose.Cells för att konvertera ett diagram till en bild i SVG-format. Koden laddar den ursprungliga Microsoft Excel-filen och sparar sedan det första diagrammet som hittas på den första arbetsbladet till SVG.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"SampleChartBook.xlsx";

    // Create workbook object from source file
    Workbook workbook(inputFilePath);

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first chart inside the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Set image or print options
    ImageOrPrintOptions opts;
    opts.SetImageType(Aspose::Cells::Drawing::ImageType::Svg);

    // Save the chart to svg format
    chart.ToImage(outDir + u"Image_out.svg", opts);

    std::cout << "Chart saved to SVG format successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
