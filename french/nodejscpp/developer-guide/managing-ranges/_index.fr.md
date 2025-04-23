---
title: Gestion des plages avec Node.js via C++
linktitle: Plages
type: docs
weight: 105
url: /fr/nodejs-cpp/managing-ranges/
description: Apprenez à gérer les plages dans Excel en utilisant Aspose.Cells for Node.js via C++. Créez des plages, définissez des valeurs, des styles et effectuez diverses opérations.
---

## **Introduction**

 Dans Excel, vous pouvez sélectionner plusieurs cellules avec une sélection par boîte de souris ; l’ensemble des cellules sélectionnées est appelé "Plage".

 Par exemple, vous pouvez cliquer avec le bouton gauche de la souris sur la cellule "A1" d’Excel, puis faire glisser jusqu’à la cellule "C4". La zone rectangulaire que vous avez sélectionnée peut également être facilement créée en tant qu’objet en utilisant Aspose.Cells for Node.js via C++.

 Voici comment créer une plage, mettre une valeur, définir un style et effectuer d’autres opérations sur l’objet "Plage".

## ** Gestion des plages avec Aspose.Cells for Node.js via C++**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contient une collection [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) fournit une collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells).

### **Créer une plage**

Lorsque vous souhaitez créer une zone rectangulaire qui s'étend sur A1:C4, vous pouvez utiliser le code suivant :

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Create Range
const range = cells.createRange("A1:C4");
```

### **Placer une valeur dans les cellules de la plage**

Imaginons que vous avez une plage de cellules qui s'étend sur A1:C4. La matrice contient 4 * 3 = 12 cellules. Les cellules individuelles de la plage sont disposées de manière séquentielle : Plage[0,0], Plage[0,1], Plage[0,2], Plage[1,0], Plage[1,1], Plage[1,2], Plage[2,0], Plage[2,1], Plage[2,2], Plage[3,0], Plage[3,1], Plage[3,2].

L'exemple suivant montre comment saisir des valeurs dans les cellules de la plage.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "RangeValueTest.xlsx");

// Create a Workbook
const workbook = new AsposeCells.Workbook();
// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Create Range
const range = cells.createRange("A1:C4");
// Put value
range.get(0, 0).setValue("A1");
range.get(0, 1).setValue("B1");
range.get(0, 2).setValue("C1");
range.get(3, 0).setValue("A4");
range.get(3, 1).setValue("B4");
range.get(3, 2).setValue("C4");
// Save the Workbook
workbook.save(filePath);
```

### **Définir le style des cellules de la plage**

 L’exemple suivant montre comment définir le style des cellules de la plage.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Creates a Workbook
const workbook = new AsposeCells.Workbook();
// Gets Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Creates Range
const range = cells.createRange("A1:C4");
// Puts value
range.get(0, 0).setValue("A1");
range.get(3, 2).setValue("C4");
// Sets Style
let style00 = workbook.createStyle();
style00.setPattern(AsposeCells.BackgroundType.Solid);
style00.setForegroundColor(new AsposeCells.Color(255, 0, 0)); // Red
range.get(0, 0).setStyle(style00);
let style32 = workbook.createStyle();
style32.setPattern(AsposeCells.BackgroundType.HorizontalStripe);
style32.setForegroundColor(new AsposeCells.Color(0, 255, 0)); // Green
range.get(3, 2).setStyle(style32);
// Saves the Workbook
workbook.save("RangeStyleTest.xlsx");
```

### **Obtenir la région actuelle de la plage**

CurrentRegion est une propriété qui renvoie un objet Range qui représente la région actuelle. 

La région actuelle est une plage délimitée par une combinaison de lignes vierges et de colonnes vierges. En lecture seule.

 En Excel, vous pouvez obtenir la zone CurrentRegion en :
 1. Sélectionnez une zone (range1) avec la boîte de souris.
 2. Cliquez sur "Accueil - Edition - Rechercher & Sélectionner - Aller à spécial - Région actuelle", ou utilisez "Ctrl+Shift+*", vous verrez Excel vous aider à sélectionner automatiquement une zone (range2). Une fois fait, range2 est la CurrentRegion de range1.

 Veuillez télécharger le fichier de test suivant, l’ouvrir dans Excel, utiliser la boîte de souris pour sélectionner une zone "A1:D7", puis cliquez sur "Ctrl+Shift+*", vous verrez la zone "A1:C3" sélectionnée.

[current_region.xlsx](current_region.xlsx)

 Essayez maintenant l'exemple suivant pour voir comment cela fonctionne avec Aspose.Cells :

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "current_region.xlsx");
// Create a Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Create Range
const src = cells.createRange("A1:D7");
// Get CurrentRegion
const A1C3 = src.getCurrentRegion();
```


## **Sujets avancés**
- [Plage AutoFill du fichier Excel](/cells/fr/nodejs-cpp/autofill-ranges/)
- [Copier des plages de cellules d'Excel](/cells/fr/nodejs-cpp/copy-ranges-of-Excel/)
- [Copier uniquement les données de la plage](/cells/fr/nodejs-cpp/copy-range-data-only/)
- [Copier les données de la plage avec le style](/cells/fr/nodejs-cpp/copy-range-data-with-style/)
- [Copier uniquement le style de la plage](/cells/fr/nodejs-cpp/copy-range-style-only/)
- [Créer l'union de la plage](/cells/fr/nodejs-cpp/create-union-range/)
- [Couper et coller la plage](/cells/fr/nodejs-cpp/cut-and-paste-cells/)
- [Supprimer les plages](/cells/fr/nodejs-cpp/delete-ranges-from-Excel/)
- [Obtenir le nombre de cellules, le décalage de la plage entière de colonne et de ligne entière](/cells/fr/nodejs-cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Insérer des plages](/cells/fr/nodejs-cpp/insert-ranges-to-Excel/)
- [Fusionner ou séparer la plage de cellules](/cells/fr/nodejs-cpp/merge-or-unmerge-range-of-cells/)
- [Déplacer une plage de cellules dans une feuille de calcul](/cells/fr/nodejs-cpp/move-range-of-cells-in-a-worksheet/)
- [Créer des plages nommées en fonction du classeur et de la feuille de calcul](/cells/fr/nodejs-cpp/create-workbook-and-worksheet-scoped-named-ranges/)
- [Rechercher et remplacer des données dans une plage](/cells/fr/nodejs-cpp/search-and-replace-data-in-a-range/)
