---  
title: Vérifier le mot de passe des fichiers chiffrés avec Node.js via C++  
linktitle: Vérifier le mot de passe des fichiers chiffrés  
type: docs  
weight: 10  
url: /fr/nodejs-cpp/verify-password-of-encrypted-excel-and-ods-files/  
description: Vérifiez le mot de passe des fichiers Excel chiffrés (xlsx, xlsb, xls, xlsm) et Open Office (ODS) en utilisant Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Si des fichiers Excel (xlsx, xlsb, xls, xlsm) et Open Office (ODS) sont verrouillés par mot de passe, Aspose supporte une vérification simple du mot de passe sans parser les données spécifiques des fichiers.  
{{% /alert %}}  

## **Vérifiez le mot de passe du fichier chiffré**  

Pour vérifier le mot de passe du fichier chiffré, Aspose.Cells for Node.js via C++ fournit la méthode [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#verifyPassword-uint8array-string-). Cette méthode accepte deux paramètres, le flux de fichier et le mot de passe à vérifier.  
Le code d'exemple suivant démontre l'utilisation de la méthode [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#verifyPassword-uint8array-string-) pour vérifier si le mot de passe fourni est valide ou non.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "EncryptedBook1.xlsx");

// Create a Stream object
const fs = require("fs");
const fstream = fs.readFileSync(filePath);

const isPasswordValid = AsposeCells.FileFormatUtil.verifyPassword(fstream, "1234");

console.log("Password is Valid: " + isPasswordValid);
```  

