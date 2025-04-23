---  
title: Ignorer les erreurs lors de la rendu d Excel en PDF avec Node.js via C++  
linktitle: Ignorer les erreurs lors de la conversion Excel en PDF  
type: docs  
weight: 80  
url: /fr/nodejs-cpp/ignore-errors-while-rendering-excel-to-pdf/  
description: Apprenez comment ignorer les erreurs lors de la conversion de fichiers Excel en PDF en utilisant Aspose.Cells for Node.js via C++.  
---  

## **Scénarios d'utilisation possibles**  

Parfois, lors de la conversion de votre fichier Excel en PDF, des erreurs ou exceptions se produisent et le processus de conversion se termine. Vous pouvez ignorer toutes ces erreurs pendant la conversion en utilisant la propriété [**PdfSaveOptions.getIgnoreError()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getIgnoreError--). De cette façon, le processus de conversion se terminera en douceur sans générer d'erreur ou d'exception, mais une perte de données peut survenir. Utilisez cette propriété uniquement si la perte de données n'est pas critique pour vous.  

## **Ignorer les erreurs lors du rendu Excel vers PDF**  

Le code suivant charge le [fichier Excel d'exemple](55541778.xlsx) mais ce fichier Excel est erroné et génère une erreur lors de la [conversion en PDF](55541779.pdf) en 17.11. Mais comme nous utilisons la propriété [**PdfSaveOptions.getIgnoreError()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getIgnoreError--), aucune erreur n'est levée. Cependant, une *forme en flèche rouge arrondie* comme montrée dans cette capture d'écran est perdue.  

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)  

## **Code d'exemple**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleErrorExcel2Pdf.xlsx");
// Load the Sample Workbook that throws Error on Excel2Pdf conversion
const wb = new AsposeCells.Workbook(filePath);

// Specify Pdf Save Options - Ignore Error
const opts = new AsposeCells.PdfSaveOptions();
opts.IgnoreError = true;

// Save the Workbook in Pdf with Pdf Save Options
wb.save("outputErrorExcel2Pdf.pdf", opts);
```  

