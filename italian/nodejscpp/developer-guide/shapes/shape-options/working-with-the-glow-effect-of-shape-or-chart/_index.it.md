---  
title: Lavorare con l’effetto bagliore di forma o grafico con Node.js tramite C++  
linktitle: Lavorare con l effetto Glow della forma o del grafico  
type: docs  
weight: 240  
url: /it/nodejs-cpp/working-with-the-glow-effect-of-shape-or-chart/  
description: Impara come lavorare con l’effetto bagliore di forme o grafici in Node.js usando Aspose.Cells for Node.js via C++.  
---  

## **Possibili Scenari di Utilizzo**  
Aspose.Cells fornisce la proprietà [Shape.getGlow()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getGlow--) insieme alla classe [GlowEffect](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/) per lavorare con l’effetto bagliore di forma o grafico. La classe [GlowEffect](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/) contiene le seguenti proprietà che possono essere impostate per ottenere risultati diversi in base ai requisiti dell’applicazione.  

- [GlowEffect.getSize()](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/#getSize--)  
- [GlowEffect.getTransparency()](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/#getTransparency--)  
- [GlowEffect.getColor()](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/#getColor--)  

## **Lavorare con l'effetto Glow della forma o del grafico**  
Il codice di esempio seguente carica il file Excel di origine ([source excel file](5115407.xlsx)) e accede alla prima forma nel primo foglio, impostando le sottoproprietà della proprietà [Shape.getGlow()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getGlow--) e quindi salva il workbook nel file Excel di output ([output excel file](5115414.xlsx)).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load your source excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first shape
const shape = worksheet.getShapes().get(0);

// Set the glow effect of the shape, Set its Size and Transparency properties
const glowEffect = shape.getGlow();
glowEffect.setSize(30);
glowEffect.setTransparency(0.4);

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  
