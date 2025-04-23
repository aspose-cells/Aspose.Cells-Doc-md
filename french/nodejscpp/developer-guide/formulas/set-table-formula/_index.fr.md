---
title: Propager une formule dans un tableau ou un objet liste automatiquement lors de la saisie de nouvelles lignes avec Node.js via C++
linktitle: Définit la formule de tableau
type: docs
weight: 260
url: /fr/nodejs-cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
description: Apprenez comment propager automatiquement les formules dans les tableaux ou objets de liste lors de la saisie de nouvelles données en utilisant Aspose.Cells for Node.js via C++.
---

## **Scénarios d'utilisation possibles**
Parfois, vous souhaitez qu'une formule dans votre tableau ou objet de liste se propage automatiquement aux nouvelles lignes lors de la saisie de nouvelles données. C'est le comportement par défaut de Microsoft Excel. Pour réaliser la même fonctionnalité avec Aspose.Cells for Node.js via C++, veuillez utiliser la propriété [ListColumn.getFormula()](https://reference.aspose.com/cells/nodejs-cpp/listcolumn/#getFormula--).

## **Propagation automatique de la formule dans un tableau ou objet de liste lors de la saisie de nouvelles données**
Le code d'exemple suivant crée un tableau ou objet de liste de manière à ce que la formule dans la colonne B se propage automatiquement aux nouvelles lignes lorsque vous saisissez de nouvelles données. Veuillez vérifier le [fichier Excel généré](5115469.xlsx) avec ce code. Si vous entrez un quelconque chiffre dans la cellule A3, vous verrez que la formule dans la cellule B2 se propage automatiquement à la cellule B3.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const book = new AsposeCells.Workbook();

// Access first worksheet
const sheet = book.getWorksheets().get(0);

// Add column headings in cell A1 and B1
sheet.getCells().get(0, 0).putValue("Column A");
sheet.getCells().get(0, 1).putValue("Column B");

// Add list object, set its name and style
const listObject = sheet.getListObjects().get(sheet.getListObjects().add(0, 0, 1, sheet.getCells().getMaxColumn(), true));
listObject.setTableStyleType(AsposeCells.TableStyleType.TableStyleMedium2);
listObject.setDisplayName("Table");

// Set the formula of second column so that it propagates to new rows automatically while entering data
listObject.getListColumns().get(1).setFormula("=[Column A] + 1");

// Save the workbook in xlsx format
book.save(path.join(dataDir, "output_out.xlsx"));
```
