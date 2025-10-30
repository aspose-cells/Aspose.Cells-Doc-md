---
title: Controlla se il codice VBA è firmato con Node.js via C++
linktitle: Verifica se il Codice VBA è Firmato
type: docs
weight: 100
url: /it/nodejs-cpp/check-if-vba-code-is-signed/
description: Impara come verificare se il progetto di codice VBA è firmato usando Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Aspose.Cells permette all'utente di verificare se il progetto di codice VBA è firmato o no. Si prega di utilizzare la proprietà [**VbaProject.isSigned()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isSigned--) per verificare se il progetto di codice VBA è firmato o no.

{{% /alert %}}

Il seguente codice spiega come verificare se il codice VBA è firmato o meno usando la proprietà [**VbaProject.isSigned()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isSigned--). Puoi usare qualsiasi tuo file Excel per testare questo codice. Per scopi di test, puoi usare [questo file Excel usato nel codice](5115032.xlsm).

## **Verifica se il codice VBA è firmato in Node.js**

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

## Output della console

Di seguito è riportato l'output della console del codice precedente utilizzando il [file Excel di esempio](5115032.xlsm) fornito dal link.

{{< highlight java >}}

Is VBA Code Project Signed: True

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
