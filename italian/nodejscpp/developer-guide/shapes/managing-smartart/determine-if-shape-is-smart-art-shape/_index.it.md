---  
title: Determinare se una Forma è Forma Smart Art con Node.js tramite C++  
linktitle: Determinare se la forma è una forma di arte intelligente  
type: docs  
weight: 400  
url: /it/nodejs-cpp/determine-if-shape-is-smart-art-shape/  
description: Impara come determinare se una forma in Excel è una forma Smart Art utilizzando Aspose.Cells for Node.js via C++.  
---  

## **Possibili Scenari di Utilizzo**  

Le forme Smart Art sono forme speciali in Microsoft Excel che consentono di creare diagrammi complessi automaticamente. Puoi verificare se la forma è una forma smart art o una forma normale usando la proprietà [**Shape.isSmartArt()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#isSmartArt--).  

## **Determinare se la forma è una forma SmartArt**  

Il seguente esempio di codice carica il [file Excel di esempio](55541792.xlsx) contenente una forma smart art come mostrato in questo screenshot. Successivamente stampa il valore della proprietà [**Shape.isSmartArt()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#isSmartArt--) della prima forma. Si prega di consultare l'output della console del codice di esempio fornito di seguito.  

![todo:image_alt_text](determine-if-shape-is-smart-art-shape_1.png)  

## **Codice di Esempio**  

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

## **Output della console**  

{{< highlight java >}}  

Is Smart Art Shape: True  

{{< /highlight >}}  

