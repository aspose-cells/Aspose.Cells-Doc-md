---  
title: Détecter le format de fichier des fichiers Office Open XML cryptés avec Node.js via C++  
linktitle: Détecter le format de fichier des fichiers Office Open XML chiffrés  
type: docs  
weight: 340  
url: /fr/nodejs-cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/  
description: Apprenez comment détecter le format de fichier des fichiers OOXML cryptés avec Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

 **Office Open XML** (également appelé **OOXML** ou **Microsoft Open XML** (MOX)) est un format de fichier basé sur XML développé par Microsoft pour représenter des documents Office tels que feuilles de calcul, graphiques, présentations et documents de traitement de texte.  

{{% /alert %}}  

 Aspose.Cells offre un moyen de détecter le format de fichier des fichiers **Microsoft Open XML** cryptés. Pour identifier le type de fichier, utilisez la méthode [FileFormatUtil.detectFileFormat(Uint8Array)](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#detectFileFormat-uint8array-) comme illustré dans l'exemple de code.  

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
