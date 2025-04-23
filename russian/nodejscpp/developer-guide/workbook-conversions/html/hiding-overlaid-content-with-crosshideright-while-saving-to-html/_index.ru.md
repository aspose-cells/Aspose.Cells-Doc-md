---
title: Скрытие накладываемого содержимого с помощью CrossHideRight при сохранении в HTML с Node.js через C++
linktitle: Скрытие перекрывающегося контента с помощью CrossHideRight при сохранении в HTML
type: docs
weight: 100
url: /ru/nodejs-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/
---


## **Возможные сценарии использования**

При сохранении файла Excel в HTML вы можете указать разные типы пересечения для строк ячеек. По умолчанию Aspose.Cells генерирует HTML по Microsoft Excel, но если изменить тип пересечения на [**CrossHideRight**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype), то все строки справа от ячейки, наложенные или перекрывающиеся с содержимым ячейки, скрываются.

## **Скрытие перекрывающегося содержимого с CrossHideRight при сохранении в Html**

Следующий пример загрузит [образец файла Excel](64716894.xlsx), сохранит его в [выходной HTML](64716893.zip), установив [**HtmlSaveOptions.getHtmlCrossStringType()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getHtmlCrossStringType--) в [**CrossHideRight**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype). Скриншот показывает, как [**CrossHideRight**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype) влияет на вывод HTML по умолчанию.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Образец кода**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load sample Excel file
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Specify HtmlSaveOptions - Hide Overlaid Content with CrossHideRight while saving to Html
const opts = new AsposeCells.HtmlSaveOptions();
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.CrossHideRight);

// Save to HTML with HtmlSaveOptions
workbook.save(path.join(dataDir, "outputHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.html"), opts);
``` 
