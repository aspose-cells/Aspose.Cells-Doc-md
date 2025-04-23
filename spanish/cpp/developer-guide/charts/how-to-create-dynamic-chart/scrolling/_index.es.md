---
title: Cómo Crear un Gráfico de Desplazamiento Dinámico con C++
linktitle: Crear Gráfico de Desplazamiento Dinámico
description: Aprenda a crear un gráfico de desplazamiento dinámico usando Aspose.Cells for C++. Nuestra guía paso a paso demostrará cómo implementar transiciones de datos suaves y desplazamiento automático en su gráfico para una visualización continua y actualizada.
keywords: Aspose.Cells for C++, Gráfico de Desplazamiento Dinámico, Transiciones de Datos, Desplazamiento Suave, Visualización Continua, Actualizaciones.
type: docs
weight: 75
url: /es/cpp/create-dynamic-scrolling-chart/
---

## **Escenarios de uso posibles**
El gráfico de desplazamiento dinámico es un tipo de representación gráfica utilizada para mostrar datos que cambian con el tiempo. Está diseñado para proporcionar una vista en tiempo real de los datos, permitiendo a los usuarios rastrear actualizaciones continuas y tendencias. El gráfico se actualiza continuamente a medida que se agregan nuevos datos, y se desplaza automáticamente para mostrar la información más reciente.

Los gráficos de desplazamiento dinámico se utilizan comúnmente en diversas industrias, como finanzas, análisis del mercado de valores, seguimiento del clima y análisis de redes sociales. Permiten a los usuarios visualizar y analizar patrones de datos y tomar decisiones informadas basadas en información en tiempo real.

Estos gráficos suelen ser interactivos, permitiendo al usuario hacer zoom o desplazarse por datos históricos, y ajustar intervalos de tiempo. A menudo admiten múltiples series de datos, proporcionando una vista integral de diferentes métricas y sus correlaciones.

En general, los gráficos de desplazamiento dinámico son herramientas valiosas para monitorear y analizar datos de series temporales, facilitando la toma de decisiones en tiempo real y mejorando las capacidades de visualización de datos.

## **Use Aspose Cells para Crear Gráfico de Desplazamiento Dinámico**
En los siguientes párrafos, le mostraremos cómo crear un Gráfico de Desplazamiento Dinámico usando Aspose.Cells. Le mostraremos el código del ejemplo, así como el archivo de Excel creado con este código.

## **Código de muestra**
El siguiente código de ejemplo generará el [Archivo de Gráfico de Desplazamiento Dinámico](DynamicScrollingChart.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String localPath(u"");

    Workbook workbook;
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet sheet = sheets.Get(0);

    sheet.GetCells().Get(u"A1").PutValue(u"Day");
    sheet.GetCells().Get(u"B1").PutValue(u"Sales");

    int allDays = 30;
    int showDays = 10;
    int currentDay = 1;

    Cells cells = sheet.GetCells();
    for (int i = 0; i < allDays; i++)
    {
        int row = i + 1;
        cells.Get(row, 0).PutValue(i + 1);
        cells.Get(row, 1).PutValue(50 * (i % 2) + 20 * (i % 3) + 10 * (i / 3));
    }

    sheet.GetCells().Get(u"G19").PutValue(u"Start Day");
    sheet.GetCells().Get(u"G20").PutValue(currentDay);
    sheet.GetCells().Get(u"H19").PutValue(u"Show Days");
    sheet.GetCells().Get(u"H20").PutValue(showDays);

    int index = sheets.GetNames().Add(u"Sheet1!ChtScrollData");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)");

    index = sheets.GetNames().Add(u"Sheet1!ChtScrollLabels");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$A$2,Sheet1!$G$20,0,Sheet1!$H$20,1)");

    ScrollBar bar = sheet.GetShapes().AddScrollBar(2, 0, 3, 0, 200, 30);
    bar.SetMin(0);
    bar.SetMax(allDays - showDays);
    bar.SetCurrentValue(currentDay);
    bar.SetLinkedCell(u"$G$20");

    int chartIndex = sheet.GetCharts().Add(ChartType::Line, 2, 4, 15, 10);
    Chart chart = sheet.GetCharts().Get(chartIndex);
    chart.GetNSeries().Add(u"Sales", true);
    chart.GetNSeries().Get(0).SetValues(u"Sheet1!ChtScrollData");
    chart.GetNSeries().Get(0).SetXValues(u"Sheet1!ChtScrollLabels");

    workbook.Save(localPath + u"DynamicScrollingChart.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **Notas**
En el archivo generado, puedes operar en la barra de desplazamiento, mientras el gráfico cuenta dinámicamente los últimos 10 conjuntos de datos. Esto se hace usando la fórmula "OFFSET" en el código de ejemplo:

```
"=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)"
```

Puedes intentar cambiar el número "10" a "15" en la celda "Sheet1!$H$20", y el gráfico dinámico contará los últimos 15 conjuntos de datos. Ahora hemos creado exitosamente un gráfico de desplazamiento dinámico usando Aspose.Cells.
