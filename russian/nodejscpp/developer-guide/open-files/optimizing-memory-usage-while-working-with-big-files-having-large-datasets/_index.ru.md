---  
title: Оптимизация использования памяти при работе с большими файлами и большими наборами данных с помощью Node.js через C++  
linktitle: Оптимизация использования памяти при работе с большими файлами с большими наборами данных  
type: docs  
weight: 180  
url: /ru/nodejs-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/  
---  

{{% alert color="primary" %}}  

При создании рабочей книги с большими наборами данных или чтении большого файла Microsoft Excel общий расход ОЗУ всегда вызывает обеспокоенность. Были разработаны меры для решения этой задачи. API Aspose.Cells for Node.js via C++ предоставляет релевантные параметры и вызовы API для снижения, уменьшения и оптимизации использования памяти. Также это помогает ускорить работу процесса.  

Используйте опцию [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) для оптимизации использования памяти для данных ячеек и уменьшения общей затраты памяти. При создании большого набора данных для ячеек можно сохранить определенное количество памяти по сравнению с использованием настройки по умолчанию ([**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/)).  

{{% /alert %}}  

## **Оптимизация памяти**  

### **Чтение больших файлов Excel**  

Следующий пример показывает, как считать большой файл Microsoft Excel в оптимизированном режиме.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the LoadOptions
const opt = new AsposeCells.LoadOptions();
// Set the memory preferences
opt.setMemorySetting(AsposeCells.MemorySetting.MemoryPreference);

// Instantiate the Workbook
// Load the Big Excel file having large Data set in it
const wb = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"), opt);
```  

### **Запись больших файлов Excel**  

Следующий пример показывает, как записать большой набор данных на листе в оптимизированном режиме.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook();

// Set the memory preferences
wb.getSettings().setMemorySetting(AsposeCells.MemorySetting.MemoryPreference);

// Note: The memory settings also would not work for the default sheet i.e., "Sheet1" etc. automatically created by the Workbook

// To change the memory setting of existing sheets, please change memory setting for them manually:
let cells = wb.getWorksheets().get(0).getCells();
cells.setMemorySetting(AsposeCells.MemorySetting.MemoryPreference);

// Input large dataset into the cells of the worksheet.
// Your code goes here.
// .........

// Get cells of the newly created Worksheet "Sheet2" whose memory setting is same with the one defined in WorkbookSettings:
cells = wb.getWorksheets().add("Sheet2").getCells();
// .........
// Input large dataset into the cells of the worksheet.
// Your code goes here.
// .........
```  

## **Предостережение**  

Стандартная настройка, [**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/), применяется ко всем версиям. В некоторых случаях при создании рабочей книги с большим набором данных для ячеек опция [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) может оптимизировать использование памяти и снизить расходы на память. Однако в некоторых случаях это может снизить производительность, например, как описано ниже.  

1. **Доступ к ячейкам случайным образом и повторно**: наиболее эффективная последовательность доступа к коллекции ячеек — ячейка за ячейкой по строке, затем строка за строкой. Особенно, если вы получаете доступ к строкам/ячейкам через перечислитель, полученный из [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells), [**RowCollection**](https://reference.aspose.com/cells/nodejs-cpp/rowcollection) и [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row), производительность будет максимально возможной с [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/).  
2. **Вставка и удаление ячеек и строк**: обратите внимание, что при большом количестве операций вставки/удаления для ячеек/строк производительность заметно ухудшается в режиме *MemoryPreference* по сравнению с режимом *Normal*.  
3. **Работа с разными типами ячеек**: если большинство ячеек содержат строковые значения или формулы, затраты памяти будут примерно такими же, как в режиме *Normal*, но если много пустых ячеек или значения ячеек — числовые, логические и т.п., то опция [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) обеспечит лучшую производительность.  

