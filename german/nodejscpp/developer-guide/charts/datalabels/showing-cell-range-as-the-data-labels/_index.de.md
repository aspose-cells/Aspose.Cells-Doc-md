---  
title: Anzeigen des Zellbereichs als Datenetiketten mit Node.js über C++  
linktitle: Anzeige des Zellenbereichs als Datenbeschriftungen  
description: Erfahren Sie, wie Sie einen Zellbereich in Diagrammen als Datenetiketten mit Aspose.Cells for Node.js via C++ anzeigen. Unser Leitfaden zeigt, wie Sie die Labels mit Ihrer Datenquelle verknüpfen und formatieren, um präzise und aussagekräftige Informationen in Ihren Diagrammen bereitzustellen.  
keywords: Aspose.Cells for Node.js via C++, Diagrammerstellung, Datenetiketten, Zellbereich, Datenquelle, Formatierung, Genauigkeit, aussagekräftige Informationen.  
type: docs  
weight: 130  
url: /de/nodejs-cpp/showing-cell-range-as-the-data-labels/  
---  

{{% alert color="primary" %}}  
In Microsoft Excel 2013 können Sie einen Zellbereich für Datenbeschriftungen anzeigen. Aspose.Cells für Node.js unterstützt diese Funktion.  
{{% /alert %}}  

## **Kontrollkästchen zum Anzeigen des Zellenbereichs als Datenbeschriftungen**  

So zeigen Sie den Zellenbereich als Datenbeschriftungen in Microsoft Excel:  

1. Wählen Sie die Seriendatenbeschriftungen aus und klicken Sie mit der rechten Maustaste, um das Kontextmenü zu öffnen.  
1. Wählen Sie **Datenelemente formatieren** aus. Beschriftungsoptionen werden angezeigt.  
1. Wählen oder deaktivieren Sie die Option **Beschriftung enthält - Wert aus Zellen**.  

Der folgende Beispielcode greift auf die Datenbeschriftungen einer Diagrammserie zu und setzt die [**DataLabels.getShowCellRange()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#getShowCellRange--) Eigenschaft auf **true**, um die Option **Beschriftung enthält - Wert aus Zellen** auszuwählen.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "source_show_range.xlsx");

// Create workbook from the source Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the chart inside the worksheet
const chart = worksheet.getCharts().get(0);

// Check the "Label Contains - Value From Cells"
const dataLabels = chart.getNSeries().get(0).getDataLabels();
dataLabels.setShowCellRange(true);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
