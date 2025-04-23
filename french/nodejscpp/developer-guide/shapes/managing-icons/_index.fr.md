---  
title: Ajoutez des icônes à la feuille de calcul avec Node.js via C++  
linktitle: Gestion des icônes  
type: docs  
weight: 100  
url: /fr/nodejs-cpp/insert-svg-to-excel/  
---  

## Ajouter des icônes à la feuille de calcul dans Aspose.Cells for Node.js via C++

Si vous avez besoin d'utiliser [Aspose.Cells](https://products.aspose.com/cells/) pour ajouter des 'icônes' dans un fichier Excel, alors ce document peut vous aider. 

L'interface Excel correspondant à l'opération d'insertion d'icône est la suivante : 

![](1.png)

- Sélectionnez la position de l'icône à insérer dans la feuille de calcul
- Cliquez gauche sur *Insérer*->*Icônes*
- Dans la fenêtre qui s'ouvre, sélectionnez l'icône dans le rectangle rouge de la figure ci-dessus
- Clique gauche sur *Insérer*, cela sera inséré dans le fichier Excel.

L'effet est le suivant :

![](2.png)

Ici, nous avons préparé un *exemple de code* pour vous aider à insérer des icônes en utilisant [Aspose.Cells](https://products.aspose.com/cells/). Il y a aussi un [fichier d'exemple](sample.xlsx) nécessaire et un [fichier de ressources d'icônes](icon.zip). Nous avons utilisé l'interface Excel pour insérer une icône avec le même effet d'affichage que le [fichier de ressources](icon.zip) dans le [fichier d'exemple](sample.xlsx).

### Node.js

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Read icon resource file data
const fileName = path.join(dataDir, "icon.svg");
const bytes = fs.readFileSync(fileName).buffer;

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the icon to the worksheet
sheet.getShapes().addIcons(3, 0, 7, 0, 100, 100, bytes, null);

// Set a prompt message
const c = sheet.getCells().get(8, 7);
c.putValue("Insert via Aspose.Cells");
const s = c.getStyle();
s.getFont().setColor(AsposeCells.Color.Blue);
c.setStyle(s);

// Save. You can check your icon in this way.
workbook.save("sample2.xlsx", AsposeCells.SaveFormat.Xlsx);
```

Lorsque vous exécutez le code ci-dessus dans votre projet, vous obtiendrez les résultats suivants :

![](3.png)  

