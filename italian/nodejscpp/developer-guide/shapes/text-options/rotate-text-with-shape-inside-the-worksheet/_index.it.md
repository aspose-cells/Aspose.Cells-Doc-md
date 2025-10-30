---
title: Ruota il testo con forma all interno del foglio di lavoro utilizzando Node.js via C++
linktitle: Ruota il testo con la forma all interno del foglio di lavoro
type: docs
weight: 1300
url: /it/nodejs-cpp/rotate-text-with-shape-inside-the-worksheet/
description: Impara come ruotare il testo con forma all interno di un foglio Excel usando Aspose.Cells for Node.js via C++.
---

## **Possibili Scenari di Utilizzo**

Puoi aggiungere testo all'interno di qualsiasi forma utilizzando Microsoft Excel. Se aggiungi una forma usando la vecchia versione di Microsoft Excel 2003, il testo non ruoterà con la forma. Ma se aggiungi una forma usando versioni più recenti di Microsoft Excel, ad esempio 2007, 2010, 2013 o 2016, ecc., allora il testo ruoterà con la forma. Puoi controllare se il testo dovrebbe ruotare con la forma o meno usando la proprietà [**ShapeTextAlignment.getRotateTextWithShape()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getRotateTextWithShape--). Il valore predefinito è **true** che significa che il testo ruoterà con la forma, ma se lo imposti come **false**, allora il testo non ruoterà con la forma.

## **Ruota il testo con la forma all'interno del foglio di lavoro**

Il seguente codice di esempio carica il [file Excel di esempio](64716896.xlsx) che ha una forma triangolare e il suo testo ruota con la forma. Se apri il file Excel di esempio in Microsoft Excel e ruoti la forma triangolare, il testo ruoterà anche con essa. Il codice imposta poi la proprietà [**ShapeTextAlignment.getRotateTextWithShape()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getRotateTextWithShape--) come **false** e lo salva come [file Excel di output](64716897.xlsx). Se ora apri il file Excel di output in Microsoft Excel e ruoti la forma triangolare, il testo non ruoterà con essa. Consulta la schermata seguente che mostra l'effetto del codice sul file Excel di esempio per riferimento.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Codice di Esempio**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleRotateTextWithShapeInsideWorksheet.xlsx");

// Load sample Excel file.
const workbook = new AsposeCells.Workbook(sourceFilePath);

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access cell B4 and add message inside it.
const cellB4 = worksheet.getCells().get("B4");
cellB4.putValue("Text is not rotating with shape because RotateTextWithShape is false.");

// Access first shape.
const shape = worksheet.getShapes().get(0);

// Access shape text alignment.
const shapeTextAlignment = shape.getTextBody().getTextAlignment();

// Do not rotate text with shape by setting RotateTextWithShape as false.
shapeTextAlignment.setRotateTextWithShape(false);

// Save the output Excel file.
const outputFilePath = path.join(dataDir, "outputRotateTextWithShapeInsideWorksheet.xlsx");
workbook.save(outputFilePath);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
