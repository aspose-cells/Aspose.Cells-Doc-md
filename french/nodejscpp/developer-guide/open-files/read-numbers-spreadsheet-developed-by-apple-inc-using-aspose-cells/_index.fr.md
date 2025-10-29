---
title: Lire le tableur Numbers développé par Apple Inc. avec Aspose.Cells for Node.js via C++
linktitle: Lire Numbers Spreadsheet Developpé par Apple Inc. en utilisant Aspose.Cells
type: docs
weight: 140
url: /fr/nodejs-cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/
description: Apprenez comment lire les tableurs Numbers développés par Apple Inc. avec Aspose.Cells for Node.js via C++. 
---

## **Scénarios d'utilisation possibles**

Numbers est une application de feuille de calcul développée par Apple Inc. Aspose.Cells peut lire les fichiers Numbers, mais ne supporte pas l’écriture dans ceux-ci. Il peut lire les données, le style, et les formules des fichiers Numbers.

## **Lecture du tableur Numbers développé par Apple Inc. avec Aspose.Cells for Node.js via C++**

Le code d’exemple suivant charge le [Exemple de feuille Numbers](sampleNumbersByAppleInc.numbers) et le convertit en [Format PDF de sortie](outputNumbersByAppleInc.pdf). Vous devrez utiliser la classe [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) et spécifier [**LoadFormat.Numbers**](https://reference.aspose.com/cells/nodejs-cpp/loadformat) comme paramètre dans son constructeur pour le charger avec succès. Téléchargez-les tous deux depuis les liens donnés. Vous pouvez essayer le code avec n’importe quelle feuille Numbers. Veuillez également lire les commentaires du code pour plus d’aide.

## **Code d'exemple**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleNumbersByAppleInc.numbers");
const outputFilePath = path.join(dataDir, "outputNumbersByAppleInc.pdf");

// Specify load options, we want to load Numbers spreadsheet
const opts = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Numbers);

// Load the Numbers spreadsheet in workbook with above load options
const wb = new AsposeCells.Workbook(sourceFilePath, opts);

// Save the workbook to pdf format
wb.save(outputFilePath, AsposeCells.SaveFormat.Pdf);
```

{{< app/cells/assistant language="nodejs-cpp" >}}
