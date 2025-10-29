---
title: Excel в HTML  использование опции PresentationPreference для лучшей раскладки с помощью Node.js через C++
linktitle: Excel в HTML  Используйте опцию PresentationPreference для лучшего макета
type: docs
weight: 220
url: /ru/nodejs-cpp/excel-to-html-use-presentationpreference-option-for-better-layout/
---

{{% alert color="primary" %}} 

Aspose.Cells предоставляет полезное свойство HtmlSaveOptions.presentationPreference для разработчиков, которым нужно добиться лучшей раскладки при сохранении файла Microsoft Excel в формат HTML или MHT. Значение свойства по умолчанию - false. Рекомендуется установить это свойство в true для более привлекательной презентации отчетов Excel.

{{% /alert %}} 

Ниже приведен пример кода, демонстрирующий, как рендерить HTML-файл из отчета Excel с включенной опцией презентации.



```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate the Workbook
// Load an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Create HtmlSaveOptions object
const options = new AsposeCells.HtmlSaveOptions();
// Set the Presentation preference option
options.setPresentationPreference(true);

// Save the Excel file to HTML with specified option
workbook.save(path.join(dataDir, "outPresentationlayout1.out.html"), options);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
