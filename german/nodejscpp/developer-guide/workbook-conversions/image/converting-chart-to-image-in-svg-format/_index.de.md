---  
title: Diagramm in SVG Format mit Node.js über C++ in Bild umwandeln  
linktitle: Diagramm in SVG Format konvertieren  
type: docs  
weight: 240  
url: /de/nodejs-cpp/converting-chart-to-image-in-svg-format/  
description: Erfahren Sie, wie Sie ein Diagramm in SVG Format mit Aspose.Cells for Node.js via C++ umwandeln.  
---  

{{% alert color="primary" %}}  

Scalable Vector Graphics (SVG) ist ein auf XML basierendes Vektorbildformat für zweidimensionale Grafiken, das auch Interaktivität und Animation unterstützt. Die SVG-Spezifikation ist ein offener Standard, der seit 1999 vom World Wide Web Consortium (W3C) entwickelt wird.  

SVG-Bilder und ihr Verhalten sind in XML-Textdateien definiert. Das bedeutet, dass sie durchsucht, indexiert, skriptgesteuert und komprimiert werden können. Als XML-Dateien können SVG-Bilder mit jedem Texteditor erstellt und bearbeitet werden, werden jedoch häufiger mit Zeichensoftware erstellt.  

Aspose.Cells kann Diagramme in verschiedenen Formaten wie BMP, JPEG, PNG, GIF, SVG usw. als Bild speichern. Dieser Artikel erklärt, wie man ein Diagramm im SVG-Format speichert.  

{{% /alert %}}  

Der folgende Beispielcode erläutert, wie Aspose.Cells verwendet wird, um ein Diagramm in ein SVG-Formatbild zu konvertieren. Der Code lädt die Quelldatei von Microsoft Excel und speichert dann das erste auf dem ersten Arbeitsblatt gefunden Diagramm als SVG.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object from source file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "SampleChartBook.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart inside the worksheet
const chart = worksheet.getCharts().get(0);

// Set image or print options
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setImageType(AsposeCells.ImageType.Svg);

// Save the chart to svg format
chart.toImage(path.join(dataDir, "Image_out.svg"), opts);
```  

