---
title: Controlla se la firma digitale del codice VBA è valida con Node.js via C++
linktitle: Verifica se la Firma Digitale del Codice VBA è Valida
type: docs
weight: 120
url: /it/nodejs-cpp/check-if-digital-signature-of-vba-code-is-valid/
description: Impara come verificare la validità di una firma digitale del codice VBA usando Aspose.Cells for Node.js via C++.
--- 

{{% alert color="primary" %}}

Aspose.Cells ti permette di verificare se la firma digitale del codice VBA è valida utilizzando la proprietà [**Workbook.isValidSigned()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isValidSigned--). Restituirà **true** se la firma è valida, altrimenti restituirà **false**. La firma digitale del codice VBA diventa non valida quando si cambia il codice VBA.

{{% /alert %}}

## **Verifica se la firma digitale del codice VBA è valida in Node.js**

Il codice seguente dimostra l'uso di questa proprietà utilizzando il [file Excel di esempio](5115030.xlsm) che puoi scaricare dal link fornito. Lo stesso file Excel ha una firma valida ma quando modifichiamo il suo codice VBA e salviamo il workbook e poi ricontrolliamo, troviamo che la sua firma è diventata non valida.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleVBAProjectSigned.xlsm");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Signature is valid
console.log("Is VBA Code Project Valid Signed: " + workbook.getVbaProject().isValidSigned());

// Modify the VBA Code, save the workbook then reload
// VBA Code Signature will now be invalid
let code = workbook.getVbaProject().getModules().get(1).getCodes();
code = code.replace("Welcome to Aspose", "Welcome to Aspose.Cells");
workbook.getVbaProject().getModules().get(1).setCodes(code);

// Save
workbook.save(path.join(dataDir, "output_out.xlsm"));

// Reload
workbook = new AsposeCells.Workbook(path.join(dataDir, "output_out.xlsm"));

// Now the signature is invalid
console.log("Is VBA Code Project Valid Signed: " + workbook.getVbaProject().isValidSigned());
```
{{< app/cells/assistant language="nodejs-cpp" >}}
