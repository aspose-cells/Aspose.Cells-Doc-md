---  
title: Erkennung des Dateiformats verschlüsselter Office Open XML  OOXML Dateien mit Node.js via C++  
linktitle: Dateiformat von verschlüsselten Office Open XML  OOXML Dateien erkennen  
type: docs  
weight: 340  
url: /de/nodejs-cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/  
description: Erfahren Sie, wie Sie das Dateiformat verschlüsselter OOXML Dateien mit Aspose.Cells for Node.js via C++ erkennen können.  
---  

{{% alert color="primary" %}}  

**Office Open XML** (auch bekannt als **OOXML** oder **Microsoft Open XML** (MOX)) ist ein XML-basiertes Dateiformat, das von Microsoft entwickelt wurde, um Office-Dokumente wie Tabellen, Diagramme, Präsentationen und Textverarbeitungsdokumente darzustellen.  

{{% /alert %}}  

Aspose.Cells bietet eine Möglichkeit, das Dateiformat verschlüsselter **Microsoft Open XML**-Dateien zu erkennen. Um den Dateityp zu bestimmen, verwenden Sie die Methode [FileFormatUtil.detectFileFormat(Uint8Array)](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#detectFileFormat-uint8array-) wie im Beispiel im Code gezeigt.  

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
