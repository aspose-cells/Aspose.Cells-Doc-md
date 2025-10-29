---
title: Copier et déplacer des feuilles de calcul dans et entre des classeurs avec Node.js via C++
linktitle: Copier et Déplacer des Feuilles de Calcul Dans et Entre des Classeurs
type: docs
weight: 80
url: /fr/nodejs-cpp/copy-and-move-worksheets-within-and-between-workbooks/
description: Découvrez comment copier et déplacer des feuilles de calcul dans et entre des classeurs en utilisant Aspose.Cells for Node.js via C++. Gérez efficacement la structure de vos classeurs.
---

{{% alert color="primary" %}}

Parfois, vous avez besoin d'un certain nombre de feuilles de calcul avec une mise en forme commune et une saisie de données. Par exemple, si vous travaillez avec des budgets trimestriels, vous voudrez peut-être créer un classeur avec des feuilles contenant les mêmes en-têtes de colonnes, en-têtes de lignes et formules. Il y a une façon de faire cela : en créant une feuille, puis en la copiant trois fois.

Aspose.Cells for Node.js via C++ prend en charge la copie ou le déplacement de feuilles de calcul dans ou entre des classeurs. Les feuilles y compris les données, la mise en forme, les tableaux, les matrices, les graphiques, les images, et autres objets sont copiés avec la plus grande précision.

{{% /alert %}}

## **Copier et Déplacer des Feuilles de calcul**

### **Copier une Feuille de Calcul à l'Intérieur d'un Classeur**

Les étapes initiales sont les mêmes pour tous les exemples.

1. Créez deux classeurs avec des données dans Microsoft Excel. Dans le cadre de cet exemple, nous avons créé deux nouveaux classeurs dans Microsoft Excel et saisi certaines données dans les feuilles de calcul.

- FirstWorkbook.xlsx (3 feuilles de calcul).
- SecondWorkbook.xlsx (1 feuille de calcul).

1. Téléchargez et installez Aspose.Cells :
   1. [Téléchargez Aspose.Cells for Node.js via C++](https://downloads.aspose.com/cells/nodejs-cpp).
   1. Installez-le sur votre ordinateur de développement.
      Tous les composants [Aspose](http://www.aspose.com/), une fois installés, fonctionnent en mode d'évaluation. Le mode d'évaluation n'a pas de limite de temps et il ne fait qu'ajouter des filigranes aux documents produits.
1. Créer un projet :
   1. Démarrez votre environnement de développement.
   1. Créez une nouvelle application console.
1. Ajouter des références:
   1. Ajoutez une référence à Aspose.Cells dans le projet.
      Par exemple, ajoutez une référence à ...\Program Files\Aspose\Aspose.Cells\Bin\NodeJs\Aspose.Cells.dll
1. Copiez la feuille de calcul dans un classeur
   Le premier exemple copie la première feuille de calcul (Copie) dans FirstWorkbook.xlsx.

Lors de l'exécution du code, la feuille de calcul nommée Copie est copiée dans FirstWorkbook.xlsx avec le nom Dernière Feuille.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open a file into the first book.
const excelWorkbook1 = new AsposeCells.Workbook(path.join(dataDir, "FirstWorkbook.xlsx"));

// Copy the first sheet of the first book within the workbook
excelWorkbook1.getWorksheets().get(2).copy(excelWorkbook1.getWorksheets().get("Copy"));

// Save the file.
excelWorkbook1.save(path.join(dataDir, "FirstWorkbookCopied_out.xlsx"));
```

### **Déplacer une feuille de calcul dans un classeur**

Le code ci-dessous montre comment déplacer une feuille de calcul d'une position à une autre dans un classeur. En exécutant le code, la feuille de calcul appelée Déplacer de l'index 1 à l'index 2 dans FirstWorkbook.xlsx.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "FirstWorkbook.xlsx");
// Open a file into the first book.
const excelWorkbook2 = new AsposeCells.Workbook(filePath);

// Move the sheet
const worksheets = excelWorkbook2.getWorksheets();
const worksheet = worksheets.get(0);
worksheet.moveTo(1);

// Save the file.
excelWorkbook2.save(path.join(dataDir, "FirstWorkbookMoved_out.xlsx"));
```

### **Copier une feuille de calcul entre des classeurs**

L'exécution du code copie la feuille nommée Copy dans SecondWorkbook.xlsx avec le nom Sheet2.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const excelWorkbook3 = new AsposeCells.Workbook();
const excelWorkbook4 = new AsposeCells.Workbook();

// Create source worksheet
excelWorkbook3.getWorksheets().add("Copy");

// Add new worksheet into second Workbook
excelWorkbook4.getWorksheets().add();

// Copy the first sheet of the first book into second book.
excelWorkbook4.getWorksheets().get(1).copy(excelWorkbook3.getWorksheets().get("Copy"));

// Save the file.
excelWorkbook4.save(path.join(dataDir, "CopyWorksheetsBetweenWorkbooks_out.xlsx"));
```

### **Déplacer une feuille de calcul entre des classeurs**

En exécutant le code, la feuille de calcul nommée Déplacer de FirstWorkbook.xlsx est déplacée vers SecondWorkbook.xlsx avec le nom Feuille3.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create new workbooks instead of opening existing files
const excelWorkbook5 = new AsposeCells.Workbook();
const excelWorkbook6 = new AsposeCells.Workbook();

// Add New Worksheet
excelWorkbook6.getWorksheets().add();

// Copy the sheet from first book into second book.
excelWorkbook6.getWorksheets().get(0).copy(excelWorkbook5.getWorksheets().get(0));

// Remove the copied worksheet from first workbook
excelWorkbook5.getWorksheets().removeAt(0);

// Save the file.
excelWorkbook5.save(path.join(dataDir, "FirstWorkbookWithMove_out.xlsx"));

// Save the file.
excelWorkbook6.save(path.join(dataDir, "SecondWorkbookWithMove_out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
