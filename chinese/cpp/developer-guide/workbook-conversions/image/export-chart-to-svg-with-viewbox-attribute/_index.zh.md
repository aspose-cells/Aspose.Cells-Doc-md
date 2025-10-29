---
title: 使用C++导出带有viewBox属性的SVG图表
linktitle: 导出带有viewBox属性的SVG图表
type: docs
weight: 280
url: /zh/cpp/export-chart-to-svg-with-viewbox-attribute/
description: 使用Aspose.Cells结合C++将带有viewBox属性的图表导出为SVG格式。
---

{{% alert color="primary" %}}

默认情况下，将图表导出为SVG格式时，其XML中不包括**viewBox**属性。但是，Aspose.Cells提供了[**ImageOrPrintOptions.GetSVGFitToViewPort()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getsvgfittoviewport/)属性，将其设置为**true**时会导出具有viewBox属性的SVG图表。

{{% /alert %}}

## 导出带有viewBox属性的SVG图表

以下示例代码将图表导出为带有viewBox属性的SVG格式。

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

如果在记事本中打开图表的SVG文件，将会找到类似于这样的**viewBox**属性。

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
