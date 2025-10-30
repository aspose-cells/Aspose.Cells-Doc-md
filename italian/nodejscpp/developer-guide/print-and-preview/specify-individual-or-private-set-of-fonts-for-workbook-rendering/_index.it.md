---  
title: Specifica set di font individuali o privati per il rendering del workbook con Node.js tramite C++  
linktitle: Specificare un insieme individuale o privato di caratteri per la rappresentazione del workbook  
type: docs  
weight: 40  
url: /it/nodejs-cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/  
description: Impara come specificare set di font individuali o privati per il rendering del workbook usando Aspose.Cells for Node.js via C++.  
---  

## **Possibili Scenari di Utilizzo**  

In generale, si specifica la directory dei font o l'elenco di font per tutti i workbook, ma a volte è necessario specificare set di font individuali o privati per i propri workbook. Aspose.Cells for Node.js via C++ fornisce la classe [**IndividualFontConfigs**](https://reference.aspose.com/cells/nodejs-cpp/individualfontconfigs) che può essere usata per specificare set di font individuali o privati.  

## **Specificare un insieme individuale o privato di caratteri per la rappresentazione del foglio di lavoro**  

Il seguente esempio di codice carica il [file Excel di esempio](67338268.xlsx) con il suo set di font individuali o privati specificato usando la classe [**IndividualFontConfigs**](https://reference.aspose.com/cells/nodejs-cpp/individualfontconfigs). Vedi anche il [font di esempio](67338271.zip) usato nel codice e il [PDF di output](67338269.pdf) generato. La schermata seguente mostra l’aspetto del PDF generato se il font viene trovato con successo.  

![todo:image_alt_text](specify-individual-or-private-set-of-fonts-for-workbook-rendering_1.png)  

## **Codice di Esempio**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Path of your custom font directory.
const customFontsDir = "C:\\TempDir\\CustomFonts";

// Specify individual font configs custom font directory.
const fontConfigs = new AsposeCells.IndividualFontConfigs();

// If you comment this line or if custom font directory is wrong or 
// if it does not contain required font then output pdf will not be rendered correctly.
fontConfigs.setFontFolder(customFontsDir, false);

// Specify load options with font configs.
const opts = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
opts.setFontConfigs(fontConfigs);

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.xlsx");
// Output directory
const outputDir = path.join(__dirname, "output");
// Load the sample Excel file with individual font configs. 
const wb = new AsposeCells.Workbook(filePath, opts);

// Save to PDF format.
wb.save(outputDir + "outputSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.pdf", AsposeCells.SaveFormat.Pdf);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
