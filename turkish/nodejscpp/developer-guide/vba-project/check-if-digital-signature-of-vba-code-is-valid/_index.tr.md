---
title: VBA Kodu Dijital İmzasının Geçerli olup olmadığını Node.js kullanarak kontrol edin
linktitle: VBA Kodunun Dijital İmzasının Geçerli Olup Olmadığını Kontrol Et
type: docs
weight: 120
url: /tr/nodejs-cpp/check-if-digital-signature-of-vba-code-is-valid/
description: VBA kodunun dijital imzasının geçerliliğini Aspose.Cells for Node.js via C++ kullanarak nasıl kontrol edeceğinizi öğrenin.
--- 

{{% alert color="primary" %}}

Aspose.Cells, VBA kodunun dijital imzasının [**Workbook.isValidSigned()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isValidSigned--) özelliğini kullanarak geçerli olup olmadığını kontrol etmenizi sağlar. İmza geçerliyse **true** döndürecek, aksi takdirde **false** döndürecektir. VBA kodunun dijital imzası değiştirildiğinde geçersiz hale gelir.

{{% /alert %}}

## **VBA Kodu Dijital İmzası Geçerliğini Node.js'de Kontrol Et**

Aşağıdaki kod, sağlanan bağlantıdan indirebileceğiniz [örnek excel dosyası](5115030.xlsm) kullanarak bu özelliğin kullanımını göstermektedir. Aynı excel dosyasının geçerli bir imzası vardır ancak VBA kodunu değiştirip çalıştırdıktan sonra imzanın geçersiz olduğunu buluruz.

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
