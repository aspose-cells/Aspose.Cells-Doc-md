---
title: Node.js ve C++ kullanarak Çalışma Sayfası Parola Korumasını Tespit Etmek
linktitle: Çalışma sayfasının Parola Korumalı Olup Olmadığını Algılama
type: docs
weight: 360
url: /tr/nodejs-cpp/detect-if-worksheet-is-password-protected/
description: Aspose.Cells for Node.js via C++ kullanarak bir sayfa parolalı olup olmadığını nasıl tespit edeceğinizi öğrenin. 
keywords: Node.js ve C++ kullanarak Çalışma Sayfası Parola Korumasını Tespit Etmek, Parola Koruması Var mı Kontrol Et, Aspose.Cells for Node.js via C++
---

{{% alert color="primary" %}}

Çalışma kitapları ve çalışma sayfaları ayrı ayrı korunabilir. Örneğin, bir elektronik tablo bir veya daha fazla parola korumalı çalışma sayfası içerebilir, ancak elektronik tablo kendisi korumalı veya değil olabilir. Aspose.Cells API'leri, belirli bir çalışma sayfasının parola korumalı olup olmadığını tespit etmenin yollarını sağlar. Bu makale, aynı amaca ulaşmak için Aspose.Cells for Node.js via C++ API'sinin kullanımını gösterir.

{{% /alert %}}

Aspose.Cells for Node.js via C++, bir çalışma sayfasının parola korumalı olup olmadığını tespit etmek için [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/nodejs-cpp/protection/#isProtectedWithPassword--) özelliğini ortaya çıkardı. Boolean türündeki [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/nodejs-cpp/protection/#isProtectedWithPassword--) özelliği, [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) password-protected ise **true**, değilse **false** döner.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create an instance of Workbook and load a spreadsheet
const book = new AsposeCells.Workbook(filePath);

// Access the protected Worksheet
const sheet = book.getWorksheets().get(0);

// Check if Worksheet is password protected
if (sheet.getProtection().isProtectedWithPassword()) {
console.log("Worksheet is password protected");
} else {
console.log("Worksheet is not password protected");
}
```
