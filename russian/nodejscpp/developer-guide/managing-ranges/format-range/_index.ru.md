---  
title: Форматировать диапазоны с помощью Node.js через C++  
linktitle: Форматирование диапазонов  
type: docs  
weight: 105  
url: /ru/nodejs-cpp/how-to-format-a-range/  
description: Узнайте, как форматировать диапазон ячеек в Excel с помощью Aspose.Cells for Node.js via C++.  
---  

## **Возможные сценарии использования**  
Когда вам необходимо применить стиль к диапазону, вы можете использовать форматирование диапазона.  

## **Как форматировать диапазон в Excel**  

Для форматирования диапазона ячеек в Excel вы можете использовать встроенные варианты форматирования, предоставленные Excel. Вот как можно форматировать диапазон ячеек непосредственно в Excel:  

1. Откройте Excel и книгу, которая содержит диапазон, который вы хотите отформатировать.  

2. Выберите диапазон ячеек, который вы хотите отформатировать. Вы можете щелкнуть и перетащить, чтобы выбрать диапазон, или вы можете использовать комбинации клавиш, такие как Shift + стрелки, чтобы расширить выбор.  

3. После выбора диапазона щелкните правой кнопкой мыши по выбранному диапазону и выберите "Формат ячеек" в контекстном меню. В качестве альтернативы, вы можете перейти на вкладку "Домой" на ленте Excel, щелкнуть на выпадающем списке "Формат" в группе "Ячейки" и выбрать "Формат ячеек".  

4. Появится диалоговое окно "Формат ячеек". Здесь вы можете выбрать различные варианты форматирования для применения к выбранному диапазону. Например, вы можете изменить стиль шрифта, размер шрифта, цвет шрифта, формат чисел, границы, цвет фона и т. д. Исследуйте различные вкладки в диалоговом окне, чтобы получить доступ к различным вариантам форматирования.  

5. После внесения желаемых изменений форматирования нажмите кнопку "OK", чтобы применить форматирование к выбранному диапазону.  

## **Как форматировать диапазон с помощью Node.js**  

Чтобы отформатировать диапазон с помощью Aspose.Cells for Node.js via C++, вы можете использовать следующие методы:  
1. [Range.applyStyle(стиль, флаг)](https://reference.aspose.com/cells/nodejs-cpp/range/#applyStyle-style-styleflag-)  
2. [Range.setStyle(стиль)](https://reference.aspose.com/cells/nodejs-cpp/range/#setStyle-style-)  
3. [Range.setStyle(стиль)](https://reference.aspose.com/cells/nodejs-cpp/range/#setStyle-style-)  

## **Образец кода**  
В этом примере мы создаем книгу Excel, добавляем некоторые образцовые данные, получаем доступ к первому рабочему листу и определяем два диапазона ("A1:C3" и "A4:C5"). Затем создаем новые стили, устанавливаем различные параметры форматирования (например, цвет шрифта, жирный) и применяем стиль к диапазону. Наконец, сохраняем книгу в новый файл.  
<br>  
![todo:image_alt_text](format-range.png)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create the workbook
const workbook = new AsposeCells.Workbook(filePath);
// Get the first worksheet
const ws = workbook.getWorksheets().get(0);

const cells = ws.getCells();

// Setting the value to the cells
let cell = cells.get("A1");
cell.putValue("Fruit");
cell = cells.get("B1");
cell.putValue("Count");
cell = cells.get("C1");
cell.putValue("Price");

cell = cells.get("A2");
cell.putValue("Apple");
cell = cells.get("A3");
cell.putValue("Mango");
cell = cells.get("A4");
cell.putValue("Blackberry");
cell = cells.get("A5");
cell.putValue("Cherry");

cell = cells.get("B2");
cell.putValue(5);
cell = cells.get("B3");
cell.putValue(3);
cell = cells.get("B4");
cell.putValue(6);
cell = cells.get("B5");
cell.putValue(4);

cell = cells.get("C2");
cell.putValue(5);
cell = cells.get("C3");
cell.putValue(20);
cell = cells.get("C4");
cell.putValue(30);
cell = cells.get("C5");
cell.putValue(60);

// Access the worksheet
const worksheet = workbook.getWorksheets().get(0);

// Define the range
const range = worksheet.getCells().createRange("A1:C3");

// Apply formatting to the range
const style = workbook.createStyle();
style.getFont().setColor(AsposeCells.Color.Red);
style.getFont().setIsBold(true);

const flag = new AsposeCells.StyleFlag();
flag.setFont(true);
range.applyStyle(style, flag);

// Define the range
const range2 = worksheet.getCells().createRange("A4:C5");

// Apply formatting to the range
const style2 = workbook.createStyle();
style2.getFont().setColor(AsposeCells.Color.Blue);
style2.getFont().setIsItalic(true);
range2.setStyle(style2);

// Save the modified workbook
workbook.save("output.xlsx");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
