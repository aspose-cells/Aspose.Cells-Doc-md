---  
title: Обнаружение формата файла зашифрованных офисных XML файлов — OOXML с помощью Node.js через C++  
linktitle: Определить формат файла зашифрованного Office Open XML  OOXML  
type: docs  
weight: 340  
url: /ru/nodejs-cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/  
description: Узнайте, как обнаруживать формат файла зашифрованных OOXML файлов с помощью Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

**Office Open XML** (также известный как **OOXML** или **Microsoft Open XML** (MOX)) — это основанный на XML формат файла, разработанный Microsoft для представления офисных документов, таких как таблицы, диаграммы, презентации и текстовые документы.  

{{% /alert %}}  

Aspose.Cells предоставляет способ обнаружения формата файла зашифрованных **Microsoft Open XML** файлов. Для определения типа файла используйте метод [FileFormatUtil.detectFileFormat(Uint8Array)](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#detectFileFormat-uint8array-), как показано в примере кода.  

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

