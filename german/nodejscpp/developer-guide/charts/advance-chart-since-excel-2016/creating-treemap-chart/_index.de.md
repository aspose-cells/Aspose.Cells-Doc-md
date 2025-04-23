---  
title: So erstellen Sie ein TreeMap Diagramm mit Node.js über C++  
linktitle: Wie erstelle ich ein TreeMap Diagramm  
description: Erfahren Sie, wie Sie in Aspose.Cells for Node.js via C++ ein Reingrafik Diagramm erstellen. Unser Leitfaden hilft Ihnen, die verschiedenen Eigenschaften und Formatierungsoptionen für Reingrafik Diagramme zu verstehen, einschließlich Farben, Beschriftungen und Datenrepräsentation.  
keywords: Aspose.Cells für Node.js, Reingrafik Diagramm, erstellen, Eigenschaften, Formatierung, Farben, Beschriftungen, Datenrepräsentation, Kreisdiagramm, hierarchisches Diagramm.  
type: docs  
weight: 161  
url: /de/nodejs-cpp/creating-treemap-chart/  
---  

## **Mögliche Verwendungsszenarien**  
Ein Treemap-Chart bietet eine hierarchische Ansicht Ihrer Daten und macht es einfach, Muster zu erkennen, beispielsweise welche Artikel die Bestseller eines Ladens sind. Die Baumzweige werden durch Rechtecke dargestellt und jede Unterzweig wird als kleineres Rechteck angezeigt. Das Treemap-Chart zeigt Kategorien nach Farbe und Nähe an und kann problemlos viele Daten anzeigen, was bei anderen Diagrammtypen schwierig wäre.  

![todo:image_alt_text](sample.png)  
## **Treemap-Diagramm**  
Nach Ausführung des folgenden Codes sehen Sie das Treemap-Diagramm wie unten gezeigt.  

![todo:image_alt_text](result.png)  
## **Beispielcode**  
Der folgende Beispielscode lädt die [Beispieldatei Excel](treemap.xlsx) und generiert die [Ausgabedatei Excel](out.xlsx).  

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

