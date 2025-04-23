---  
title: Использование API LightCells с Node.js через C++  
linktitle: Использование API LightCells  
type: docs  
weight: 160  
url: /ru/nodejs-cpp/using-lightcells-api/  
description: Узнайте, как читать и писать большие Excel файлы с помощью API LightCells в Node.js через C++. Повышайте производительность и эффективность с меньшим потреблением памяти.  
---  

{{% alert color="primary" %}}  

Иногда вам необходимо читать и записывать большие файлы Microsoft Excel с огромным списком данных или контента на листе. API LightCells полезен для создания больших электронных таблиц Excel: благодаря этому, требуется меньше памяти, и достигается лучшая производительность и эффективность.  

{{% /alert %}}  
# Архитектура, основанная на событиях  
Aspose.Cells предоставляет API LightCells, преимущественно предназначенный для манипулирования данными ячейки одна за другой без построения полной модели данных (используя коллекцию Cell и т. д.) в памяти. Он работает в режиме событийного управления.  

Для сохранения рабочих книг предоставьте содержание ячейки по ячейке при сохранении, и компонент сохранит его непосредственно в выходной файл.  

При считывании файлов-шаблонов компонент анализирует каждую ячейку и предоставляет их значение по одной.  

В обеих процедурах один объект Cell обрабатывается и затем удаляется; объект Workbook не содержит коллекцию. В этом режиме сохраняется память при импорте и экспорте файлов Microsoft Excel с большим набором данных, которые иначе занимали бы много памяти.  

Несмотря на то, что API LightCells обрабатывает ячейки одинаково для файлов XLSX и XLS (он на самом деле не загружает все ячейки в память, а обрабатывает одну ячейку, а затем удаляет ее), он более эффективно экономит память для файлов XLSX, чем для файлов XLS из-за разных моделей данных и структур двух форматов.  

Однако, **для XLS файлов**, чтобы сэкономить больше памяти, разработчики могут указать временное местоположение для сохранения временных данных, создаваемых в процессе сохранения. Обычно, **использование API LightCells для сохранения XLSX файлов может сэкономить 50% или более памяти**, чем стандартный способ; **сохранение XLS может сэкономить около 20-40% памяти**.  

## Создание большого файла Excel  
Aspose.Cells предоставляет интерфейс `LightCellsDataProvider`, который необходимо реализовать в вашей программе. Этот интерфейс представляет собой поставщика данных для сохранения больших файлов таблиц в легком режиме.  

При сохранении рабочей книги в этом режиме, при сохранении каждого листа проверяется `StartSheet(int)`. Если для листа он возвращает true, то все данные и свойства строк и ячеек этого листа предоставляются этой реализацией. В первую очередь вызывается `NextRow()` для получения следующего индекса строки для сохранения. Если возвращается допустимый индекс строки (индекс строки должен быть в порядке возрастания для сохраняемых строк), то указывается объект Row, представляющий эту строку, для установки его свойств через `StartRow(Row)`.  

Для одной строки сначала проверяется `NextCell()`. Если возвращается допустимый индекс столбца (он должен быть в порядке возрастания для всех ячеек одной строки), то объект Cell, представляющий эту ячейку, передается для установки данных и свойств через `StartCell(Cell)`. После установки данных ячейки, ячейка сохраняется напрямую в сгенерированный файл таблицы, и проверяется и обрабатывается следующая ячейка.  
### Запись большого Excel-файла: пример  
Пожалуйста, ознакомьтесь со следующим образцовым кодом, чтобы увидеть работу API LightCells. Добавьте, удалите или обновите сегменты кода в соответствии с вашими потребностями.  

Программа создает огромный файл с **10 000 (матрица 10000x30) записей** на листе и заполняет их тестовыми данными. Вы можете указать свою матрицу, изменяя переменные `rowsCount` и `colsCount` в методе `Main()`.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

class TestDataProvider {
constructor(workbook, maxRows, maxColumns) {
this._workbook = workbook;
this.maxRows = maxRows;
this.maxColumns = maxColumns;
this._row = -1;
this._column = -1;
}

isGatherString() {
return false;
}

nextCell() {
this._column++;
if (this._column < this.maxColumns) {
return this._column;
} else {
this._column = -1;
return -1;
}
}

nextRow() {
this._row++;
if (this._row < this.maxRows) {
this._column = -1;
return this._row;
} else {
return -1;
}
}

startCell(cell) {
cell.putValue(this._row + this._column);
if (this._row !== 1) {
cell.setFormula("=Rand() + A2");
}
}

startRow(row) {
}

startSheet(sheetIndex) {
return sheetIndex === 0;
}
}

const run = async () => {
const dataDir = path.join(__dirname, "data");

const rowsCount = 10000;
const colsCount = 30;

const workbook = new AsposeCells.Workbook();
const ooxmlSaveOptions = new AsposeCells.OoxmlSaveOptions();

ooxmlSaveOptions.setLightCellsDataProvider(new TestDataProvider(workbook, rowsCount, colsCount));

await workbook.saveAsync(path.join(dataDir, "output.out.xlsx"), ooxmlSaveOptions);
};

run();
```  

## Чтение больших файлов Excel  
Aspose.Cells предоставляет интерфейс `LightCellsDataHandler`, который необходимо реализовать в вашей программе. Этот интерфейс представляет поставщика данных для чтения больших файлов таблиц в легком режиме.  

При чтении рабочей книги в этом режиме, при чтении каждого листа проверяется `StartSheet`. Если он возвращает true, то все данные и свойства ячеек строк и столбцов этого листа проверяются и обрабатываются реализацией этого интерфейса. Для каждой строки вызывается `StartRow`, чтобы определить, нужно ли её обрабатывать. Если строка должна обрабатываться, её свойства считываются сначала, и разработчик может получить доступ к её свойствам через `ProcessRow`. Если ячейки строки также нужно обрабатывать, то `ProcessRow` должен вернуть true, после чего для каждой существующей ячейки строки вызывается `StartCell`, чтобы проверить, нужно ли её обрабатывать. Если ячейка должна обрабатываться, вызывается `ProcessCell` для обработки ячейки этим интерфейсом.  
### Чтение больших Excel-файлов: пример  
Пожалуйста, ознакомьтесь со следующим образцовым кодом, чтобы увидеть работу API LightCells. Добавьте, удалите или обновите сегменты кода в соответствии с вашими потребностями.  

Программа читает огромный файл с миллионами записей в листе. Немного времени занимает чтение каждого листа в рабочей книге. В примере кода файл читается и определяется общее количество ячеек, количество строк и формул в каждом листе.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

class LightCellsDataHandlerVisitCells {
constructor() {
this.cellCount = 0;
this.formulaCount = 0;
this.stringCount = 0;
}

get CellCount() {
return this.cellCount;
}

get FormulaCount() {
return this.formulaCount;
}

get StringCount() {
return this.stringCount;
}

StartSheet(sheet) {
console.log("Processing sheet[" + sheet.getName() + "]");
return true;
}

StartRow(rowIndex) {
return true;
}

ProcessRow(row) {
return true;
}

StartCell(column) {
return true;
}

ProcessCell(cell) {
this.cellCount++;
if (cell.isFormula()) {
this.formulaCount++;
} else if (cell.getType() === AsposeCells.CellValueType.IsString) {
this.stringCount++;
}
return false;
}
}

async function run() {
const dataDir = path.join(__dirname, "data");
const opts = new AsposeCells.LoadOptions();
const v = new LightCellsDataHandlerVisitCells();
opts.setLightCellsDataHandler(v);
const wb = new AsposeCells.Workbook(path.join(dataDir, "LargeBook1.xlsx"), opts);
const sheetCount = wb.getWorksheets().getCount();
console.log("Total sheets: " + sheetCount + ", cells: " + v.CellCount
+ ", strings: " + v.StringCount + ", formulas: " + v.FormulaCount);
}

run();
```  

