---
title: Установка ширины столбца в масштабируемую единицу, такую как em или процент, с помощью Node.js через C++
linktitle: Установка ширины столбца в масштабируемую единицу, такую как em или процент
type: docs
weight: 130
url: /ru/nodejs-cpp/set-column-width-to-scalable-unit-like-em-or-percent/
description: Узнайте, как установить ширину столбца в масштабируемых единицах, таких как em или проценты, в Aspose.Cells for Node.js via C++. Улучшите представление сгенерированных HTML таблиц.
---

Генерация HTML-файла из электронной таблицы очень распространена. Размер столбцов определяется в "pt", что работает во многих случаях. Однако может возникнуть ситуация, когда эта фиксированная величина не требуется. Например, если ширина контейнера панели составляет 600 пикселей, где отображается эта HTML-страница, могут появиться горизонтальные полосы прокрутки, если сгенерированная таблица будет шире. Требовалось, чтобы эта фиксированная ширина была заменена на масштабируемую единицу, такую как em или проценты, для лучшего отображения. Следующий пример кода можно использовать, где [**HtmlSaveOptions.getWidthScalable()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getWidthScalable--) устанавливается в **true** для создания масштабируемой ширины.

Образец исходного файла и выходные файлы можно загрузить по следующим ссылкам:

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load sample source file
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleForScalableColumns.xlsx");
const workbook = new AsposeCells.Workbook(sourceFilePath);

// Specify Html Save Options
const options = new AsposeCells.HtmlSaveOptions();

// Set the property for scalable width
options.setWidthScalable(true);

// Specify image save format
options.setExportImagesAsBase64(true);

// Save the workbook in Html format with specified Html Save Options
const outputFilePath = path.join(dataDir, "outsampleForScalableColumns.html");
workbook.save(outputFilePath, options);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
