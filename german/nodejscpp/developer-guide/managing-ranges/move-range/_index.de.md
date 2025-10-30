---  
title: Bereich von Zellen in einem Arbeitsblatt mit Node.js über C++ verschieben  
linktitle: Bereich von Zellen in einem Arbeitsblatt verschieben  
type: docs  
weight: 370  
url: /de/nodejs-cpp/move-range-of-cells-in-a-worksheet/  
description: Erfahren Sie, wie Sie einen Zellbereich in einem Arbeitsblatt mit Aspose.Cells for Node.js via C++ verschieben.  
---  

{{% alert color="primary" %}}  
In diesem Artikel wird gezeigt, wie man einen Bereich von Zellen in einem Arbeitsblatt verschiebt.  
{{% /alert %}}  

## **Bereich von Zellen in einem Arbeitsblatt verschieben**  
Der Beispielcode verwendet eine Vorlagendatei, um die Aufgabe zu demonstrieren.  

**Die Eingabedatei**  

![todo:image_alt_text](move-range-of-cells-in-a-worksheet_1.png)  

Bitte sehen Sie die folgende generierte Datei mit dem Bereich A1:B5, der nach C1:D5 verschoben wurde.  

**Die Ausgabedatei**  

![todo:image_alt_text](move-range-of-cells-in-a-worksheet_2.png)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xlsx");
// Instantiate the workbook object. Open the Excel file
const workbook = new AsposeCells.Workbook(filePath);

const cells = workbook.getWorksheets().get(0).getCells();

const range = cells.createRange("A1", "B5");
//move the range to right.
range.moveTo(0, 2);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
