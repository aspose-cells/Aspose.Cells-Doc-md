---
title: Text aus der Gear Type SmartArt Shape mit Node.js via C++ extrahieren
linktitle: Extrahieren Sie Text aus der SmartArt Form des Zahnradtyps
type: docs
weight: 500
url: /de/nodejs-cpp/extract-text-from-the-gear-type-smartart-shape/
description: Lernen Sie, wie Sie Text aus der Gear Type SmartArt Shape mit Aspose.Cells for Node.js via C++ extrahieren.
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells kann Text aus der Gear Type Smart Art Shape extrahieren. Dazu müssen Sie zuerst Smart Art Shape mittels der [**Shape.getResultOfSmartArt()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getResultOfSmartArt--)-Methode in Gruppengefüge umwandeln. Dann erhalten Sie das Array aller einzelnen Formen, die das Gruppengefüge bilden, mit der [**GroupShape.getGroupedShapes()**](https://reference.aspose.com/cells/nodejs-cpp/groupshape/#getGroupedShapes--)-Methode. Schließlich können Sie jede einzelne Form in einer Schleife durchlaufen und ihren Text mit der [**Shape.getText()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getText--)-Eigenschaft extrahieren.

## **Text aus dem SmartArt-Form 'Zahnräder' extrahieren**

Der folgende Beispielcode lädt die [Beispieldatei Excel](67338483.xlsx) mit der SmartArt-Form des Zahnradtyps. Anschließend werden die Texte aus den einzelnen Formen extrahiert, wie oben diskutiert. Bitte beachten Sie die Konsolenausgabe des folgenden Codes zur Referenz.

## **Beispielcode**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleExtractTextFromGearTypeSmartArtShape.xlsx");

// Load sample Excel file containing gear type smart art shape.
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access first shape.
const shape = worksheet.getShapes().get(0);

// Get the result of gear type smart art shape in the form of group shape.
const groupShape = shape.getResultOfSmartArt();

// Get the list of individual shapes consisting of group shape.
const shapes = groupShape.getGroupedShapes();

// Extract the text of gear type shapes and print them on console.
for (let i = 0; i < shapes.length; i++) {
const s = shapes[i];

if (s.getType() === AsposeCells.AutoShapeType.Gear9 || s.getType() === AsposeCells.AutoShapeType.Gear6) {
console.log("Gear Type Shape Text: " + s.getText());
}
}
```

## **Konsolenausgabe**

{{< highlight javascript >}}

Gear Type Shape Text: Nice

Gear Type Shape Text: Good

Gear Type Shape Text: Excellent

{{< /highlight >}}
