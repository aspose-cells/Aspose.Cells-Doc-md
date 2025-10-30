---
title: Cómo crear un gráfico de desplazamiento dinámico con Node.js vía C++
linktitle: Cómo crear un gráfico de desplazamiento dinámico
description: Aprende cómo crear un gráfico de desplazamiento dinámico usando Aspose.Cells for Node.js via C++. Nuestra guía paso a paso demostrará cómo implementar transiciones suaves de datos y desplazamiento automático en tu gráfico para una visualización continua y actualizada.
keywords: Aspose.Cells para Node.js, gráfico de desplazamiento dinámico, transiciones de datos, desplazamiento suave, visualización continua, actualización.
type: docs
weight: 75
url: /es/nodejs-cpp/create-dynamic-scrolling-chart/
---

## **Escenarios de uso posibles**
El gráfico de desplazamiento dinámico es un tipo de representación gráfica utilizada para mostrar datos que cambian con el tiempo. Está diseñado para proporcionar una vista en tiempo real de los datos, permitiendo a los usuarios rastrear actualizaciones continuas y tendencias. El gráfico se actualiza continuamente a medida que se agregan nuevos datos, y se desplaza automáticamente para mostrar la información más reciente.

Los gráficos de desplazamiento dinámico se utilizan comúnmente en diversas industrias, como finanzas, análisis del mercado de valores, seguimiento del clima y análisis de redes sociales. Permiten a los usuarios visualizar y analizar patrones de datos y tomar decisiones informadas basadas en información en tiempo real.

Estos gráficos suelen ser interactivos, permitiendo al usuario hacer zoom o desplazarse por datos históricos, y ajustar intervalos de tiempo. A menudo admiten múltiples series de datos, proporcionando una vista integral de diferentes métricas y sus correlaciones.

En general, los gráficos de desplazamiento dinámico son herramientas valiosas para monitorear y analizar datos de series temporales, facilitando la toma de decisiones en tiempo real y mejorando las capacidades de visualización de datos.

## **Usa Aspose.Cells para crear un gráfico de desplazamiento dinámico**
En los siguientes párrafos, te mostraremos cómo crear un gráfico de desplazamiento dinámico usando Aspose.Cells for Node.js via C++. Mostraremos el código del ejemplo, así como el archivo Excel creado con este código.

## **Código de muestra**
El siguiente código de ejemplo generará el [Archivo de Gráfico de Desplazamiento Dinámico](DynamicScrollingChart.xlsx).

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
sheet.getCells().get("A1").putValue("Day");
sheet.getCells().get("B1").putValue("Sales");
// In this example, we will add 30 days of data
const allDays = 30;
const showDays = 10;
let currentDay = 1;

for (let i = 0; i < allDays; i++) {
const cellA = `A${i + 2}`;
const cellB = `B${i + 2}`;
sheet.getCells().get(cellA).putValue(i + 1);
sheet.getCells().get(cellB).putValue(50 * (i % 2) + 20 * (i % 3) + 10 * Math.floor(i / 3));
}

// This is the Dynamic Scrolling Control Data
sheet.getCells().get("G19").putValue("Start Day");
sheet.getCells().get("G20").putValue(currentDay);
sheet.getCells().get("H19").putValue("Show Days");
sheet.getCells().get("H20").putValue(showDays);

// Set the dynamic range for the chart's data source. 
let index = sheets.getNames().add("Sheet1!ChtScrollData");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)");

// Set the dynamic range for the chart's data labels. 
index = sheets.getNames().add("Sheet1!ChtScrollLabels");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$A$2,Sheet1!$G$20,0,Sheet1!$H$20,1)");

// Add a ScrollBar for the Dynamic Scrolling Chart
const bar = sheet.getShapes().addScrollBar(2, 0, 3, 0, 200, 30);
bar.setMin(0);
bar.setMax(allDays - showDays);
bar.setCurrentValue(currentDay);
bar.setLinkedCell("$G$20");

// Create a chart object and set its data source.
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Line, 2, 4, 15, 10);
const chart = sheet.getCharts().get(chartIndex);
chart.getNSeries().add("Sales", true);
chart.getNSeries().get(0).setValues("Sheet1!ChtScrollData");
chart.getNSeries().get(0).setXValues("Sheet1!ChtScrollLabels");

// Save the workbook as an Excel file.
workbook.save(path.join(localPath, "DynamicScrollingChart.xlsx"));
```

## **Notas**
En el archivo generado, puedes operar en la barra de desplazamiento, mientras el gráfico cuenta dinámicamente los últimos 10 conjuntos de datos. Esto se hace usando la fórmula "OFFSET" en el código de ejemplo:

```
"=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)"
```

Puedes intentar cambiar el número "10" por "15" en la celda "Sheet1!$H$20", y el gráfico dinámico contará los últimos 15 conjuntos de datos. Ahora hemos creado con éxito un gráfico de desplazamiento dinámico usando Aspose.Cells for Node.js via C++.
{{< app/cells/assistant language="nodejs-cpp" >}}
