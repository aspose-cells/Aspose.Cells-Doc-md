---
title: Exportieren Sie ein Diagramm mit viewBox Attribut in SVG mit C++
linktitle: Diagramm als SVG mit viewBox Attribut exportieren
type: docs
weight: 280
url: /de/cpp/export-chart-to-svg-with-viewbox-attribute/
description: Exportieren Sie ein Diagramm mit viewBox Attribut im SVG Format mit Aspose.Cells in C++.
---

{{% alert color="primary" %}}

Standardmäßig ist das **viewBox**-Attribut beim Export des Diagramms ins SVG-Format nicht in seinem XML enthalten. Allerdings bietet Aspose.Cells [**ImageOrPrintOptions.GetSVGFitToViewPort()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getsvgfittoviewport/) Eigenschaft, die beim Einstellen auf **true** das Diagramm ins SVG mit viewBox-Attribut exportiert.

{{% /alert %}}

## Diagramm als SVG mit viewBox-Attribut Exportieren

Der folgende Beispielcode exportiert das Diagramm im SVG-Format mit dem viewBox-Attribut.

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

Wenn Sie das SVG des Diagramms in Notepad öffnen, finden Sie das **viewBox**-Attribut ähnlich wie dieses.

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
