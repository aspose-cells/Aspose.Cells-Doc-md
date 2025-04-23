---
title: Verificar si la firma digital del código VBA es válida con Node.js vía C++
linktitle: Verifica si la Firma Digital del Código VBA es Válida
type: docs
weight: 120
url: /es/nodejs-cpp/check-if-digital-signature-of-vba-code-is-valid/
description: Aprende cómo verificar la validez de una firma digital del código VBA usando Aspose.Cells for Node.js via C++.
--- 

{{% alert color="primary" %}}

Aspose.Cells te permite verificar si la firma digital del código VBA es válida usando la propiedad [**Workbook.isValidSigned()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isValidSigned--). Devolverá **true** si la firma es válida, de lo contrario devolverá **false**. La firma digital del código VBA se vuelve inválida cuando se cambia el código VBA.

{{% /alert %}}

## **Verificar si la firma digital del código VBA es válida en Node.js**

El siguiente código demuestra el uso de esta propiedad utilizando el [archivo excel de muestra](5115030.xlsm) que puedes descargar desde el enlace proporcionado. El mismo archivo de Excel tiene una firma válida pero cuando modificamos su código VBA y guardamos el libro de trabajo y luego volvemos a verificar, encontramos que su firma se ha vuelto inválida.

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
