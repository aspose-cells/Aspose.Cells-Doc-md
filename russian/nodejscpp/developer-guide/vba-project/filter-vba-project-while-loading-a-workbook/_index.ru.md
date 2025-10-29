---
title: Фильтровать проект VBA при загрузке книги с помощью Node.js через C++
linktitle: Фильтрация проекта VBA при загрузке книги
type: docs
weight: 140
url: /ru/nodejs-cpp/filter-vba-project-while-loading-a-workbook/
description: Узнайте, как фильтровать проекты VBA при загрузке книг Excel с помощью Aspose.Cells for Node.js via C++.
---

## **Фильтровать проект VBA при загрузке книги Excel в Node.js через C++**

Некоторые файлы .xlsm/.xslb содержат очень большое количество макросов или очень длинные макросы. Aspose.Cells for Node.js via C++ будет безусловно загружать эти метаданные при открытии таких книг. Возможно, вам потребуется контролировать это [**LoadDataFilterOptions**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions), когда вам нужно только извлечь имена листов для большого количества книг, пропуская ненужный контент. Этот фильтр предоставляется с помощью новой опции, [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions).

## **Образец кода**

Приведенный ниже образец кода загружает книгу так, чтобы было выполнено только фильтрование VBA. Образец файла для тестирования этой функции можно загрузить по следующей ссылке:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Set the load options, we do not want to load VBA
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Auto);
const loadFilter = new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.VBA);
loadOptions.setLoadFilter(loadFilter);

// Create workbook object from sample excel file using load options
const book = new AsposeCells.Workbook(path.join(sourceDir, "sampleMacroEnabledWorkbook.xlsm"), loadOptions);

// Save the output in pdf format
book.save(outputDir + "OutputSampleMacroEnabledWorkbook.xlsm", AsposeCells.SaveFormat.Xlsm);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
