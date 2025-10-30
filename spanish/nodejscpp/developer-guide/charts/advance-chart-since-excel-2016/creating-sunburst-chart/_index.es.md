---
title: Cómo crear un gráfico Sunburst con Node.js vía C++
linktitle: Cómo crear un gráfico de anillo solar
description: Aprende cómo crear un gráfico de estallido solar en Aspose.Cells for Node.js via C++, un gráfico que presenta datos en un círculo. Nuestra guía te ayudará a configurar varias propiedades y formateo de tu gráfico, incluyendo etiquetas de datos, leyendas, colores y más.
keywords: Aspose.Cells for Node.js via C++, gráfico de estallido solar, crear, configurar propiedades, etiquetas de datos, leyenda, formato, color, círculo, renderizado de datos.
type: docs
weight: 162
url: /es/nodejs-cpp/creating-sunburst-chart/
---

## **Escenarios de uso posibles**
Los gráficos de árbol de mapa son buenos para comparar proporciones dentro de la jerarquía; sin embargo, los gráficos de árbol de mapa no son ideales para mostrar niveles jerárquicos entre las categorías más grandes y cada punto de datos. Un gráfico de estallido solar es mucho mejor para mostrar eso. El gráfico de estallido solar es ideal para mostrar datos jerárquicos. Cada nivel de la jerarquía se representa mediante un aro o círculo, con el círculo más interior como la cima de la jerarquía. Un gráfico de estallido solar sin datos jerárquicos (un nivel de categorías) se parece a un gráfico de dona. Sin embargo, un gráfico de estallido solar con múltiples niveles de categorías muestra cómo los anillos exteriores se relacionan con los interiores. El gráfico de estallido solar es más efectivo para mostrar cómo un aro se divide en sus piezas contribuyentes, mientras que otro tipo de gráfico jerárquico, el gráfico de mapa de árbol, es ideal para comparar tamaños relativos.

![todo:image_alt_text](sample.png)
## **Gráfico de ráfaga solar**
Después de ejecutar el código a continuación, verá el gráfico de ráfaga solar como se muestra a continuación.

![todo:image_alt_text](result.png)
## **Código de muestra**
El siguiente código de muestra carga el [archivo de Excel de muestra](sunburst.xlsx) y genera el [archivo de Excel de salida](out.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sunburst.xlsx");
// Create an instance of Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Add a Treemap chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.Sunburst, 5, 6, 25, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("Sunburst Chart");
// Add series data range
chart.getNSeries().add("D2:D16", true);
// Set category data (A2:A16 is incorrect, as hierarchical category)
chart.getNSeries().setCategoryData("A2:C16");
// Show the DataLabels with category names
chart.getNSeries().get(0).getDataLabels().setShowCategoryName(true);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("out.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
