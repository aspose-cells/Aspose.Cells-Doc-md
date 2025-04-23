---  
title: Mostrar rango de celdas como las etiquetas de datos con Node.js a través de C++  
linktitle: Mostrar rango de celdas como las etiquetas de datos  
description: Aprende cómo mostrar un rango de celdas como etiquetas de datos en gráficos usando Aspose.Cells for Node.js via C++. Nuestra guía demostrará cómo vincular las etiquetas a tu fuente de datos y formatearlas para proporcionar información precisa y significativa en tus gráficos.  
keywords: Aspose.Cells for Node.js via C++, gráfico, etiquetas de datos, rango de celdas, fuente de datos, formato, precisión, información significativa.  
type: docs  
weight: 130  
url: /es/nodejs-cpp/showing-cell-range-as-the-data-labels/  
---  

{{% alert color="primary" %}}  
En Microsoft Excel 2013, puedes mostrar un rango de celdas para las etiquetas de datos. Aspose.Cells para Node.js soporta esta función.  
{{% /alert %}}  

## **Casilla de verificación para Mostrar rango de celdas como etiquetas de datos**  

Para mostrar el rango de celdas como etiquetas de datos en Microsoft Excel:  

1. Selecciona las etiquetas de datos de la serie y haz clic derecho para abrir el menú contextual.  
1. Selecciona **Formato de etiquetas de datos**. Se muestran las opciones de etiquetas.  
1. Selecciona o deselecciona la opción **La etiqueta contiene - Valor de las celdas**.  

El código de ejemplo a continuación accede a las etiquetas de datos de una serie de gráficos y establece la propiedad [**DataLabels.getShowCellRange()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#getShowCellRange--) en **true** para seleccionar la opción **Etiqueta Contiene - Valor de Celdas**.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "source_show_range.xlsx");

// Create workbook from the source Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the chart inside the worksheet
const chart = worksheet.getCharts().get(0);

// Check the "Label Contains - Value From Cells"
const dataLabels = chart.getNSeries().get(0).getDataLabels();
dataLabels.setShowCellRange(true);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

