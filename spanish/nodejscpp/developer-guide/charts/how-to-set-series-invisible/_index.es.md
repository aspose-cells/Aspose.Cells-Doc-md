---
title: Cómo hacer invisible una serie en Nodo.js vía C++
linktitle: Cómo establecer la serie como invisible
description: Aprende cómo hacer que una serie sea invisible en gráficos de Excel usando Aspose.Cells for Node.js via C++. 
keywords: Gráfico de Excel, Series, Invisibles, IsFiltered Nodo.js vía C++.
type: docs
weight: 74
url: /es/nodejs-cpp/how-to-set-series-invisible/
---

## Cómo hacer que una serie sea invisible en un gráfico de Excel

En un gráfico de Excel, puedes hacer clic derecho en el gráfico, seleccionar "Seleccionar datos", y en la ventana emergente, puedes definir si una serie está visible marcándola o desmarcándola. Puedes descargar el siguiente [archivo de ejemplo](SeriesFiltered.xlsx) y operarlo en Excel como se muestra en la figura para lograr esta función. A continuación, te explicaremos cómo lograrlo usando la biblioteca Aspose.Cells.

![todo:image_alt_text](series-invisible.png)

## Cómo hacer que una serie sea invisible usando Aspose.Cells 

Usamos el siguiente código para hacer que una serie sea invisible usando Aspose.Cells:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SeriesFiltered.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const charts = workbook.getWorksheets().get(0).getCharts();
const chart = charts.get("Chart 1");
const nSeriesFiltered = chart.getFilteredNSeries();
const nSeries = chart.getNSeries();
nSeries.get(1).setIsColorVaried(true);
nSeries.get(0).setIsColorVaried(true);
workbook.save(path.join(dataDir, "output.xlsx"));
```

Puedes obtener el [archivo de entrada](SeriesFiltered.xlsx) y el [archivo de salida](output.xlsx).

Como se muestra en la figura a continuación, las dos primeras series que originalmente estaban visibles, se han vuelto invisibles en el archivo de salida.
![todo:image_alt_text](output.png)
