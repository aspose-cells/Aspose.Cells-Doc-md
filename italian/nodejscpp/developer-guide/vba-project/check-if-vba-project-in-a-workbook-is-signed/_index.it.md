---
title: Verifica se il progetto VBA in un file Excel è firmato con Node.js tramite C++
linktitle: Verifica se il progetto VBA in un workbook è firmato
type: docs
weight: 70
url: /it/nodejs-cpp/check-if-vba-project-in-a-workbook-is-signed/
description: Impara come verificare se un progetto VBA in un file Excel è firmato usando Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Puoi verificare se il tuo progetto VBA è firmato o meno utilizzando Microsoft Excel tramite il comando del menu **Strumenti > Firme digitali...**. Analogamente, puoi verificarlo in modo programmatico utilizzando la proprietà [**Workbook.getVbaProject()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getVbaProject--) di Aspose.Cells.

{{% /alert %}}

## **Verifica se il progetto VBA in un file Excel è firmato in Node.js**

Il seguente esempio di codice carica il workbook e verifica se il suo progetto VBA è firmato usando la proprietà [**Workbook.getVbaProject()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getVbaProject--). La proprietà restituirà **true** se il progetto è firmato, altrimenti restituirà **false**.

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
{{< app/cells/assistant language="nodejs-cpp" >}}
