---  
title: Как обнаружить формат файла и проверить, зашифрован ли файл, с помощью Node.js через C++  
linktitle: Как определить формат файла и проверить, зашифрован ли файл  
type: docs  
weight: 2700  
url: /ru/nodejs-cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/  
description: Узнайте, как обнаружить формат файла и проверить, зашифрован ли файл, с помощью Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Иногда нужно определить формат файла перед его открытием, потому что расширение файла не гарантирует правильность содержимого. Файл может быть зашифрован (защищен паролем), поэтому его нельзя читать напрямую, или нам не следует его читать. Aspose.Cells for Node.js via C++ предоставляет статический метод [**FileFormatUtil.detectFileFormat(Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#detectFileFormat-uint8array-) и некоторые соответствующие API, которые можно использовать для обработки документов.  
{{% /alert %}}  

В следующем образце кода показано, как определить формат файла (с использованием пути к файлу) и проверить его расширение. Вы также можете определить, зашифрован ли файл.  

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
