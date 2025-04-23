---
title: 通过 Node.js 和 C++ 设置页眉和页脚
linktitle: 设置页眉和页脚
type: docs
weight: 30
url: /zh/nodejs-cpp/setting-headers-and-footers/
description: 本文介绍了如何通过 Aspose.Cells for Node.js via C++ 编程方式在 Excel 工作表的页眉和页脚中插入图片。 
keywords: 在 Excel 页眉页脚中插入图片，使用 C++ 和 Node.js 设置 Excel 页眉页脚脚本命令
---

{{% alert color="primary" %}}

页眉和页脚是显示在顶部边距下方或底部边距上方的文本行。还可以将页眉和页脚添加到工作表中。页眉和页脚可用于显示有用的信息，如页码、作者姓名、主题名称或日期和时间。通过页面设置设置页眉和页脚。

{{% /alert %}}

## **设置页眉和页脚**

Aspose.Cells for Node.js via C++ 允许你在运行时为工作表添加页眉和页脚，但我们建议在预先设计的文件中手动设置页眉和页脚以便打印。你可以使用 Microsoft Excel 作为 GUI 工具设置页眉和页脚，以节省时间和开发成本。Aspose.Cells 可以导入文件并保存设置。

要在运行时添加页眉和页脚，Aspose.Cells提供了特殊的API调用和脚本命令来格式化页眉和页脚。

### **脚本命令**

脚本命令是特殊命令，允许您设置页眉和页脚的格式。

|**脚本命令**|**描述**|
| :- | :- |
当前页号||&P|
图片||&G|
总页数||&N|
|&D|当前日期|
|&T|当前时间|
|&A|工作表名称|
|&F|文件名（不含路径）|
|&&文本|显示 &文本。例如：&&WO 将显示为 &WO|
|&"\<FontName>"|表示字体名称。例如：&"Arial"|
|&"\<FontName>, \<FontStyle>"|表示带有样式的字体名称。例如：&"Arial,Bold"|
|&\<FontSize>|代表字体大小。例如：“&14abc”。但如果此命令后跟一个要在页眉中打印的普通数字，则应与字体大小用空格分隔。例如：“&14 123”。

### **设置页眉和页脚**

[**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) 类提供两个方法，[**setHeader(number, string)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#setHeader-number-string-) 和 [**setFooter(number, string)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#setFooter-number-string-)，用于向工作表添加页眉和页脚。这些方法只接受两个参数：

- **Section** – 应放置页眉或页脚的部分。有三个部分：左、中、右，分别由0、1和2表示。
- **Script** – 用于页眉或页脚的脚本。此脚本包含对页眉或页脚进行格式化的脚本命令。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const excel = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = excel.getWorksheets().get(0).getPageSetup();

// Setting worksheet name at the left section of the header
pageSetup.setHeader(0, "&A");

// Setting current date and current time at the central section of the header
// and changing the font of the header
pageSetup.setHeader(1, "&\"Times New Roman,Bold\"&D-&T");

// Setting current file name at the right section of the header and changing the
// font of the header
pageSetup.setHeader(2, "&\"Times New Roman,Bold\"&12&F");

// Setting a string at the left section of the footer and changing the font
// of a part of this string ("123")
pageSetup.setFooter(0, "Hello World! &\"Courier New\"&14 123");

// Setting the current page number at the central section of the footer
pageSetup.setFooter(1, "&P");

// Setting page count at the right section of footer
pageSetup.setFooter(2, "&N");

// Save the Workbook.
excel.save("SetHeadersAndFooters_out.xls");
```

### **将图像插入页眉或页脚**

[**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) 类还有两个额外的方法，[**setHeaderPicture(number, number[])**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#setHeaderPicture-number-numberarray-) 和 [**setFooterPicture(number, number[])**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#setFooterPicture-number-numberarray-)，用于在页眉和页脚中添加图片。这些方法接受的参数为：

- **Section** – 图片将放置的页眉或页脚部分。有三个部分：左、中、右，分别由值0、1和2表示。
- **字节数组** – 图形数据（二进制数据应写入字节数组的缓冲区）。

执行以下代码并打开文件后，请通过以下方式检查工作表的页眉：

1. 在 **文件** 菜单上，选择 **页面设置**。将显示一个对话框。
1. 选择 **页眉/页脚** 选项卡。

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Creating a Workbook object
const workbook = new AsposeCells.Workbook();

// Creating a string variable to store the url of the logo/picture
const logoUrl = path.join(dataDir, "aspose-logo.jpg");

// Declaring a byte array
const binaryData = fs.readFileSync(logoUrl);

// Creating a PageSetup object to get the page settings of the first worksheet of the workbook
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Setting the logo/picture in the central section of the page header
pageSetup.setHeaderPicture(1, binaryData);

// Setting the script for the logo/picture
pageSetup.setHeader(1, "&G");

// Setting the Sheet's name in the right section of the page header with the script
pageSetup.setHeader(2, "&A");

// Saving the workbook
workbook.save(path.join(dataDir, "InsertImageInHeaderFooter_out.xls"));
```
