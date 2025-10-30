---
title: Mostrar rango de celdas como etiquetas de datos con C++
linktitle: Mostrar rango de celdas como las etiquetas de datos
description: Aprenda cómo mostrar un rango de celdas como etiquetas de datos en gráficos usando Aspose.Cells for C++. Nuestra guía demostrará cómo vincular las etiquetas a su fuente de datos y formatearlas para proporcionar información precisa y significativa en sus gráficos.
keywords: Aspose.Cells for C++, gráficos, etiquetas de datos, rango de celdas, fuente de datos, formateo, precisión, información significativa.
type: docs
weight: 130
url: /es/cpp/showing-cell-range-as-the-data-labels/
---

{{% alert color="primary" %}}

En Microsoft Excel 2013, puedes mostrar un rango de celdas para las etiquetas de datos. Aspose.Cells es compatible con esta función.

{{% /alert %}}

## **Casilla de verificación para Mostrar rango de celdas como etiquetas de datos**

Para mostrar el rango de celdas como etiquetas de datos en Microsoft Excel:

1. Selecciona las etiquetas de datos de la serie y haz clic derecho para abrir el menú contextual.
1. Selecciona **Formato de etiquetas de datos**. Se muestran las opciones de etiquetas.
1. Selecciona o deselecciona la opción **La etiqueta contiene - Valor de las celdas**.

El código de ejemplo a continuación accede a las etiquetas de datos de una serie de gráficos y establece la propiedad [**DataLabels.GetShowCellRange()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/getshowcellrange/) como **true** para seleccionar la opción **La etiqueta contiene - Valor de las celdas**.

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
    U16String inputFilePath = srcDir + u"source.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Create workbook from the source Excel file
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the chart inside the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Check the "Label Contains - Value From Cells"
    DataLabels dataLabels = chart.GetNSeries().Get(0).GetDataLabels();
    dataLabels.SetShowCellRange(true);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
