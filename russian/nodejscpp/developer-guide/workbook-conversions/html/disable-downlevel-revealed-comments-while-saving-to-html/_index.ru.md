---
title: Отключить комментарии Downlevel Revealed при сохранении в HTML с помощью Node.js через C++
linktitle: Отключить отображение комментариев уровня Downlevel при сохранении в HTML
type: docs
weight: 20
url: /ru/nodejs-cpp/disable-downlevel-revealed-comments-while-saving-to/
description: Узнайте, как отключить комментарии Downlevel Revealed при сохранении файла Excel в HTML с помощью Aspose.Cells for Node.js via C++.
---

## **Возможные сценарии использования**

При сохранении файла Excel в HTML, Aspose.Cells отображает Downlevel Conditional Comments. Эти условные комментарии актуальны для более старых версий Internet Explorer и не важны для современных браузеров. Подробнее об этом можно прочитать по ссылке.

- [Условный комментарий - условный комментарий с раскрытием](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells for Node.js via C++ позволяет избавиться от этих комментариев, установив свойство [**HtmlSaveOptions.getDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDisableDownlevelRevealedComments--) в **true**.

## **Отключить отображение устаревших комментариев при сохранении в HTML**

Следующий пример показывает использование свойства [**HtmlSaveOptions.getDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDisableDownlevelRevealedComments--). Скриншот демонстрирует эффект этого свойства, когда оно не установлено в true. Загрузите [пример файла Excel](50528257.xlsx), использованный в этом коде, и [сгенерированный HTML](50528258.zip) для ознакомления.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Образец кода**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample workbook
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleDisableDownlevelRevealedComments.xlsx"));

// Disable DisableDownlevelRevealedComments
const opts = new AsposeCells.HtmlSaveOptions();
opts.setDisableDownlevelRevealedComments(true);

// Save the workbook in html
workbook.save(path.join(outputDir, "outputDisableDownlevelRevealedComments_true.html"), opts);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
