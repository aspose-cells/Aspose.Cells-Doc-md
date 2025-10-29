---  
title: Проверка пароля зашифрованных файлов с помощью Node.js через C++  
linktitle: Проверить пароль зашифрованных файлов  
type: docs  
weight: 10  
url: /ru/nodejs-cpp/verify-password-of-encrypted-excel-and-ods-files/  
description: Проверьте пароль зашифрованных файлов Excel (xlsx, xlsb, xls, xlsm) и Open Office (ODS) с помощью Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Если файлы Excel (xlsx, xlsb, xls, xlsm) и Open Office (ODS) защищены паролем, Aspose поддерживает простую проверку пароля без разбора конкретных данных файлов.  
{{% /alert %}}  

## **Проверьте пароль зашифрованного файла**  

Для проверки пароля зашифрованного файла Aspose.Cells for Node.js via C++ предоставляет метод [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#verifyPassword-uint8array-string-). Этот метод принимает два параметра: поток файла и пароль, который нужно проверить.  
Следующий фрагмент кода демонстрирует использование метода [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#verifyPassword-uint8array-string-) для проверки, является ли предоставленный пароль допустимым или нет.  

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
