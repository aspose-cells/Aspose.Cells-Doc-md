---  
title: Указание значимых цифр для хранения в Excel с Node.js через C++  
linktitle: Указание значащих разрядов для хранения в файле Excel  
type: docs  
weight: 30  
url: /ru/nodejs-cpp/specifying-significant-digits-to-be-stored-in-excel-file/  
description: Узнайте, как указать значимые цифры для хранения в Excel с помощью Aspose.Cells for Node.js via C++.  
---  

## **Возможные сценарии использования**  

По умолчанию, Aspose.Cells for Node.js via C++ сохраняет 17 значимых цифр для значений double внутри файла Excel, в отличие от MS-Excel, который сохраняет только 15 значимых цифр. Вы можете изменить поведение Aspose.Cells с 17 до 15 значимых цифр, используя свойство [**CellsHelper.getSignificantDigits()**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#getSignificantDigits--).  

## **Указание значащих разрядов для хранения в файле Excel**  

Следующий пример кода принуждает Aspose.Cells использовать 15 значимых цифр при сохранении double значений внутри файла Excel. Проверьте [выходной файл Excel](22774105.xlsx). Переименуйте расширение в .zip, распакуйте и увидите, что внутри файла сохраняется только 15 значимых цифр. Следующий скриншот демонстрирует эффект свойства [**CellsHelper.getSignificantDigits()**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#getSignificantDigits--) на итоговый файл Excel.  

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)  

## **Образец кода**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// By default, Aspose.Cells stores 17 significant digits unlike
// MS-Excel which stores only 15 significant digits
AsposeCells.CellsHelper.setSignificantDigits(15);

// Create workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access cell A1
const c = worksheet.getCells().get("A1");

// Put double value, only 15 significant digits as specified by
// CellsHelper.SignificantDigits above will be stored in excel file just like MS-Excel does
c.putValue(1234567890.123451711);

// Save the workbook
workbook.save(path.join(dataDir, "out_SignificantDigits.xlsx"));
```  

