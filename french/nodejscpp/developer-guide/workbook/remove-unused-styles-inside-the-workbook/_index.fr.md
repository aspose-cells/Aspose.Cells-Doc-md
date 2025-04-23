---  
title: Supprimer les styles inutilisés dans le classeur avec Node.js via C++  
linktitle: Supprimer les styles inutilisés dans le classeur  
type: docs  
weight: 340  
url: /fr/nodejs-cpp/remove-unused-styles-inside-the-workbook/  
description: Apprenez comment supprimer les styles inutilisés d un classeur en utilisant Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Les styles inutilisés dans les fichiers Excel prennent non seulement de la place mais causent également des problèmes de performance lors de la conversion en différents formats comme PDF, HTML, etc. Aspose.Cells fournit la [**Workbook.removeUnusedStyles()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#removeUnusedStyles--) pour supprimer tous les styles inutilisés à l'intérieur du classeur.  
{{% /alert %}}  

Le code suivant explique l'utilisation de [**Workbook.removeUnusedStyles()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#removeUnusedStyles--). Le code charge le [fichier Excel modèle](5115520.xlsx) que vous pouvez télécharger via le lien fourni. Il contient un style inutilisé nommé **AsposeStyle** ; ce style et tous les autres styles inutilisés seront supprimés après exécution du code.  

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Template-With-Unused-Custom-Style.xlsx");

// Load template excel file containing unused styles
const workbook = new AsposeCells.Workbook(filePath);

// Remove all unused styles inside the template this will also remove AsposeStyle which is an unused style inside the template
workbook.removeUnusedStyles();

// Save the file
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

