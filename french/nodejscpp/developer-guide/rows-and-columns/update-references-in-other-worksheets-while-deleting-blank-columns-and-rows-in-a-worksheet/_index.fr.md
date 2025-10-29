---
title: Mettre à jour les références dans d autres feuilles de calcul tout en supprimant les colonnes et les rangées vides dans une feuille de calcul
linktitle: Mettre à jour les références dans d autres feuilles de calcul tout en supprimant les colonnes et les rangées vides dans une feuille de calcul
type: docs
weight: 5000
url: /fr/nodejs-cpp/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
description: Apprenez comment maintenir les références dans d autres feuilles lors de la suppression de colonnes et lignes vides dans une feuille de calcul en utilisant Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Lorsque vous supprimez les colonnes et les rangées vides dans une feuille de calcul, les références dans d'autres feuilles de calcul deviennent invalides. Si vous souhaitez éviter ce comportement et que ces références de la feuille de calcul actuelle dans d'autres feuilles de calcul soient également mises à jour, veuillez utiliser la propriété [**DeleteOptions.getUpdateReference()**](https://reference.aspose.com/cells/nodejs-cpp/deleteoptions/#getUpdateReference--) et la définir sur **true**.

{{% /alert %}}

## **Mettre à jour les références dans d'autres feuilles de calcul tout en supprimant les colonnes et les rangées vides dans une feuille de calcul**

Veuillez consulter le code d'exemple ci-dessous et sa sortie dans la console. La cellule E3 dans la deuxième feuille a une formule =Sheet1!C3 qui fait référence à la cellule C3 dans la première feuille. Si vous définissez la propriété [**DeleteOptions.getUpdateReference()**](https://reference.aspose.com/cells/nodejs-cpp/deleteoptions/#getUpdateReference--) à **true**, cette formule sera mise à jour et deviendra =Sheet1!A1 lors de la suppression de colonnes et lignes vides dans la première feuille. Cependant, si vous définissez la propriété [**DeleteOptions.getUpdateReference()**](https://reference.aspose.com/cells/nodejs-cpp/deleteoptions/#getUpdateReference--) à **false**, la formule dans la cellule E3 de la deuxième feuille restera =Sheet1!C3 et deviendra invalide.

### **Exemple de programmation**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create workbook
const wb = new AsposeCells.Workbook();

// Add second sheet with name Sheet2
wb.getWorksheets().add("Sheet2");

// Access first sheet and add some integer value in cell C1
// Also add some value in any cell to increase the number of blank rows and columns
const sht1 = wb.getWorksheets().get(0);
sht1.getCells().get("C1").putValue(4);
sht1.getCells().get("K30").putValue(4);

// Access second sheet and add formula in cell E3 which refers to cell C1 in first sheet
const sht2 = wb.getWorksheets().get(1);
sht2.getCells().get("E3").setFormula("'Sheet1'!C1");

// Calculate formulas of workbook
wb.calculateFormula();

// Print the formula and value of cell E3 in second sheet before deleting blank columns and rows in Sheet1.
console.log("Cell E3 before deleting blank columns and rows in Sheet1.");
console.log("--------------------------------------------------------");
console.log("Cell Formula: " + sht2.getCells().get("E3").getFormula());
console.log("Cell Value: " + sht2.getCells().get("E3").getStringValue());

// If you comment DeleteOptions.UpdateReference property below, then the formula in cell E3 in second sheet will not be updated
const opts = new AsposeCells.DeleteOptions();
opts.setUpdateReference(true);

// Delete all blank rows and columns with delete options
sht1.getCells().deleteBlankColumns(opts);
sht1.getCells().deleteBlankRows(opts);

// Calculate formulas of workbook
wb.calculateFormula();

// Print the formula and value of cell E3 in second sheet after deleting blank columns and rows in Sheet1.
console.log("");
console.log("");
console.log("Cell E3 after deleting blank columns and rows in Sheet1.");
console.log("--------------------------------------------------------");
console.log("Cell Formula: " + sht2.getCells().get("E3").getFormula());
console.log("Cell Value: " + sht2.getCells().get("E3").getStringValue());
```

### **Sortie console**

Voici la sortie de la console du code d'exemple ci-dessus lorsque la propriété [**DeleteOptions.getUpdateReference()**](https://reference.aspose.com/cells/nodejs-cpp/deleteoptions/#getUpdateReference--) a été définie à **true**.

{{< highlight java >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!A1

Cell Value: 4

{{< /highlight >}}

Voici la sortie de la console du code d'exemple ci-dessus lorsque la propriété [**DeleteOptions.getUpdateReference()**](https://reference.aspose.com/cells/nodejs-cpp/deleteoptions/#getUpdateReference--) a été définie à **false**. Comme vous pouvez le voir, la formule dans la cellule E3 de la deuxième feuille n'est pas mise à jour et sa valeur de cellule est maintenant 0 au lieu de 4, ce qui est invalide.

{{< highlight java >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 0

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
