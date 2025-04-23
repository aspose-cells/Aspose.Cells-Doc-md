---  
title: 如何检测文件格式并检查文件是否被加密，使用Node.js通过C++  
linktitle: 如何检测文件格式并检查文件是否已加密  
type: docs  
weight: 2700  
url: /zh/nodejs-cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/  
description: 学习如何使用Aspose.Cells for Node.js via C++检测文件格式及检查文件是否被加密。  
---  

{{% alert color="primary" %}}  
 有时候需要在打开文件之前检测文件的格式，因为文件扩展名不能保证文件内容的正确性。文件可能被加密（密码保护文件）因此不能直接读取，或者不应读取。Aspose.Cells for Node.js via C++提供了[**FileFormatUtil.detectFileFormat(Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#detectFileFormat-uint8array-)静态方法和一些相关的API，供你处理文档。  
{{% /alert %}}  

以下示例代码说明如何通过文件路径检测文件格式并检查其扩展名。您还可以确定该文件是否已加密。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Detect file format
const info = AsposeCells.FileFormatUtil.detectFileFormat(new Uint8Array(require("fs").readFileSync(filePath)));

// Gets the detected load format
console.log("The spreadsheet format is: " + AsposeCells.FileFormatUtil.loadFormatToExtension(info.getLoadFormat()));

// Check if the file is encrypted.
console.log("The file is encrypted: " + info.isEncrypted());
```  
