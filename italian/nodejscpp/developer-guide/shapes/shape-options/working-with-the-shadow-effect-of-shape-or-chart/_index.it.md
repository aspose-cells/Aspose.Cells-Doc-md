---  
title: Lavorare con l effetto ombra di forma o grafico con Node.js tramite C++  
linktitle: Lavorare con l Effetto Ombra di una Forma o di un Grafico  
type: docs  
weight: 220  
url: /it/nodejs-cpp/working-with-the-shadow-effect-of-shape-or-chart/  
description: Impara come lavorare con l effetto ombra di forme o grafici usando Aspose.Cells for Node.js via C++.  
---  

## **Possibili Scenari di Utilizzo**  
Aspose.Cells for Node.js via C++ fornisce la proprietà [Shape.getShadowEffect()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getShadowEffect--) insieme alla classe [ShadowEffect](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect) per lavorare con l'effetto ombra di forma o grafico. La classe [ShadowEffect](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect) contiene le seguenti proprietà che possono essere impostate per ottenere risultati diversi in base alle esigenze dell'applicazione.  

- [ShadowEffect.getAngle()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getAngle--)  
- [ShadowEffect.getBlur()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getBlur--)  
- [ShadowEffect.getColor()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getColor--)  
- [ShadowEffect.getDistance()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getDistance--)  
- [ShadowEffect.getPresetType()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getPresetType--)  
- [ShadowEffect.getSize()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getSize--)  
- [ShadowEffect.getTransparency()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getTransparency--)  

## **Lavorare con l'Effetto Ombra della forma o del grafico**  
Il seguente esempio di codice carica il [file excel di origine](5115425.xlsx) e accede alla prima forma nel primo foglio di lavoro e imposta le sotto-proprietà della proprietà [Shape.getShadowEffect()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getShadowEffect--) e quindi salva il workbook nel [file excel di output](5115411.xlsx).  

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

// Set the shadow effect of the shape, set its Angle, Blur, Distance and Transparency properties
const shadowEffect = shape.getShadowEffect();
shadowEffect.setAngle(150);
shadowEffect.setBlur(4);
shadowEffect.setDistance(45);
shadowEffect.setTransparency(0.3);

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

