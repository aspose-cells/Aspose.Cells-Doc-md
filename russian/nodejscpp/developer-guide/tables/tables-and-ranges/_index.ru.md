---  
title: Таблицы и диапазоны с помощью Node.js и C++  
linktitle: Таблицы и диапазоны  
type: docs  
weight: 50  
url: /ru/nodejs-cpp/tables-and-ranges/  
---  

## **Введение**  

Иногда вы создаете таблицу в Microsoft Excel и не хотите продолжать работу с функциональностью таблицы, которая в ней есть. Вместо этого вы хотите что-то, что похоже на таблицу. Чтобы сохранить данные в таблице без потери форматирования, преобразуйте таблицу в обычный диапазон данных.  
Aspose.Cells действительно поддерживает эту функцию Microsoft Excel для таблиц и объектов списка.  

## **Использование Microsoft Excel**  

Используйте функцию **Преобразовать в диапазон** , чтобы быстро преобразовать таблицу в диапазон без потери форматирования. В Microsoft Excel 2007/2010:  

1. Щелкните в любом месте таблицы, чтобы активная ячейка находилась в столбце таблицы.  
1. На вкладке **Разрботка** , в группе **Инструменты** , щелкните **Преобразовать в диапазон** .  

## **Использование Aspose.Cells**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "table_ranges.xlsx");

// Open an existing file that contains a table/list object in it
const wb = new AsposeCells.Workbook(filePath);

// Convert the first table/list object (from the first worksheet) to normal range
wb.getWorksheets().get(0).getListObjects().get(0).convertToRange();

// Save the file
wb.save(path.join(dataDir, "output.xlsx"));
```  

{{% alert color="primary" %}}  

После преобразования таблицы в диапазон функции таблицы больше не доступны. Например, заголовки строк больше не включают стрелки сортировки и фильтра, и структурированные ссылки (ссылки, использующие имена таблиц) , используемые в формулах, превращаются в обычные ссылки на ячейки.  

{{% /alert %}}  

## **Преобразовать таблицу в диапазон с параметрами**  

Aspose.Cells предоставляет дополнительные опции при преобразовании таблицы в диапазон с помощью класса [**TableToRangeOptions**](https://reference.aspose.com/cells/nodejs-cpp/tabletorangeoptions/).  Класс [**TableToRangeOptions**](https://reference.aspose.com/cells/nodejs-cpp/tabletorangeoptions/) предоставляет свойство [**getLastRow()**](https://reference.aspose.com/cells/nodejs-cpp/tabletorangeoptions/#getLastRow--), которое позволяет установить последний индекс строки таблицы. Форматирование таблицы будет сохранено до указанного индекса строки, а остальное форматирование будет удалено.  

Приведенный ниже примерный код демонстрирует использование класса [**TableToRangeOptions**](https://reference.aspose.com/cells/nodejs-cpp/tabletorangeoptions/).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "table_ranges.xlsx");
// Open an existing file that contains a table/list object in it
const workbook = new AsposeCells.Workbook(filePath);

const options = new AsposeCells.TableToRangeOptions();
options.setLastRow(5);

// Convert the first table/list object (from the first worksheet) to normal range
workbook.getWorksheets().get(0).getListObjects().get(0).convertToRange(options);

// Save the file
workbook.save(path.join(dataDir, "output.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
