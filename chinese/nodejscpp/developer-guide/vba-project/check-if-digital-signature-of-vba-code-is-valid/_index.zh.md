---
title: 使用Node.js的C++检查VBA代码的数字签名是否有效
linktitle: 检查VBA代码的数字签名是否有效
type: docs
weight: 120
url: /zh/nodejs-cpp/check-if-digital-signature-of-vba-code-is-valid/
description: 学习如何使用Aspose.Cells for Node.js via C++检查VBA代码的数字签名的有效性。
--- 

{{% alert color="primary" %}}

Aspose.Cells允许您使用[**Workbook.isValidSigned()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isValidSigned--)属性检查VBA代码的数字签名是否有效。如果签名有效，则返回**true**，否则返回**false**。当您更改VBA代码时，VBA代码的数字签名将变为无效。

{{% /alert %}}

## **在Node.js中检查VBA代码的数字签名是否有效**

以下代码演示了使用该属性的用法，使用[示例Excel文件](5115030.xlsm)进行测试。相同的Excel文件具有有效的签名，但当我们修改其VBA代码并保存工作簿后重新检查时，我们发现其签名已变为无效。

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
