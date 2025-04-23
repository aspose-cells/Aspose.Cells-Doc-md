---  
title: Рендеринг одного PDF страницы на один лист Excel — преобразование Excel в PDF с помощью Node.js и C++  
linktitle: Рендеринг одной страницы PDF на один лист Excel – Преобразование Excel в PDF  
type: docs  
weight: 100  
url: /ru/nodejs-cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/  
---  

{{% alert color="primary" %}}  

 При работе с большими файлами Microsoft Excel (например, с книгой, содержащей много листов, каждый с 50 столбцами и 300 или более строками данных), вам может понадобиться, чтобы итоговый PDF отображал по одной странице на каждый лист, независимо от размера листа. Это означает, что каждая страница будет иметь значительно разный размер страницы. Этого можно добиться, используя Aspose.Cells for Node.js via C++.  

{{% /alert %}}  

Пожалуйста, ознакомьтесь с следующим образцом кода, который преобразует файл Excel с несколькими листами в PDF.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Initialize a new Workbook
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "input.xlsx"));

// Implement one page per worksheet option
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setOnePagePerSheet(true);

// Save the PDF file
workbook.save(path.join(dataDir, "OutputFile.out.pdf"), pdfSaveOptions);
```  

{{% alert color="primary" %}}  

Если опция [PdfSaveOptions.getOnePagePerSheet()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOnePagePerSheet--) установлена в **true**, весь контент листа будет отображен на одной странице PDF.  

{{% /alert %}} {{% alert color="primary" %}}  

Если в вашей таблице есть формулы, лучше всего вызвать [Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) прямо перед преобразованием таблицы в PDF. Это обеспечивает переодчисление зависимых значений формул и правильное отображение значений в PDF.  

{{% /alert %}}  

