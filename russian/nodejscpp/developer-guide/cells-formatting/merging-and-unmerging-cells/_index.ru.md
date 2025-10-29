---
title: Объединение и разъединение ячеек с помощью Node.js и C++
linktitle: Объединение и разъединение ячеек
description: Aspose.Cells — это библиотека Node.js для работы с файлами электронных таблиц, которая поддерживает объединение и разъединение ячеек. В этой статье рассказывается, как объединять и разъединять ячейки с помощью Aspose.Cells, а также как настраивать стиль объединенных ячеек.
keywords: Aspose.Cells, библиотека Node.js, электронная таблица, объединить ячейки, разъединить ячейки, настройки стилей, пользовательские стили
type: docs
weight: 190
url: /ru/nodejs-cpp/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells поддерживает эту функцию и также может объединять ячейки в листе. Вы также можете разъединить или разделить объединенные ячейки. Ссылка на объединенную ячейку - это ссылка на верхнюю левую ячейку в изначально выбранном диапазоне.

{{% /alert %}} 
## **Введение**
Не всегда нужно иметь одинаковое количество ячеек в каждой строке или столбце. Например, вы можете захотеть поместить заголовок в ячейку, которая охватывает несколько столбцов. Или, если создаете счет-фактуру, вам может понадобиться меньше столбцов для итоговой суммы. Чтобы объединить несколько ячеек в одну, объедините их. Microsoft Excel позволяет пользователям выбирать файлы и объединять их, чтобы структурировать электронную таблицу так, как им нужно.

{{% alert color="primary" %}} 

Обратите внимание, что при объединении ячеек сохраняются только данные в верхней левый ячейке. Если в других ячейках диапазона есть данные, эти данные удаляются. Форматирование также основывается на ссылочной ячейке, поэтому при объединении ячеек настройки форматирования верхней левой ячейки диапазона применяются к объединенной ячейке. Когда ячейки разбиваются, новые ячейки сохраняют свои исходные настройки формата.

{{% /alert %}} 
## **Объединение ячеек в листе**
### **Объединение ячеек в Microsoft Excel**
Следующие шаги описывают, как объединить ячейки в электронной таблице с использованием MS Excel.

1. Копируйте данные, которые вы хотите в верхнюю левую ячейку в пределах диапазона.
1. Выберите ячейки, которые вы хотите объединить.
1. Чтобы объединить ячейки в строке или столбце и центрировать содержимое ячейки, нажмите на значок **Объединить и центрировать** на панели инструментов **Форматирование**.

### **Объединение ячеек с помощью Aspose.Cells**
Класс Aspose.Cells.Cells содержит полезные методы для выполнения этой задачи. Например, метод `merge()` объединяет ячейки в одну в заданном диапазоне.

В следующем примере показано, как объединить ячейки (C6:E7) в электронной таблице.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a Workbook.
const wbk = new AsposeCells.Workbook();

// Create a Worksheet and get the first sheet.
const worksheet = wbk.getWorksheets().get(0);

// Create a Cells object to fetch all the cells.
const cells = worksheet.getCells();

// Merge some Cells (C6:E7) into a single C6 Cell.
cells.merge(5, 2, 2, 3);

// Input data into C6 Cell.
cells.get(5, 2).putValue("This is my value");

// Create a Style object to fetch the Style of C6 Cell.
const style = cells.get(5, 2).getStyle();

// Create a Font object
const font = style.getFont();

// Set the name.
font.setName("Times New Roman");

// Set the font size.
font.setSize(18);

// Set the font color
font.setColor(AsposeCells.Color.Blue);

// Bold the text
font.setIsBold(true);

// Make it italic
font.setIsItalic(true);

// Set the background color of C6 Cell to Red
style.setForegroundColor(AsposeCells.Color.Red);
style.setPattern(AsposeCells.BackgroundType.Solid);

// Apply the Style to C6 Cell.
cells.get(5, 2).setStyle(style);

// Save the Workbook.
wbk.save(path.join(dataDir, "mergingcells.out.xls"));
```

## **Разъединение (разделение) объединенных ячеек**
### **Использование Microsoft Excel**
Следующие шаги описывают, как разделить объединенные ячейки с помощью Microsoft Excel.

1. Выберите объединенную ячейку.
   Когда ячейки были объединены, на панели инструментов **Форматирование** выбрано **Объединить и центрировать**.
1. Нажмите на **Объединить и центрировать** на панели инструментов **Форматирование**.

### **Использование Aspose.Cells**
Класс Aspose.Cells.Cells содержит метод `unmerge()`, который разбивает ячейки до их исходного состояния. Метод разъединяет ячейки, используя ссылку ячейки в диапазоне объединенных ячеек.

Приведенный ниже пример показывает, как разделить объединенные ячейки (C6). Пример использует файл, созданный в предыдущем примере, и разбивает объединенные ячейки.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a Workbook.
// Open the excel file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "mergingcells.xls"));

// Create a Worksheet and get the first sheet.
const worksheet = workbook.getWorksheets().get(0);

// Create a Cells object to fetch all the cells.
const cells = worksheet.getCells();

// Unmerge the cells.
cells.unMerge(5, 2, 2, 3);

// Save the file.
workbook.save(path.join(dataDir, "unmergingcells.out.xls"));
```

## **Продвинутые темы**
- [Обнаружение объединенных ячеек в листе](/cells/ru/nodejs-cpp/detect-merged-cells-in-a-worksheet/)
{{< app/cells/assistant language="nodejs-cpp" >}}
