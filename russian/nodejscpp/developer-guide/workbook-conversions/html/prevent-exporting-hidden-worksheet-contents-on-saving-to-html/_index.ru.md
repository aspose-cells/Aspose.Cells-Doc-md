---
title: Предотвращение экспорта скрытого содержимого рабочего листа при сохранении в HTML с Node.js через C++
linktitle: Предотвращение экспорта скрытого содержимого листа при сохранении в HTML
type: docs
weight: 210
url: /ru/nodejs-cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/
description: Узнайте, как предотвратить экспорт скрытого содержимого рабочего листа при сохранении файлов Excel в HTML с помощью Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Вы можете сохранять книги Excel в HTML. Однако, если в книге есть скрытые листы, Aspose.Cells по умолчанию экспортирует скрытое содержимое листа в выходной каталог HTML (_files), который содержит файлы, такие как листы, изображения, tabstrip.htm, stylesheet.css и т. д. Иногда экспорт содержимого скрытых листов таким образом нецелесообразен. Например, если скрытый лист содержит изображения, которые не должны быть экспортированы в каталог _files.

{{% /alert %}}

Aspose.Cells for Node.js via C++ предлагает свойство [**HtmlSaveOptions.getExportHiddenWorksheet()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportHiddenWorksheet--). По умолчанию оно установлено в **true**, и скрытые листы экспортируются в HTML. Если установить его в **false**, Aspose.Cells не будет экспортировать скрытое содержимое листов.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook object
const workbook = new AsposeCells.Workbook(path.join(dataDir, "WorkbookWithHiddenContent.xlsx"));

// Do not export hidden worksheet contents
const options = new AsposeCells.HtmlSaveOptions();
options.setExportHiddenWorksheet(false);

// Save the workbook
workbook.save(path.join(dataDir, "HtmlWithoutHiddenContent_out.html"), options);
```

