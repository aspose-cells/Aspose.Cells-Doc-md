---
title: Desactivar ajuste de línea de texto para etiquetas de datos del gráfico con C++
linktitle: Desactivar ajuste de línea de texto
description: Aprende cómo desactivar el ajuste de línea de texto para las etiquetas de datos en gráficos usando Aspose.Cells for C++. Nuestra guía te mostrará cómo evitar que las etiquetas largas se superpongan y ofrecer gráficos más legibles y claros.
keywords: Aspose.Cells for C++, graficación, etiquetas de datos, ajuste de texto, superposición, legibilidad, pantallas.
type: docs
weight: 70
url: /es/cpp/disable-text-wrapping-for-data-labels-of-the-chart/
---

{{% alert color="primary" %}}

Microsoft Excel 2013 permite a los usuarios ajustar o desajustar el texto dentro de las etiquetas de datos del gráfico. De forma predeterminada, el texto dentro de las etiquetas de datos del gráfico está en estado desajustado.

Aspose.Cells proporciona una propiedad [**DataLabels.IsTextWrapped**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/istextwrapped/) que se puede establecer en Verdadero o Falso para habilitar o deshabilitar el ajuste de texto de las etiquetas de datos, respectivamente.

{{% /alert %}}

El siguiente ejemplo de código muestra cómo deshabilitar el ajuste de texto para las etiquetas de datos del gráfico.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"Output_out.xlsx";

    // Load the sample Excel file inside the workbook object
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first chart inside the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Disable the Text Wrapping of Data Labels in all Series
    chart.GetNSeries().Get(0).GetDataLabels().SetIsTextWrapped(false);
    chart.GetNSeries().Get(1).GetDataLabels().SetIsTextWrapped(false);
    chart.GetNSeries().Get(2).GetDataLabels().SetIsTextWrapped(false);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Text wrapping disabled successfully in data labels!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
