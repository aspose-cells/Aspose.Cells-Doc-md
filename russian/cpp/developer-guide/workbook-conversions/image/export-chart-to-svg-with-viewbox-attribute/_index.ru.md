---
title: Экспорт диаграммы в SVG с атрибутом viewBox с использованием C++
linktitle: Экспорт диаграммы в SVG с атрибутом viewBox
type: docs
weight: 280
url: /ru/cpp/export-chart-to-svg-with-viewbox-attribute/
description: Экспортируйте диаграмму в формат SVG с атрибутом viewBox, используя Aspose.Cells и C++.
---

{{% alert color="primary" %}}

По умолчанию, когда диаграмма экспортируется в формат SVG, атрибут **viewBox** не включается в его XML. Однако Aspose.Cells предоставляет свойство [**ImageOrPrintOptions.GetSVGFitToViewPort()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getsvgfittoviewport/), которое, когда установлено в **истину**, экспортирует диаграмму в SVG с атрибутом viewBox.

{{% /alert %}}

## Экспорт диаграммы в SVG с атрибутом viewBox

В следующем образце кода диаграмма экспортируется в формат SVG с атрибутом viewBox.

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

Если вы откроете файл SVG диаграммы в блокноте, вы обнаружите атрибут **viewBox** аналогичный этому.

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
