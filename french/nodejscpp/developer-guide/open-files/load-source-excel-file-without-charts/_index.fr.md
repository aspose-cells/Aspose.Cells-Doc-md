---
title: Charger un fichier Source Excel sans graphiques avec Node.js via C++
linktitle: Charger le fichier Excel source sans graphiques
type: docs
weight: 420
url: /fr/nodejs-cpp/load-source-excel-file-without-charts/
description: Découvrez comment charger un fichier Excel sans graphiques en utilisant Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Aspose.Cells vous permet de charger votre fichier Excel sans graphiques. Veuillez utiliser la propriété [**LoadOptions.getLoadFilter()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--) à cette fin.

{{% /alert %}}

## **Charger la feuille de calcul sans graphiques**

Le code d’exemple suivant charge le fichier Excel d’exemple sans graphiques et le sauvegarde au format PDF en sortie.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the load options and filter the data
const options = new AsposeCells.LoadOptions();

// Include everything except charts
options.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.Chart));

// Load the workbook with specified load options
const workbook = new AsposeCells.Workbook(path.join(dataDir, "chart.xlsx"), options);

// Save the workbook in PDF format
workbook.save(path.join(dataDir, "ResultWithoutChart.pdf"), AsposeCells.SaveFormat.Pdf);
```
