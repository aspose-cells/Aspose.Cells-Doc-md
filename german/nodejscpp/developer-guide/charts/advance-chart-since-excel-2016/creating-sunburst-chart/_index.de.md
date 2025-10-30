---
title: Hinweise zur Erstellung eines Sunburst Diagramms mit Node.js über C++
linktitle: Wie erstelle ich ein Sonnenstrahlendiagramm
description: Lernen, wie man in Aspose.Cells for Node.js via C++ ein Sunburst Diagramm erstellt, ein Diagramm, das Daten in einem Kreis darstellt. Unser Leitfaden hilft Ihnen dabei, verschiedene Eigenschaften und Formate Ihres Diagramms einzustellen, einschließlich Datenbeschriftungen, Legenden, Farben und mehr.
keywords: Aspose.Cells for Node.js via C++, Sunburst Diagramm, erstellen, Eigenschaften einstellen, Datenbeschriftungen, Legende, Format, Farbe, Kreis, Datenrendering.
type: docs
weight: 162
url: /de/nodejs-cpp/creating-sunburst-chart/
---

## **Mögliche Verwendungsszenarien**
Reingrafik-Diagramme sind gut geeignet, um Anteile innerhalb der Hierarchie zu vergleichen; jedoch sind Reingrafik-Diagramme nicht optimal, um hierarchische Ebenen zwischen den größten Kategorien und jedem Datenpunkt darzustellen. Ein Sonnenstrahldiagramm ist dafür viel besser geeignet. Das Sonnenstrahldiagramm ist ideal zur Anzeige hierarchischer Daten. Jede Ebene der Hierarchie wird durch einen Ring oder Kreis dargestellt, wobei der innerste Kreis die Spitze der Hierarchie ist. Ein Sonnenstrahldiagramm ohne hierarchische Daten (eine Kategorieebene) sieht ähnlich wie ein Donut-Diagramm aus. Ein Sonnenstrahldiagramm mit mehreren Kategorienebenen zeigt, wie die äußeren Ringe zu den inneren Ringen in Beziehung stehen. Das Sonnenstrahldiagramm ist am besten geeignet, um zu zeigen, wie ein Ring in seine beitragenden Teile zerlegt ist, während eine andere Art hierarchischer Diagramme, das Reingrafik-Diagramm, ideal zum Vergleich relativer Größen ist.

![todo:image_alt_text](sample.png)
## **Sonnenstrahlendiagramm**
Nach Ausführen des unten stehenden Codes wird das Sonnenstrahlendiagramm wie unten gezeigt angezeigt.

![todo:image_alt_text](result.png)
## **Beispielcode**
Der folgende Beispielcode lädt die [Beispieldatei Excel](sunburst.xlsx) und erstellt die [Ausgabedatei Excel](out.xlsx).

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
