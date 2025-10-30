---  
title: Erstellen Sie Vereinigung Bereich mit Node.js über C++  
linktitle: Union Range erstellen  
type: docs  
weight: 360  
url: /de/nodejs-cpp/create-union-range/  
description: Lernen Sie, wie man einen Vereinigung Bereich mit Aspose.Cells for Node.js via C++ erstellt.  
keywords: Erstellen Sie Vereinigung Bereich Node.js über C++, Union Range Aspose.Cells Node.js, WorksheetCollection erstellen Vereinigung Bereich Node.js  
---  

## **Union Range erstellen**  
Aspose.Cells bietet die Möglichkeit, einen Vereinigung Bereich mithilfe der Methode [WorksheetCollection.createUnionRange](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#createUnionRange-string-number-). Die Methode [WorksheetCollection.createUnionRange](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#createUnionRange-string-number-) akzeptiert zwei Parameter, die Adresse zur Erstellung des Vereinigung Bereichs und den Index des Arbeitsblatts. Die Methode gibt ein [UnionRange](https://reference.aspose.com/cells/nodejs-cpp/unionrange) Objekt zurück.  

Der folgende Codeausschnitt demonstriert die Erstellung eines Vereinigung Bereichs mit der Methode [WorksheetCollection.createUnionRange](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#createUnionRange-string-number-). Die vom Code erzeugte Ausgabedatei ist als Referenz beigefügt.  

- [Ausgabedatei](106364952.xlsx)  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create union range
const unionRange = workbook.getWorksheets().createUnionRange("sheet1!A1:A10,sheet1!C1:C10", 0);

// Put value "ABCD" in the range
unionRange.setValue("ABCD");

// Save the output workbook.
workbook.save("CreateUnionRange_out.xlsx");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
