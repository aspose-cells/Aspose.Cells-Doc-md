---
title: Esporta Grafico in SVG con attributo viewBox usando C++
linktitle: Esporta il grafico in SVG con attributo viewBox
type: docs
weight: 280
url: /it/cpp/export-chart-to-svg-with-viewbox-attribute/
description: Esporta un grafico in formato SVG con attributo viewBox usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Per impostazione predefinita, quando il grafico viene esportato nel formato SVG, l'attributo **viewBox** non è incluso nel suo XML. Tuttavia, Aspose.Cells fornisce [**ImageOrPrintOptions.GetSVGFitToViewPort()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getsvgfittoviewport/) proprietà che, quando impostata su **true**, esporta il grafico in SVG con l'attributo viewBox.

{{% /alert %}}

## Esportare il grafico in SVG con attributo viewBox

Il seguente codice di esempio esporta il grafico nel formato SVG con l'attributo viewBox.

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

Se apri l'SVG del grafico in notepad, troverai l'attributo **viewBox** simile a questo.

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
