---  
title: 使用Node.js通过C++验证加密文件的密码  
linktitle: 验证加密文件的密码  
type: docs  
weight: 10  
url: /zh/nodejs-cpp/verify-password-of-encrypted-excel-and-ods-files/  
description: 使用Aspose.Cells for Node.js via C++验证Excel（xlsx、xlsb、xls、xlsm）和Open Office（ODS）文件的密码。  
---  

{{% alert color="primary" %}}  
 如果Excel（xlsx、xlsb、xls、xlsm）和Open Office（ODS）文件被密码锁定，Aspose支持简单的密码验证，无需解析文件的具体数据。  
{{% /alert %}}  

## **验证加密文件的密码**  

 为了验证加密文件的密码，Aspose.Cells for Node.js via C++提供了[**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#verifyPassword-uint8array-string-)方法。该方法接受两个参数：文件流和需要验证的密码。  
以下代码片段演示了使用[**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#verifyPassword-uint8array-string-)方法来验证提供的密码是否有效。  

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

