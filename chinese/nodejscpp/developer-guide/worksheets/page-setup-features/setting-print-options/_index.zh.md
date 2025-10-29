---
title: 使用Node.js通过C++设置打印选项
linktitle: 设置打印选项
type: docs
weight: 40
url: /zh/nodejs-cpp/setting-print-options/
description: 本文演示了如何使用Node.js API和C++库以编程方式设置Excel工作表页面设置的打印选项。可以设置打印区域、打印标题和页面顺序。
keywords: 使用Node.js通过C++设置Excel打印区域、设置打印标题、设置页面顺序
---

{{% alert color="primary" %}}

Microsoft Excel的页面设置提供了几个打印选项（也称为工作表选项），允许用户控制工作表页面的打印方式。

{{% /alert %}}

## **设置打印选项**

这些打印选项允许用户：

- 选择工作表上的特定打印区域。
- 打印标题。
- 打印网格线。
- 打印行/列标题。
- 获得草稿质量。
- 打印注释。
- 打印单元格错误。
- 定义页面排序。

 Aspose.Cells for Node.js via C++支持Microsoft Excel所有的打印选项，开发者可以轻松使用[**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup)类提供的属性为工作表配置这些选项。以下更详细讨论这些属性的使用方法。

### **设置打印区域**

默认情况下，打印区域包括包含数据的工作表的所有区域。开发人员可以为工作表确定特定的打印区域。

要选择特定的打印区域，请使用 [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) 类的 [**PageSetup.getPrintArea()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintArea--) 属性。将定义打印区域的单元范围分配给此属性。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Specifying the cells range (from A1 cell to T35 cell) of the print area
pageSetup.setPrintArea("A1:T35");

// Save the workbook.
workbook.save(path.join(dataDir, "SetPrintArea_out.xls"));
```

### **设置打印标题**

Aspose.Cells 允许您指定行列标题在打印工作表的所有页面上重复显示。要这样做，请使用 [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) 类的 [**PageSetup.getPrintTitleColumns()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintTitleColumns--) 和 [**PageSetup.getPrintTitleRows()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintTitleRows--) 属性。

要重复显示的行或列是通过传递它们的行号或列号来定义的。例如，行被定义为 $1:$2，列被定义为 $A:$B。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Defining column numbers A & B as title columns
pageSetup.setPrintTitleColumns("$A:$B");

// Defining row numbers 1 & 2 as title rows
pageSetup.setPrintTitleRows("$1:$2");

// Save the workbook.
workbook.save(path.join(dataDir, "SetPrintTitle_out.xls"));
```

### **设置其他打印选项**

[**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) 类还提供了几个其他属性来设置常规打印选项如下：

 - [**PageSetup.getPrintGridlines()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintGridlines--)：一个布尔属性，定义是否打印网格线。
 - [**PageSetup.getPrintHeadings()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintHeadings--)：一个布尔属性，定义是否打印行和列标题。
 - [**PageSetup.getBlackAndWhite()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getBlackAndWhite--)：一个布尔属性，定义是否以黑白模式打印工作表。
 - [**PageSetup.getPrintComments()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintComments--)：定义是否在工作表上或在工作表末尾显示打印注释。
 - [**PageSetup.getPrintDraft()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintDraft--)：一个布尔属性，定义是否无图形打印工作表。
- [**PageSetup.getPrintErrors()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintErrors--)：定义是否按显示的方式、空白、短横线或N/A打印单元格错误。

 要设置[**PageSetup.getPrintComments()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintComments--)和[**PageSetup.getPrintErrors()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintErrors--)属性，Aspose.Cells for Node.js via C++还提供了两个枚举类型[**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype)和[**PrintErrorsType**](https://reference.aspose.com/cells/nodejs-cpp/printerrorstype)，其中包含预定义值，可分别赋值给[**PageSetup.getPrintComments()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintComments--)和[**PageSetup.getPrintErrors()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintErrors--)属性。

 [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype)枚举中的预定义值及其描述如下。

|**打印备注类型**|**描述**|
| :- | :- |
|PrintInPlace|指定将批注打印为显示在工作表上的形式。
|PrintNoComments|指定不打印批注。
|PrintSheetEnd|指定将批注打印在工作表末尾。

 [**PrintErrorsType**](https://reference.aspose.com/cells/nodejs-cpp/printerrorstype)枚举的预定义值及其描述如下。

|**打印错误类型**|**描述**|
| :- | :- |
|PrintErrorsBlank|指定不打印错误。|
|PrintErrorsDash|指定打印错误为"--"。|
|PrintErrorsDisplayed|指定打印错误为显示的形式。|
|PrintErrorsNA|指定打印错误为"#N/A"。|

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Allowing to print gridlines
pageSetup.setPrintGridlines(true);

// Allowing to print row/column headings
pageSetup.setPrintHeadings(true);

// Allowing to print worksheet in black & white mode
pageSetup.setBlackAndWhite(true);

// Allowing to print comments as displayed on worksheet
pageSetup.setPrintComments(AsposeCells.PrintCommentsType.PrintInPlace);

// Allowing to print worksheet with draft quality
pageSetup.setPrintDraft(true);

// Allowing to print cell errors as N/A
pageSetup.setPrintErrors(AsposeCells.PrintErrorsType.PrintErrorsNA);

// Save the workbook.
workbook.save(path.join(dataDir, "OtherPrintOptions_out.xls"));
```

### **设置页面顺序**

 [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup)类提供了[**PageSetup.getOrder()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getOrder--)属性，用于排序工作表的多个页面以进行打印。主要有两种页面排序方式。

- **先向下再向右：** 在打印右侧页面之前，将所有页面向下打印。
- **先向右再向下：** 在打印下方页面之前，从左到右打印页面。

 Aspose.Cells 提供了包含所有预定义排序类型的枚举[**PrintOrderType**](https://reference.aspose.com/cells/nodejs-cpp/printordertype)。

 [**PrintOrderType**](https://reference.aspose.com/cells/nodejs-cpp/printordertype)枚举的预定义值及其描述如下。

|**打印顺序类型**|**描述**|
| :- | :- |
|DownThenOver|表示打印顺序为先向下再向右。|
|OverThenDown|表示打印顺序为先向右再向下。|

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Setting the printing order of the pages to over then down
pageSetup.setOrder(AsposeCells.PrintOrderType.OverThenDown);

// Save the workbook.
workbook.save(path.join(dataDir, "SetPageOrder_out.xls"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
