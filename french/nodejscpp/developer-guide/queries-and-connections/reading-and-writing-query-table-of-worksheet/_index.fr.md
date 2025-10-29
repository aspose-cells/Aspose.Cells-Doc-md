---
title: Lecture et écriture de la table de requête d’une feuille de calcul avec Node.js via C++
linktitle: Lecture et écriture de table de requêtes de feuille de calcul
type: docs
weight: 40
url: /fr/nodejs-cpp/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells fournit une collection Worksheet.QueryTables qui renvoie l'objet de type QueryTable par index. Il dispose des deux propriétés suivantes

- QueryTable.adjustColumnWidth
- QueryTable.preserveFormatting

Ce sont deux valeurs booléennes. Vous pouvez les afficher dans Microsoft Excel via Données > Connexions > Propriétés.

{{% /alert %}}

## Lecture et écriture de table de requêtes de feuille de calcul

Le code suivant lit la première QueryTable de la première feuille de calcul, puis affiche les deux propriétés de la QueryTable. Ensuite, il définit QueryTable.preserveFormatting à true.

Vous pouvez télécharger le fichier Excel source utilisé dans ce code et le fichier Excel de sortie généré par le code à partir des liens suivants.

- [Fichier Excel Source](5115533.xlsx)
- [Fichier Excel de Sortie](5115537.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample_queries.xlsx");
// Create workbook from source excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first Query Table
const qt = worksheet.getQueryTables().get(0);

// Print Query Table Data
console.log("Adjust Column Width: " + qt.getAdjustColumnWidth());
console.log("Preserve Formatting: " + qt.getPreserveFormatting());

// Now set Preserve Formatting to true
qt.setPreserveFormatting(true);

// Save the workbook
workbook.save(path.join(dataDir, "Output_out.xlsx"));
```

### Sortie de la Console

Voici la sortie de la console du code d'exemple ci-dessus

{{< highlight java >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## Récupérer la plage de résultats de la table de requête

Aspose.Cells offre la possibilité de lire l'adresse, c'est-à-dire la plage de résultats des cellules pour une table de requête. Le code suivant démontre cette fonctionnalité en lisant l'adresse de la plage de résultats pour une table de requête. Le fichier d'exemple peut être téléchargé [ici](72417290.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample_queries.xlsx");

// Create workbook from source excel file
const wb = new AsposeCells.Workbook(filePath);

// Display the address(range) of result range of query table
console.log(wb.getWorksheets().get(0).getQueryTables().get(0).getResultRange().getAddress());
```
{{< app/cells/assistant language="nodejs-cpp" >}}
