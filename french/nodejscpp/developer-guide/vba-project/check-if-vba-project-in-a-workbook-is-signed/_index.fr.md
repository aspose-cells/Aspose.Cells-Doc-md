---
title: Vérifier si le projet VBA dans un classeur est signé avec Node.js via C++
linktitle: Vérifier si le projet VBA dans un classeur est signé
type: docs
weight: 70
url: /fr/nodejs-cpp/check-if-vba-project-in-a-workbook-is-signed/
description: Apprenez comment vérifier si un projet VBA dans un classeur est signé en utilisant Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Vous pouvez vérifier si votre projet VBA est signé ou non en utilisant Microsoft Excel via la commande de menu **Outils > Signatures numériques...** De même, vous pouvez le vérifier de manière programmatique en utilisant la propriété Aspose.Cells [**Workbook.getVbaProject()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getVbaProject--).

{{% /alert %}}

## **Vérifier si le projet VBA dans un classeur est signé dans Node.js**

Le code suivant charge le classeur et vérifie si son projet VBA est signé en utilisant la propriété [**Workbook.getVbaProject()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getVbaProject--). La propriété retournera **true** si le projet est signé, sinon elle retournera **false**.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample1.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
console.log("VBA Project is Signed: " + workbook.getVbaProject().isSigned());
```
