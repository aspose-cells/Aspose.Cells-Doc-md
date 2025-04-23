---
title: Укажите, как переносить строки в выводимом HTML с помощью HtmlCrossType совместно с Node.js через C++
linktitle: Указать, как пересекать строку в выходном HTML с использованием HtmlCrossType
type: docs
weight: 140
url: /ru/nodejs-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
description: Узнайте, как управлять переполнением строк в HTML выходных данных, задавая HtmlCrossType в Aspose.Cells for Node.js via C++. 
---

## **Возможные сценарии использования**

Когда ячейка содержит текст или строку, но она больше ширины ячейки, строка выходит за пределы, если следующая ячейка в следующем столбце пустая или отсутствует. При сохранении файла Excel в HTML вы можете управлять этим переполнением, задавая тип переноса через перечисление [**HtmlCrossType**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype). Оно имеет следующие значения:

- **HtmlCrossType.Default**: отображается как в MS Excel; зависит от следующей ячейки. Если следующая ячейка null, строка будет перепрыгивать или обрезаться.

- **HtmlCrossType.MSExport**: Отображение строки как при экспорте HTML из MS Excel.

- **HtmlCrossType.Cross**: отображение HTML-перепрыгивания строки; производительность при создании крупных HTML-файлов будет более чем в десять раз быстрее, чем при установке значения по умолчанию или FitToCell.

- **HtmlCrossType.FitToCell**: отображает строку только внутри ширины ячейки.

## **Указать, как пересекать строку в выходном HTML с использованием HtmlCrossType**

Следующий пример кода загружает [пример файла Excel](51740732.xlsx) и сохраняет его в формате HTML, задавая разные значения [**HtmlCrossType**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype). Пожалуйста, скачайте [выходные HTML](51740734.zip), созданные этим кодом. Пример файла Excel содержит изображение с красной рамкой, как показано на этом скриншоте, который демонстрирует эффект значений [**HtmlCrossType**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype) на выводимый HTML.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Образец кода**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleHtmlCrossStringType.xlsx");

// Load the sample Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Specify HTML Cross Type
const opts = new AsposeCells.HtmlSaveOptions();
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.Default);
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.MSExport);
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.Cross);
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.FitToCell);

// Output Html
workbook.save("out" + opts.getHtmlCrossStringType() + ".htm", opts);
```
