---  
title: Excel 2016 Diagramme mit Node.js über C++ lesen und manipulieren  
linktitle: Excel 2016 Diagramme lesen und bearbeiten  
description: Lernen Sie, wie Sie Excel 2016 Diagramme mit Aspose.Cells for Node.js via C++ lesen und manipulieren. Dieser Leitfaden zeigt, wie man auf verschiedene Diagrammeigenschaften zugreift und sie ändert.  
keywords: Aspose.Cells für Node.js, Excel 2016 Diagramme, lesen, manipulieren, Datenbeschriftungen, Serienfarben, Layout, hierarchisches Diagramm, Kreisdiagramm.  
type: docs  
weight: 48  
url: /de/nodejs-cpp/read-and-manipulate-excel-2016-charts/  
---  

## **Mögliche Verwendungsszenarien**  
Aspose.Cells unterstützt jetzt das Lesen und die Manipulation von Microsoft Excel 2016-Diagrammen, die in Microsoft Excel 2013 oder früheren Versionen nicht vorhanden sind.  
## **Excel 2016 Diagramme lesen und bearbeiten**  
Der folgende Beispielcode lädt die [Quelldatei](22774101.xlsx), die Excel 2016-Diagramme im ersten Arbeitsblatt enthält. Es liest alle Diagramme nacheinander aus und ändert den Titel entsprechend ihrem Diagrammtyp. Das folgende Bildschirmfoto zeigt die Quelldatei vor der Ausführung des Codes. Wie Sie sehen können, ist der Diagrammtitel bei allen Diagrammen gleich.

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_1.png)

Der folgende Screenshot zeigt die [Ausgabedatei Excel](22774104.xlsx) nach der Ausführung des Codes. Wie Sie sehen können, wurde der Diagrammtitel entsprechend seinem Diagrammtyp geändert.

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_2.png)  
## **Beispielcode**  
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
## **Konsolenausgabe**  
Hier ist die Konsolenausgabe des obigen Beispielcodes, wenn er mit der bereitgestellten [Quelldatei Excel](22774101.xlsx) ausgeführt wird.

{{< highlight javascript >}}  

 Waterfall  

Treemap  

Sunburst  

Histogram  

BoxWhisker  

{{< /highlight >}}  

## **Erweiterte Themen**  
- [Erstellung eines Wasserfalldiagramms](/cells/de/nodejs-cpp/creating-waterfall-chart/)  
- [Erstellung eines TreeMap-Diagramms](/cells/de/nodejs-cpp/creating-treemap-chart/)  
- [Erstellung eines Sunburst-Diagramms](/cells/de/nodejs-cpp/creating-sunburst-chart/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
