---
title: Kontrollera om digital signatur av VBA koden är giltig med Node.js via C++
linktitle: Kontrollera om den digitala signaturen av VBA koden är giltig
type: docs
weight: 120
url: /sv/nodejs-cpp/check-if-digital-signature-of-vba-code-is-valid/
description: Lär dig hur man kontrollerar giltigheten av en digital signatur av VBA koden med Aspose.Cells for Node.js via C++.
--- 

{{% alert color="primary" %}}

Aspose.Cells låter dig kontrollera om den digitala signaturen av VBA-koden är giltig med hjälp av [**Workbook.isValidSigned()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isValidSigned--) -egenskapen. Den kommer att returnera **true** om signaturen är giltig, annars kommer den att returnera **false**. Den digitala signaturen av VBA-koden blir ogiltig när du ändrar VBA-koden.

{{% /alert %}}

## **Kontrollera om digital signatur av VBA-koden är giltig i Node.js**

Följande kod visar användningen av denna egenskap med [exempel excelfil](5115030.xlsm) som du kan ladda ner från den angivna länken. Samma excelfil har en giltig signatur, men när vi ändrar dess VBA-kod och sparar arbetsboken och sedan kontrollerar på nytt, finner vi att dess signatur har blivit ogiltig.

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
