---  
title: Ajuster automatiquement la hauteur des lignes pour le rendu avec Node.js via C++  
linktitle: Ajuster automatiquement les lignes pour le rendu  
type: docs  
weight: 130  
url: /fr/nodejs-cpp/autofit-rows-for-rendering/  
description: Apprenez comment ajuster automatiquement la hauteur des lignes pour le rendu dans Excel en utilisant Aspose.Cells for Node.js via C++. Empêchez la coupure du texte dans les fichiers PDF sauvegardés.  
---  

En général, lorsque vous souhaitez afficher tout le texte dans une cellule, vous pouvez ajuster automatiquement la hauteur de la ligne en mode Normal avec un zoom de 100% dans Microsoft Excel. Cela permet au texte d'être entièrement visible en mode Normal, et même lors de l'impression ou de la sauvegarde du fichier en PDF, le texte sera affiché correctement.

Cependant, dans certains cas, l'ajustement automatique de la ligne fonctionne bien en mode Normal, mais lorsque vous passez en mode impression ou que vous enregistrez le fichier en PDF, le texte est coupé. Veuillez vérifier le fichier source [Book1.xlsx](Book1.xlsx) et les captures d'écran.

![le texte est tronqué en mode d'impression](text_clipped_in_printview.png)

Si vous souhaitez empêcher la coupure du texte dans le fichier PDF sauvegardé, vous pouvez ajuster automatiquement la ligne avec l'option [AutoFitterOptions.getForRendering()](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions/#getForRendering--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Init workbook instance.
const workbook = new AsposeCells.Workbook(filePath);

// Set autofit options for rendering.
const autoFitterOptions = new AsposeCells.AutoFitterOptions();
autoFitterOptions.setForRendering(true);

// Autofit rows with options.
workbook.getWorksheets().get(0).autoFitRows(autoFitterOptions);

// Save to pdf.
workbook.save("output.pdf", AsposeCells.SaveFormat.Pdf);
```

Maintenant, le texte n'est pas tronqué dans le fichier PDF de sortie.

![le texte n'est pas tronqué dans le PDF enregistré](text_not_clipped_in_saved_pdf.png)  
{{< app/cells/assistant language="nodejs-cpp" >}}
