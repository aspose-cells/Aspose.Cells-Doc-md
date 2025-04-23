---
title: Отключить экспорт скриптов рамки и свойств документа с помощью Node.js через C++
linktitle: Отключить экспорт блоков сценариев и свойств документа
type: docs
weight: 310
url: /ru/nodejs-cpp/disable-exporting-frame-scripts-and-document-properties/
description: Узнайте, как отключить экспорт скриптов рамки и свойств документа при преобразовании workbook в HTML с помощью Aspose.Cells for Node.js via C++.
--- 

{{% alert color="primary" %}}

Aspose.Cells экспортирует скрипты рамки и свойства документа при преобразовании книги в HTML. В версии 8.6.0 Aspose.Cells for Node.js via C++ появилась возможность по желанию отключить экспорт этих элементов. Используйте свойство `HtmlSaveOptions.exportFrameScriptsAndProperties` для отключения экспорта.

{{% /alert %}}

## **Отключение экспорта сценариев рамки и свойств документа**

Следующий образец кода позволяет отключить экспорт сценариев рамки и свойств документа. После преобразования книги в HTML выходной файл не будет содержать никаких сценариев рамки и свойств документа.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the required workbook to convert
const filePath = path.join(dataDir, "Sample1.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Disable exporting frame scripts and document properties
const options = new AsposeCells.HtmlSaveOptions();
options.setExportFrameScriptsAndProperties(false);

// Save workbook as HTML
workbook.save(path.join(dataDir, "output.out.html"), options);
```
