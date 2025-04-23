---
title: Vérifier si le code VBA est signé avec Node.js via C++
linktitle: Vérifier si le code VBA est signé
type: docs
weight: 100
url: /fr/nodejs-cpp/check-if-vba-code-is-signed/
description: Apprenez comment vérifier si le projet de code VBA est signé en utilisant Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Aspose.Cells permet à l'utilisateur de vérifier si le projet de code VBA est signé ou non. Veuillez utiliser la propriété [**VbaProject.isSigned()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isSigned--) pour vérifier si le projet de code VBA est signé ou non.

{{% /alert %}}

Le code suivant explique comment vérifier si le code VBA est signé ou non en utilisant la propriété [**VbaProject.isSigned()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isSigned--). Vous pouvez utiliser n'importe lequel de vos fichiers Excel pour tester ce code. Pour les tests, vous pouvez utiliser [ce fichier Excel utilisé dans le code](5115032.xlsm).

## **Vérifier si le code VBA est signé dans Node.js**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleVBAProjectSigned.xlsm");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

console.log("Is VBA Code Project Signed: " + workbook.getVbaProject().isSigned());
```

## Sortie de la console

Ci-dessous se trouve la sortie de la console du code ci-dessus en utilisant le [fichier excel d'exemple](5115032.xlsm) fourni par le lien.

{{< highlight java >}}

Is VBA Code Project Signed: True

{{< /highlight >}}
