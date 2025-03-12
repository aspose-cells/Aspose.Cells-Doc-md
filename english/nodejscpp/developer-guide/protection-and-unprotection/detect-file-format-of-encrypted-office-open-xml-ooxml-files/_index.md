---  
title: Detect File Format of Encrypted Office Open XML - OOXML Files with Node.js via C++  
linktitle: Detect File Format of Encrypted Office Open XML - OOXML Files  
type: docs  
weight: 340  
url: /nodejs-cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/  
description: Learn how to detect the file format of encrypted OOXML files using Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

**Office Open XML** (also known as **OOXML** or **Microsoft Open XML** (MOX)) is an XML-based file format developed by Microsoft for representing office documents like spreadsheets, charts, presentations, and word processing documents.  

{{% /alert %}}  

Aspose.Cells provides a way to detect the file format of encrypted **Microsoft Open XML** files. To identify the file type, use the [FileFormatUtil.detectFileFormat(Uint8Array)](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#detectFileFormat-uint8array-) method as shown below in the code example.  

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
  