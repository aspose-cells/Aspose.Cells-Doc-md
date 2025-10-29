---
title: Calcul de la formule matricielle des tables de données avec Node.js via C++
linktitle: Calcul de la formule de tableau de données
description: Comment utiliser la bibliothèque Aspose.Cells pour calculer les formules matricielles d une table de données dans Microsoft Excel en utilisant Node.js via C++. Chargez ou créez un fichier Excel, calculez la formule matricielle, et enregistrez le fichier modifié.
keywords: Aspose.Cells, Excel, tables de données, formules matricielles, calculs Node.js via C++
type: docs
weight: 70
url: /fr/nodejs-cpp/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}}

Vous pouvez créer une table de données dans Microsoft Excel en utilisant Données > Analyse hypothèse > Table de données.... Aspose.Cells vous permet maintenant de calculer la formule matricielle d’une table de données. Veuillez utiliser [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) normalement pour calculer tout type de formules.

{{% /alert %}}

Dans le code d'exemple suivant, nous avons utilisé le [fichier Excel source](5115535.xlsx). Si vous changez la valeur de la cellule B1 à 100, les valeurs du tableau de données qui sont remplies de couleur jaune deviendront 120 comme indiqué dans les images suivantes. Le code d'exemple génère le [PDF de sortie](5115538.pdf).

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

Voici le code d'exemple utilisé pour générer le [PDF de sortie](5115538.pdf) à partir du [fichier Excel source](5115535.xlsx). Veuillez lire les commentaires pour plus d'informations.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook from source excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "DataTable.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// When you will put 100 in B1, then all Data Table values formatted as Yellow will become 120
worksheet.getCells().get("B1").putValue(100);

// Calculate formula, now it also calculates Data Table array formula
workbook.calculateFormula();

// Save the workbook in pdf format
workbook.save(path.join(dataDir, "output_out.pdf"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
