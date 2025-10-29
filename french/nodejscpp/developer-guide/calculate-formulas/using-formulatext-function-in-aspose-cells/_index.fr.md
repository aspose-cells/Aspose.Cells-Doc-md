---
title: Utiliser la fonction FormulaText dans Aspose.Cells for Node.js via C++
linktitle: Utilisation de la fonction FormulaText dans Aspose.Cells
description: Cet article explique comment utiliser la fonction FormulaText dans la bibliothèque Aspose.Cells pour traiter les formules dans Microsoft Excel. Apprenez à obtenir et définir le texte de la formule des cellules et à sauvegarder les fichiers Excel modifiés en utilisant Node.js via C++.
keywords: Aspose.Cells, Excel, fonctions FormulaText Node.js via C++
type: docs
weight: 60
url: /fr/nodejs-cpp/using-formulatext-function-in-aspose-cells/
---

{{% alert color="primary" %}} 

FormulaText est une fonction Excel 2013 et ultérieure. Elle n'est pas supportée par les versions antérieures comme Excel 2010 ou 2007, etc. Comme son nom l'indique, elle affiche le texte de la formule présente dans une cellule donnée. Cet article montre comment utiliser cette fonction avec Aspose.Cells for Node.js via C++.

{{% /alert %}} 

Le code d'exemple suivant montre l'utilisation de FormulaText avec Aspose.Cells for Node.js via C++. Le code écrit d'abord une formule dans la cellule A1, puis affiche le texte de la formule en utilisant FormulaText dans la cellule A2.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create a workbook object
// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Put some formula in cell A1
const cellA1 = worksheet.getCells().get("A1");
cellA1.setFormula("=Sum(B1:B10)");

// Get the text of the formula in cell A2 using FORMULATEXT function
const cellA2 = worksheet.getCells().get("A2");
cellA2.setFormula("=FormulaText(A1)");

// Calculate the workbook
workbook.calculateFormula();

// Print the results of A2, It will now print the text of the formula inside cell A1
console.log(cellA2.getStringValue());
```
## **Sortie console**
Voici la sortie de la console du code d'exemple ci-dessus.

{{< highlight java >}}

 =SUM(B1:B10)

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
