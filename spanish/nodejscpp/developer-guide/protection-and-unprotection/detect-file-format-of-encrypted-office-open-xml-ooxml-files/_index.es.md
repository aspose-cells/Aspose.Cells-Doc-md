---  
title: Detectar formato de archivo de archivos OAAX encriptados con Node.js vía C++  
linktitle: Detectar formato de archivo de XML abierto de oficina encriptado archivos OOXML  
type: docs  
weight: 340  
url: /es/nodejs-cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/  
description: Aprende cómo detectar el formato de archivo de archivos OOXML encriptados usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

**Office Open XML** (también conocido como **OOXML** o **Microsoft Open XML** (MOX)) es un formato de archivo basado en XML desarrollado por Microsoft para representar documentos de oficina como hojas de cálculo, gráficos, presentaciones y documentos de procesamiento de textos.  

{{% /alert %}}  

Aspose.Cells proporciona una manera de detectar el formato de archivo de archivos **Microsoft Open XML** encriptados. Para identificar el tipo de archivo, usa el método [FileFormatUtil.detectFileFormat(Uint8Array)](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#detectFileFormat-uint8array-) como se muestra en el ejemplo de código.  

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
