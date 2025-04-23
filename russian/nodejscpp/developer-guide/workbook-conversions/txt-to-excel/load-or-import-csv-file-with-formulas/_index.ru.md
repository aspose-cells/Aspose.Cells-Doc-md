---  
title: Загрузка или импорт CSV файла с формулами с помощью Node.js  
linktitle: Загрузка или импорт файла CSV с формулами  
type: docs  
weight: 350  
url: /ru/nodejs-cpp/load-or-import-csv-file-with-formulas/  
description: Узнайте, как загружать и импортировать CSV файлы с формулами с помощью Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

 Большинство CSV-файлов содержит текстовые данные и не содержат формул. Тем не менее, иногда CSV-файлы также содержат формулы. Такие файлы нужно загружать, устанавливая [TxtLoadOptions.getHasFormula()](https://reference.aspose.com/cells/nodejs-cpp/txtloadoptions/#getHasFormula--) в **true**. После установки свойства в **true**, Aspose.Cells не будет воспринимать формулы как простой текст. Они будут обрабатываться как формулы, и движок вычисления формул Aspose.Cells будет их обрабатывать как обычно.

{{% /alert %}}  

 Следующий код демонстрирует, как загружать и импортировать CSV-файл с формулами. Можно использовать любой CSV-файл. В качестве примера используется [простой CSV-файл](5115034.csv), содержащий эти данные. Как видите, он содержит формулу.

{{< highlight javascript >}}  
const fs = require('fs');  
const AsposeCells = require('aspose.cells');  

let loadOptions = new AsposeCells.TxtLoadOptions();  
loadOptions.setHasFormula(true);  

let workbook = new AsposeCells.Workbook();  
workbook.open("path/to/your/file.csv", loadOptions);  
workbook.save("path/to/output.xlsx");  
{{< /highlight >}}  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.csv");

// TxtLoadOptions configuration
const opts = new AsposeCells.TxtLoadOptions();
opts.setSeparator(',');
opts.setHasFormula(true);

// Load your CSV file with formulas in a Workbook object
const workbook = new AsposeCells.Workbook(filePath, opts);

// You can also import your CSV file like this
// The code below is importing CSV file starting from cell D4
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().importCSV(filePath, opts, 3, 3);

// Save your workbook in Xlsx format
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

Сначала код загружает CSV-файл, затем импортирует его заново в ячейку D4. В конце он сохраняет рабочую книгу в формате XLSX. [Выходной XLSX-файл](5115052.xlsx) выглядит так. Как видно, ячейки C3 и F4 содержат формулы, а их результат — 800.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|  
| :- |  


