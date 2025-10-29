---  
title: Как и где использовать перечислители с Node.js через C++  
linktitle: Итерация данных  
type: docs  
weight: 55  
url: /ru/nodejs-cpp/how-and-where-to-use-enumerators/  
description: Узнайте, как использовать перечислители через API Aspose.Cells for Node.js via C++.  
keywords: Как использовать перечислители Node.js через C++, перечислитель ячеек Node.js, перечислитель строк Node.js, перечислитель столбцов Node.js через C++  
---  

{{% alert color="primary" %}}  

Перечислитель — это объект, который обеспечивает возможность обхода контейнера или коллекции. Перечислители могут использоваться для чтения данных в коллекции, но не могут изменять исходную коллекцию, в то время как Array — это интерфейс, который определяет один метод `getEnumerator`, возвращающий интерфейс `IEnumerator`, что в свою очередь позволяет только чтение коллекции.  

API Aspose.Cells предоставляет множество перечислителей, однако в данной статье обсуждаются в основном три типа, перечисленные ниже.  

1. Перечислитель ячеек  
1. Перечислитель строк  
1. Перечислитель столбцов  

{{% /alert %}}  

## **Как использовать перечислители**  

### **Перечислитель ячеек**  

Существуют различные способы доступа к перечислителю ячеек, и можно использовать любые из этих методов в зависимости от требований приложения. Вот методы, возвращающие перечислитель ячеек.  

1. [**Cells.getEnumerator()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getEnumerator--)  
1. [**Row.getEnumerator()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getEnumerator--)  
1. [**Range.getEnumerator()**](https://reference.aspose.com/cells/nodejs-cpp/range/#getEnumerator--)  

Все вышеперечисленные методы возвращают перечислитель, который позволяет осуществлять обход коллекции ячеек, которые были инициализированы.  

{{% alert color="primary" %}}  

При обходе ячеек коллекция не должна изменяться (операции, которые приведут к созданию новой ячейки или удалению существующей). В противном случае перечислитель может не иметь возможности правильно обойти все ячейки (некоторые элементы могут быть обойдены повторно или пропущены).  

{{% /alert %}}  

Следующий пример кода демонстрирует реализацию интерфейса `IEnumerator` для коллекции ячеек.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const cells = workbook.getWorksheets().get(0).getCells().getEnumerator();
for (const cell of cells) {
console.log(`${cell.getName()} ${cell.getValue()}`);
}

const rowCells = workbook.getWorksheets().get(0).getCells().getRows().get(0).getEnumerator();
for (const cell of rowCells) {
console.log(`${cell.getName()} ${cell.getValue()}`);
}

const rangeCells = workbook.getWorksheets().get(0).getCells().createRange("A1:B10").getEnumerator();
for (const cell of rangeCells) {
console.log(`${cell.getName()} ${cell.getValue()}`);
}
```  

### **Перечислитель строк**  

Перечислитель строк можно получить при использовании метода [**RowCollection.getEnumerator()**](https://reference.aspose.com/cells/nodejs-cpp/rowcollection/#getEnumerator--). Следующий пример кода демонстрирует реализацию интерфейса `IEnumerator` для [**RowCollection**](https://reference.aspose.com/cells/nodejs-cpp/rowcollection).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get RowCollection and iterate using index
const rows = workbook.getWorksheets().get(0).getCells().getRows();
const rowCount = rows.getCount();

// Traverse rows in the collection
for (let i = 0; i < rowCount; i++) {
const row = rows.get(i);
console.log(row.getIndex());
}
```  

### **Перечислитель столбцов**  

Перечислитель столбцов можно получить при использовании метода [**ColumnCollection.getEnumerator**](https://reference.aspose.com/cells/nodejs-cpp/columncollection). Следующий пример кода демонстрирует реализацию интерфейса `IEnumerator` для [**ColumnCollection**](https://reference.aspose.com/cells/nodejs-cpp/columncollection).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get columns collection
const columns = workbook.getWorksheets().get(0).getCells().getColumns();
// Traverse columns using index
const count = columns.getCount();
for (let i = 0; i < count; i++) {
const col = columns.get(i);
console.log(col.getIndex());
}
```  

## **Где использовать перечислители**  

Чтобы обсудить преимущества использования перечислителей, возьмем реальный пример.  

**Сценарий**  

Требование приложения состоит в том, чтобы обойти все ячейки в заданном [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) для чтения их значений. Существует несколько способов реализации этой цели. Некоторые из них показаны ниже.  

### **Использование диапазона отображения**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get Cells collection of first worksheet
const cells = workbook.getWorksheets().get(0).getCells();

// Get the MaxDisplayRange
const displayRange = cells.getMaxDisplayRange();

// Loop over all cells in the MaxDisplayRange
for (let row = displayRange.getFirstRow(); row < displayRange.getRowCount(); row++) {
for (let col = displayRange.getFirstColumn(); col < displayRange.getColumnCount(); col++) {
// Read the Cell value
console.log(displayRange.get(row, col).getStringValue());
}
}
```  

### **Использование MaxDataRow и MaxDataColumn**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get Cells collection of first worksheet
const cells2 = workbook.getWorksheets().get(0).getCells();
const maxDataRow = cells2.getMaxDataRow();
const maxDataColumn = cells2.getMaxDataColumn();

// Loop over all cells
for (let row = 0; row <= maxDataRow; row++) {
for (let col = 0; col <= maxDataColumn; col++) {
// Read the Cell value
const currentCell = cells2.checkCell(row, col);
if (currentCell) {
console.log(currentCell.getStringValue());
}
}
}
```  

Как видите, оба вышеупомянутых подхода используют более или менее похожую логику: цикл по всем ячейкам в коллекции для чтения значений ячеек. Это может вызвать проблемы по ряду причин, о которых рассказано ниже.  

1. API, такие как [**getMaxRow()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxRow--), [**getMaxDataRow()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataRow--), [**getMaxColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxColumn--), [**getMaxDataColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataColumn--) и [**getMaxDisplayRange()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDisplayRange--), требуют дополнительного времени для сбора соответствующей статистики. В случае большой матрицы данных (строки x столбцы) использование этих API может отрицательно сказаться на производительности.  
1. В большинстве случаев не все ячейки в заданном диапазоне созданы. В таких ситуациях проверка каждой ячейки в матрице не так эффективна, как проверка только инициализированных ячеек.  
1. Доступ к ячейке в цикле в виде Cells row, column заставит создавать все объекты ячеек в диапазоне, что в конечном итоге может вызвать исключение OutOfMemoryException.  

## **Заключение**  

Исходя из вышеуказанных фактов, возможны следующие сценарии использования перечислителей.  

1. Требуется только чтение коллекции ячеек, то есть только проверка ячеек.  
1. Необходимо пройти большое количество ячеек.  
1. Требуется пройти только инициализированные ячейки/строки/столбцы.  

{{< app/cells/assistant language="nodejs-cpp" >}}
