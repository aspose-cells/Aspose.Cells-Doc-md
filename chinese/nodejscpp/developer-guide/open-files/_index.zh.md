---
title: 加载和管理Excel、OpenOffice、Json、Csv和Html文件
linktitle: 打开文件
type: docs
weight: 20
url: /zh/nodejs-cpp/loading-saving-and-managing/
description: 使用Aspose.Cells，可以在Node.js via C++中轻松创建、打开和管理Excel、CSV、TSV、ODS、HTML、Numbers、Json、XML、Pdf、Jpg、Tiff、图片、Mht和XPS文件。
---

{{% alert color="primary" %}}

使用Aspose.Cells，可以轻松创建、打开和管理Excel文件，例如检索数据或使用设计模板以加快开发流程。

{{% /alert %}}

## **创建新工作簿**
以下示例从零创建一个新工作簿。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const licensePath = path.join(dataDir, "Aspose.Cells.lic");

try {
// Create a License object
const license = new AsposeCells.License();

// Set the license of Aspose.Cells to avoid the evaluation limitations
license.setLicense(licensePath);
} catch (ex) {
console.log(ex.message);
}

// Instantiate a Workbook object that represents Excel file.
const wb = new AsposeCells.Workbook();

// When you create a new workbook, a default "Sheet1" is added to the workbook.
const sheet = wb.getWorksheets().get(0);

// Access the "A1" cell in the sheet.
const cell = sheet.getCells().get("A1");

// Input the "Hello World!" text into the "A1" cell
cell.putValue("Hello World!");

// Save the Excel file.
wb.save(path.join(dataDir, "MyBook_out.xlsx"));
```

## **打开和保存文件**
使用Aspose.Cells，轻松打开、保存和管理Excel文件。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening through Path
// Creating a Workbook object and opening an Excel file using its file path
const workbook1 = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"));
// Adding new sheet
const sheet = workbook1.getWorksheets().add("MySheet");
// Setting active sheet
workbook1.getWorksheets().setActiveSheetIndex(1);
// Setting values.
const cells = sheet.getCells();
// Setting text
cells.get("A1").putValue("Hello!");
// Setting number
cells.get("A2").putValue(1000);
// Setting Date Time
const cell = cells.get("A3");
cell.putValue(new Date());
const style = cell.getStyle();
style.setNumber(14);
cell.setStyle(style);
// Setting formula
cells.get("A4").setFormula("=SUM(A1:A3)");
// Saving the workbook to disk.
workbook1.save(path.join(dataDir, "dest.xlsx"));
```

## ** 高级主题**
- [打开文件的不同方式](/cells/zh/nodejs-cpp/different-ways-to-open-files/)
- [在加载工作簿时过滤定义名称](/cells/zh/nodejs-cpp/filter-defined-names-while-loading-workbook/)
- [在加载工作簿或工作表时筛选对象](/cells/zh/nodejs-cpp/filter-objects-while-loading-workbook-or-worksheet/)
- [从模板文件加载工作簿时筛选数据类型](/cells/zh/nodejs-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/)
- [加载 Excel 文件时获取警告](/cells/zh/nodejs-cpp/get-warnings-while-loading-excel-file/)
- [在不包含图表的源Excel文件中加载](/cells/zh/nodejs-cpp/load-source-excel-file-without-charts/)
- [加载工作簿中特定的工作表](/cells/zh/nodejs-cpp/load-specific-worksheets-in-a-workbook/)
- [加载带有指定打印纸张大小的工作簿](/cells/zh/nodejs-cpp/load-workbook-with-specified-printer-paper-size/)
- [打开不同版本的Microsoft Excel文件](/cells/zh/nodejs-cpp/opening-different-microsoft-excel-versions-files/)
- [打开具有不同格式的文件](/cells/zh/nodejs-cpp/opening-files-with-different-formats/)
- [在处理具有大数据集的大文件时优化内存使用](/cells/zh/nodejs-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [使用 Aspose.Cells 读取由 Apple Inc. 开发的 Numbers 电子表格](/cells/zh/nodejs-cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [在转换或加载花费太长时间时使用InterruptMonitor停止转换或加载](/cells/zh/nodejs-cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [使用LightCells API](/cells/zh/nodejs-cpp/using-lightcells-api/)
- [将CSV转换为JSON](/cells/zh/nodejs-cpp/convert-csv-to-json/)
- [将Excel转换为JSON](/cells/zh/nodejs-cpp/convert-excel-to-json/)
- [将JSON转换为CSV](/cells/zh/nodejs-cpp/convert-json-to-csv/)
- [将JSON转换为Excel](/cells/zh/nodejs-cpp/convert-json-to-excel/)
- [将Excel转换为Html](/cells/zh/nodejs-cpp/convert-excel-to-html/)
{{< app/cells/assistant language="nodejs-cpp" >}}
