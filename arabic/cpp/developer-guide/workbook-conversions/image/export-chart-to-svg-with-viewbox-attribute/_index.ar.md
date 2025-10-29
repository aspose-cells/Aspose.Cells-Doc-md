---
title: تصدير المخطط إلى SVG مع خاصية viewBox باستخدام C++
linktitle: تصدير الرسم البياني إلى SVG مع خاصية viewBox
type: docs
weight: 280
url: /ar/cpp/export-chart-to-svg-with-viewbox-attribute/
description: تصدير مخطط إلى صيغة SVG مع خاصية viewBox باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}}

بشكل افتراضي، عند تصدير الرسم البياني إلى تنسيق SVG، لا يتم تضمين سمة **viewBox** في XML الخاص به. ومع ذلك، يوفر Aspose.Cells خاصية [**ImageOrPrintOptions.GetSVGFitToViewPort()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getsvgfittoviewport/) التي عند تعيينها على **true** يقوم بتصدير الرسم البياني إلى SVG مع سمة viewBox.

{{% /alert %}}

## تصدير الرسم البياني إلى SVG بسمة viewBox

الرمز العينة التالي يقوم بتصدير الرسم البياني إلى تنسيق SVG مع سمة viewBox.

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

إذا فتحت ملف SVG الخاص بالرسم البياني في المفكرة، فستجد سمة viewBox مماثلة لهذه.

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
