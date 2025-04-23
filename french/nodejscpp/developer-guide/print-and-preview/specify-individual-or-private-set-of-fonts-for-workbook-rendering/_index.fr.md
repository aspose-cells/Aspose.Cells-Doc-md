---  
title: Spécifier un ensemble individuel ou privé de polices pour le rendu du classeur avec Node.js via C++  
linktitle: Spécifier un ensemble individuel ou privé de polices pour le rendu de classeur  
type: docs  
weight: 40  
url: /fr/nodejs-cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/  
description: Apprenez comment spécifier des ensembles individuels ou privés de polices pour le rendu du classeur avec Aspose.Cells for Node.js via C++.  
---  

## **Scénarios d'utilisation possibles**  

 En général, vous spécifiez le répertoire ou la liste de polices pour tous les classeurs, mais parfois, vous devez spécifier un ensemble individuel ou privé de polices pour vos classeurs. Aspose.Cells for Node.js via C++ fournit la classe [**IndividualFontConfigs**](https://reference.aspose.com/cells/nodejs-cpp/individualfontconfigs) qui peut être utilisée pour spécifier l'ensemble individuel ou privé de polices pour votre classeur.  

## **Spécifier un ensemble de polices individuelles ou privées pour le rendu du classeur**  

Le code exemple suivant charge le [fichier Excel d'exemple](67338268.xlsx) avec son ensemble individuel ou privé de polices qui sont spécifiées à l'aide de la classe [**IndividualFontConfigs**](https://reference.aspose.com/cells/nodejs-cpp/individualfontconfigs). Veuillez voir la [police d'exemple](67338271.zip) utilisée dans le code ainsi que le [PDF de sortie](67338269.pdf) généré par celui-ci. La capture d'écran suivante montre à quoi ressemble le PDF de sortie si la police est trouvée avec succès.  

![todo:image_alt_text](specify-individual-or-private-set-of-fonts-for-workbook-rendering_1.png)  

## **Code d'exemple**  

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

