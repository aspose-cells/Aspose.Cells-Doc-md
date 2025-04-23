---
title: 通过Node.js的C++检查VBA代码是否已签名
linktitle: 检查VBA代码是否已签名
type: docs
weight: 100
url: /zh/nodejs-cpp/check-if-vba-code-is-signed/
description: 学习如何使用Aspose.Cells for Node.js via C++检查VBA代码项目是否已签名。 
---

{{% alert color="primary" %}}

Aspose.Cells允许用户检查VBA代码项目是否已签名。请使用[**VbaProject.isSigned()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isSigned--)属性来检查VBA代码项目是否已签名。

{{% /alert %}}

以下代码说明如何使用[**VbaProject.isSigned()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isSigned--)属性检查VBA代码是否已签名。您可以使用任何Excel文件测试此代码。为了测试，可以使用[此代码中用到的Excel文件](5115032.xlsm)。

## **在Node.js中检查VBA代码是否已签名**

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

## 控制台输出

以下是上述代码的控制台输出，使用链接提供的[示例Excel文件](5115032.xlsm)。

{{< highlight java >}}

Is VBA Code Project Signed: True

{{< /highlight >}}
