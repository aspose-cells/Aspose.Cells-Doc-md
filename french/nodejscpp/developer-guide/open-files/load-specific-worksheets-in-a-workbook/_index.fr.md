---
title: Charger des feuilles de calcul spécifiques dans un classeur avec Node.js via C++
linktitle: Charger des feuilles de calcul spécifiques dans un classeur
type: docs
weight: 100
url: /fr/nodejs-cpp/load-specific-worksheets-in-a-workbook/
description: Découvrez comment charger des feuilles de calcul spécifiques dans un classeur en utilisant Aspose.Cells for Node.js via C++. Améliorez les performances et réduisez la consommation de mémoire.
---

{{% alert color="primary" %}}

Par défaut, Aspose.Cells charge l'intégralité de la feuille de calcul en mémoire. Il est possible de charger uniquement des feuilles spécifiques. Cela peut améliorer les performances et consommer moins de mémoire. Cette approche est utile lorsqu'on travaille avec un grand classeur composé de nombreuses feuilles de calcul.

{{% /alert %}}

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Define a new Workbook.
let workbook;

// Load the workbook with the specified worksheet only.
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
loadOptions.setLoadFilter(new CustomLoad());

// Create the workbook.
workbook = new AsposeCells.Workbook(path.join(dataDir, "TestData.xlsx"), loadOptions);

// Perform your desired task.

// Save the workbook.
workbook.save(path.join(dataDir, "outputFile.out.xlsx"));
```

Voici l’implémentation de la classe CustomLoad.

```javascript
const AsposeCells = require("aspose.cells.node");

class CustomLoad extends AsposeCells.LoadFilter {
startSheet(sheet) {
if (sheet.getName() === "Sheet2") {
// Load everything from worksheet "Sheet2"
this.setLoadDataFilterOptions(AsposeCells.LoadDataFilterOptions.All);
} else {
// Load nothing
this.setLoadDataFilterOptions(AsposeCells.LoadDataFilterOptions.Structure);
}
}
}
```


