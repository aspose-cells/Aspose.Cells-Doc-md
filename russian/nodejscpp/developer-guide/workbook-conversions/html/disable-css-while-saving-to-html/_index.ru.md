---
title: Отключить CSS при сохранении в HTML с помощью Node.js через C++
linktitle: Отключить CSS при сохранении в HTML
type: docs
weight: 320
url: /ru/nodejs-cpp/disable-css-while-saving-to-html/
description: Узнайте, как отключить CSS при сохранении файлов Excel в HTML с помощью Aspose.Cells for Node.js via C++. 
---

## **Возможные сценарии использования**

При сохранении файла Excel в одностраничный HTML, CSS-элементы обычно внедряются в HTML и размещаются в разделе HEAD. Если вы вставите такой файл как содержание/тело письма, большинство почтовых клиентов удалит CSS и произойдет неправильное отображение. В версии Aspose.Cells 24.12 появилась возможность по желанию отключить CSS, чтобы стили применялись непосредственно к HTML-элементам. Для установки HTML в качестве содержимого тела письма используйте свойство [**HtmlSaveOptions.getDisableCss()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDisableCss--) и установите его в **true**.

## **Отключить CSS при сохранении в HTML**

Следующий пример показывает использование свойства [**HtmlSaveOptions.getDisableCss()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDisableCss--). 

## **Образец кода**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample workbook
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleDisableCss.xlsx"));

// Disable CSS
const opts = new AsposeCells.HtmlSaveOptions();
opts.setDisableCss(true);

// Save the workbook in HTML
workbook.save(path.join(outputDir, "outputDisable.html"), opts);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
