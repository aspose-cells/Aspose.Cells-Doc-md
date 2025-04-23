---
title: Exportar gráfico a SVG con atributo viewBox usando C++
linktitle: Exportar gráfico a SVG con el atributo viewBox
type: docs
weight: 280
url: /es/cpp/export-chart-to-svg-with-viewbox-attribute/
description: Exportar un gráfico a formato SVG con atributo viewBox usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

De forma predeterminada, cuando el gráfico se exporta al formato SVG, el atributo **viewBox** no se incluye en su XML. Sin embargo, Aspose.Cells proporciona la propiedad [**ImageOrPrintOptions.GetSVGFitToViewPort()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getsvgfittoviewport/) que, cuando se establece en **true**, exporta el gráfico a SVG con el atributo viewBox.

{{% /alert %}}

## Exportar gráfico a SVG con el atributo viewBox

El siguiente código de ejemplo exporta el gráfico al formato SVG con el atributo viewBox.

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

Si abres el SVG del gráfico en el bloc de notas, encontrarás el atributo **viewBox** similar a este:

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
