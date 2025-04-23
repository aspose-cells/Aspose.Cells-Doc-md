---
title: Обнаружение, заблокирован ли лист паролем, с помощью Node.js через C++
linktitle: Определить, защищен ли рабочий лист паролем
type: docs
weight: 360
url: /ru/nodejs-cpp/detect-if-worksheet-is-password-protected/
description: Изучите, как определить, защищён ли лист паролем, с помощью Aspose.Cells for Node.js via C++. 
keywords: Обнаружение защиты листа паролем с помощью Node.js через C++, проверка защищен ли лист паролем в Node.js через C++, Aspose.Cells for Node.js via C++
---

{{% alert color="primary" %}}

Возможно защищать рабочие книги и листы отдельно. Например, в таблице может быть один или несколько листов, защищённых паролем, однако сама таблица может быть защищена или нет. API Aspose.Cells предоставляет средства для определения, защищён ли конкретный лист паролем. В этой статье демонстрируется использование API Aspose.Cells for Node.js via C++ для достижения этого.

{{% /alert %}}

Aspose.Cells for Node.js via C++ предоставляет свойство [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/nodejs-cpp/protection/#isProtectedWithPassword--) для определения, защищён ли лист паролем или нет. Логическое свойство [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/nodejs-cpp/protection/#isProtectedWithPassword--) возвращает **true**, если [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) защищён паролем, и **false**, если нет.

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
