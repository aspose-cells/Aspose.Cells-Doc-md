---  
title: Загрузка книги с указанием размера бумаги принтера через Node.js и C++  
linktitle: Загружать книгу с указанным размером бумаги принтера  
type: docs  
weight: 430  
url: /ru/nodejs-cpp/load-workbook-with-specified-printer-paper-size/  
description: Узнайте, как установить размер бумаги принтера при загрузке книги с помощью Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Вы можете указать размер бумаги принтера по вашему выбору при загрузке вашей книги с помощью метода [**LoadOptions.setPaperSize(PaperSizeType)**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setPaperSize-papersizetype-). Пожалуйста, обратите внимание, что если создать новый файл в MS Excel, вы обнаружите, что размер бумаги такой же, как установка выбранного принтера по умолчанию на вашем компьютере.  
{{% /alert %}}  

Следующий пример кода демонстрирует использование метода [**LoadOptions.setPaperSize(PaperSizeType)**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setPaperSize-papersizetype-). Он сначала создает книгу, затем сохраняет ее в памяти в формате XLSX. Затем она загружается с размером бумаги A5 и сохраняется в PDF. После этого она снова загружается с размером бумаги A3 и сохраняется в PDF. Если открыть итоговые PDF и проверить их размер бумаги, вы увидите, что они разные — один A5, другой A3. Пожалуйста, скачайте [выходной PDF формата А5](5115234.pdf) и [выходной PDF формата А3](5115233.pdf), созданные этим кодом.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a sample workbook and add some data inside the first worksheet
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("P30").putValue("This is sample data.");

// Save the workbook in memory stream
const ms = workbook.saveToStream();

// Now load the workbook from memory stream with A5 paper size
const opts = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
opts.setPaperSize(AsposeCells.PaperSizeType.PaperA5);
let workbookA5 = new AsposeCells.Workbook(ms, opts);

// Save the workbook in pdf format
workbookA5.save(path.join(dataDir, "LoadWorkbookWithPrinterSize-a5_out.pdf"));

// Now load the workbook again from memory stream with A3 paper size
ms.position = 0;
opts.setPaperSize(AsposeCells.PaperSizeType.PaperA3);
let workbookA3 = new AsposeCells.Workbook(ms, opts);

// Save the workbook in pdf format
workbookA3.save(path.join(dataDir, "LoadWorkbookWithPrinterSize-a3_out.pdf"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
