---
title: Cómo gestionar PivotChart con PivotOptions para Node.js mediante C++
linktitle: Opciones de Gráfico Dinámico
type: docs
weight: 10
url: /es/nodejs-cpp/how-to-manage-pivotchart-with-pivotoptions/
description: Cómo gestionar PivotChart con PivotOptions en Node.js a través de C++.
keywords: PivotChart Node.js a través de C++
---
## ¿Qué es un PivotChart?

Un PivotChart en Excel es una representación gráfica de datos creada a partir de una tabla dinámica. Permite a los usuarios visualizar y analizar datos de forma dinámica resumiendo y mostrando información en forma de gráfico. Los PivotCharts son interactivos y pueden modificarse fácilmente para mostrar diferentes perspectivas de los datos, convirtiéndolo en una poderosa herramienta para el análisis y la presentación de datos en Excel.

## Cómo gestionar el Gráfico Dinámico con Opciones de Gráfico Dinámico

Al usar Aspose.Cells for Node.js via C++, puedes usar [**PivotOptions**](https://reference.aspose.com/cells/nodejs-cpp/pivotoptions/) para gestionar PivotChart.

Archivo y código de ejemplo:
[Archivo de muestra](Sample.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const chart = workbook.getWorksheets().get(0).getCharts().get(0);
const opt = chart.getPivotOptions();

// Hide ZoneFilter in PivotChart
opt.setDropZoneFilter(false); // HideZoneFilter

// You can set more properties, try them!
// opt.setDropZoneCategories(false); // HideZoneCategories
// opt.setDropZoneData(false); // HideZoneData
// opt.setDropZoneSeries(false); // HideZoneSeries
// opt.setDropZonesVisible(false); // Hide All

// Save the file and see the effect.
workbook.save(path.join(dataDir, "HideZoneFilter.xlsx"));
```

Con el código de ejemplo anterior, puede verificar el archivo de resultado con el siguiente efecto, como se muestra en la figura:

**![Salida](Output.png)**
{{< app/cells/assistant language="nodejs-cpp" >}}
