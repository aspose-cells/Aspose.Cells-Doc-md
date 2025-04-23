---
title: Determina qué eje existe en el gráfico con C++
description: Aprende cómo determinar qué eje existe en un gráfico creado usando Aspose.Cells for C++. Nuestra guía te ayudará a entender cómo identificar y acceder a los diferentes ejes en un gráfico, incluyendo los ejes de categoría, valor y secundario.
keywords: Aspose.Cells for C++, gráfico, eje, existencia, categoría, valor, secundario.
type: docs
weight: 140
url: /es/cpp/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}

A veces, el usuario necesita saber si un eje particular existe en el gráfico. Por ejemplo, quiere saber si existe un Eje de Valor Secundario dentro del gráfico o no. Algunos gráficos como Pie, PieExploded, PiePie, PieBar, Pie3D, Pie3DExploded, Doughnut, DoughnutExploded, etc. no tienen un eje.

Aspose.Cells proporciona [**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/hasaxis/) método para determinar si el gráfico tiene un eje específico o no.

{{% /alert %}}

El siguiente código de ejemplo demuestra el uso de [**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/hasaxis/) para determinar si el gráfico de muestra tiene Ejes de Categoría y Valor Principales y Secundarios.

## Código C++ para determinar qué eje existe en el gráfico

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create a workbook object
    Workbook workbook(srcDir + u"source.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the chart
    Chart chart = worksheet.GetCharts().Get(0);

    // Determine which axis exists in the chart
    bool ret = chart.HasAxis(AxisType::Category, true);
    std::wcout << u"Has Primary Category Axis: " << ret << std::endl;

    ret = chart.HasAxis(AxisType::Category, false);
    std::wcout << u"Has Secondary Category Axis: " << ret << std::endl;

    ret = chart.HasAxis(AxisType::Value, true);
    std::wcout << u"Has Primary Value Axis: " << ret << std::endl;

    ret = chart.HasAxis(AxisType::Value, false);
    std::wcout << u"Has Secondary Value Axis: " << ret << std::endl;

    Aspose::Cells::Cleanup();
}
```

## Salida de consola generada por el código de ejemplo

La salida de consola del código se muestra a continuación, que muestra verdadero para Eje de Categoría y Valor Primario y falso para Eje de Categoría y Valor Secundario.

{{< highlight java >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
