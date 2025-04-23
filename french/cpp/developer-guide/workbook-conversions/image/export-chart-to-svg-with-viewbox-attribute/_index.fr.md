---
title: Exporter un graphique au format SVG avec l’attribut viewBox en utilisant C++
linktitle: Exporter le graphique en SVG avec l attribut viewBox
type: docs
weight: 280
url: /fr/cpp/export-chart-to-svg-with-viewbox-attribute/
description: Exporter un graphique au format SVG avec l’attribut viewBox en utilisant Aspose.Cells avec C++.
---

{{% alert color="primary" %}}

Par défaut, lorsque le graphique est exporté au format SVG, l'attribut **viewBox** n'est pas inclus dans son XML. Cependant, Aspose.Cells fournit la propriété [**ImageOrPrintOptions.GetSVGFitToViewPort()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getsvgfittoviewport/) qui, lorsqu'elle est définie sur **true**, exporte le graphique en SVG avec l'attribut viewBox.

{{% /alert %}}

## Exporter le graphique en SVG avec l'attribut viewBox

Le code d'exemple suivant exporte le graphique au format SVG avec l'attribut viewBox.

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

Si vous ouvrez le SVG du graphique dans le bloc-notes, vous trouverez l'attribut **viewBox** similaire à ceci.

{{< highlight java >}}

 <svg xmlns="http://www.w3.org/2000/svg"

     xmlns:xlink="http://www.w3.org/1999/xlink"

     width="100%" height="100%"

     viewBox="0 0 480 288">

{{< /highlight >}}

{{% /alert %}}
