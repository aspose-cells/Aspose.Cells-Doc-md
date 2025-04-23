---
title: Encuentra el tipo de valores X e Y de puntos en la serie del gráfico con C++
linktitle: Encontrar el tipo de valores X e Y de los puntos en la serie del gráfico
description: Aprende cómo determinar el tipo de valores de X e Y en los puntos de la serie del gráfico usando Aspose.Cells for C++. Nuestra guía explicará los diferentes tipos de valores de datos y cómo acceder y trabajar con ellos en tus gráficos.
keywords: Aspose.Cells for C++, graficación, valores X, valores Y, tipos de datos, acceder, trabajar con, serie del gráfico.
type: docs
weight: 150
url: /es/cpp/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **Escenarios de uso posibles**
A veces, quieres saber el tipo de valores de X e Y de los puntos del gráfico en una serie. Aspose.Cells ofrece los métodos `ChartPoint::get_XValueType` y `ChartPoint::get_YValueType` que se pueden usar para esto. Ten en cuenta que primero debes llamar a `Chart::Calculate()` antes de usar estas propiedades eficazmente.

## **Encontrar el tipo de valores X e Y de los puntos en la serie del gráfico**
 El siguiente código de ejemplo carga el [archivo Excel de muestra](64716905.xlsx) y accede al primer gráfico dentro de la primera hoja de cálculo. Luego llama al método `Chart::Calculate()` y encuentra el tipo de valores X y Y del primer punto de la serie del gráfico y los imprime en la consola. Consulta la salida de la consola mostrada abajo como referencia.

## **Código de muestra**
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

    // Load sample Excel file containing chart
    Workbook wb(srcDir + u"sampleFindTypeOfXandYValuesOfPointsInChartSeries.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first chart
    Chart ch = ws.GetCharts().Get(0);

    // Calculate chart data
    ch.Calculate();

    // Access first chart point in the first series
    ChartPoint pnt = ch.GetNSeries().Get(0).GetPoints().Get(0);

    // Print the types of X and Y values of chart point
    std::cout << "X Value Type: " << static_cast<int>(pnt.GetXValueType()) << std::endl;
    std::cout << "Y Value Type: " << static_cast<int>(pnt.GetYValueType()) << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Salida de la consola**

{{< highlight java >}}

X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
