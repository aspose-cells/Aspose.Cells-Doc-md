---
title: Exportera diagram till SVG med viewBox atribut med C++
linktitle: Exportera diagram till SVG med viewBox attribut
type: docs
weight: 280
url: /sv/cpp/export-chart-to-svg-with-viewbox-attribute/
description: Exportera ett diagram till SVG format med viewBox atribut med Aspose.Cells och C++.
---

{{% alert color="primary" %}}

Som standard, när diagrammet exporteras till SVG-format, ingår inte attributet **viewBox** i dess XML. Men Aspose.Cells tillhandahåller [**ImageOrPrintOptions.GetSVGFitToViewPort()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getsvgfittoviewport/)-egenskapen som när den är inställd på **true** exporterar diagrammet till SVG med viewBox-attributen.

{{% /alert %}}

## Exportera diagram till SVG med viewBox-attribut

Följande kodexempel exporterar diagrammet till SVG-format med viewBox-attributet.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook object from source file
    U16String sampleChartBook = srcDir + u"SampleChartBook.xlsx";
    Workbook workbook(sampleChartBook);

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first chart inside the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Set image or print options with SVGFitToViewPort true
    ImageOrPrintOptions opts;
    opts.SetImageType(ImageType::Svg);
    opts.SetSVGFitToViewPort(true);

    // Save the chart to svg format
    U16String outputSvg = srcDir + u"Image_out.svg";
    chart.ToImage(outputSvg, opts);

    std::cout << "Chart saved successfully in SVG format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Om du öppnar diagrammets SVG i anteckningar kommer du att hitta **viewBox** -attributet som liknar detta.

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
