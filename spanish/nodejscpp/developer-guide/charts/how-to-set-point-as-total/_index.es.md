---  
title: Cómo establecer un punto como total con Nodo.js vía C++  
linktitle: Cómo establecer un punto como total  
description: Aprende a definir puntos como totales en gráficos de cascada usando Aspose.Cells for Node.js via C++.  
keywords: Gráfico de cascada, punto, establecer como total, Nodo.js vía C++  
type: docs  
weight: 72  
url: /es/nodejs-cpp/how-to-set-point-as-total/  
---  

## ¿Qué es "Establecer punto como total" en el gráfico de Excel?

En algunos gráficos de Excel, por ejemplo, un gráfico de cascada, algunos datos de puntos son la suma de los puntos anteriores, y puede que necesites "establecer punto como total". Mostraremos el código de ejemplo y la ilustración a continuación.

## Un gráfico de cascada necesita "Establecer punto como total" 

![todo:image_alt_text](set-as-total1.png)

Esta imagen muestra un gráfico de cascada en Excel. Podemos ver que hay cuatro puntos de datos comenzando con "Total" y que se usan para contar todos los puntos de datos anteriores. En esta imagen, las configuraciones no son exactamente correctas. Cuando seleccionamos un punto "Total 2024", podemos ver que la opción "Establecer como total" no está marcada en Excel. Adjuntamos el [archivo de ejemplo de Excel](SampleSheet.xlsx) que necesita ser modificado, y usaremos Aspose.Cells for Node.js via C++ para configurarlo correctamente.

## Usa Aspose.Cells for Node.js via C++ para "Establecer punto como total" 

Usamos el siguiente código para configurar el archivo correctamente:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleSheet.xlsx");

const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(0);
const chart = worksheet.getCharts().get("Graphiq5");

// set some points as total column 
// In this example, we set points 0, 4, 8, 12 as total
chart.getNSeries().get(0).getLayoutProperties().setSubtotals([0, 4, 8, 12]);
workbook.save(path.join(dataDir, "output.xlsx"));
```

Puedes obtener el siguiente [archivo de salida correcto](output.xlsx)

Como se muestra en la figura a continuación, los cuatro puntos de datos "Total" están configurados correctamente, y puedes ver la diferencia respecto a la gráfica anterior.

![todo:image_alt_text](set-as-total2.png)  
