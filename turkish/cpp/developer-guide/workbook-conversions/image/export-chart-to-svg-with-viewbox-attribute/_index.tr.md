---
title: Görüntüleme Alanı özniteliğiyle SVG ye Grafik Dışa Aktarma (C++)
linktitle: viewBox özniteliği ile SVG ye Grafik Dışa Aktarma
type: docs
weight: 280
url: /tr/cpp/export-chart-to-svg-with-viewbox-attribute/
description: Aspose.Cells kullanarak bir grafikizi viewBox özniteliğiyle SVG formatına dışa aktarın.
---

{{% alert color="primary" %}}

Varsayılan olarak, grafik SVG biçimine dışa aktarıldığında, **viewBox** özniteliği içinde yer almaz. Ancak, Aspose.Cells, **true** olarak ayarlandığında grafiği viewBox özniteliği ile SVG'ye dışa aktarır.

{{% /alert %}}

## viewBox Özniteliği ile SVG'ye Grafik Dışa Aktarma

Aşağıdaki örnek kod, grafiği viewBox özniteliği ile SVG biçiminde dışa aktarır.

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

Grafiğin SVG'sini not defterinde açarsanız, benzer bir **viewBox** özniteliği bulacaksınız.

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
