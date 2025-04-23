---  
title: Конвертация текста в столбцы с помощью Aspose.Cells for Node.js via C++  
linktitle: Преобразование текста в столбцы  
type: docs  
weight: 30  
url: /ru/nodejs-cpp/convert-text-to-columns-using-aspose-cells/  
description: Узнайте, как конвертировать текст в столбцы в Excel с помощью Aspose.Cells for Node.js via C++.  
---  

## **Возможные сценарии использования**  

Вы можете конвертировать ваш текст в столбцы с помощью Microsoft Excel. Эта функция доступна в *Инструментах данных* на вкладке *Данные*. Для разделения содержимого столбца на несколько столбцов данные должны содержать определенный разделитель, такой как запятая (или любой другой символ), по которому Microsoft Excel разделит содержимое ячейки. Aspose.Cells for Node.js via C++ также предоставляет эту функцию через [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#textToColumns-number-number-number-txtloadoptions-).  

## **Конвертация текста в столбцы с помощью Aspose.Cells for Node.js via C++**  

Следующий пример кода объясняет использование метода [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#textToColumns-number-number-number-txtloadoptions-). Сначала в столбец А первого листа добавляются имена людей — имя и фамилия разделены пробелом. Затем применяется метод [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#textToColumns-number-number-number-txtloadoptions-) к столбцу А и сохраняется как файл Excel с результатом. Если открыть [выходной файл Excel](25395213.xlsx), вы увидите, что имена находятся в столбце А, а фамилии — в столбце В, как на этом скриншоте.  

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)  

## **Образец кода**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create a workbook.
const wb = new AsposeCells.Workbook();

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Add people name in column A. First name and last name are separated by space.
ws.getCells().get("A1").putValue("John Teal");
ws.getCells().get("A2").putValue("Peter Graham");
ws.getCells().get("A3").putValue("Brady Cortez");
ws.getCells().get("A4").putValue("Mack Nick");
ws.getCells().get("A5").putValue("Hsu Lee");

// Create text load options with space as separator.
const opts = new AsposeCells.TxtLoadOptions();
opts.setSeparator(' ');

// Split the column A into two columns using TextToColumns() method.
// Now column A will have first name and column B will have second name.
ws.getCells().textToColumns(0, 0, 5, opts);

// Save the workbook in xlsx format.
wb.save(path.join(dataDir, "outputTextToColumns.xlsx"));
```  

