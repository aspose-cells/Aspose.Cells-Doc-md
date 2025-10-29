---
title: Автоматическая подгонка строк для объединенных ячеек с помощью Node.js через C++
linktitle: Автоподгонка строк для объединенных ячеек
type: docs
weight: 120
url: /ru/nodejs-cpp/autofit-rows-for-merged-cells/
description: Узнайте, как автоматически подгонять строки для объединенных ячеек с помощью Aspose.Cells for Node.js via C++. Реализуйте функцию автоматической подгонки для объединенных ячеек в таблицах.
---

{{% alert color="primary" %}}

Microsoft Excel предоставляет функцию, которая позволяет автоматически подгонять высоту ячейки в соответствии с ее содержимым. Функция называется автоматическим регулированием строк. В Microsoft Excel не устанавливается автоматическое регулирование на объединенных ячейках по умолчанию. Иногда функция становится жизненно важной для пользователя, который действительно нуждается в реализации автоподгонки строк и на объединенных ячейках тоже.

{{% /alert %}}

## **Как использовать AutoFitMergedCellsType для автоподгонки строк**
Aspose.Cells for Node.js via C++ поддерживает эту функцию через API [**AutoFitterOptions.autoFitMergedCellsType**](https://reference.aspose.com/cells/nodejs-cpp/autofitmergedcellstype/). Используя этот API, возможно автоматически подгонять высоту строк в листе, включая объединенные ячейки. Ниже приведен список всех возможных типов автоматической подгонки объединенных ячеек:

- Нет
- Первая строка
- Последняя строка
- Каждая строка

## **Автонастройка строк для объединенных ячеек**

Пожалуйста, посмотрите следующий код, он создает объект рабочей книги и добавляет несколько листов. Используйте различные методы для автоподгонки операций на каждом листе. Скриншот показывает результаты после выполнения примерного кода.

<br>
<img src="result.png" width=80% />

## **Пример кода Node.js**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();
// Obtaining the reference of the newly added worksheet
const sheet1 = workbook.getWorksheets().get(0);

// Create a range A1:B2
const range = sheet1.getCells().createRange(0, 0, 2, 2);

// Merge the cells
range.merge();

// Insert value to the merged cell A1
sheet1.getCells().get(0, 0).setValue("A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end");

// Create a style object
const style = sheet1.getCells().get(0, 0).getStyle();

// Set wrapping text on
style.setIsTextWrapped(true);

// Apply the style to the cell
sheet1.getCells().get(0, 0).setStyle(style);

// Create an object for AutoFitterOptions
const options = new AsposeCells.AutoFitterOptions();

// Only expands the height of the first row.
options.setAutoFitMergedCellsType(AsposeCells.AutoFitMergedCellsType.FirstLine);

// Autofit rows in the sheet (including the merged cells)
sheet1.autoFitRows(options);

let index = workbook.getWorksheets().add();
const sheet2 = workbook.getWorksheets().get(index);
sheet2.setName("Sheet2");
// Create a range A1:B2
const range2 = sheet2.getCells().createRange(0, 0, 2, 2);

// Merge the cells
range2.merge();

// Insert value to the merged cell A1
sheet2.getCells().get(0, 0).setValue("A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end");

// Create a style object
const style2 = sheet2.getCells().get(0, 0).getStyle();

// Set wrapping text on
style2.setIsTextWrapped(true);

// Apply the style to the cell
sheet2.getCells().get(0, 0).setStyle(style2);

// Create an object for AutoFitterOptions
const options2 = new AsposeCells.AutoFitterOptions();

// Only expands the height of the last row.
options2.setAutoFitMergedCellsType(AsposeCells.AutoFitMergedCellsType.LastLine);

// Autofit rows in the sheet (including the merged cells)
sheet2.autoFitRows(options2);

index = workbook.getWorksheets().add();
const sheet3 = workbook.getWorksheets().get(index);
sheet3.setName("Sheet3");
// Create a range A1:B2
const range3 = sheet3.getCells().createRange(0, 0, 2, 2);

// Merge the cells
range3.merge();

// Insert value to the merged cell A1
sheet3.getCells().get(0, 0).setValue("A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end");

// Create a style object
const style3 = sheet3.getCells().get(0, 0).getStyle();

// Set wrapping text on
style3.setIsTextWrapped(true);

// Apply the style to the cell
sheet3.getCells().get(0, 0).setStyle(style3);

// Create an object for AutoFitterOptions
const options3 = new AsposeCells.AutoFitterOptions();

// Only expands the height of each row.
options3.setAutoFitMergedCellsType(AsposeCells.AutoFitMergedCellsType.EachLine);

// Autofit rows in the sheet (including the merged cells)
sheet3.autoFitRows(options3);

index = workbook.getWorksheets().add();
const sheet4 = workbook.getWorksheets().get(index);
sheet4.setName("Sheet4");
// Create a range A1:B2
const range4 = sheet4.getCells().createRange(0, 0, 2, 2);

// Merge the cells
range4.merge();

// Insert value to the merged cell A1
sheet4.getCells().get(0, 0).setValue("A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end");

// Create a style object
const style4 = sheet4.getCells().get(0, 0).getStyle();

// Set wrapping text on
style4.setIsTextWrapped(true);

// Apply the style to the cell
sheet4.getCells().get(0, 0).setStyle(style4);

// Create an object for AutoFitterOptions
const options4 = new AsposeCells.AutoFitterOptions();

// Ignore merged cells.
options4.setAutoFitMergedCellsType(AsposeCells.AutoFitMergedCellsType.None);

// Autofit rows in the sheet (not including the merged cells)
sheet4.autoFitRows(options4);

// Save the Excel file
workbook.save("out.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
