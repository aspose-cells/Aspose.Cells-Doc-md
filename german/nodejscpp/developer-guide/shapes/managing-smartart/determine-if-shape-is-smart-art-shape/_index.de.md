---  
title: Bestimmen, ob Shape eine Smart Art Shape ist mit Node.js via C++  
linktitle: Bestimmen, ob es sich um eine SmartArt Form handelt  
type: docs  
weight: 400  
url: /de/nodejs-cpp/determine-if-shape-is-smart-art-shape/  
description: Lernen Sie, wie man mit Aspose.Cells for Node.js via C++ feststellt, ob eine Form in Excel eine Smart Art Form ist.  
---  

## **Mögliche Verwendungsszenarien**  

Smart Art Shapes sind spezielle Formen in Microsoft Excel, die es Ihnen ermöglichen, komplexe Diagramme automatisch zu erstellen. Sie können feststellen, ob die Form eine Smart Art-Form oder eine normale Form ist, indem Sie die [**Shape.isSmartArt()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#isSmartArt--)-Eigenschaft verwenden.  

## **Feststellen, ob eine Form ein SmartArt-Form ist**  

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](55541792.xlsx), die eine Smart Art Shape enthält, wie in diesem Screenshot gezeigt. Danach gibt er den Wert der [**Shape.isSmartArt()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#isSmartArt--)-Eigenschaft der ersten Form aus. Bitte beachten Sie die Konsolenausgabe des Beispielcodes unten.  

![todo:image_alt_text](determine-if-shape-is-smart-art-shape_1.png)  

## **Beispielcode**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSmartArtShape.xlsx");

// Load the sample smart art shape - Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first shape
const shape = worksheet.getShapes().get(0);

// Determine if shape is smart art
console.log("Is Smart Art Shape: " + shape.isSmartArt());
```  

## **Konsolenausgabe**  

{{< highlight java >}}  

Is Smart Art Shape: True  

{{< /highlight >}}  

