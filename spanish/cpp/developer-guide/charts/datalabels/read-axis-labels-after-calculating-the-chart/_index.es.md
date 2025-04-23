---
title: Leer etiquetas del eje después de calcular el gráfico con C++
linktitle: Leer etiquetas del eje después de calcular el gráfico
description: Aprende cómo leer las etiquetas del eje en Aspose.Cells for C++ después de calcular el gráfico. Nuestra guía te mostrará cómo acceder y recuperar las etiquetas del eje, incluyendo su formato y posición.
keywords: Aspose.Cells for C++, gráfico, etiquetas del eje, cálculo, lectura, acceso, recuperación, formato, posición.
type: docs
weight: 90
url: /es/cpp/read-axis-labels-after-calculating-the-chart/
---

## **Escenarios de uso posibles**

Puede leer las etiquetas del eje de su gráfico después de calcular sus valores utilizando el método [**Chart.Calculate()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/calculate/). Utilice el método [**Axis.GetAxisTexts()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/axis/getaxistexts/) para este propósito, que devolverá la lista de etiquetas del eje.

## **Leer etiquetas del eje después de calcular el gráfico**

Consulte el siguiente código de ejemplo que carga el [archivo de Excel de muestra](ReadAxisLabels.xlsx) y lee las etiquetas del eje de categoría del gráfico en la primera hoja de cálculo. Luego imprime los valores de las etiquetas del eje en la consola. Consulte la salida de la consola del código de ejemplo a continuación como referencia.

## **Código de muestra**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook wb(srcDir + u"ReadAxisLabels.xlsx");

    Worksheet ws = wb.GetWorksheets().Get(0);

    Chart ch = ws.GetCharts().Get(0);

    ch.Calculate();

    Vector<U16String> lstLabels = ch.GetCategoryAxis().GetAxisTexts();

    std::wcout << L"Category Axis Labels: " << std::endl;
    std::wcout << L"---------------------" << std::endl;

    for (int32_t i = 0; i < lstLabels.GetLength(); ++i)
    {
        std::wcout << reinterpret_cast<const wchar_t*>(lstLabels[i].GetData()) << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Salida de la consola**

{{< highlight cpp >}}

 Category Axis Labels:

\---------------------

Iran

China

USA

Brazil

England

{{< /highlight >}}
