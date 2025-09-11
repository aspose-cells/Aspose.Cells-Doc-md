---  
title: How to Detect a File Format and Check if the File is Encrypted with Node.js via C++  
linktitle: How to Detect a File Format and Check if the File is Encrypted  
type: docs  
weight: 2700  
url: /nodejs-cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/  
description: Learn how to detect a file format and check if a file is encrypted using Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Sometimes you need to detect a file's format before opening it because the file extension does not guarantee that the file content is appropriate. The file might be encrypted (a password-protected file) so it can't be read directly, or we should not read it. Aspose.Cells for Node.js via C++ provides the [**FileFormatUtil.detectFileFormat(Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#detectFileFormat-uint8array-) static method and some relevant APIs that you can use to process documents.  
{{% /alert %}}  

The following sample code illustrates how to detect a file format (using the file path) and check its extension. You can also determine whether the file is encrypted.  

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
{{< app/cells/assistant language="nodejs-cpp" >}}