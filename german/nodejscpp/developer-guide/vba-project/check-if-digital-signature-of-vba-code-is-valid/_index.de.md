---
title: Überprüfen, ob die Digitale Signatur des VBA Codes mit Node.js via C++ gültig ist
linktitle: Prüfen, ob die digitale Signatur des VBA Codes gültig ist
type: docs
weight: 120
url: /de/nodejs-cpp/check-if-digital-signature-of-vba-code-is-valid/
description: Erfahren Sie, wie Sie die Gültigkeit einer digitalen Signatur des VBA Codes mit Aspose.Cells for Node.js via C++ überprüfen.
--- 

{{% alert color="primary" %}}

Aspose.Cells ermöglicht es Ihnen, mithilfe der [**Workbook.isValidSigned()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isValidSigned--)-Eigenschaft zu überprüfen, ob die digitale Signatur des VBA-Codes gültig ist. Es gibt **true** zurück, wenn die Signatur gültig ist, andernfalls **false**. Die digitale Signatur des VBA-Codes wird ungültig, wenn Sie den VBA-Code ändern.

{{% /alert %}}

## **Überprüfen, ob die Digitale Signatur des VBA-Codes in Node.js gültig ist**

Der folgende Code demonstriert die Verwendung dieser Eigenschaft anhand der [Beispieldatei](5115030.xlsm), die Sie über den bereitgestellten Link herunterladen können. Die gleiche Excel-Datei hat eine gültige Signatur, aber wenn wir ihren VBA-Code ändern und die Arbeitsmappe speichern, finden wir heraus, dass ihre Signatur ungültig geworden ist.

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
