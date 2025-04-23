---
title: Cómo crear un gráfico de barras móvil dinámico con Node.js vía C++
linktitle: Cómo crear un Gráfico Dinámico Continuo
description: Aprende cómo crear un gráfico móvil dinámico usando Aspose.Cells for Node.js via C++. Nuestra guía demostrará cómo implementar transiciones suaves de datos y promedios móviles en tu gráfico para una visualización continua y actualizada.
keywords: Aspose.Cells para Node.js, gráfico móvil dinámico, transiciones de datos, promedios suaves, visualización continua, actualización.
type: docs
weight: 74
url: /es/nodejs-cpp/create-dynamic-rolling-chart/
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

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Your local test path
const localPath = "";

// Create a new workbook and access the first worksheet.
const workbook = new AsposeCells.Workbook();
const sheets = workbook.getWorksheets();
const sheet = sheets.get(0);

// Populate the data for the chart. Add values to cells and set series names.
sheet.getCells().get("A1").putValue("Month");
sheet.getCells().get("A2").putValue(1);
sheet.getCells().get("A3").putValue(2);
sheet.getCells().get("A4").putValue(3);
sheet.getCells().get("A5").putValue(4);
sheet.getCells().get("A6").putValue(5);
sheet.getCells().get("A7").putValue(6);
sheet.getCells().get("A8").putValue(7);

sheet.getCells().get("B1").putValue("Sales");
sheet.getCells().get("B2").putValue(50);
sheet.getCells().get("B3").putValue(45);
sheet.getCells().get("B4").putValue(55);
sheet.getCells().get("B5").putValue(60);
sheet.getCells().get("B6").putValue(55);
sheet.getCells().get("B7").putValue(65);
sheet.getCells().get("B8").putValue(70);

// Set the dynamic range for the chart's data source.
let index = sheets.getNames().add("Sheet1!ChtData");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$B$1,COUNT(Sheet1!$B:$B),0,-5,1)");

// Set the dynamic range for the chart's data labels.
index = sheets.getNames().add("Sheet1!ChtLabels");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)");

// Create a chart object and set its data source.
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Line, 10, 3, 25, 10);
const chart = sheet.getCharts().get(chartIndex);
chart.getNSeries().add("Sales", true);
chart.getNSeries().get(0).setValues("Sheet1!ChtData");
chart.getNSeries().get(0).setXValues("Sheet1!ChtLabels");

// Save the workbook as an Excel file.
workbook.save(path.join(localPath, "DynamicRollingChart.xlsx"));
```

## **Notas**
En el archivo generado, puedes seguir agregando datos en las columnas A y B, mientras que el gráfico cuenta dinámicamente los últimos 5 conjuntos de datos. Esto se hace usando la fórmula "OFFSET" en el código de muestra:

```
"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)"
```

Puedes intentar cambiar el número "-5" por "-10" en la fórmula, y el gráfico dinámico contará los últimos 10 conjuntos de datos. Ahora hemos creado un gráfico de desplazamiento dinámico usando Aspose.Cells con éxito.
