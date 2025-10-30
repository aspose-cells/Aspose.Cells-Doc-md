---
title: Konvertieren Sie die Smart Art in Gruppengefüge mit Node.js via C++
linktitle: Konvertieren Sie die SmartArt in eine Gruppenform
type: docs
weight: 200
url: /de/nodejs-cpp/convert-the-smart-art-to-group-shape/
---

## **Mögliche Verwendungsszenarien**

Sie können Smart Art Shape mit der [**Shape.getResultOfSmartArt()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getResultOfSmartArt--)-Methode in Gruppengefüge umwandeln. Dadurch können Sie Smart Art Shapes wie ein Gruppengefüge behandeln. Folglich haben Sie Zugriff auf die einzelnen Teile oder Formen des Gruppengefüges.

## **Konvertieren des SmartArt in Gruppenform**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](55541793.xlsx), die eine Smart Art Shape enthält, wie in diesem Screenshot gezeigt. Danach wandelt er die Smart Art Shape in Gruppengefüge um und gibt die Shape.isGroup-Eigenschaft aus. Bitte beachten Sie die Konsolenausgabe des Beispielcodes unten.

![todo:image_alt_text](convert-the-smart-art-to-group-shape_1.png)

## **Beispielcode**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load the sample smart art shape - Excel file
const filePath = path.join(__dirname, "data", "sampleSmartArtShape_GetResultOfSmartArt.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first shape
const shape = worksheet.getShapes().get(0);

// Determine if shape is smart art
console.log("Is Smart Art Shape: " + shape.isSmartArt());

// Determine if shape is group shape
console.log("Is Group Shape: " + shape.isGroup());

// Convert smart art shape into group shape
console.log("Is Group Shape: " + shape.getResultOfSmartArt().isGroup());
```

## **Konsolenausgabe**

{{< highlight javascript >}}

Is Smart Art Shape: True

Is Group Shape: False

Is Group Shape: True

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
