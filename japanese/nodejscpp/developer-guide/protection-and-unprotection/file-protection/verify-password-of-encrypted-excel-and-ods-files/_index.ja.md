---  
title: 暗号化されたファイルのパスワードをNode.js経由のC++で検証する  
linktitle: 暗号化されたファイルのパスワードを確認する  
type: docs  
weight: 10  
url: /ja/nodejs-cpp/verify-password-of-encrypted-excel-and-ods-files/  
description: Aspose.Cells for Node.js via C++を使用して暗号化されたExcel（xlsx、xlsb、xls、xlsm）およびOpen Office（ODS）ファイルのパスワードを検証します。  
---  

{{% alert color="primary" %}}  
Excel（xlsx、xlsb、xls、xlsm）とOpen Office（ODS）ファイルがパスワードでロックされている場合、Asposeはファイルの特定のデータを解析せずに簡単なパスワード検証をサポートします。  
{{% /alert %}}  

## **暗号化されたファイルのパスワードを確認します**  

暗号化されたファイルのパスワードを検証するには、Aspose.Cells for Node.js via C++は[**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#verifyPassword-uint8array-string-)メソッドを提供します。このメソッドは2つのパラメータを受け取ります：ファイルストリームと検証するパスワード。  
以下のコードスニペットは、提供されたパスワードが有効かどうかを確認する[**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#verifyPassword-uint8array-string-)メソッドの使用を示しています。  

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
