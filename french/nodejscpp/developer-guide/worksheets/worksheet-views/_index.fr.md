---
title: Vues de feuille de calcul avec Node.js via C++
linktitle: Vues de la feuille de calcul
type: docs
weight: 40
url: /fr/nodejs-cpp/worksheet-views/
description: Cet article décrira comment utiliser Node.js et l API Node.js pour interagir avec l aperçu des sauts de page d un classeur Excel et des feuilles de calcul. Travailler avec des volets fractionnés, des volets figés et le facteur de zoom également.
---

## **Aperçu des sauts de page**

Toutes les feuilles de calcul peuvent être visualisées sous deux modes :

-Vue normale.
-Aperçu des sauts de page.

La vue normale est la vue par défaut d'une feuille de calcul. La prévisualisation des sauts de page est une vue de modification qui affiche une feuille de calcul tel qu'elle sera imprimée. La prévisualisation des sauts de page montre quelles données iront sur chaque page afin que vous puissiez ajuster la zone d'impression et les sauts de page. En utilisant Aspose.Cells for Node.js via C++, les développeurs peuvent activer la vue normale ou la prévisualisation des sauts de page.

### **Contrôle des modes d'affichage**

Aspose.Cells fournit une classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contient une collection [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) offre une vaste gamme de propriétés et de méthodes pour gérer les feuilles de calcul. Pour activer les modes d'affichage normal ou d'aperçu de saut de page, utilisez la propriété [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--) de la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--) est une propriété booléenne, ce qui signifie qu'elle ne peut stocker qu'une valeur **true** ou **false**.

#### **Activation de la vue normale**

Définissez une feuille de calcul en affichage normal en définissant la propriété [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--) de la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sur **false**.

#### **Activation de l'aperçu des sauts de page**

Définissez n'importe quelle feuille de calcul en aperçu de saut de page en définissant la propriété [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--) de la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sur **true**. Ce faisant, la feuille de calcul passe de l'affichage normal à l'aperçu de saut de page.

Un exemple complet est donné ci-dessous qui démontre comment utiliser la propriété [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--) pour activer le mode d'aperçu de saut de page pour la première feuille de calcul d'un fichier Excel.

Le fichier book1.xls est ouvert en créant une instance de la classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook). La vue est basculée en aperçu de saut de page pour la première feuille de calcul en définissant la propriété [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isPageBreakPreview--) sur **true**. Le fichier modifié est enregistré sous le nom output.xls.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");


// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Displaying the worksheet in page break preview
worksheet.setIsPageBreakPreview(true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Facteur de zoom**

### **Utilisation de Microsoft Excel**

Microsoft Excel offre une fonctionnalité permettant aux utilisateurs de définir le zoom ou le facteur d'échelle d'une feuille de calcul. Cette fonctionnalité aide les utilisateurs à voir le contenu de la feuille de calcul dans des vues plus petites ou plus grandes. Les utilisateurs peuvent définir le facteur de zoom sur n'importe quelle valeur.

### **Aspose.Cells & Facteur de zoom**

Aspose.Cells permet aux développeurs de définir le facteur de zoom de la feuille de calcul.
Aspose.Cells fournit une classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contient une collection [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) offre une vaste gamme de propriétés et de méthodes pour gérer les feuilles de calcul. Pour définir le facteur de zoom d'une feuille de calcul, utilisez la propriété [**Worksheet.getZoom()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getZoom--) de la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Le facteur de zoom est défini en attribuant une valeur numérique (entier) à la propriété [**Worksheet.getZoom()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getZoom--).

Un exemple complet est donné ci-dessous qui démontre comment utiliser la propriété [**Worksheet.getZoom()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getZoom--) pour définir le facteur de zoom de la première feuille du fichier Excel.

Le fichier book1.xls est ouvert en créant une instance de la classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook). Le facteur de zoom de la première feuille de calcul est défini à 75 et le fichier modifié est enregistré sous le nom de output.xls.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the zoom factor of the worksheet to 75
worksheet.setZoom(75);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Figer les volets**

### **Utilisation de Microsoft Excel**

Les volets figés sont une fonctionnalité fournie par Microsoft Excel. Le fait de figer les volets vous permet de sélectionner des données à rester visibles lors du défilement dans une feuille de calcul.

### **Aspose.Cells & Les Volets Figés**

Aspose.Cells permet aux développeurs d'appliquer des volets figés sur des feuilles de calcul à l'exécution.

Aspose.Cells fournit une classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contient une collection [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) fournit une large gamme de propriétés et de méthodes pour gérer les feuilles de calcul. Pour configurer des volets gelés, appelez la méthode [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-) de la classe Worksheet. La méthode [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-) prend les paramètres suivants :

- **Ligne**, l'index de la ligne de la cellule à partir de laquelle le gel commencera.
- **Colonne**, l'index de la colonne de la cellule à partir de laquelle le gel commencera.
- **Lignes gelées**, le nombre de lignes visibles dans le volet supérieur.
- **Colonnes gelées**, le nombre de colonnes visibles dans le volet de gauche.

Le fichier book1.xls est ouvert en appelant le constructeur de la classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) lors de son instanciation et quelques lignes et colonnes sont figées dans la première feuille de calcul. Le fichier modifié est enregistré sous le nom de output.xls.

Un exemple complet est donné ci-dessous qui montre comment utiliser la méthode [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-) pour figer des lignes et des colonnes (à partir de C4, représenté par la 4e ligne et la 3e colonne, où les lignes et les colonnes commencent à partir de l'index 0) de la première feuille de calcul du fichier Excel.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fs = require("fs");
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Applying freeze panes settings
worksheet.freezePanes(3, 2, 3, 2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));

// The file stream will be automatically closed after saving
```

## **Diviser les volets**

Si vous avez besoin de diviser l'écran pour obtenir deux vues différentes dans la même feuille de calcul, utilisez la fonction de division des volets. Microsoft Excel propose une fonctionnalité très pratique qui vous permet de voir plus d'une copie de votre feuille de calcul, et de pouvoir faire défiler indépendamment chaque volet de votre feuille de calcul : diviser les volets.

Les volets fonctionnent simultanément. Si vous apportez une modification dans l'un, la modification apparaît simultanément dans l'autre. Aspose.Cells fournit la fonctionnalité de diviser les volets aux utilisateurs.

### **Application et Suppression des Volets Divisés**

#### **Division des Volets**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) offre une large gamme de propriétés et de méthodes pour gérer un fichier Excel. Pour implémenter des vues divisées, utilisez la méthode [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) de la classe [**Worksheet.split()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#split--). Pour supprimer les volets divisés, utilisez la méthode [**Worksheet.removeSplit()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#removeSplit--).

Dans l'exemple, nous utilisons un fichier de modèle simple qui est chargé, puis la fonctionnalité de volets divisés est appliquée sur une cellule dans la première feuille de calcul. Le fichier mis à jour est enregistré.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate a new workbook and Open a template file
const book = new AsposeCells.Workbook(filePath);

// Set the active cell
book.getWorksheets().get(0).setActiveCell("A20");

// Split the worksheet window
book.getWorksheets().get(0).split();

// Save the excel file
book.save(path.join(dataDir, "output.xls"));
```

Après l'exécution du code ci-dessus, le fichier généré aura une vue fractionnée.

#### **Suppression de volets**

Supprimer les volets fractionnés en utilisant la méthode [**Worksheet.removeSplit()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#removeSplit--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate a new workbook and Open a template file
const workbook = new AsposeCells.Workbook(filePath);

// Set the active cell
workbook.getWorksheets().get(0).setActiveCell("A20");

// Split the worksheet window
workbook.getWorksheets().get(0).removeSplit();

// Save the excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Sujets avancés**
- [Masquer l'affichage des valeurs nulles dans la feuille de calcul](/cells/fr/nodejs-cpp/hiding-the-display-of-zero-values-in-the-worksheet/)
- [Définir la couleur d'onglet de feuille de calcul](/cells/fr/nodejs-cpp/set-worksheet-tab-color/)
- [Afficher et masquer les quadrillages, les en-têtes de lignes et de colonnes](/cells/fr/nodejs-cpp/show-and-hide-gridlines-and-row-column-headers/)
- [Afficher et masquer les lignes, les colonnes et les barres de défilement](/cells/fr/nodejs-cpp/show-and-hide-rows-columns-and-scroll-bars/)
- [Afficher et masquer les feuilles de calcul et les onglets](/cells/fr/nodejs-cpp/show-and-hide-worksheets-and-tabs/)
- [Afficher les formules au lieu des valeurs dans une feuille de calcul](/cells/fr/nodejs-cpp/show-formulas-instead-of-values-in-a-worksheet/)
- [Utiliser les options de vérification des erreurs](/cells/fr/nodejs-cpp/use-error-checking-options/)

{{< app/cells/assistant language="nodejs-cpp" >}}
