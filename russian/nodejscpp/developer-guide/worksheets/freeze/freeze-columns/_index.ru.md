---  
title: Заморозить первый(е) столбец(ы) листа Excel с помощью Node.js через C++  
linktitle: Заморозить столбцы  
type: docs  
weight: 190  
url: /ru/nodejs-cpp/how-to-freeze-columns-of-excel-worksheet  
description: Узнайте, как замораживать левый столбцы листов Excel программно с помощью Aspose.Cells for Node.js via C++.  
keywords: Заморозить левый столбцы, Заморозить первые столбцы, Заблокировать столбец(ы)  
---  

## **Введение**  

В этой статье мы узнаем, как зафиксировать левый(е) столбец(ы). Когда у вас есть большое количество данных в строке, вы можете не видеть левы�� столбцы при горизонтальной прокрутке листа. Вы можете зафиксировать и заблокировать первый(е) столбец(ы), чтобы видеть зафиксированную часть даже при прокрутке остальной части данных. Вы легко сможете видеть заголовки в левых столбцах.  

## **Заморозить столбцы в Excel**  

**![Заморозить левые столбцы в Excel](freeze-columns.png)**  

1. Если хотите заморозить левый(е) столбец(ы), сначала выберите столбец под столбцом, который необходимо зафиксировать.
2. Нажмите Вид > Заморозка областей.
3. В раскрывающемся меню нажмите "Заморозить первый столбец".
4. Если вы прокрутите вниз, первый столбец всегда останется слева.

**![Замороженный столбец](frozen-columns.png)**  

Как видите, первый столбец зафиксирован, и он всегда закреплён вверху при горизонтальной прокрутке.

Фиксация столбцов позволяет вам просматривать ваши длинные данные без необходимости отслеживать первый столбец.

## **Фиксация столбцов с помощью Aspose.Cells for Node.js via C++**  
Просто зафиксировать первый(е) столбец(цы) с помощью Aspose.Cells for Node.js via C++.  
Пожалуйста, используйте метод [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-) для заморозки столбцов в выбранном столбце.  
1. Создать рабочую книгу для открытия файла или создать пустой файл.
2. Зафиксируйте первый столбец с помощью метода Worksheet.freezePanes().
3. Сохранить файл.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Freeze.xlsx");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);
// Freezing panes at the second column
workbook.getWorksheets().get(0).freezePanes("B1", 0, 1);
// Saving the file
workbook.save("frozen.xlsx");
```  

Прикреплен файл [образец исходного файла Excel](Freeze.xlsx).  

