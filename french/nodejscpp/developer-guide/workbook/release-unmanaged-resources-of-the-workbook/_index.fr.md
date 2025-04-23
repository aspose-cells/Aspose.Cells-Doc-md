---
title: Libérer les ressources non gérées du classeur avec Node.js via C++
linktitle: Libérer les ressources non gérées du classeur
type: docs
weight: 310
url: /fr/nodejs-cpp/release-unmanaged-resources-of-the-workbook/
description: Apprenez comment libérer les ressources non gérées de l objet Workbook en utilisant Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Aspose.Cells fournit la méthode [**Workbook.dispose()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#dispose--) pour libérer les ressources non gérées de l'objet [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook). Le modèle de disposition est utilisé uniquement pour les objets qui accèdent à des ressources non gérées, telles que les poignées de fichiers et de tuyaux, les poignées de registre, les poignées d'attente, ou les pointeurs vers des blocs de mémoire non gérée. Cela est dû au fait que le ramasse-miettes est très efficace pour récupérer les objets gérés inutilisés, mais incapable de récupérer les objets non gérés.

{{% /alert %}}

L'objet [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) implémente maintenant l'interface *System.IDisposable* qui possède une seule méthode [**Workbook.dispose()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#dispose--). Vous pouvez soit appeler directement la méthode [**Workbook.dispose()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#dispose--) ou utiliser la déclaration *Using* pour l'appeler automatiquement.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create workbook object
const wb1 = new AsposeCells.Workbook();

// Call Dispose method
wb1.dispose();

// Call Dispose method via a scoped approach
(async () => {
const wb2 = new AsposeCells.Workbook();
// Any other code goes here
wb2.dispose();
})();
```
