---
title: Вычислить коэффициент масштабирования установки страниц с помощью Node.js через C++
linktitle: Вычислить масштабирование настройки страницы
type: docs
weight: 300
url: /ru/nodejs-cpp/calculate-page-setup-scaling-factor/
description: Этот пример кода показывает, как использовать API Node.js с C++, чтобы программно вычислить коэффициент масштабирования установки страниц с использованием опции подогнать на n страниц в ширину и m страниц по высоте рабочей книги Excel.
keywords: Подогнать на n страниц в ширину и m страниц по высоте Excel Node.js через C++, вычислить коэффициент масштабирования установки страниц с помощью Node.js через C++
---

{{% alert color="primary" %}}

При установке масштаба оформления страницы с помощью опции **подогнать на n страниц в ширину и m страниц по высоте** Microsoft Excel вычисляет коэффициент масштабирования. Вы можете вычислить то же самое, используя свойство [**SheetRender.getPageScale()**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#getPageScale--). Оно возвращает число с плавающей точкой, которое можно преобразовать в процент. Например, если возвращается 0.5, это означает масштаб 50%.

{{% /alert %}}

В следующем примере кода показано, как рассчитать масштабный коэффициент настроек страницы, используя свойство [**SheetRender.getPageScale()**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#getPageScale--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Put some data in these cells
worksheet.getCells().get("A4").putValue("Test");
worksheet.getCells().get("S4").putValue("Test");

// Set paper size
worksheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA4);

// Set fit to pages wide as 1
worksheet.getPageSetup().setFitToPagesWide(1);

// Calculate page scale via sheet render
const sr = new AsposeCells.SheetRender(worksheet, new AsposeCells.ImageOrPrintOptions());

// Convert page scale double value to percentage
const strPageScale = (sr.getPageScale() * 100).toFixed(0) + "%";

// Write the page scale value
console.log(strPageScale);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
