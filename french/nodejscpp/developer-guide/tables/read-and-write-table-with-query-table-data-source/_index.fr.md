---
title: Lire et écrire une table avec la source de données Query Table via Node.js
linktitle: Lire et écrire un tableau avec la source de données de table de requête
type: docs
weight: 30
url: /fr/nodejs-cpp/read-and-write-table-with-query-table-data-source/
description: Apprenez comment lire et écrire une table avec une source de données QueryTable en utilisant Aspose.Cells for Node.js via C++. 
---

## **Lire et Écrire un Tableau avec une Source de Données de Table de Requête**
Avec Aspose.Cells for Node.js via C++, vous pouvez lire et écrire une table qui a un QueryTable comme source de données. La prise en charge de cette fonctionnalité existe également pour les fichiers XLS. Le code suivant montre comment lire et écrire une telle table en lisant d'abord la table puis en la modifiant pour ajouter la ligne des totaux.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the source directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load workbook object
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SampleTableWithQueryTable.xls"));

const worksheet = workbook.getWorksheets().get(0);

const table = worksheet.getListObjects().get(0);

// Check the data source type if it is query table
if (table.getDataSourceType() === AsposeCells.TableDataSourceType.QueryTable) {
table.setShowTotals(true);
}

// Save the file
workbook.save(path.join(outputDir, "SampleTableWithQueryTable_out.xls"));
```

Les fichiers Excel source et de sortie sont joints pour référence.

[Fichier source](96928091.xls)

[Fichier de sortie](96928092.xls)
{{< app/cells/assistant language="nodejs-cpp" >}}
