---  
title: Upptäck filformat på krypterade Office Open XML  OOXML filer med Node.js via C++  
linktitle: Identifiera filformat för krypterade Office Open XML  OOXML filer  
type: docs  
weight: 340  
url: /sv/nodejs-cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/  
description: Lär dig hur du upptäcker filformatet för krypterade OOXML filer med Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

**Office Open XML** (även känt som **OOXML** eller **Microsoft Open XML** (MOX)) är ett XML-baserat filformat utvecklat av Microsoft för att representera kontorsdokument som kalkylblad, diagram, presentationer och ordbehandlingsdokument.  

{{% /alert %}}  

Aspose.Cells erbjuder ett sätt att upptäcka filformatet för krypterade **Microsoft Open XML**-filer. För att identifiera filtypen använd [FileFormatUtil.detectFileFormat(Uint8Array)](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#detectFileFormat-uint8array-) metoden som visas i kodexemplet nedan.  

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

{{< app/cells/assistant language="nodejs-cpp" >}}
