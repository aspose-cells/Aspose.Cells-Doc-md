---
title: Export Chart to SVG with viewBox attribute using C++
linktitle: Export Chart to SVG with viewBox attribute
type: docs
weight: 280
url: /cpp/export-chart-to-svg-with-viewbox-attribute/
description: Export a chart to SVG format with viewBox attribute using Aspose.Cells with C++.
---

{{% alert color="primary" %}}

By default, when the chart is exported to SVG format, the **viewBox** attribute is not included in its XML. However, Aspose.Cells provides [**ImageOrPrintOptions.SVGFitToViewPort**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/svgfittoviewport/) property which when set to **true** exports the chart to SVG with viewBox attribute.

{{% /alert %}}

## Export Chart to SVG with viewBox attribute

The following sample code exports the chart to SVG format with the viewBox attribute.

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

If you open the chart's SVG in notepad, you will find the **viewBox** attribute similar to this.

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}