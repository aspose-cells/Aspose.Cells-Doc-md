---  
title: Rileva il formato file di Office Open XML criptato  file OOXML con Node.js tramite C++  
linktitle: Rileva il Formato File dei File Office Open XML Crittografati  File OOXML  
type: docs  
weight: 340  
url: /it/nodejs-cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/  
description: Impara come rilevare il formato dei file di OOXML criptati usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

**Office Open XML** (noto anche come **OOXML** o **Microsoft Open XML** (MOX)) è un formato di file basato su XML sviluppato da Microsoft per rappresentare documenti di ufficio come fogli di calcolo, grafici, presentazioni e documenti di word processing.  

{{% /alert %}}  

Aspose.Cells fornisce un metodo per rilevare il formato di file di **Microsoft Open XML criptati**. Per identificare il tipo di file, usa il metodo [FileFormatUtil.detectFileFormat(Uint8Array)](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#detectFileFormat-uint8array-) come mostrato nell’esempio di codice.  

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

