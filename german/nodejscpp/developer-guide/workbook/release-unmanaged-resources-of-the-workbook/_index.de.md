---
title: Unabhängige Ressourcen der Arbeitsmappe mit Node.js über C++ freigeben
linktitle: Freigeben unbeaufsichtigter Ressourcen der Arbeitsmappe
type: docs
weight: 310
url: /de/nodejs-cpp/release-unmanaged-resources-of-the-workbook/
description: Lernen Sie, wie Sie mit Aspose.Cells for Node.js via C++ die nicht verwalteten Ressourcen des Workbook Objekts freigeben können. 
---

{{% alert color="primary" %}}

Aspose.Cells stellt die [**Workbook.dispose()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#dispose--) Methode bereit, um die nicht verwalteten Ressourcen des [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) Objekts freizugeben. Das Dispose-Muster wird nur für Objekte verwendet, die nicht verwaltete Ressourcen wie Dateien, Pipe-Handles, Registry-Handles, Warte-Handles oder Zeiger auf Blockspeicher zugreifen. Dies liegt daran, dass der Garbage Collector sehr effizient bei der Rückgewinnung ungenutzter verwalteter Objekte ist, aber nicht in der Lage ist, nicht verwaltete Objekte zurückzuholen.

{{% /alert %}}

Das [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) Objekt implementiert jetzt die *System.IDisposable* Schnittstelle, die eine einzelne Methode [**Workbook.dispose()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#dispose--) hat. Sie können entweder direkt die [**Workbook.dispose()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#dispose--) Methode aufrufen oder den *Using* Befehl verwenden, um diese Methode automatisch aufzurufen.

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
