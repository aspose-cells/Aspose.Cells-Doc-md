---  
title: Diagramm Datenetiketten Größe an Text anpassen mit Node.js über C++  
linktitle: Größe der Beschriftungsform des Diagramms anpassen, um den Text anzupassen  
description: Erfahren Sie, wie Sie die Größe der Datenetikett Form in einem Diagramm an den Text anpassen, um es richtig anzuzeigen, ohne Abschneidung oder Überlappung in Aspose.Cells for Node.js via C++. Unser Leitfaden zeigt, wie Sie die Größe und Form des Etikettencontainers anpassen, um die korrekte Anzeige sicherzustellen.  
keywords: Aspose.Cells for Node.js via C++, Diagrammerstellung, Datenetiketten, Formanpassung, Textanpassung, Abschneidung, Überlappung.  
type: docs  
weight: 220  
url: /de/nodejs-cpp/resize-chart-s-data-label-shape-to-fit-text/  
---  

{{% alert color="primary" %}}  
Die Excel-Anwendung bietet die Option **Form an Text anpassen** für Diagrammdatenbeschriftungen, um die Größe der Form zu erhöhen, damit der Text hineinpasst.  
{{% /alert %}}  

## **So passen Sie die Form der Datenbeschriftung in einem Diagramm an, damit der Text in Microsoft Excel passt**  

Diese Option kann in der Excel-Benutzeroberfläche durch Auswahl einer beliebigen Datenbeschriftung im Diagramm aufgerufen werden. Klicken Sie mit der rechten Maustaste und wählen Sie das Menü **Datenbeschriftungen formatieren**. Unter dem Tab **Größe & Eigenschaften** expandieren Sie **Ausrichtung**, um die zugehörigen Eigenschaften einschließlich der Option **Form ändern, um Text anzupassen** anzuzeigen.  

## **So ändern Sie die Größe der Datenetiketten im Diagramm, um den Text mit Aspose.Cells for Node.js via C++ anzupassen**  

Um die Excel-Funktion nachzuahmen, die die Formen der Datenbeschriftungen an den Text anpasst, haben die Aspose.Cells APIs die boolesche Eigenschaft [**DataLabels.isResizeShapeToFitText()**](https://reference.aspose.com/cells/nodejs-cpp/charttextframe/#isResizeShapeToFitText--) freigegeben. Der folgende Code zeigt ein einfaches Nutzungsszenario der [**DataLabels.isResizeShapeToFitText()**](https://reference.aspose.com/cells/nodejs-cpp/charttextframe/#isResizeShapeToFitText--)-Eigenschaft.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "source.xlsx");

// Create an instance of Workbook containing the Chart
const workbook = new AsposeCells.Workbook(filePath);

// Access the Worksheet that contains the Chart
const sheet = workbook.getWorksheets().get(0);

for (let c = 0; c < sheet.getCharts().getCount(); c++) 
{
// Access the Chart
const chart = sheet.getCharts().get(c);

for (let index = 0; index < chart.getNSeries().getCount(); index++) {
// Access the DataLabels of indexed NSeries
const labels = chart.getNSeries().get(index).getDataLabels();

// Set ResizeShapeToFitText property to true
labels.setIsResizeShapeToFitText(true);
}

// Calculate Chart
chart.calculate();
}

// Save the result
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

