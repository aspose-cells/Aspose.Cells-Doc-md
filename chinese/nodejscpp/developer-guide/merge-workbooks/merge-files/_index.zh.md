---
title: 通过 Node.js 以 C++ 合并文件
linktitle: 合并文件
type: docs
weight: 20
url: /zh/nodejs-cpp/merge-files/
---

## **介绍**

Aspose.Cells 提供多种合并文件的方法。对于包含数据、格式和公式的简单文件，可以使用 [**Workbook.combine(Workbook)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#combine-workbook-) 方法合并多个工作簿，使用 [**Worksheet.copy(Worksheet)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#copy-worksheet-) 方法将工作表复制到新工作簿。这些方法使用简单且有效，但如果需要合并大量文件，可能会占用大量系统资源。为了避免此问题，可以使用更高效的 [**CellsHelper.mergeFiles(string[], string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#mergeFiles-stringarray-string-string-) 静态方法来合并多个文件。

## ** 使用 Aspose.Cells for Node.js via C++ 合并文件**

以下示例代码演示如何使用 [**CellsHelper.mergeFiles(string[], string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#mergeFiles-stringarray-string-string-) 方法合并大文件。它处理两个简单但较大的文件 Book1.xls 和 Book2.xls。这些文件仅包含格式化数据和公式。

{{% alert color="primary" %}}

[**CellsHelper.mergeFiles(string[], string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#mergeFiles-stringarray-string-string-)方法仅支持合并数据、样式、格式和公式。使用此方法可能无法合并图表、图片、批注或其他对象。此外，该方法使用一个缓存文件来存储临时数据以进行处理。

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
