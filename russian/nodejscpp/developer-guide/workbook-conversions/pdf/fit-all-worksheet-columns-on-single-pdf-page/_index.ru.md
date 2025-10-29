---
title: Оставьте все столбцы листа на одной странице PDF с помощью Node.js через C++
linktitle: Вписать все столбцы листа в одну страницу PDF
type: docs
weight: 160
url: /ru/nodejs-cpp/fit-all-worksheet-columns-on-single-pdf-page/
---

{{% alert color="primary" %}}

Иногда требуется создать PDF-файл, в который поместятся все столбцы листа на одну страницу. Cвойство [**PdfSaveOptions.getAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getAllColumnsInOnePagePerSheet--) предоставляет эту функцию в очень удобной форме использования. Сложные вычисления, такие как высота и ширина выходного PDF, обрабатываются внутри и основаны на данных в листе.

{{% /alert %}}

## **Вписать столбцы листа на одну страницу PDF**

[**PdfSaveOptions.getAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getAllColumnsInOnePagePerSheet--) обеспечивает отображение всех столбцов листа на одной странице PDF, при этом строки могут расходиться на несколько страниц в зависимости от данных в листе.

Приведенный ниже образец кода показывает, как использовать свойство [**PdfSaveOptions.getAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getAllColumnsInOnePagePerSheet--) для отображения большого листа с 100 столбцами.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create and initialize an instance of Workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "TestBook.xlsx"));
// Create and initialize an instance of PdfSaveOptions
const saveOptions = new AsposeCells.PdfSaveOptions();
// Set AllColumnsInOnePagePerSheet to true
saveOptions.setAllColumnsInOnePagePerSheet(true);
// Save Workbook to PDF format by passing the object of PdfSaveOptions
const outputFilePath = path.join(dataDir, "output.out.pdf");
workbook.save(outputFilePath, saveOptions);
```

{{% alert color="primary" %}}

Когда у какого-либо листа много столбцов, сгенерированный PDF-файл может отображать содержимое очень маленького размера. Оно все еще читаемо при увеличении в приложении для просмотра, таком как Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

Если ваш электронный таблицы содержит формулы, лучше всего вызвать [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) прямо перед преобразованием таблицы в формат PDF. Таким образом будет гарантирован пересчет значений, зависящих от формул, и в PDF файл будут выведены правильные значения.

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}
