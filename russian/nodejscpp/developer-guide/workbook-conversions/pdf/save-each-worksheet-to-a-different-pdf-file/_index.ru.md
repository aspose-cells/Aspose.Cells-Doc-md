---  
title: Сохранять каждый лист в отдельный PDF файл с помощью Node.js через C++  
linktitle: Сохраните каждый рабочий лист в отдельный файл PDF  
type: docs  
weight: 130  
url: /ru/nodejs-cpp/save-each-worksheet-to-a-different-pdf-file/  
---  

{{% alert color="primary" %}}  
Aspose.Cells поддерживает преобразование XLS-файлов (с изображениями, диаграммами и др.) в PDF-документы. Aspose.Cells for Node.js via C++ может работать независимо для преобразования таблицы в PDF, и для этого не нужно использовать Aspose.PDF для Node.js через C++. Всё преобразование может быть выполнено в памяти без создания временных файлов.  
{{% /alert %}}  

## **Сохранить каждый лист в отдельный файл PDF**  
Если вам нужно сохранить каждый лист из вашего шаблонного файла Excel для генерации различных PDF-файлов, это легко реализовать. Можно установить индекс одного листа в [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/nodejs-cpp/pdfs saveoptions/#sheetSet) за раз для преобразования в PDF.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Get the Excel file path
const filePath = path.join(dataDir, "input.xlsx");

// Instantiate a new workbook and open the Excel file from its location
const workbook = new AsposeCells.Workbook(filePath);

// Get the count of the worksheets in the workbook
const sheetCount = workbook.getWorksheets().getCount();

// Define PdfSaveOptions
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();

// Take PDFs of each sheet
for (let j = 0; j < sheetCount; j++) {
const ws = workbook.getWorksheets().get(j);

// set worksheet to output
const sheetSet = new AsposeCells.SheetSet([ws.getIndex()]);
pdfSaveOptions.setSheetSet(sheetSet);

workbook.save(path.join(dataDir, `worksheet-${ws.getName()}.out.pdf`), pdfSaveOptions);
}
```  

{{% alert color="primary" %}}  
Если ваш электронный таблицы содержит формулы, лучше всего вызвать [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) прямо перед преобразованием таблицы в формат PDF. Таким образом будет гарантирован пересчет значений, зависящих от формул, и в PDF файл будут выведены правильные значения.  
{{% /alert %}}  

