---  
title: Leer y Manipular gráficos de Excel 2016 con Node.js a través de C++  
linktitle: Leer y manipular gráficos de Excel 2016  
description: Aprende cómo leer y manipular gráficos de Excel 2016 usando Aspose.Cells for Node.js via C++. Esta guía te mostrará cómo acceder y modificar varias propiedades de los gráficos.  
keywords: Aspose.Cells para Node.js, gráficos de Excel 2016, lectura, manipulación, etiquetas de datos, colores de series, disposición, gráficos jerárquicos, gráficos circulares.  
type: docs  
weight: 48  
url: /es/nodejs-cpp/read-and-manipulate-excel-2016-charts/  
---  

## **Escenarios de uso posibles**  
Aspose.Cells ahora admite la lectura y manipulación de gráficos de Microsoft Excel 2016 que no están presentes en Microsoft Excel 2013 o versiones anteriores.  
## **Leer y manipular los gráficos de Excel 2016**  
El siguiente código de ejemplo carga el archivo [Excel fuente](22774101.xlsx) que contiene gráficos de Excel 2016 en la primera hoja. Lee todos los gráficos uno por uno y cambia su título según su tipo de gráfico. La siguiente captura de pantalla muestra el archivo Excel fuente antes de la ejecución del código. Como se puede ver, el título del gráfico es el mismo para todos.

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_1.png)

La siguiente captura de pantalla muestra el [archivo de Excel de salida](22774104.xlsx) después de la ejecución del código. Como puede ver, el título del gráfico se ha cambiado según su tipo de gráfico.

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_2.png)  
## **Código de muestra**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "excel2016Charts.xlsx");

// Load source excel file containing excel 2016 charts
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet which contains the charts
const sheet = workbook.getWorksheets().get(0);

// Access all charts one by one and read their types
for (let i = 0; i < sheet.getCharts().getCount(); i++) {
// Access the chart
const ch = sheet.getCharts().get(i);

// Print chart type
console.log(ch.getType());

// Change the title of the charts as per their types
ch.getTitle().setText("Chart Type is " + ch.getType().toString());
}

// Save the workbook
workbook.save(path.join(dataDir, "out_excel2016Charts.xlsx"));
```  
## **Salida de la consola**  
A continuación se muestra la salida de la consola del código de muestra anterior cuando se ejecuta con el [archivo de Excel fuente](22774101.xlsx) proporcionado.

{{< highlight javascript >}}  

 Waterfall  

Treemap  

Sunburst  

Histogram  

BoxWhisker  

{{< /highlight >}}  

## **Temas avanzados**  
- [Creación de gráfico de cascada](/cells/es/nodejs-cpp/creating-waterfall-chart/)  
- [Creación de gráfico de mapa de árbol](/cells/es/nodejs-cpp/creating-treemap-chart/)  
- [Creación de gráfico de ráfaga solar](/cells/es/nodejs-cpp/creating-sunburst-chart/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
