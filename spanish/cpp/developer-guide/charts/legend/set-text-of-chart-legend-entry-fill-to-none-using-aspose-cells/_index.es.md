---
title: Establecer Texto de la Entrada de la Leyenda del Gráfico a Ninguno con C++
linktitle: Establecer Texto de la Entrada de la Leyenda del Gráfico a Ninguno
description: Aprenda a usar Aspose.Cells for C++ para establecer el texto de la entrada de la leyenda del gráfico a ninguno. Nuestra guía demostrará cómo modificar el color de relleno de las entradas de la leyenda en los gráficos de Microsoft Excel para mejor visualización y personalización.
keywords: Aspose.Cells for C++, Entrada de leyenda de gráfico, Microsoft Excel, Visualización, Personalización.
type: docs
weight: 320
url: /es/cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/
---

{{% alert color="primary" %}}

Si desea establecer el texto del relleno de la entrada de leyenda del gráfico en ninguno para que no se muestre dentro de la leyenda del gráfico, establezca el [**LegendEntry.IsTextNoFill**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/legendentry/istextnofill/) en **verdadero**.

{{% /alert %}}

El siguiente código de muestra establece el texto del relleno de la segunda entrada de leyenda del gráfico en ninguno. Descargue el [archivo de Excel de muestra](5115219.xlsx) utilizado en este código y el [archivo de Excel de salida](5115217.xlsx) generado por él para su referencia.

La siguiente captura de pantalla destaca el efecto de este código en el [archivo de Excel de muestra](5115219.xlsx).

![todo:image_alt_text](set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells_1.png)

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

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Sample.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"ChartLegendEntry_out.xlsx";

    // Open the template file
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Access the first chart inside the sheet
    Chart chart = sheet.GetCharts().Get(0);

    // Set text of second legend entry fill to none
    chart.GetLegend().GetLegendEntries().Get(1).SetIsTextNoFill(true);

    // Save the workbook in xlsx format
    workbook.Save(outputFilePath, SaveFormat::Xlsx);

    std::cout << "Chart legend entry modified successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
