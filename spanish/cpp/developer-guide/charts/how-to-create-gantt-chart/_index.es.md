---
title: Cómo crear un gráfico de Gantt con C++
linktitle: Cómo crear un gráfico de Gantt
type: docs
weight: 72
url: /es/cpp/how-to-create-gantt-chart/
description: Aprende cómo crear un gráfico de Gantt con la API Aspose.Cells for C++.
keywords: Crear un gráfico de Gantt con C++, agregar un gráfico de Gantt, insertar un gráfico de Gantt
---

## **Qué es un gráfico de Gantt**

Un gráfico de Gantt es un tipo de gráfico de barras que ilustra un cronograma de proyecto. Muestra las fechas de inicio y fin de los diferentes elementos de un proyecto. Cada tarea o actividad está representada por una barra, cuya duración corresponde a su período. Los gráficos de Gantt también indican dependencias entre tareas, permitiendo a los gerentes de proyecto visualizar la secuencia en la que las tareas deben completarse. Son ampliamente utilizados en la gestión de proyectos para planificar, programar y rastrear proyectos de manera efectiva.

## **Cómo crear un gráfico de Gantt en Excel**

Puedes crear un gráfico de Gantt en Excel siguiendo estos pasos:
1. Agrega algunos datos para el gráfico de Gantt. 
<br>
<img src="00.png" width=50% />
1. Selecciona los datos y ve a Insertar --> Gráficos --> Insertar gráfico de columnas o barras --> Barra apilada. En nuestro ejemplo, eso es B1:B7, y luego Inserta un gráfico de **barra apilada**.
<br>
<img src="1.png" width=50% />

1. Selecciona el gráfico, **Seleccionar datos**->**Agregar**, configura el **nombre de la serie** y los **valores de la serie** de la siguiente manera.
<br>
<img src="2.png" width=50% />

1. Selecciona el gráfico, edita las **Etiquetas del eje horizontal (categoría)**.
<br>
<img src="3.png" width=50% />

1. **Formatear eje** la Eje Y, selecciona **Categorías en orden inverso**.
1. Selecciona la **Serie Azul** y configura el **Relleno -> Sin relleno**.
1. **Formatar eje** la Eje X, configura el **Mínimo y Máximo**(1/5/2019:43470, 1/30/2019:43494).
<br>
<img src="4.png" width=50% />

1. **Agregar etiquetas de datos** para el gráfico, ahora obtendrás un gráfico de Gantt.
<br>
<img src="0.png" width=50% />


## **Cómo agregar un gráfico de Gantt en Aspose.Cells**
Por favor, vea el siguiente código de ejemplo. Carga el [archivo de Excel de ejemplo](sample.xlsx) que contiene algunos datos de muestra. Luego crea el gráfico de barras apiladas basado en los datos iniciales y establece las propiedades relevantes. Finalmente, guarda el libro de trabajo en [formato XLSX de salida](result.xlsx). La siguiente captura de pantalla muestra el gráfico de Gantt creado por Aspose.Cells en el archivo de Excel de salida.
<br>
<img src="5.png" width=60% />

### **Código de muestra**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"sample.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create BarStacked Chart
    int32_t chartIndex = worksheet.GetCharts().Add(ChartType::BarStacked, 5, 6, 20, 15);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Set the chart title name
    chart.GetTitle().SetText(u"Gantt Chart");

    // Set the chart title visibility
    chart.GetTitle().SetIsVisible(true);

    // Set data range
    chart.SetChartDataRange(u"B1:B6", true);

    // Add series data range
    chart.GetNSeries().Add(u"C2:C6", true);

    // No fill for one series
    chart.GetNSeries().Get(0).GetArea().GetFillFormat().SetFillType(FillType::None);

    // Set the Horizontal(Category) Axis
    chart.GetNSeries().SetCategoryData(u"A2:A6");

    // Reverse the Horizontal(Category) Axis
    chart.GetCategoryAxis().SetIsPlotOrderReversed(true);

    // Set the value axis's MinValue and MaxValue
    chart.GetValueAxis().SetMinValue(worksheet.GetCells().Get(u"B2").GetValue());
    chart.GetValueAxis().SetMaxValue(worksheet.GetCells().Get(u"D6").GetValue());

    // Set the PlotArea with no fill
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Show the DataLabels
    chart.GetNSeries().Get(1).GetDataLabels().SetShowValue(true);

    // Disable the Legend
    chart.SetShowLegend(false);

    // Save the result
    workbook.Save(u"result.xlsx");

    Aspose::Cells::Cleanup();
}
```

