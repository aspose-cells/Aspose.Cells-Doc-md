---
title: Cómo establecer un punto como total con C++
linktitle: Cómo establecer un punto como total
description: En algunos gráficos de Excel, por ejemplo, gráficos WaterFall, puede ser necesario establecer un punto como total. Este artículo describe cómo usar Aspose.Cells con C++ para hacerlo.
keywords: Gráfico WaterFall, Punto, Establecer como total.
type: docs
weight: 72
url: /es/cpp/how-to-set-point-as-total/
---

## ¿Qué es "Establecer punto como total" en el gráfico de Excel?

En algunos gráficos de Excel, por ejemplo, gráficos WaterFall, algunos datos de puntos son la suma de los puntos anteriores, puede que necesite "establecer el punto como total". Mostraremos el código de ejemplo y la ilustración a continuación.

## Un gráfico WaterFall necesita "Establecer punto como total" 

![todo:image_alt_text](set-as-total1.png)

Esta imagen muestra un gráfico WaterFall en Excel. Podemos ver que hay cuatro puntos de datos que comienzan con "Total", y se usan para contar todos los datos anteriores.
En esta imagen, la configuración no es exactamente correcta, cuando seleccionamos un punto "Total 2024" y podemos ver que la opción "Establecer como total" no está marcada en Excel.
Adjunto abajo está el [archivo de Excel de muestra](SampleSheet.xlsx) que necesita ser modificado, y usaremos Aspose.Cells para configurarlo correctamente.

## Usar Aspose.Cells para "Establecer punto como total" 

Usamos el siguiente código para configurar el archivo correctamente:

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Initialize file path
    U16String filePath(u"");

    // Load the workbook
    Workbook wb(filePath + u"SampleSheet.xlsx");

    // Get the first worksheet
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // Get the chart by name
    Chart chart = worksheet.GetCharts().Get(u"Graphiq5");

    // Set some points as total column
    // In this example, we set points 0, 4, 8, 12 as total
    Vector<int32_t> subtotals = {0, 4, 8, 12};
    chart.GetNSeries().Get(0).GetLayoutProperties().SetSubtotals(subtotals);

    // Save the workbook
    wb.Save(filePath + u"output.xlsx");

    std::cout << "Chart subtotals set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Puedes obtener el siguiente [archivo de salida correcto](output.xlsx)

Como se muestra en la figura a continuación, los cuatro puntos de datos "Total" están configurados correctamente, y puedes ver la diferencia respecto a la gráfica anterior.

![todo:image_alt_text](set-as-total2.png)
