---  
title: Сохранять разделители для пустых строк при экспорте таблиц в формат CSV с помощью Node.js через C++  
linktitle: Сохранять разделители для пустых строк при экспорте таблиц в формат CSV  
type: docs  
weight: 160  
url: /ru/nodejs-cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/  
---  

## **Сохранять разделители для пустых строк при экспорте таблиц в формат CSV**  

 Aspose.Cells позволяет сохранять разделители строк при конвертации таблиц в CSV формат. Для этого можно использовать свойство [**TxtSaveOptions.getKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getKeepSeparatorsForBlankRow--) из [**TxtSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/). [**TxtSaveOptions.getKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getKeepSeparatorsForBlankRow--) — логическое свойство. Чтобы сохранить разделители для пустых строк при конвертации файла Excel в CSV, установите свойство [**TxtSaveOptions.getKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getKeepSeparatorsForBlankRow--) в значение **true**.  

Следующий пример загружает [исходный файл Excel](84378743.xlsx). Он устанавливает свойство [**TxtSaveOptions.getKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getKeepSeparatorsForBlankRow--) в **true** и сохраняет файл как [output.csv](84378744.csv). Скриншот показывает сравнение исходного файла Excel, стандартного вывода при преобразовании в CSV и итогового результата, созданного при установке [**TxtSaveOptions.getKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getKeepSeparatorsForBlankRow--) в **true**.  

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)  

## **Образец кода**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Create a Workbook object and opening the file from its path
const wb = new AsposeCells.Workbook(filePath);

// Instantiate Text File's Save Options
const options = new AsposeCells.TxtSaveOptions();

// Set KeepSeparatorsForBlankRow to true to show separators in blank rows
options.setKeepSeparatorsForBlankRow(true);

// Save the file with the options
wb.save(path.join(dataDir, "output.csv"), options);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
