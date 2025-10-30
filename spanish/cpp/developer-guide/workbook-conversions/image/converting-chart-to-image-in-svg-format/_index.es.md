---
title: Convertir gráfico a imagen en formato SVG con C++
linktitle: Conversión de gráfico a imagen en formato SVG
type: docs
weight: 240
url: /es/cpp/converting-chart-to-image-in-svg-format/
description: Aprenda cómo convertir gráficos en imágenes SVG usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Scalable Vector Graphics (SVG) es un formato de imagen vectorial en XML para gráficos bidimensionales que también admite interactividad y animación. La especificación SVG es un estándar abierto desarrollado por el World Wide Web Consortium (W3C) desde 1999.

Las imágenes SVG y sus comportamientos se definen en archivos de texto XML. Esto significa que pueden ser buscados, indexados, escritos en script y comprimidos. Como archivos XML, las imágenes SVG pueden ser creadas y editadas con cualquier editor de texto, pero más a menudo se crean con software de dibujo.

Aspose.Cells puede guardar gráficos en imágenes en diversos formatos como BMP, JPEG, PNG, GIF, SVG, etc. Este artículo explica cómo guardar un gráfico en formato SVG.

{{% /alert %}}

El siguiente código de ejemplo explica cómo usar Aspose.Cells para convertir un gráfico en una imagen en formato SVG. El código carga el archivo de Microsoft Excel fuente y luego guarda el primer gráfico encontrado en la primera hoja de cálculo como SVG.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"SampleChartBook.xlsx";

    // Create workbook object from source file
    Workbook workbook(inputFilePath);

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first chart inside the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Set image or print options
    ImageOrPrintOptions opts;
    opts.SetImageType(Aspose::Cells::Drawing::ImageType::Svg);

    // Save the chart to svg format
    chart.ToImage(outDir + u"Image_out.svg", opts);

    std::cout << "Chart saved to SVG format successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
