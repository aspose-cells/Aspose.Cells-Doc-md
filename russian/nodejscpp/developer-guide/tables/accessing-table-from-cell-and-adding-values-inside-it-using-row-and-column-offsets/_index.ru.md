---  
title: Доступ к таблице из ячейки и добавление значений внутри неё с помощью смещения по строкам и столбцам с помощью Node.js и C++  
linktitle: Доступ к таблице из ячейки и добавление значений в нее с использованием смещений строк и столбцов  
type: docs  
weight: 230  
url: /ru/nodejs-cpp/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/  
---  

{{% alert color="primary" %}}  

Обычно вы добавляете значения внутри объекта Table или List, используя метод [**Cell.putValue(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-). Но иногда вам может потребоваться добавлять значения внутри объекта Table или List, используя смещения строки и столбца.  

Чтобы получить доступ к таблице или списковому объекту из ячейки, используйте метод [**Cell.getTable()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getTable--). Чтобы добавить значения внутри с помощью смещений строки и столбца, используйте метод [**ListObject.putCellValue(number, number, object)**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#putCellValue-number-number-object-).  

{{% /alert %}}  

Следующий скриншот показывает исходный файл Excel, используемый в коде. Он содержит пустую таблицу и выделяет ячейку D5 внутри таблицы. Мы получим доступ к этой таблице из ячейки D5 с помощью метода [**Cell.getTable()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getTable--), а затем добавим значения внутри с использованием методов [**Cell.putValue(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) и [**ListObject.putCellValue(number, number, object)**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#putCellValue-number-number-object-).  

## Пример  

### Снимки экрана сравнивают исходные и выходные файлы  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|  
| :- |  

На следующем снимке экрана показан созданный код. Как видно, ячейка D5 имеет значение, и ячейка F6, которая находится в смещении 2,2 от таблицы, имеет значение.  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|  
| :- |  

### Код Node.js для доступа к таблице из ячейки и добавления значений внутри с помощью смещения по строкам и столбцам  

Следующий примерный код загружает исходный файл Excel, как показано на снимке экрана выше, добавляет значения в таблицу и создает выходной файл Excel, как показано выше.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Accessing_Table.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access cell D5 which lies inside the table
const cell = worksheet.getCells().get("D5");

// Put value inside the cell D5
cell.putValue("D5 Data");

// Access the Table from this cell
const table = cell.getTable();

// Add some value using Row and Column Offset
table.putCellValue(2, 2, "Offset [2,2]");

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

