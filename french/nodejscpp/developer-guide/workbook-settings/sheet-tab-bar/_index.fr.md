---  
title: Comment contrôler la barre d onglets de la feuille avec Node.js via C++  
linktitle: Comment contrôler la barre d onglets de feuilles  
type: docs  
weight: 600  
url: /fr/nodejs-cpp/how-to-control-sheet-tab-bar/  
description: Apprenez à contrôler la barre d onglets de la feuille en utilisant Aspose.Cells for Node.js via C++.  
keywords: Comment contrôler la barre d onglets de feuille avec Node.js via C++, gérer la barre d onglets de feuille avec Node.js via C++, définir la barre d onglets de feuille avec Node.js via C++, contrôler la barre d onglets de feuille avec Node.js via C++.  
---  

## **Scénarios d'utilisation possibles**  
Lorsque vous devez ajuster l'affichage de la barre de feuille Excel, vous devez savoir comment contrôler la barre d'onglets, comme masquer ou afficher la barre d'onglets, changer la largeur de la barre d'onglets, spécifier le premier onglet visible, etc. Aspose.Cells for Node.js via C++ prend en charge ces fonctionnalités. Aspose.Cells fournit les propriétés et méthodes suivantes pour vous aider à atteindre vos objectifs.

- [**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--)
- [**WorkbookSettings.getSheetTabBarWidth()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getSheetTabBarWidth--)
- [**WorkbookSettings.getFirstVisibleTab()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getFirstVisibleTab--)

## **Comment contrôler la barre d'onglets de la feuille avec Aspose.Cells for Node.js via C++**  
Cet exemple montre comment :

1. Créer un classeur.
1. Ajouter des données aux cellules dans la première feuille de calcul.
1. Affichez l'onglet de feuille et définissez la largeur de la barre d'onglets.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the newly added worksheet
const ws = workbook.getWorksheets().get(0);
const cells = ws.getCells();

// Setting the value to the cells
let cell = cells.get("A1");
cell.putValue("Fruit");
cell = cells.get("B1");
cell.putValue("Count");
cell = cells.get("C1");
cell.putValue("Price");

cell = cells.get("A2");
cell.putValue("Apple");
cell = cells.get("A3");
cell.putValue("Mango");
cell = cells.get("A4");
cell.putValue("Blackberry");
cell = cells.get("A5");
cell.putValue("Cherry");

// Display the sheet tab and set the width of the tab bar
workbook.getSettings().setShowTabs(true);
workbook.getSettings().setSheetTabBarWidth(150);

workbook.save("out.xlsx");
```

Aperçu du fichier résultat:  
<br>  
<image src="result.png" width="70%" />  


