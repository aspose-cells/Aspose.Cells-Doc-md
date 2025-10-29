---
title: Проверьте, действительна ли цифровая подпись VBA кода с помощью Node.js через C++
linktitle: Проверить, действителен ли цифровой подпись кода VBA
type: docs
weight: 120
url: /ru/nodejs-cpp/check-if-digital-signature-of-vba-code-is-valid/
description: Узнайте, как проверить действительность цифровой подписи VBA кода с помощью Aspose.Cells for Node.js via C++.
--- 

{{% alert color="primary" %}}

Aspose.Cells позволяет проверить, действительна ли цифровая подпись кода VBA с помощью свойства [**Workbook.isValidSigned()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isValidSigned--). Он вернет **true**, если подпись действительна, в противном случае он вернет **false**. Цифровая подпись кода VBA становится недействительной, когда вы изменяете код VBA.

{{% /alert %}}

## **Проверьте, действительна ли цифровая подпись VBA-кода в Node.js**

Следующий код демонстрирует использование этого свойства с [образцовым файлом Excel](5115030.xlsm), который вы можете загрузить по предоставленной ссылке. В этом же файле Excel имеется действительная подпись, но после изменения его кода VBA, сохранения книги и повторной проверки мы обнаружим, что его подпись стала недействительной.

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
