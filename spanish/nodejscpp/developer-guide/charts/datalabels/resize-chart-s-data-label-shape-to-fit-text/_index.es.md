---  
title: Redimensionar la forma de la etiqueta de datos del gráfico para que se ajuste al texto con Node.js a través de C++  
linktitle: Redimensionar la forma de la etiqueta de datos del gráfico para ajustar el texto  
description: Aprende cómo redimensionar la forma de la etiqueta de datos en un gráfico para que se ajuste al texto en Aspose.Cells for Node.js via C++. Nuestra guía te mostrará cómo ajustar el tamaño y la forma del contenedor de la etiqueta para garantizar que el texto se muestre correctamente sin truncamiento ni superposición.  
keywords: Aspose.Cells for Node.js via C++, creación de gráficos, etiquetas de datos, redimensionamiento de forma, ajuste de texto, truncamiento, superposición.  
type: docs  
weight: 220  
url: /es/nodejs-cpp/resize-chart-s-data-label-shape-to-fit-text/  
---  

{{% alert color="primary" %}}  
La aplicación de Excel proporciona la opción **Redimensionar la forma para que se ajuste al texto** para las Etiquetas de Datos en el Gráfico con el fin de aumentar el tamaño de la forma para que el texto quepa en ella.  
{{% /alert %}}  

## **Cómo Cambiar el Tamaño de la Forma de la Etiqueta de Datos en un Gráfico en Microsoft Excel**  

Esta opción puede accederse en la interfaz de Excel seleccionando alguna de las etiquetas de datos en el gráfico. Haz clic derecho y selecciona el menú **Formato de etiquetas de datos**. En la pestaña **Tamaño y propiedades**, expande **Alineación** para revelar las propiedades relacionadas, incluyendo la opción **Redimensionar forma para ajustar el texto**.  

## **Cómo redimensionar la forma de las etiquetas de datos del gráfico para que se ajusten al texto usando Aspose.Cells for Node.js via C++**  

Para imitar la función de Excel de redimensionar las formas de etiquetas de datos para que se ajusten al texto, las API de Aspose.Cells han expuesto la propiedad booleana [**DataLabels.isResizeShapeToFitText()**](https://reference.aspose.com/cells/nodejs-cpp/charttextframe/#isResizeShapeToFitText--). El siguiente código muestra un escenario de uso simple de la propiedad [**DataLabels.isResizeShapeToFitText()**](https://reference.aspose.com/cells/nodejs-cpp/charttextframe/#isResizeShapeToFitText--).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "source.xlsx");

// Create an instance of Workbook containing the Chart
const workbook = new AsposeCells.Workbook(filePath);

// Access the Worksheet that contains the Chart
const sheet = workbook.getWorksheets().get(0);

for (let c = 0; c < sheet.getCharts().getCount(); c++) 
{
// Access the Chart
const chart = sheet.getCharts().get(c);

for (let index = 0; index < chart.getNSeries().getCount(); index++) {
// Access the DataLabels of indexed NSeries
const labels = chart.getNSeries().get(index).getDataLabels();

// Set ResizeShapeToFitText property to true
labels.setIsResizeShapeToFitText(true);
}

// Calculate Chart
chart.calculate();
}

// Save the result
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

