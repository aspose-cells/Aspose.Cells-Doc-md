---
title: Kundenspezifische Sektoren oder Segmentsfarben im Kreisdiagramm mit Node.js via C++
linktitle: Benutzerdefinierte Slice oder Sektorenfarben in einem Tortendiagramm
description: Lernen Sie, wie Sie mit Aspose.Cells for Node.js via C++ Sektoren und Segmentfarben in einem Kreisdiagramm anpassen. Unser Leitfaden zeigt, wie man jeder Scheibe, jedem Sektor oder Legion eine einzigartige Farbe zuweist, für eine verbesserte visuelle Attraktivität und Datenvisualisierung.
keywords: Aspose.Cells for Node.js via C++, Kreisdiagramm, Anpassbare Sektorfedfarben, Anpassbare Segmentsfarben, Visuelle Attraktivität, Datenvisualisierung.
type: docs
weight: 60
url: /de/nodejs-cpp/custom-slice-or-sector-colors-in-pie-chart/
---

{{% alert color="primary" %}}

In diesem Artikel wird erläutert, wie benutzerdefinierte Farben zu Tortendiagrammslices/Sektoren hinzugefügt werden. Standardmäßig verwenden Tortendiagramme die Microsoft Excel-Standardvorlage. Um andere Farben zu verwenden, definieren Sie die Farben im Diagramm neu.

{{% /alert %}}

Um eine benutzerdefinierte Farbe für die einzelnen Slices oder Sektoren eines Tortendiagramms festzulegen:

1. Zugriff auf das [**Series**](https://reference.aspose.com/cells/nodejs-cpp/series)-Objekt mit [**ChartPoint**](https://reference.aspose.com/cells/nodejs-cpp/chartpoint).
1. Zuweisen der gewünschten Farbe unter Verwendung der [**ChartPoint.getForegroundColor()**](https://reference.aspose.com/cells/nodejs-cpp/area/#getForegroundColor--)-Eigenschaft.

In diesem Artikel wird auch erläutert, wie:

- Die Kategoriedaten eines Diagramms.
- Ein Diagrammtitel, der mit einer Zelle verknüpft ist.
- Die Schriftarteinstellungen des Diagrammtitels.
- Die Position der Legende.

{{% alert color="primary" %}}

[**ChartPoint.getForegroundColor()**](https://reference.aspose.com/cells/nodejs-cpp/area/#getForegroundColor--) ist nicht spezifisch für Tortendiagramme, kann aber für alle Arten von Diagrammen verwendet werden.

{{% /alert %}}

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Put the sample values used in a pie chart
worksheet.getCells().get("C3").putValue("India");
worksheet.getCells().get("C4").putValue("China");
worksheet.getCells().get("C5").putValue("United States");
worksheet.getCells().get("C6").putValue("Russia");
worksheet.getCells().get("C7").putValue("United Kingdom");
worksheet.getCells().get("C8").putValue("Others");

// Put the sample values used in a pie chart
worksheet.getCells().get("D2").putValue("% of world population");
worksheet.getCells().get("D3").putValue(25);
worksheet.getCells().get("D4").putValue(30);
worksheet.getCells().get("D5").putValue(10);
worksheet.getCells().get("D6").putValue(13);
worksheet.getCells().get("D7").putValue(9);
worksheet.getCells().get("D8").putValue(13);

// Create a pie chart with desired length and width
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.Pie, 1, 6, 15, 14);

// Access the pie chart
const pie = worksheet.getCharts().get(pieIdx);

// Set the pie chart series
pie.getNSeries().add("D3:D8", true);

// Set the category data
pie.getNSeries().setCategoryData("=Sheet1!$C$3:$C$8");

// Set the chart title that is linked to cell D2
pie.getTitle().setLinkedSource("D2");

// Set the legend position at the bottom.
pie.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);

// Set the chart title's font name and color
pie.getTitle().getFont().setName("Calibri");
pie.getTitle().getFont().setSize(18);

// Access the chart series
const srs = pie.getNSeries().get(0);

// Color the individual points with custom colors
srs.getPoints().get(0).getArea().setForegroundColor(new AsposeCells.Color(0, 246, 22, 219));
srs.getPoints().get(1).getArea().setForegroundColor(new AsposeCells.Color(0, 51, 34, 84));
srs.getPoints().get(2).getArea().setForegroundColor(new AsposeCells.Color(0, 46, 74, 44));
srs.getPoints().get(3).getArea().setForegroundColor(new AsposeCells.Color(0, 19, 99, 44));
srs.getPoints().get(4).getArea().setForegroundColor(new AsposeCells.Color(0, 208, 223, 7));
srs.getPoints().get(5).getArea().setForegroundColor(new AsposeCells.Color(0, 222, 69, 8));

// Autofit all columns
worksheet.autoFitColumns();

const outputPath = path.join(dataDir, "output.out.xlsx");
// Save the workbook
workbook.save(outputPath, AsposeCells.SaveFormat.Xlsx);
```
