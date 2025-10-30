---
title: Cambiar la dirección de las etiquetas de las marcas de tic con C++
linktitle: Cambiar la dirección de la etiqueta del eje
description: Aprende cómo cambiar la dirección de las etiquetas de las marcas de tic en Aspose.Cells for C++. Nuestra guía te ayudará a entender cómo ajustar la orientación de las etiquetas de las marcas de tic en los ejes, incluyendo orientaciones horizontales, verticales y inclinadas.
keywords: Aspose.Cells for C++, etiquetas de marcas de tic, dirección, orientación, ejes, horizontal, vertical, inclinada.
type: docs
weight: 170
url: /es/cpp/change-tick-label-direction/
---

## **Cambiar la dirección de la etiqueta del eje**

Aspose.Cells te permite cambiar la dirección de las etiquetas de marcas en el gráfico usando la propiedad [**TickLabels.GetDirectionType()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/ticklabels/getdirectiontype/). La propiedad [**TickLabels.GetDirectionType()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/ticklabels/getdirectiontype/) acepta el valor de enumeración [**ChartTextDirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextdirectiontype). La enumeración [**ChartTextDirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextdirectiontype) proporciona los siguientes miembros:

- Horizontal
- Vertical
- Rotar 90
- Rotar 270
- Apilado

 La siguiente imagen compara los archivos fuente y de salida:

### **Imagen del archivo de origen**

![todo:image_alt_text](change-tick-label-direction_1.jpg)

### **Imagen del archivo de salida**

![todo:image_alt_text](change-tick-label-direction_2.jpg)

El siguiente fragmento de código cambia la dirección de las etiquetas de las marcas de verificación de Rotar90 a Horizontal.

## **Código de muestra**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Directory source and output paths
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook and load the sample Excel file
    Workbook workbook(sourceDir + u"SampleChangeTickLabelDirection.xlsx");

    // Obtain the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Load the chart from the source worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Set the category axis tick labels direction to Horizontal
    chart.GetCategoryAxis().GetTickLabels().SetDirectionType(ChartTextDirectionType::Horizontal);

    // Output the modified workbook to a new file
    workbook.Save(outDir + u"outputChangeChartDataLableDirection.xlsx");

    std::cout << "Chart tick label direction changed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Los archivos de origen y de salida se pueden descargar desde los siguientes enlaces.

[Archivo de origen](105480221.xlsx)

[Archivo de salida](105480223.xlsx)
{{< app/cells/assistant language="cpp" >}}
