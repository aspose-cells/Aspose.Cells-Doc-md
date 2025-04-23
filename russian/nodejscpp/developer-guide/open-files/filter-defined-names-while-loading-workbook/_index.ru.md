---
title: Фильтрация Имени при загрузке Рабочей книги с помощью Node.js через C++
linktitle: Фильтрация заданных имен при загрузке рабочей книги
type: docs
weight: 50
url: /ru/nodejs-cpp/filter-defined-names-while-loading-workbook/
---

## **Возможные сценарии использования**

Aspose.Cells позволяет фильтровать или удалять определенные имена внутри рабочей книги. Пожалуйста, используйте [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions/) для загрузки определенных имен и [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions/) для их удаления при загрузке книги. Обратите внимание, что при удалении определенных имен формулы внутри книги могут перестать работать.

## **Фильтрация заданных имен при загрузке рабочей книги**

Следующий пример кода загружает [пример файла Excel](61767860.xlsx), в ячейке **C1** содержится формула с определенными именами, т.е. *=SUM(MyName1, MyName2)*. Поскольку мы используем [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions/) для удаления определенных имен при загрузке, формула в ячейке C1 в [выходной Excel-файл](61767861.xlsx) ломается, и вместо этого отображается *#NAME?*. Посмотрите следующий скриншот, который демонстрирует эффект кода на пример файла Excel.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Образец кода**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleFilterDefinedNamesWhileLoadingWorkbook.xlsx");
// Specify the load options
let opts = new AsposeCells.LoadOptions();
// We do not want to load defined names
opts.setLoadFilter(new AsposeCells.LoadFilter(~AsposeCells.LoadDataFilterOptions.DefinedNames));

// Load the workbook
const workbook = new AsposeCells.Workbook(filePath, opts);

// Save the output Excel file, it will break the formula in C1
workbook.save(path.join(dataDir, "outputFilterDefinedNamesWhileLoadingWorkbook.xlsx"));

console.log("FilterDefinedNamesWhileLoadingWorkbook executed successfully.");
```
