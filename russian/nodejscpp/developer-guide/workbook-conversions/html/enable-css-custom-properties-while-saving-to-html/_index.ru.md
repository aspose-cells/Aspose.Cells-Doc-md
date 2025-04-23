---
title: Включить CSS персональные свойства при сохранении в HTML с помощью Node.js через C++
linktitle: Включить пользовательские CSS свойства при сохранении в HTML
type: docs
weight: 320
url: /ru/nodejs-cpp/enable-css-custom-properties-while-saving-to-html/
description: Узнайте, как включить пользовательские свойства CSS при сохранении файлов Excel в HTML с помощью Aspose.Cells for Node.js via C++. 
---

## **Возможные сценарии использования**

При сохранении файла Excel в HTML, при наличии нескольких случаев одной базовой64 изображения, с пользовательским свойством данных изображения необходимо сохранять только один раз, чтобы повысить производительность итогового HTML. Пожалуйста, используйте свойство [**HtmlSaveOptions.getEnableCssCustomProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getEnableCssCustomProperties--) и установите его **true** при сохранении в HTML.
![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg) 


## **Включить пользовательские свойства CSS при сохранении в HTML**

Следующий пример кода показывает использование свойства [**HtmlSaveOptions.getEnableCssCustomProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getEnableCssCustomProperties--). Скриншот демонстрирует эффект этого свойства, когда оно не установлено в **true**. Пожалуйста, скачайте [пример файла Excel](50528260.xlsx), использованный в этом примере, и [выходной HTML файл](50528261.zip), сгенерированный им, для справки.



## **Образец кода**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load sample workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sampleEnableCssCustomProperties.xlsx"));

const opts = new AsposeCells.HtmlSaveOptions();
opts.setExportImagesAsBase64(true);

// Enable EnableCssCustomProperties
opts.setEnableCssCustomProperties(true);

// Save the workbook in HTML
workbook.save(path.join(dataDir, "outputEnableCssCustomProperties.html"), opts);
```
