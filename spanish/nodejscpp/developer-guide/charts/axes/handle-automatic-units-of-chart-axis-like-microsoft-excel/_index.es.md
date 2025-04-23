---  
title: Gestionar unidades automáticas del eje del gráfico como Microsoft Excel con Node.js vía C++  
linktitle: Manejar las unidades automáticas del eje del gráfico como en Microsoft Excel  
description: Aprende cómo gestionar las unidades automáticas en los ejes del gráfico en Aspose.Cells for Node.js via C++. Nuestra guía te mostrará cómo configurar y personalizar las unidades automáticas en un eje de gráfico, incluyendo la visualización en notación científica y ajuste de la escala.  
keywords: Aspose.Cells for Node.js via C++, ejes del gráfico, unidades automáticas, Microsoft Excel, configuración, personalización, notación científica, escalado.  
type: docs  
weight: 120  
url: /es/nodejs-cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/  
---  

## **Escenarios de uso posibles**  
Las versiones anteriores de Aspose.Cells for Node.js via C++ no podían manejar correctamente las unidades automáticas del eje del gráfico cuando el gráfico se representa en imagen o PDF. Ahora, Aspose.Cells for Node.js via C++ soporta el manejo de unidades automáticas del eje del gráfico. No hay cambios en el código. Solo convierte tu gráfico en una imagen o PDF y se renderizará el eje del gráfico igual que lo hace Microsoft Excel.  

## **Manejar Unidades Automáticas del Eje del Gráfico como Microsoft Excel**  
El siguiente código de ejemplo carga el [archivo de Excel de muestra](61767755.xlsx) y genera el [gráfico PDF de salida](61767752.pdf). La captura de pantalla muestra las unidades automáticas del eje del gráfico en rectángulos rojos y también compara el gráfico del archivo de Excel de muestra con el gráfico PDF de salida. Ambos son exactamente iguales.  

![todo:image_alt_text](handle-automatic-units-of-chart-axis-like-microsoft-excel_1.png)  

## **Código de muestra**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.xlsx");

// Load the sample Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart
const chart = worksheet.getCharts().get(0);

// Render chart to pdf
chart.toPdf("outputHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.pdf");
```  
