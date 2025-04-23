---
title: Converti l Art Smart in Gruppo Forma con Node.js tramite C++
linktitle: Convertire l Arte intelligente in Forma di gruppo
type: docs
weight: 200
url: /it/nodejs-cpp/convert-the-smart-art-to-group-shape/
---

## **Possibili Scenari di Utilizzo**

Puoi convertire la Forma Smart Art in Gruppo Forma utilizzando il metodo [**Shape.getResultOfSmartArt()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getResultOfSmartArt--). Ti consentirà di gestire la forma smart art come una forma di gruppo. Di conseguenza, avrai accesso alle parti o forme individuali del gruppo forma.

## **Convertire la SmartArt in una forma di gruppo**

Il seguente esempio di codice carica il [file Excel di esempio](55541793.xlsx) contenente una forma smart art come mostrato in questo screenshot. Successivamente converte la forma smart art in forma di gruppo e stampa la proprietà Shape.isGroup. Si prega di consultare l'output della console del codice di esempio fornito di seguito.

![todo:image_alt_text](convert-the-smart-art-to-group-shape_1.png)

## **Codice di Esempio**

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

## **Output della console**

{{< highlight javascript >}}

Is Smart Art Shape: True

Is Group Shape: False

Is Group Shape: True

{{< /highlight >}}
