---
title: Удалите лишние пробелы после разрывов строк при импорте HTML с помощью Node.js через C++
linktitle: Удаление избыточных пробелов после переноса строки при импорте HTML
type: docs
weight: 20
url: /ru/nodejs-cpp/delete-redundant-spaces-after-line-break-while-importing/
description: Узнайте, как удалить лишние пробелы после разрывов строк при импорте HTML с помощью Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Пожалуйста, используйте свойство [**HtmlLoadOptions.getDeleteRedundantSpaces()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getDeleteRedundantSpaces--) и установите его в **true**, чтобы удалить все лишние пробелы после тега разрыва строки. По умолчанию это свойство равно **false**, и лишние пробелы сохраняются в выходных файлах Excel.

{{% /alert %}}

## Влияние установки свойства HTMLLoadOptions.deleteRedundantSpaces в значение false и true

На следующем скриншоте показан эффект установки этого свойства в **false** и **true**.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

## Удаление избыточных пробелов после переноса строки при импорте HTML

### Пример программирования

Следующий пример показывает использование свойства [**HtmlLoadOptions.getDeleteRedundantSpaces()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getDeleteRedundantSpaces--). Пожалуйста, установите его в **true** или **false**, чтобы получить вывод, показанный на вышеуказанном скриншоте.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Sample Html containing redundant spaces after <br> tag
const html = "<html> <body> <table> <tr> <td> <br>    This is sample data <br>    This is sample data<br>    This is sample data</td> </tr> </table> </body> </html>";

// Convert Html to byte array
const byteArray = Buffer.from(html, 'utf-8');

// Set Html load options and keep precision true
const loadOptions = new AsposeCells.HtmlLoadOptions(AsposeCells.LoadFormat.Html);
loadOptions.setDeleteRedundantSpaces(true);

// Convert byte array into stream
const stream = Uint8Array.from(byteArray);

// Create workbook from stream with Html load options
const workbook = new AsposeCells.Workbook(stream, loadOptions);

// Access first worksheet
const sheet = workbook.getWorksheets().get(0);

// Auto fit the sheet columns
sheet.autoFitColumns();

// Save the workbook
const outputDir = path.join(__dirname, "output");
workbook.save(path.join(outputDir, "outputDeleteRedundantSpacesWhileImportingFromHtml.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
