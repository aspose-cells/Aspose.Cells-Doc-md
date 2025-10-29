---
title: Удаление ведущих пустых строк и столбцов при экспорте таблиц в CSV с помощью Node.js через C++
linktitle: Обрезать ведущие пустые строки и столбцы при экспорте электронных таблиц в формат CSV
type: docs
weight: 100
url: /ru/nodejs-cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: Научитесь удалять ведущие пустые строки и столбцы при экспорте таблиц в CSV формат с помощью Aspose.Cells for Node.js via C++.
---

## **Возможные сценарии использования**

Иногда ваш файл Excel или CSV имеет ведущие пустые столбцы или строки. Например, рассмотрим эту строку

{{< highlight javascript >}}

 ,,,data1,data2

{{< /highlight >}}

Здесь первые три ячейки или столбца пусты. Когда вы открываете такой файл CSV в Microsoft Excel, то Microsoft Excel отбрасывает эти ведущие пустые строки и столбцы.

По умолчанию Aspose.Cells for Node.js via C++ не удаляет ведущие пустые столбцы и строки при сохранении, но если вы хотите удалить их так же, как делает Microsoft Excel, то Aspose.Cells предоставляет свойство [**TxtSaveOptions.getTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getTrimLeadingBlankRowAndColumn--). Установите его в **true**, и все ведущие пустые строки и столбцы будут удалены при сохранении.

{{% alert color="primary" %}}

 Перед выпуском версии 20.4 Aspose.Cells for Node.js via C++, значение [**TxtSaveOptions.getTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getTrimLeadingBlankRowAndColumn--) по умолчанию было **false**. Начиная с версии 20.4, значение по умолчанию для [**TxtSaveOptions.getTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getTrimLeadingBlankRowAndColumn--) — **true**.

{{% /alert %}}

## **Обрезать ведущие пустые строки и столбцы при экспорте электронных таблиц в формат CSV**

Следующий пример кода загружает [исходный Excel-файл](sampleTrimBlankColumns.xlsx), который содержит два ведущих пустых столбца. Он сначала сохраняет файл в формате CSV без изменений, затем устанавливает свойство [**TxtSaveOptions.getTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getTrimLeadingBlankRowAndColumn--) в **true** и сохраняет файл снова. Скриншоты показывают [исходный файл Excel](sampleTrimBlankColumns.xlsx), [выходной CSV без обрезки](outputWithoutTrimBlankColumns.csv) и [обрезанный CSV](outputTrimBlankColumns.csv).

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **Образец кода**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load source workbook
const wb = new AsposeCells.Workbook(path.join(dataDir, "sampleTrimBlankColumns.xlsx"));

// Save in csv format
wb.save(path.join(dataDir, "outputWithoutTrimBlankColumns.csv"), AsposeCells.SaveFormat.Csv);

// Now save again with TrimLeadingBlankRowAndColumn as true
const opts = new AsposeCells.TxtSaveOptions();
opts.setTrimLeadingBlankRowAndColumn(true);

// Save in csv format
wb.save(path.join(dataDir, "outputTrimBlankColumns.csv"), opts);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
