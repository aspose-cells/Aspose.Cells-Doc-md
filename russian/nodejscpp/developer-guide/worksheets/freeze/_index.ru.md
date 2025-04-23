---  
title: Заморозка панелей листа Excel с помощью Node.js через C++  
linktitle: Замораживание областей  
type: docs  
weight: 190  
url: /ru/nodejs-cpp/how-to-freeze-panes-of-excel-worksheet  
description: В этой статье вы узнаете, как программно заморозить панели листов Excel с помощью Aspose.Cells for Node.js via C++.  
keywords: Зафиксировать панели, зафиксировать окно.  
---  

## **Введение**  

 В этой статье мы расскажем, как зафиксировать панели. Когда у вас есть большой объем данных с общей заголовком, вы не сможете видеть заголовки при прокрутке листа. Каждый запис содержит много данных. Вы можете зафиксировать панели, чтобы видеть зафиксированную часть, даже когда остальная часть данных прокручивается. Вы легко сможете видеть заголовки в верхних строках или первых столбцах. Зафиксировать и разблокировать панели — это лишь изменение вида данных, без изменения самих данных.  

## **В Excel**  

**![Замораживание областей в Excel](Freeze-panes.png)**  

1. Если хотите зафиксировать панели, закрепите строки и столбцы, сначала выберите ячейку (например, B2).  
2. Нажмите Вид > Заморозка областей.  
3. В выпадающем меню выберите Заморозить области.  
4. При прокрутке вниз или вправо первая строка и первый столбец останутся зафиксированными.  

**![Зафиксированные панели](Frozen-Panes.png)**  

Как видно, первая строка и столбец A заморожены, вторая строка — 32, а вторая видимая колонка — D.  

Заморозка панелей позволяет просматривать большие данные, не теряя из виду метки строк или столбцов.  

## **Заморозить панели с помощью Aspose.Cells for Node.js via C++**  
Это просто — заморозить панели с помощью Aspose.Cells for Node.js via C++. Используйте метод [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-), чтобы зафиксировать панели в выбранной ячейке.  
1. Создать рабочую книгу для открытия файла или создать пустой файл.  
2. Заморозка панелей с помощью метода Worksheet.freezePanes().  
3. Сохранить файл.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Freeze.xlsx")); 
// Freezing panes at the cell B2
workbook.getWorksheets().get(0).freezePanes("B2", 1, 1);
// Saving the file
workbook.save("frozen.xlsx");
```  

Прикреплен файл [образец исходного файла Excel](Freeze.xlsx).  

