---  
title: Установка границы диапазона с помощью Node.js через C++  
linktitle: Установить границу диапазона  
type: docs  
weight: 600  
url: /ru/nodejs-cpp/set-range-border/  
---  

## **Возможные сценарии использования**  
Когда необходимо установить границу для диапазона, не нужно задавать каждую ячейку отдельно. Можно установить границу на весь диапазон. Aspose.Cells for Node.js via C++ предлагает эту возможность.  
Эта статья содержит пример кода, использующего Aspose.Cells for Node.js via C++ для установки границы диапазона.  

## **Установить границу диапазона в Excel**  
Чтобы установить границу диапазона в Excel, выполните следующие шаги:  
1. Выберите диапазон ячеек, к которым вы хотите применить границу.  
2. На вкладке "Домой" ленты найдите группу "Шрифт".  
3. Внутри группы "Шрифт" нажмите на кнопку "Границы".  
<br>  
<img src="border.png" />  
4. Выберите тип границы, который вы хотите применить из вариантов в выпадающем меню. Вы можете выбрать из предустановленных стилей границы или настроить свою собственную границу.  
5. Как только вы выбрали желаемый стиль границы, она будет применена к выбранному диапазону ячеек.  

## **Установка границы диапазона с помощью Aspose.Cells for Node.js via C++**  
Этот пример показывает, как:  

1. Создать книгу.  
2. Добавьте данные в ячейки на первом листе.  
3. Создайте [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range).  
4. Установите внутреннюю границу диапазона.  
5. Установите внешнюю границу диапазона.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();
// Obtaining the reference of the newly added worksheet
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

// Create a range (A1:C5).
const range = cells.createRange("A1", "C5");

// set inner border of range
const innerColor = workbook.createCellsColor();
innerColor.setColor(AsposeCells.Color.Red);
range.setInsideBorders(AsposeCells.BorderType.Vertical, AsposeCells.CellBorderType.Thin, innerColor);
innerColor.setColor(AsposeCells.Color.Green);
range.setInsideBorders(AsposeCells.BorderType.Horizontal, AsposeCells.CellBorderType.Thin, innerColor);

// set outer border of range
const outerColor = workbook.createCellsColor();
outerColor.setColor(AsposeCells.Color.Blue);
range.setOutlineBorders(AsposeCells.CellBorderType.Thin, outerColor);

workbook.save("out.xlsx");
```  
{{< app/cells/assistant language="nodejs-cpp" >}}
