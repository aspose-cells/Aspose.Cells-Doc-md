---
title: Node.js kullanarak şifre koruması yapılan sayfayı doğrulama (C++ ile)
linktitle: Çalışma Sayfasını Korumak İçin Kullanılan Şifreyi Doğrulayın
type: docs
weight: 370
url: /tr/nodejs-cpp/verify-password-used-to-protect-the-worksheet/
description: Aspose.Cells for Node.js via C++ kullanarak çalışma sayfasını korumak için kullanılan şifreyi nasıl doğrulayacağınızı öğrenin.
---

{{% alert color="primary" %}}

Aspose.Cells API'leri, [**Protection**](https://reference.aspose.com/cells/nodejs-cpp/protection) sınıfını çeşitli kullanışlı özellikler ve metodlar ile geliştirdi. Bu metodlardan biri, şifreyi bir *string* örneği olarak belirlemeye olanak tanıyan ve çalışma sayfasını korumak için kullanılan şifreyi doğrulayan [**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/nodejs-cpp/protection/#verifyPassword-string-) metodudur.

{{% /alert %}}

[**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/nodejs-cpp/protection/#verifyPassword-string-) metodu, belirttiğiniz şifre ile korunan çalışma sayfasının şifresi eşleşiyorsa **true**, eşleşmiyorsa **false** döner. Bu kod parçacığı, şifre koruma tespiti için [**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/nodejs-cpp/protection/#verifyPassword-string-) metodunu ve [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/nodejs-cpp/protection/#isProtectedWithPassword--) özelliğini kullanır ve şifreyi doğrular.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample.xlsx");
// Create an instance of Workbook and load a spreadsheet
const workbook = new AsposeCells.Workbook(filePath);

// Access the protected Worksheet
const sheet = workbook.getWorksheets().get(0);

// Check if Worksheet is password protected
if (sheet.getProtection().isProtectedWithPassword()) {
// Verify the password used to protect the Worksheet
if (sheet.getProtection().verifyPassword("1234")) {
console.log("Specified password has matched");
} else {
console.log("Specified password has not matched");
}
}
```
{{< app/cells/assistant language="nodejs-cpp" >}}
