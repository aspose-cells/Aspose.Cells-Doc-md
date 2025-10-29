---
title: Преобразование XLS файла с изображениями или графиками в PDF с помощью Node.js через C++
linktitle: Преобразование XLS файла с изображениями или диаграммами в PDF
type: docs
weight: 50
url: /ru/nodejs-cpp/convert-xls-file-with-images-or-charts-to-pdf/
---

{{% alert color="primary" %}} 

Aspose.Cells поддерживает преобразование XLS файлов с изображениями и графиками в PDF документы. Aspose.Cells for Node.js via C++ может работать независимо для преобразования таблицы в PDF: для этого не требуется Aspose.PDF для Node.js через C++. Процесс можно выполнить в памяти, так как он не зависит от временных или промежуточных XML-файлов. Это означает, что большие файлы Excel, такие как содержащие изображения, графики и другие графические объекты, могут быть быстро и эффективно преобразованы.

{{% /alert %}} 
## **Образец кода**


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
try {
// Get the template excel file path.
const designerFile = path.join(dataDir, "SampleInput.xls");

// Specify the pdf file path.
const pdfFile = path.join(dataDir, "Output.out.pdf");

// Open the template excel file
const wb = new AsposeCells.Workbook(designerFile);

// Save the pdf file.
wb.save(pdfFile, AsposeCells.SaveFormat.Pdf);
} catch (e) {
console.log(e.message);
}
```

{{% alert color="primary" %}} 

Если таблица содержит формулы, лучше всего вызвать метод [Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) прямо перед преобразованием в PDF. Это обеспечивает пересчет зависимых от формул значений и правильное отображение значений в PDF.

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}
