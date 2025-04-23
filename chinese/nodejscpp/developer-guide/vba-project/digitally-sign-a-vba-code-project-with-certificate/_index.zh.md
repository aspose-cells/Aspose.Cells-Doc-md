---
title: 用证书为VBA代码项目数字签名，使用Node.js的C++
linktitle: 使用证书为VBA代码项目进行数字签名
type: docs
weight: 110
url: /zh/nodejs-cpp/digitally-sign-a-vba-code-project-with-certificate/
description: 学习如何使用Aspose.Cells for Node.js via C++用证书对VBA代码项目进行数字签名。
---

{{% alert color="primary" %}}

您可以使用Aspose.Cells及其[**VbaProject.sign(DigitalSignature)**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#sign-digitalsignature-)方法对VBA代码项目进行数字签名。请按照以下步骤检查您的Excel文件是否已用证书进行数字签名。

- 从“开发人员”选项卡中单击“Visual Basic”以打开“Visual Basic for Applications IDE”
- 从“Visual Basic for Applications IDE”中单击“工具” > “数字签名...”

将显示“数字签名表单”，显示文档是否已使用证书进行数字签名。

{{% /alert %}} 

## **使用证书在Node.js中数字签名VBA代码项目**

以下示例代码演示了如何使用[**VbaProject.sign(DigitalSignature)**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#sign-digitalsignature-)方法。这是示例代码的输入和输出文件。你可以使用任何Excel文件和任何证书来测试此代码。

- [用于示例代码的源Excel文件](5115028.xlsm)
- [示例pfx文件](5115039.pfx)用于创建数字签名。请在计算机上安装它以运行此代码。其密码为1234。
- [示例代码生成的输出Excel文件](5115029.xlsm)

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Set up paths
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");
const pfxPath = path.join(sourceDir, "sampleDigitallySignVbaProjectWithCertificate.pfx");
const workbookPath = path.join(sourceDir, "sampleDigitallySignVbaProjectWithCertificate.xlsm");

// Set Digital Signature
const password = "1234";
const comment = "Signing Digital Signature using Aspose.Cells";
const digitalSignature = new AsposeCells.DigitalSignature(fs.readFileSync(pfxPath), password, comment, new Date());

// Create workbook object from excel file
const workbook = new AsposeCells.Workbook(workbookPath);

// Sign VBA Code Project with Digital Signature
workbook.getVbaProject().sign(digitalSignature);

// Save the workbook
workbook.save(path.join(outputDir, "outputDigitallySignVbaProjectWithCertificate.xlsm"));
```
