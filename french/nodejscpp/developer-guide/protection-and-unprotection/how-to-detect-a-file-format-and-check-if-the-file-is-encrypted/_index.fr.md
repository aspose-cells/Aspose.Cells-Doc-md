---  
title: Comment détecter un format de fichier et vérifier si le fichier est crypté avec Node.js via C++  
linktitle: Comment détecter un format de fichier et vérifier si le fichier est chiffré  
type: docs  
weight: 2700  
url: /fr/nodejs-cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/  
description: Apprenez comment détecter un format de fichier et vérifier si un fichier est crypté à l aide de Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
 Parfois, vous devez détecter le format d'un fichier avant de l'ouvrir car l'extension du fichier ne garantit pas que le contenu du fichier est approprié. Le fichier pourrait être crypté (protégé par mot de passe) et ne peut pas être lu directement, ou bien il ne faut pas le lire. Aspose.Cells for Node.js via C++ fournit la méthode statique [**FileFormatUtil.detectFileFormat(Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#detectFileFormat-uint8array-) et des API pertinentes que vous pouvez utiliser pour traiter les documents.  
{{% /alert %}}  

L'exemple de code suivant illustre comment détecter un format de fichier (en utilisant le chemin du fichier) et vérifier son extension. Vous pouvez également déterminer si le fichier est chiffré.  

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
