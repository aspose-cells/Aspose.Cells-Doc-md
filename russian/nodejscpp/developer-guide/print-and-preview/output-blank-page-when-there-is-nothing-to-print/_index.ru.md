---
title: Вывод пустой страницы при отсутствии печатных данных с помощью Node.js через C++
linktitle: Вывод пустой страницы, когда нечего печатать
type: docs
weight: 90
url: /ru/nodejs-cpp/output-blank-page-when-there-is-nothing-to-print/
---

## **Возможные сценарии использования**

Если лист пустой, то Aspose.Cells не выполнит печать при экспорте листа в изображение. Вы можете изменить это поведение, используя свойство [**ImageOrPrintOptions.getOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getOutputBlankPageWhenNothingToPrint--). При установке его в **true** будет напечатана пустая страница.

## **Вывод пустой страницы, когда нечего печатать**

Следующий пример создает пустую рабочую книгу с пустым листом и отображает его как изображение после установки свойства [**ImageOrPrintOptions.getOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getOutputBlankPageWhenNothingToPrint--) в **true**. В результате появляется пустая страница, поскольку нечего печатать, что видно на изображении ниже.

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)

## **Образец кода**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Output directory
const outputDir = path.join(__dirname, "output");

// Create workbook
const wb = new AsposeCells.Workbook();

// Access first worksheet - it is empty sheet
const ws = wb.getWorksheets().get(0);

// Specify image or print options
// Since the sheet is blank, we will set OutputBlankPageWhenNothingToPrint to true
// So that empty page gets printed
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setImageType(AsposeCells.ImageType.Png);
opts.setOutputBlankPageWhenNothingToPrint(true);

// Render empty sheet to png image
const sr = new AsposeCells.SheetRender(ws, opts);
sr.toImage(0, path.join(outputDir, "OutputBlankPageWhenNothingToPrint.png"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
