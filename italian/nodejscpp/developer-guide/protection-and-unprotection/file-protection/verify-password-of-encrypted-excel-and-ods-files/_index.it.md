---  
title: Verifica password dei file crittografati con Node.js tramite C++  
linktitle: Verifica password dei file crittografati  
type: docs  
weight: 10  
url: /it/nodejs-cpp/verify-password-of-encrypted-excel-and-ods-files/  
description: Verifica la password di file Excel crittografati (xlsx, xlsb, xls, xlsm) e Open Office (ODS) usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Se i file Excel (xlsx, xlsb, xls, xlsm) e Open Office (ODS) sono bloccati con una password, Aspose supporta la verifica semplice della password senza analizzare dati specifici dei file.  
{{% /alert %}}  

## **Verifica la password del file crittografato**  

Per verificare la password del file crittografato, Aspose.Cells for Node.js via C++ fornisce il metodo [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#verifyPassword-uint8array-string-). Questo metodo accetta due parametri, il flusso di file e la password da verificare.  
Il seguente frammento di codice dimostra l'uso del metodo [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#verifyPassword-uint8array-string-) per verificare se la password fornita è valida o meno.  

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

{{< app/cells/assistant language="nodejs-cpp" >}}
