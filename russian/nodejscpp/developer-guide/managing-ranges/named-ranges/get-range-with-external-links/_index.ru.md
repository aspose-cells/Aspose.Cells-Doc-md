---
title: Получить диапазон с внешними ссылками с помощью Node.js через C++
linktitle: Получить диапазон с внешними ссылками
type: docs
weight: 120
url: /ru/nodejs-cpp/get-range-with-external-links/
description: Узнайте, как получить диапазоны с внешними ссылками, используя Aspose.Cells for Node.js via C++. Эффективно извлекайте данные из разных файлов Excel.
---

## **Получить диапазон с внешними ссылками**

Много раз файлы Excel используют внешние ссылки для доступа к данным из других файлов Excel. Aspose.Cells for Node.js via C++ предоставляет возможность получать такие внешние ссылки через метод [**Name.getReferredAreas(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/name/#getReferredAreas-boolean-). Метод [**Name.getReferredAreas(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/name/#getReferredAreas-boolean-) возвращает массив типа [**ReferredArea**](https://reference.aspose.com/cells/nodejs-cpp/referredarea). Класс [**ReferredArea**](https://reference.aspose.com/cells/nodejs-cpp/referredarea) имеет свойство [**ReferredArea.getExternalFileName()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getExternalFileName--), которое возвращает имя внешнего файла. Класс [**ReferredArea**](https://reference.aspose.com/cells/nodejs-cpp/referredarea) предоставляет следующие члены.

- [**ReferredArea.getEndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getEndColumn--): Конечный столб области
- [**ReferredArea.getEndRow()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getEndRow--): Конечная строка области
- [**ReferredArea.getExternalFileName()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getExternalFileName--): Получить имя внешнего файла, если это внешний ссылка
- [**ReferredArea.isArea()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#isArea--): Указывает, является ли это областью
- [**ReferredArea.isExternalLink()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#isExternalLink--): Указывает, является ли это внешней ссылкой
- [**ReferredArea.getSheetName()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getSheetName--): Указывает, в каком листе находится эта ссылка
- [**ReferredArea.getStartColumn()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getStartColumn--): Начальный столб области
- [**ReferredArea.getStartRow()**](https://reference.aspose.com/cells/nodejs-cpp/referredarea/#getStartRow--): Начальная строка области

Пример кода, приведенный ниже, демонстрирует использование метода [**Name.getReferredAreas(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/name/#getReferredAreas-boolean-) для получения диапазонов с внешними ссылками.

## **Образец кода**

```javascript
try 
{
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Load source Excel file
const filePath = path.join(sourceDir, "SampleExternalReferences.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
console.log(filePath);
const names = workbook.getWorksheets().getNames();
const namesCount = names.getCount();
for (let i = 0; i < namesCount; i++) 
{
const namedRange = names.get(i);
const referredAreas = namedRange.getReferredAreas(true);
if (referredAreas) 
{
referredAreas.forEach(referredArea => {
// Print the data in Referred Area
console.log("IsExternalLink: " + referredArea.isExternalLink());
console.log("IsArea: " + referredArea.isArea());
console.log("SheetName: " + referredArea.getSheetName());
console.log("ExternalFileName: " + referredArea.getExternalFileName());
console.log("StartColumn: " + referredArea.getStartColumn());
console.log("StartRow: " + referredArea.getStartRow());
console.log("EndColumn: " + referredArea.getEndColumn());
console.log("EndRow: " + referredArea.getEndRow());
```
