---  
title: Verify Password of Encrypted Files with Node.js via C++  
linktitle: Verify Password of Encrypted Files  
type: docs  
weight: 10  
url: /nodejs-cpp/verify-password-of-encrypted-excel-and-ods-files/  
description: Verify the password of encrypted Excel (xlsx, xlsb, xls, xlsm) and Open Office (ODS) files using Aspose.Cells for Node.js via C++.  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

{{% alert color="primary" %}}  
If Excel (xlsx, xlsb, xls, xlsm) and Open Office (ODS) files are locked with a password, Aspose supports simple password verification without parsing specific data of the files.  
{{% /alert %}}  

## **Verify the password of the encrypted file**  

To verify the password of the encrypted file, Aspose.Cells for Node.js via C++ provides the [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#verifyPassword-uint8array-string-) method. This method accepts two parameters, the file stream and the password that needs to be verified.  
The following code snippet demonstrates the use of the [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#verifyPassword-uint8array-string-) method to verify whether the provided password is valid or not.  

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
