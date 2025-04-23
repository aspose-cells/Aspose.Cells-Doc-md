---
title: Obtener texto de ecuación de la línea de tendencia del gráfico con C++
linktitle: Líneas de tendencia
description: Aprenda cómo usar Aspose.Cells for C++ para recuperar el texto de la ecuación de una línea de tendencia en un gráfico creado en Microsoft Excel. Nuestra guía demostrará cómo acceder y extraer la ecuación de una línea de tendencia para análisis o visualización posterior.
keywords: Aspose.Cells for C++, Línea de tendencia del gráfico, Texto de ecuación, Microsoft Excel, Análisis de datos, Visualización.
type: docs
weight: 110
url: /es/cpp/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

Puede recuperar el Texto de la Ecuación de la Línea de Tendencia del Gráfico utilizando Aspose.Cells. Aspose.Cells proporciona la propiedad [**Trendline.GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/gettext/) que devuelve el Texto de la Ecuación de la línea de tendencia del gráfico. Para hacer uso de esta propiedad, primero deberá llamar al método [**Chart.Calculate()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/calculate/).

{{% /alert %}}

La siguiente captura muestra el gráfico con una línea de tendencia y su texto de ecuación en color rojo. Nosotros recuperaremos este texto usando la propiedad [**Trendline.GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/gettext/) en el siguiente ejemplo de código.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## Código C++ para obtener el texto de la ecuación de la línea de tendencia del gráfico

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook object from source Excel file
    Workbook workbook(srcDir + u"source.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first chart inside the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Calculate the Chart first to get the Equation Text of Trendline
    chart.Calculate();

    // Access the Trendline
    Trendline trendLine = chart.GetNSeries().Get(0).GetTrendLines().Get(0);

    // Read the Equation Text of Trendline
    std::cout << "Equation Text: " << trendLine.GetDataLabels().GetText().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

Resultado generado por el código de ejemplo

Este es el resultado de consola del código de ejemplo anterior.

{{< highlight java >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
