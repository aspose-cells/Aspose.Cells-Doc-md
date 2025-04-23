---  
title: 通过C++使用Node.js检测受密码保护的Office Open XML（OOXML）文件的文件格式  
linktitle: 检测加密的Office Open XML  OOXML文件的文件格式  
type: docs  
weight: 340  
url: /zh/nodejs-cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/  
description: 学习如何使用Aspose.Cells for Node.js via C++检测加密的OOXML文件的文件格式。  
---  

{{% alert color="primary" %}}  

**Office Open XML**（也称为**OOXML**或**微软开放XML**（MOX））是一种由微软开发的基于XML的文件格式，用于表示办公文档，如电子表格、图表、演示文稿和文字处理文件。  

{{% /alert %}}  

Aspose.Cells提供了一种检测加密的**微软开放XML**文件文件格式的方法。要识别文件类型，请使用[FileFormatUtil.detectFileFormat(Uint8Array)](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#detectFileFormat-uint8array-)方法，如下面的代码示例所示。  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
const filePath = path.join(sourceDir, "encryptedBook1.out.tmp");

fs.writeFileSync(filePath, Buffer.from([0x50, 0x4B, 0x03, 0x04]));
const stream = fs.readFileSync(filePath);
AsposeCells.FileFormatUtil.verifyPassword(stream, "1234");
const fileFormatInfo = AsposeCells.FileFormatUtil.detectFileFormat(stream);

console.log("File Format: " + fileFormatInfo.getFileFormatType());
```  

