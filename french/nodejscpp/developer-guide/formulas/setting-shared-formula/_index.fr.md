---
title: Définir une formule partagée avec Node.js via C++
linktitle: Paramétrage de formule partagée
type: docs
weight: 10
url: /fr/nodejs-cpp/setting-shared-formula/
---

{{% alert color="primary" %}}

Si vous souhaitez ajouter une fonction dans une feuille de calcul qui effectuera des calculs, cet article explique comment réaliser cette tâche en utilisant Aspose.Cells for Node.js via C++.

{{% /alert %}}

## Définir une formule partagée avec Aspose.Cells for Node.js via C++

Supposons que vous ayez une feuille de calcul remplie de données dans le format qui ressemble à la feuille de calcul d'exemple suivante.

|**Fichier d'entrée avec une colonne de données**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

Vous souhaitez ajouter une fonction en B2 qui calculera la taxe de vente pour la première ligne de données. La taxe est de **9%**. La formule qui calcule la taxe de vente est: **"=A2*0.09"**. Cet article explique comment appliquer cette formule avec Aspose.Cells.

Aspose.Cells vous permet de spécifier une formule en utilisant la propriété [**Cell.getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFormula--). Il existe deux options pour ajouter des formules aux autres cellules (B3, B4, B5, etc.) de la colonne.

Faites soit ce que vous avez fait pour la première cellule, en définissant efficacement la formule pour chaque cellule, en mettant à jour la référence de cellule en conséquence (A3*0,09, A4*0,09, A5*0,09, etc.). Cela nécessite la mise à jour des références de cellule pour chaque ligne. Cela nécessite aussi que Aspose.Cells analyse chaque formule individuellement, ce qui peut prendre du temps pour de grands tableaux et des formules complexes. Cela ajoute également des lignes de code supplémentaires, bien que des boucles puissent les réduire quelque peu.

Une autre approche est d'utiliser une **formule partagée**. Avec une formule partagée, les formules sont automatiquement mises à jour pour les références de cellules dans chaque ligne afin que la taxe soit calculée correctement. La méthode [**Cell.setSharedFormula(string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setSharedFormula-string-number-number-) est plus efficace que la première méthode.

L'exemple suivant démontre comment l'utiliser.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a Workbook from existing file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "source.xlsx"));

// Get the cells collection in the first worksheet
const cells = workbook.getWorksheets().get(0).getCells();

// Apply the shared formula in the range i.e.., B2:B14
cells.get("B2").setSharedFormula("=A2*0.09", 13, 1);

// Save the excel file
workbook.save(path.join(dataDir, "Output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
