---
title: Estrazione del testo dalla forma SmartArt di tipo Gear con Node.js tramite C++
linktitle: Estrarre il testo dalla forma di Arte intelligente di tipo Gear
type: docs
weight: 500
url: /it/nodejs-cpp/extract-text-from-the-gear-type-smartart-shape/
description: Impara come estrarre il testo dalla forma SmartArt di tipo Gear usando Aspose.Cells for Node.js via C++.
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells può estrarre il testo dalla forma Smart Art di tipo Gear. Per farlo, è necessario prima convertire la forma Smart Art in Gruppo Forma usando il metodo [**Shape.getResultOfSmartArt()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getResultOfSmartArt--). Quindi si ottiene l'array di tutte le forme individuali che costituiscono il Gruppo Forma usando il metodo [**GroupShape.getGroupedShapes()**](https://reference.aspose.com/cells/nodejs-cpp/groupshape/#getGroupedShapes--). Infine, si può iterare su tutte le forme individuali in un ciclo ed estrarne il testo usando la proprietà [**Shape.getText()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getText--).

## **Estrarre il testo dalla forma SmartArt di tipo ingranaggio**

Il seguente codice di esempio carica il [file di Excel di esempio](67338483.xlsx) che contiene la forma di Arte intelligente di tipo Gear. Quindi estrae il testo dalle sue forme individuali come discusso in precedenza. Si prega di consultare l'output della console del codice fornito di seguito per riferimento.

## **Codice di Esempio**

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

## **Output della console**

{{< highlight javascript >}}

Gear Type Shape Text: Nice

Gear Type Shape Text: Good

Gear Type Shape Text: Excellent

{{< /highlight >}}
