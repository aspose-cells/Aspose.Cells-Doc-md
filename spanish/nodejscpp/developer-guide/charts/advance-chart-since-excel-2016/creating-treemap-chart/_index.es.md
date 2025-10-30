---  
title: Cómo crear un gráfico TreeMap con Node.js vía C++  
linktitle: Cómo crear un gráfico TreeMap  
description: Aprende cómo crear un gráfico de mapa de árbol en Aspose.Cells for Node.js via C++. Nuestra guía te ayudará a entender las varias propiedades y opciones de formateo disponibles para los gráficos de mapa de árbol, incluyendo colores, etiquetas y representación de datos.  
keywords: Aspose.Cells para Node.js, gráfico de mapa de árbol, crear, propiedades, formato, colores, etiquetas, representación de datos, gráfico circular, graficación jerárquica.  
type: docs  
weight: 161  
url: /es/nodejs-cpp/creating-treemap-chart/  
---  

## **Escenarios de uso posibles**  
Un gráfico Treemap proporciona una vista jerárquica de sus datos y facilita detectar patrones, como cuáles son los artículos más vendidos de una tienda. Las ramas del árbol están representadas por rectángulos y cada subrama se muestra como un rectángulo más pequeño. El gráfico Treemap muestra categorías por color y proximidad y puede mostrar fácilmente muchos datos que serían difíciles con otros tipos de gráficos.  

![todo:image_alt_text](sample.png)  
## **Gráfico TreeMap**  
Después de ejecutar el código a continuación, verá el gráfico TreeMap como se muestra a continuación.  

![todo:image_alt_text](result.png)  
## **Código de muestra**  
El siguiente código de muestra carga el [archivo de Excel de muestra](treemap.xlsx) y genera el [archivo de Excel de salida](out.xlsx).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "treemap.xlsx");
// Create an instance of Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Add a Treemap chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.Treemap, 5, 6, 20, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("TreeMap Chart");
// Add series data range(D2:D13,actually)
chart.getNSeries().add("D2:F13", true);
// Set category data(A2:A13 is incorrect )
chart.getNSeries().setCategoryData("A2:C13");
// Show the DataLabels with category names
chart.getNSeries().get(0).getDataLabels().setShowCategoryName(true);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("out.xlsx");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
