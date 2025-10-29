---
title: 通过 Node.js 以 C++ 打开文件的不同方式
linktitle: 打开文件的不同方式
type: docs
weight: 10
url: /zh/nodejs-cpp/different-ways-to-open-files/
description: 本文解释了如何使用 Aspose.Cells for Node.js via C++ API 打开Excel文件。
keywords: 在 Node.js 中打开 Excel 文件而无需 Excel，如何使用 Node.js 打开 Excel 文件。
---

{{% alert color="primary" %}}

 使用 Aspose.Cells，打开文件非常简单，例如，检索数据或使用设计器模板加快开发流程。

{{% /alert %}}

## **如何通过路径打开Excel文件**

 开发者可以通过在 [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) 类构造函数中指定本地计算机上的文件路径，打开 Microsoft Excel 文件。只需将路径作为字符串传入构造函数。Aspose.Cells 会自动识别文件格式类型。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Opening through Path
// Creating a Workbook object and opening an Excel file using its file path
const workbook1 = new AsposeCells.Workbook(filePath);
console.log("Workbook opened using path successfully!");
```

## **如何通过流打开Excel文件**

 也可以简单地通过流的方式打开 Excel 文件。使用接受包含文件的 *Stream* 对象的重载构造函数即可。

```javascript
try {
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book2.xls");
// Opening through Stream
// Create a Stream object
const fstream = fs.createReadStream(filePath);

// Creating a Workbook object, open the file from a Stream object
// That contains the content of file and it should support seeking
const chunks = [];
fstream.on('data', (chunk) => {
chunks.push(chunk);
```

## **如何只打开具有数据的文件**

 若只需要加载含数据的文件，可使用 [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) 和 [**LoadFilter**](https://reference.aspose.com/cells/nodejs-cpp/loadfilter) 类设置相关属性和选项，从而加载模板文件。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load only specific sheets with data and formulas
// Other objects, items etc. would be discarded

// Instantiate LoadOptions specified by the LoadFormat
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);

// Set LoadFilter property to load only data & cell formatting
loadOptions.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.CellData));

// Create a Workbook object and opening the file from its path
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"), loadOptions);
console.log("File data imported successfully!");
```

## **如何仅加载可见工作表**

 在加载 [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) 时，有时只需工作簿中可见工作表中的数据。Aspose.Cells 允许在加载工作簿时跳过不可见工作表中的数据。为此，可以创建继承自 [**LoadFilter**](https://reference.aspose.com/cells/nodejs-cpp/loadfilter) 类的自定义函数，并将其实例传递给 [**LoadOptions.getLoadFilter()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--) 属性。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sampleFile = "output.xlsx";
const samplePath = path.join(dataDir, sampleFile);

// Create a sample workbook
// and put some data in first cell of all 3 sheets
const createWorkbook = new AsposeCells.Workbook();
createWorkbook.getWorksheets().get("Sheet1").getCells().get("A1").putValue("Aspose");
createWorkbook.getWorksheets().add("Sheet2").getCells().get("A1").putValue("Aspose");
createWorkbook.getWorksheets().add("Sheet3").getCells().get("A1").putValue("Aspose");
createWorkbook.getWorksheets().get("Sheet3").setIsVisible(false);
createWorkbook.save(samplePath);

// Load the sample workbook
const loadOptions = new AsposeCells.LoadOptions();
loadOptions.setLoadFilter(new AsposeCells.LoadFilter()); // Corrected line by defining LoadFilter properly

const loadWorkbook = new AsposeCells.Workbook(samplePath, loadOptions);
console.log(`Sheet1: A1: ${loadWorkbook.getWorksheets().get("Sheet1").getCells().get("A1").getValue()}`);
console.log(`Sheet1: A2: ${loadWorkbook.getWorksheets().get("Sheet2").getCells().get("A1").getValue()}`);
console.log(`Sheet1: A3: ${loadWorkbook.getWorksheets().get("Sheet3").getCells().get("A1").getValue()}`);
```

 这是上述代码中引用的 *CustomLoad* 类的实现。

```javascript
const { Workbook, LoadDataFilterOptions } = require("aspose.cells.node");

class CustomLoad {
startSheet(sheet) {
if (sheet.isVisible()) {
// Load everything from visible worksheet
this.loadDataFilterOptions = LoadDataFilterOptions.All;
} else {
// Load nothing
this.loadDataFilterOptions = LoadDataFilterOptions.Structure;
}
}
}
```

{{% alert color="primary" %}}

 如果使用 Aspose.Cells 打开非本地 Excel 文件或其他文件格式（例如 PPT/PPTX，DOC/DOCX 等），会抛出异常。

{{% /alert %}} 

{{% alert color="primary" %}}

 在加载大型电子表格时，[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) 构造函数可能会抛出 *OutOfMemoryError*。此异常提示可用内存不足以完全加载电子表格，因此必须启用内存偏好设置来加载文件。

{{% /alert %}}

{{< app/cells/assistant language="nodejs-cpp" >}}
