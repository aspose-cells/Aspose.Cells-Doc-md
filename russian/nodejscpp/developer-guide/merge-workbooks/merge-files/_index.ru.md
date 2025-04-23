---
title: Объединение файлов с помощью Node.js через C++
linktitle: Объединить файлы
type: docs
weight: 20
url: /ru/nodejs-cpp/merge-files/
---

## **Введение**

Aspose.Cells предоставляет различные способы объединения файлов. Для простых файлов с данными, форматированием и формулами можно использовать метод [**Workbook.combine(Workbook)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#combine-workbook-) для объединения нескольких книг, а метод [**Worksheet.copy(Worksheet)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#copy-worksheet-) — для копирования листов в новую книгу. Эти методы просты в использовании и эффективны, но при большом количестве файлов их использование может потреблять много ресурсов системы. Чтобы этого избежать, используйте статический метод [**CellsHelper.mergeFiles(string[], string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#mergeFiles-stringarray-string-string-), более эффективный способ объединения нескольких файлов.

## **Объединение файлов с помощью Aspose.Cells for Node.js via C++**

Следующий пример показывает, как объединять большие файлы, используя метод [**CellsHelper.mergeFiles(string[], string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#mergeFiles-stringarray-string-string-). Он берет два простых, но больших файла, Book1.xls и Book2.xls. Эти файлы содержат отформатированные данные и формулы.

{{% alert color="primary" %}}

Метод [**CellsHelper.mergeFiles(string[], string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#mergeFiles-stringarray-string-string-) поддерживает только объединение данных, стилей, форматирования и формул. Объекты, такие как диаграммы, картинки, комментарии или другие объекты, возможно, не будут объединены с использованием этого метода. Кроме того, для процесса используется кэшированный файл, в котором хранятся временные данные.

{{% /alert %}}

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create an Array (length=2)
const files = new Array(2);
// Specify files with their paths to be merged
files[0] = path.join(dataDir, "book1.xls");
files[1] = path.join(dataDir, "Book2.xlsx");

// Create a cachedFile for the process
const cacheFile = path.join(dataDir, "test.txt");

// Output File to be created
const dest = path.join(dataDir, "output.xlsx");

// Merge the files in the output file. Supports only .xls files
AsposeCells.CellsHelper.mergeFiles(files, cacheFile, dest);
console.log(cacheFile);
// Now if you need to rename your sheets, you may load the output file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "output.xlsx"));

let i = 1;

// Browse all the sheets to rename them accordingly
const worksheets = workbook.getWorksheets();
for (let j = 0; j < worksheets.getCount(); j++) {
worksheets.get(j).setName(`Sheet1${i}`);
i++;
}

// Re-save the file
workbook.save(path.join(dataDir, "output.xlsx"));
```
