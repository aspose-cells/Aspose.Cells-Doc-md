---
title: Сохранить как ODF 1.1, 1.2 и 1.3 с помощью Node.js через C++
linktitle: Сохранить файл ODS в ODF 1.1, 1.2 и 1.3
description: Конвертировать Excel в спецификации ODF 1.1, 1.2 и 1.3 с помощью Aspose.Cells for Node.js via C++.
type: docs
weight: 230
url: /ru/nodejs-cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает сохранение файла ODS (**OpenDocument Spreadsheet**) в спецификациях ODF (**OpenDocument Format**) 1.1, 1.2 и 1.3. В Aspose.Cells есть свойство [**OdsSaveOptions.getOdfStrictVersion()**](https://reference.aspose.com/cells/nodejs-cpp/odssaveoptions/#getOdfStrictVersion--), которое указывает версию ODF для сохранения ODS файлов. Значение по умолчанию — [**OpenDocumentFormatVersionType.odf12**](https://reference.aspose.com/cells/nodejs-cpp/opendocumentformatversiontype/). Поэтому сохранение ODS файла без этого настройки использует спецификации 1.2.

{{% /alert %}}

Пример ниже создает объект рабочей книги, добавляет значение в ячейку A1 на первом листе и затем сохраняет файл ODS в спецификациях ODF 1.1, 1.2 и 1.3. По умолчанию файл ODS сохраняется в спецификации ODF 1.2.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Put some value in cell A1
const cell = worksheet.getCells().get("A1");
cell.putValue("Welcome to Aspose!");

// Save ODS in ODF 1.2 version which is default
let options = new AsposeCells.OdsSaveOptions();
workbook.save(path.join(dataDir, "ODF1.2_out.ods"), options);

// Save ODS in ODF 1.1 version
options.setOdfStrictVersion(AsposeCells.OpenDocumentFormatVersionType.Odf11);
workbook.save(path.join(dataDir, "ODF1.1_out.ods"), options);

// Save ODS in ODF 1.3 version
options.setOdfStrictVersion(AsposeCells.OpenDocumentFormatVersionType.Odf13);
workbook.save(path.join(dataDir, "ODF1.3_out.ods"), options);
```
