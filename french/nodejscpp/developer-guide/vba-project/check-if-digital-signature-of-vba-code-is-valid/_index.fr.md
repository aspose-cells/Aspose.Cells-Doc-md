---
title: Vérifier si la signature numérique du code VBA est valide avec Node.js via C++
linktitle: Vérifiez si la signature numérique du code VBA est valide
type: docs
weight: 120
url: /fr/nodejs-cpp/check-if-digital-signature-of-vba-code-is-valid/
description: Apprenez comment vérifier la validité d une signature numérique du code VBA utilisant Aspose.Cells for Node.js via C++.
--- 

{{% alert color="primary" %}}

Aspose.Cells vous permet de vérifier si la signature numérique du code VBA est valide en utilisant la propriété [**Workbook.isValidSigned()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isValidSigned--). Elle retournera **true** si la signature est valide, sinon elle retournera **false**. La signature numérique du code VBA devient invalide lorsque vous modifiez le code VBA.

{{% /alert %}}

## **Vérifier si la signature numérique du code VBA est valide dans Node.js**

Le code suivant démontre l'utilisation de cette propriété en utilisant le [fichier Excel d'exemple](5115030.xlsm), que vous pouvez télécharger à partir du lien fourni. Le même fichier Excel a une signature valide mais lorsque nous modifions son code VBA et sauvegardons le classeur, puis vérifions à nouveau, nous constatons que sa signature est devenue invalide.

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
