---
title: Encontrar si los puntos de datos están en la segunda rebanada o barra en un gráfico de tipo Pie of Pie o Bar of Pie con C++
linktitle: Encuentre si los Puntos de Datos están en el Segundo Círculo o Barra en un Gráfico de Círculo de Círculos o Barra de Círculos
description: Aprende cómo usar Aspose.Cells for C++ para determinar si los puntos de datos están en la segunda rebanada o barra en un gráfico de Pie of Pie o Bar of Pie. Nuestra guía demostrará cómo identificar y acceder a la segunda rebanada o barra en un gráfico compuesto, permitiendo analizar y manipular los datos de manera efectiva.
keywords: Aspose.Cells for C++, Gráfico Pie of Pie, Gráfico Bar of Pie, Rebanada secundaria, Barra secundaria, Análisis de datos, Manipulación de datos.
type: docs
weight: 180
url: /es/cpp/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **Escenarios de uso posibles**
Puedes determinar si los puntos de datos de una serie están en la segunda rebanada de un gráfico *Pie of Pie* o en la barra de un gráfico *Bar of Pie* usando Aspose.Cells. Por favor, usa la propiedad [ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartpoint/isinsecondaryplot/) para determinarlo.

Descargue el [archivo excel de ejemplo](5115193.xlsx) utilizado en el siguiente código de ejemplo y vea su salida en consola. Si abre el [archivo excel de ejemplo](5115193.xlsx), encontrará que todos los puntos de datos que son menores a 10 están dentro de la barra del Gráfico de Barra de Círculos como también se muestra en la salida de consola.

## **Encontrar si los Puntos de Datos están en el Segundo Pastel o Barra en un Gráfico de Pastel de Pastel o de Barra de Pastel**
El siguiente código de ejemplo muestra cómo averiguar si los puntos de datos están en el segundo círculo o barra en un gráfico de Círculo de Círculos o Barra de Círculos.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = srcDir + u"PieBars.xlsx";
    Workbook workbook(inputFilePath);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    Chart chart = worksheet.GetCharts().Get(0);
    chart.Calculate();

    Series series = chart.GetNSeries().Get(0);

    int pointCount = series.GetPoints().GetCount();
    for (int i = 0; i < pointCount; ++i)
    {
        ChartPoint chartPoint = series.GetPoints().Get(i);

        if (chartPoint.Get_YValue().IsNull())
            continue;

        std::cout << "Value: " << chartPoint.Get_YValue().ToDouble() << std::endl;
        std::cout << "IsInSecondaryPlot: " << (chartPoint.IsInSecondaryPlot() ? "true" : "false") << std::endl;
        std::cout << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Salida de la consola**
Por favor, mira la siguiente salida de consola generada después de ejecutar el código de ejemplo con el [archivo de Excel de ejemplo](5115193.xlsx). Si [IsInSecondaryPlot](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartpoint/isinsecondaryplot/) es **falso**, el punto de datos está dentro de la rebanada o si es **verdadero**, entonces el punto de datos está dentro de la barra.

{{< highlight java >}}

 Value: 15

IsInSecondaryPlot: False

Value: 9

IsInSecondaryPlot: True

Value: 2

IsInSecondaryPlot: True

Value: 40

IsInSecondaryPlot: False

Value: 5

IsInSecondaryPlot: True

Value: 4

IsInSecondaryPlot: True

Value: 25

IsInSecondaryPlot: False

{{< /highlight >}}
