---  
title: Verificar contraseña de archivos cifrados con Node.js a través de C++  
linktitle: Verificar contraseña de archivos cifrados  
type: docs  
weight: 10  
url: /es/nodejs-cpp/verify-password-of-encrypted-excel-and-ods-files/  
description: Verifique la contraseña de archivos cifrados de Excel (xlsx, xlsb, xls, xlsm) y Open Office (ODS) usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Si los archivos Excel (xlsx, xlsb, xls, xlsm) y Open Office (ODS) están bloqueados con contraseña, Aspose soporta la verificación simple de contraseña sin analizar datos específicos de los archivos.  
{{% /alert %}}  

## **Verificar la contraseña del archivo cifrado**  

Para verificar la contraseña del archivo cifrado, Aspose.Cells for Node.js via C++ proporciona el método [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#verifyPassword-uint8array-string-). Este método acepta dos parámetros, el flujo del archivo y la contraseña que necesita verificarse.  
El siguiente fragmento de código muestra el uso del método [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#verifyPassword-uint8array-string-) para verificar si la contraseña proporcionada es válida o no.  

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

