---
title: Проверка пароля, используемого для защиты листа с помощью Node.js через C++
linktitle: Проверить использованный пароль для защиты рабочего листа
type: docs
weight: 370
url: /ru/nodejs-cpp/verify-password-used-to-protect-the-worksheet/
description: Узнайте, как проверить пароль, используемый для защиты листа, с помощью Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

API Aspose.Cells расширили класс [**Protection**](https://reference.aspose.com/cells/nodejs-cpp/protection), добавив полезные свойства и методы. Одним из таких методов является [**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/nodejs-cpp/protection/#verifyPassword-string-), который позволяет указать пароль как экземпляр *string* и проверить, использовался ли этот пароль для защиты [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet).

{{% /alert %}}

Метод [**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/nodejs-cpp/protection/#verifyPassword-string-) возвращает **true**, если указанный пароль совпадает с паролем, используемым для защиты данного листа, и **false** — если не совпадает. Следующий код использует метод [**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/nodejs-cpp/protection/#verifyPassword-string-) совместно со свойством [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/nodejs-cpp/protection/#isProtectedWithPassword--) для обнаружения защиты паролем и проверки пароля.

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
