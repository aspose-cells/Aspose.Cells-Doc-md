---
title: Cómo crear un Gráfico de Rodamiento Dinámico con C++
linktitle: Cómo crear un Gráfico Dinámico Continuo
description: Aprenda a crear un gráfico de rodamiento dinámico usando Aspose.Cells for C++. Nuestra guía demostrará cómo implementar transiciones de datos suaves y promedios móviles en su gráfico para una visualización continua y actualizada.
keywords: Aspose.Cells for C++, Gráfico de Rodamiento Dinámico, Transiciones de Datos, Promedios Suaves, Visualización Continua, Actualizaciones.
type: docs
weight: 74
url: /es/cpp/create-dynamic-rolling-chart/
---

## **Escenarios de uso posibles**
Un gráfico de desplazamiento dinámico se refiere a una representación gráfica que muestra puntos de datos en constante cambio y actualización a lo largo del tiempo. Es un tipo de gráfico que se actualiza continuamente, mostrando una ventana en tiempo real de los puntos de datos más recientes mientras descarta los puntos de datos antiguos a medida que ingresan nuevos.

Los gráficos de desplazamiento dinámico se utilizan comúnmente para visualizar tendencias y patrones en datos en tiempo real o en streaming. Son particularmente útiles en escenarios donde los aspectos temporales y los cambios a lo largo del tiempo son críticos, como análisis del mercado de valores, monitoreo del clima o seguimiento de actuaciones en vivo.

Estos gráficos suelen emplear mecanismos de animación o desplazamiento automático para garantizar que la información más actualizada siempre se presente. La longitud de la ventana de desplazamiento se puede personalizar para mostrar un período de tiempo específico, como la última hora, día o semana.

En resumen, un gráfico de desplazamiento dinámico es una representación gráfica actualizada continuamente que muestra los últimos puntos de datos mientras descarta los antiguos, lo que permite a los usuarios observar tendencias y patrones en tiempo real.

## **Use Aspose Cells para crear un gráfico de desplazamiento dinámico**
En los siguientes párrafos, le mostraremos cómo crear un gráfico de desplazamiento dinámico usando Aspose.Cells. Le mostraremos el código del ejemplo, así como el archivo de Excel creado con este código.

## **Código de muestra**
El siguiente código de ejemplo generará el [Archivo de Gráfico de Desplazamiento Dinámico](DynamicRollingChart.xlsx).

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Your local test path
    U16String LocalPath = u"";

    // Create a new workbook and access the first worksheet.
    Workbook workbook;
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet sheet = sheets.Get(0);

    // Populate the data for the chart. Add values to cells and set series names.
    sheet.GetCells().Get(u"A1").PutValue(u"Month");
    sheet.GetCells().Get(u"A2").PutValue(1);
    sheet.GetCells().Get(u"A3").PutValue(2);
    sheet.GetCells().Get(u"A4").PutValue(3);
    sheet.GetCells().Get(u"A5").PutValue(4);
    sheet.GetCells().Get(u"A6").PutValue(5);
    sheet.GetCells().Get(u"A7").PutValue(6);
    sheet.GetCells().Get(u"A8").PutValue(7);

    sheet.GetCells().Get(u"B1").PutValue(u"Sales");
    sheet.GetCells().Get(u"B2").PutValue(50);
    sheet.GetCells().Get(u"B3").PutValue(45);
    sheet.GetCells().Get(u"B4").PutValue(55);
    sheet.GetCells().Get(u"B5").PutValue(60);
    sheet.GetCells().Get(u"B6").PutValue(55);
    sheet.GetCells().Get(u"B7").PutValue(65);
    sheet.GetCells().Get(u"B8").PutValue(70);

    // Set the dynamic range for the chart's data source.
    int index = sheets.GetNames().Add(u"Sheet1!ChtData");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$B$1,COUNT(Sheet1!$B:$B),0,-5,1)");

    // Set the dynamic range for the chart's data labels.
    index = sheets.GetNames().Add(u"Sheet1!ChtLabels");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)");

    // Create a chart object and set its data source.
    int chartIndex = sheet.GetCharts().Add(ChartType::Line, 10, 3, 25, 10);
    Chart chart = sheet.GetCharts().Get(chartIndex);
    chart.GetNSeries().Add(u"Sales", true);
    chart.GetNSeries().Get(0).SetValues(u"Sheet1!ChtData");
    chart.GetNSeries().Get(0).SetXValues(u"Sheet1!ChtLabels");

    // Save the workbook as an Excel file.
    workbook.Save(LocalPath + u"DynamicRollingChart.xlsx");

    std::cout << "Dynamic rolling chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Notas**
En el archivo generado, puedes seguir agregando datos en las columnas A y B, mientras que el gráfico cuenta dinámicamente los últimos 5 conjuntos de datos. Esto se hace usando la fórmula "OFFSET" en el código de muestra:

```
"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)"
```

Puedes intentar cambiar el número "-5" por "-10" en la fórmula, y el gráfico dinámico contará los últimos 10 conjuntos de datos. Ahora hemos creado un gráfico de desplazamiento dinámico usando Aspose.Cells con éxito.
