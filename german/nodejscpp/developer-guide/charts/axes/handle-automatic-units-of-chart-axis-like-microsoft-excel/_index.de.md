---  
title: Automatische Einheiten der Diagrammachse wie Microsoft Excel mit Node.js über C++ verwalten  
linktitle: Behandeln von automatischen Einheiten der Diagrammachse wie Microsoft Excel  
description: Erfahren Sie, wie Sie automatische Einheiten auf Diagrammarchsen in Aspose.Cells for Node.js via C++ verwalten. Unser Leitfaden zeigt Ihnen, wie Sie automatische Einheiten auf einer Diagrammachse konfigurieren und anpassen, einschließlich der Anzeige wissenschaftlicher Notation und der Skalierung.  
keywords: Aspose.Cells for Node.js via C++, Diagrammarchsen, automatische Einheiten, Microsoft Excel, Konfiguration, Anpassung, wissenschaftliche Notation, Skalierung.  
type: docs  
weight: 120  
url: /de/nodejs-cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/  
---  

## **Mögliche Verwendungsszenarien**  
Ältere Versionen von Aspose.Cells for Node.js via C++ konnten die automatischen Einheiten der Diagrammarchse beim Rendern in Bild oder PDF nicht richtig handhaben. Jetzt unterstützt Aspose.Cells for Node.js via C++ die Verwaltung der automatischen Einheiten der Diagrammarchse. Es gibt keine Code-Änderung. Wandeln Sie Ihr Diagramm einfach in ein Bild oder PDF um, und es wird die Achse wie in Microsoft Excel gerendert.  

## **Behandeln Sie automatische Einheiten der Diagrammachse wie Microsoft Excel**  
Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](61767755.xlsx) und erstellt das [Ausgabepdf-Diagramm](61767752.pdf). Der Screenshot zeigt die automatischen Einheiten der Diagrammarchse in roten Rechtecken und vergleicht die Beispiel-Excel-Datei mit dem output PDF-Diagramm. Beide sind exakt gleich.  

![todo:image_alt_text](handle-automatic-units-of-chart-axis-like-microsoft-excel_1.png)  

## **Beispielcode**  
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
