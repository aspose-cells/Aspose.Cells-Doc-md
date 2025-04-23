---  
title: Geler les volets de la feuille de calcul Excel avec Node.js via C++  
linktitle: Geler les volets  
type: docs  
weight: 190  
url: /fr/nodejs-cpp/how-to-freeze-panes-of-excel-worksheet  
description: Dans cet article, vous apprendrez comment geler les volets des feuilles de calcul Excel de manière programmatique en utilisant Aspose.Cells for Node.js via C++.  
keywords: Geler les volets, Geler la fenêtre.  
---  

## **Introduction**  

Dans cet article, nous verrons comment geler les volets. Lorsque vous avez une grande quantité de données sous un en-tête commun, vous ne pouvez pas voir l'en-tête lorsque vous faites défiler la feuille vers le bas. Et chaque enregistrement contient de nombreuses données. Vous pouvez geler les volets pour voir cette partie gelée même lorsque le reste des données est en cours de défilement. Vous pouvez facilement voir les en-têtes dans les premières lignes ou les premières colonnes. Geler et dégeler les volets ne modifient que la vue des données, sans changer les données elles-mêmes.  

## **Dans Excel**  

**![Geler les volets dans Excel](Freeze-panes.png)**  

1. Si vous souhaitez geler les volets, geler les lignes et les colonnes, sélectionnez d'abord une cellule (par exemple B2).  
2. Cliquez sur Affichage > Fenêtres figées.  
3. Dans le menu déroulant, cliquez sur Geler les volets.  
4. Si vous faites défiler vers le bas ou vers la droite, la première ligne et la première colonne restent figées.  

**![Fenêtres figées](Frozen-Panes.png)**  

 Comme vous pouvez le voir, la première ligne et la colonne A sont gelées, la deuxième ligne est la ligne 32 et la deuxième colonne visible est D.  

 Geler les volets vous permet de voir vos grandes données sans suivre les étiquettes de ligne ou de colonne.  

## ** Gel de volets avec Aspose.Cells for Node.js via C++**  
 Il est simple de geler les volets avec Aspose.Cells for Node.js via C++. Veuillez utiliser la méthode [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-) pour geler les volets à la cellule sélectionnée.  
1. Construisez un classeur pour ouvrir le fichier ou créez un fichier vide.  
2. Geler les volets avec la méthode Worksheet.freezePanes()  
3. Enregistrez le fichier.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Freeze.xlsx")); 
// Freezing panes at the cell B2
workbook.getWorksheets().get(0).freezePanes("B2", 1, 1);
// Saving the file
workbook.save("frozen.xlsx");
```  

Fichier Excel source [exemple joint](Freeze.xlsx).  

