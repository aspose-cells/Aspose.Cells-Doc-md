---  
title: Şifrelenmiş Dosyaların Parolasını Node.js ve C++ kullanarak doğrulayın  
linktitle: Şifrelenmiş Dosyaların Şifresini Doğrulama  
type: docs  
weight: 10  
url: /tr/nodejs-cpp/verify-password-of-encrypted-excel-and-ods-files/  
description: Aspose.Cells for Node.js via C++ kullanarak şifreli Excel (xlsx, xlsb, xls, xlsm) ve Open Office (ODS) dosyalarının parolasını doğrulayın.  
---  

{{% alert color="primary" %}}  
Excel (xlsx, xlsb, xls, xlsm) ve Open Office (ODS) dosyaları şifre ile kilitliyse, Aspose spesifik verilerin ayrıştırılmasına ihtiyaç duymadan basit parola doğrulamasını destekler.  
{{% /alert %}}  

## **Şifrelenmiş dosyanın parolasını doğrulama**  

Şifrelenmiş dosyanın parolasını doğrulamak için, Aspose.Cells for Node.js via C++ [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#verifyPassword-uint8array-string-) metodunu sağlar. Bu yöntem iki parametre kabul eder: dosya akışı ve doğrulanması gereken parola.  
Aşağıdaki kod parçası, sağlanan parolanın geçerli olup olmadığını doğrulamak için [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#verifyPassword-uint8array-string-) yönteminin nasıl kullanıldığını göstermektedir.  

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
