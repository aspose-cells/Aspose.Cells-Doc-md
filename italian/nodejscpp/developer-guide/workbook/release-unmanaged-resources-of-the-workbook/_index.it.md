---
title: Rilascia risorse non gestite del workbook con Node.js tramite C++
linktitle: Rilascia le risorse non gestite del libro di lavoro
type: docs
weight: 310
url: /it/nodejs-cpp/release-unmanaged-resources-of-the-workbook/
description: Impara come rilasciare le risorse non gestite dell’oggetto Workbook usando Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Aspose.Cells fornisce il metodo [**Workbook.dispose()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#dispose--) per rilasciare le risorse non gestite dell’oggetto [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook). Il pattern dispose viene usato solo per oggetti che accedono a risorse non gestite, come handle di file e pipe, handle del registro di sistema, handle di attesa o puntatori a blocchi di memoria non gestita. Questo perché il garbage collector è molto efficiente nel recuperare gli oggetti gestiti inutilizzati, ma non può recuperare gli oggetti non gestiti.

{{% /alert %}}

L’oggetto [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) ora implementa l’interfaccia *System.IDisposable* che ha un singolo metodo [**Workbook.dispose()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#dispose--). Puoi chiamare direttamente il metodo [**Workbook.dispose()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#dispose--) oppure usare la dichiarazione *Using* per chiamarlo automaticamente.

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
{{< app/cells/assistant language="nodejs-cpp" >}}
