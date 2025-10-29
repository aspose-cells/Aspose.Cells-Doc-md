---  
title: Обнаружение пустых листов с помощью Node.js через C++  
linktitle: Обнаружение пустых рабочих листов  
type: docs  
weight: 410  
url: /ru/nodejs-cpp/detecting-empty-worksheets/  
description: Эта статья показывает код, объясняющий, как программно обнаруживать пустые листы рабочих книг Excel с помощью API Node.js и библиотеки C++.  
keywords: Обнаружение пустого листа Node.js через C++, поиск пустого листа Excel Node.js через C++  
---  

## **Проверка заполненных ячеек**

Листы могут иметь один или более заполненных ячеек со значениями, где значение может быть простым (текст, число, дата/время) или формулой или значением на основе формулы. В таком случае легко определить, является ли лист пустым или нет. Все, что нужно проверить — это свойства [**Cells.getMaxDataRow()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataRow--) или [**Cells.getMaxDataColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataColumn--). Если эти свойства возвращают ноль или положительные значения, это означает, что одна или более ячеек заполнены; однако, если любое из этих свойств возвращает -1, это говорит о том, что ни одна ячейка не заполнена на данном листе.

{{% alert color="primary" %}}

Коллекции строк и столбцов имеют нумерацию с нуля; следовательно, ячейка в строке 0 и столбце 0 — это первая ячейка в листе, то есть A1.

{{% /alert %}}

## **Проверка пустых инициализированных ячеек**

Все ячейки, содержащие значения, автоматически инициализируются; однако существует вероятность, что лист содержит ячейки только с форматированием. В таком случае свойства [**Cells.getMaxDataRow()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataRow--) или [**Cells.getMaxDataColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataColumn--) вернут -1, что указывает на отсутствие заполненных значений, но инициализированные ячейки из-за форматирования определить этим методом нельзя. Чтобы проверить, есть ли в листе пустые инициализированные ячейки, рекомендуется использовать метод `Enumerator.MoveNext()` на полученном из коллекции [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) перечислителе. Если метод `Enumerator.MoveNext()` возвращает **true**, это означает, что на листе есть одна или более инициализированных ячеек.

## **Проверка фигур**

Возможно, что на листе отсутствуют заполненные ячейки; при этом, он может содержать фигуры и объекты, такие как элементы управления, диаграммы, изображения и так далее. Если нужно проверить, содержит ли лист фигуры, можно сделать это, проверяя свойство [**ShapeCollection.getCount()**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#getCount--). Любое положительное значение свидетельствует о наличии фигур на листе.

## **Пример программирования**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const book = new AsposeCells.Workbook(filePath);

// Loop over all worksheets in the workbook
for (let i = 0; i < book.getWorksheets().getCount(); i++) {
const sheet = book.getWorksheets().get(i);
// Check if worksheet has populated cells
if (sheet.getCells().getMaxDataRow() !== -1) {
console.log(`${sheet.getName()} is not empty because one or more cells are populated`);
}
// Check if worksheet has shapes
else if (sheet.getShapes().getCount() > 0) {
console.log(`${sheet.getName()} is not empty because there are one or more shapes`);
}
// Check if worksheet has empty initialized cells
else {
const range = sheet.getCells().getMaxDisplayRange();
const rangeIterator = range.getEnumerator();
if (rangeIterator.moveNext()) {
console.log(`${sheet.getName()} is not empty because one or more cells are initialized`);
}
}
}
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
