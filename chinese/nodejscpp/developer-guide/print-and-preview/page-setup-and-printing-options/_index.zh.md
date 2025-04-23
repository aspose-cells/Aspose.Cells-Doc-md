---  
title: 使用 C++ 在 Node.js 中设置页面布局和打印选项  
linktitle: 页面设置和打印选项  
type: docs  
weight: 60  
url: /zh/nodejs-cpp/page-setup-and-printing-options/  
---  

{{% alert color="primary" %}}  
有时，开发人员需要配置页面设置和打印设置以控制打印过程。页面设置和打印设置提供各种选项，并且在Aspose.Cells中得到充分支持。  

本文展示了如何在 Node.js 中使用 C++ 创建控制台应用程序，并通过少量代码使用 Aspose.Cells API 设置页面布局和打印选项。  
{{% /alert %}}  

## **处理页面和打印设置**  

在此示例中，我们在 Microsoft Excel 中创建了一个工作簿，并使用 Aspose.Cells 设置了页面布局和打印选项。  

### **使用 Aspose.Cells 设置页面设置选项**  

首先在Microsoft Excel中创建一个简单的工作表。然后将页面设置选项应用于它。执行代码将更改页面设置选项，如下面的屏幕截图所示。  

|**输出文件。**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_1.png)|  

1. 在Microsoft Excel中创建一个带有一些数据的工作表：  
   1. 在Microsoft Excel中打开一个新的工作簿。  
   1. 添加一些数据。  
1. 设置页面设置选项：  
   将页面设置选项应用于文件。以下是应用新选项之前的默认选项的屏幕截图。  

|**默认页面设置选项。**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_2.png)|  

1. 下载并安装 Aspose.Cells：  
   1. [下载](https://downloads.aspose.com/cells/nodejs-cpp) Aspose.Cells for Node.js via C++。  
   1. 在您的开发计算机上安装它。  
      所有Aspose组件在安装后都处于评估模式。评估模式没有时间限制，只会在生成的文档中插入水印。  
1. 创建一个项目：  
   1. 启动您的 Node.js 环境。  
   1. 创建新的控制台应用程序。  
      本示例展示了一个 Node.js 控制台应用程序，但您也可以使用 C++ 绑定。  
1. 添加引用：  
   1. 此示例使用 Aspose.Cells，因此请向项目添加对该组件的引用。例如：  
      …\Program Files\Aspose\Aspose.Cells\Bin\Node.js-Cpp\Aspose.Cells.node  
1. 编写调用 API 的应用程序：  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "CustomerReport.xlsx");

// Open the template workbook
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the orientation to Portrait
worksheet.getPageSetup().setOrientation(AsposeCells.PageOrientationType.Portrait);

// Setting the number of pages to which the length of the worksheet will be spanned
worksheet.getPageSetup().setFitToPagesTall(1);

// Setting the number of pages to which the width of the worksheet will be spanned
worksheet.getPageSetup().setFitToPagesWide(1);

// Setting the paper size to A4
worksheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA4);

// Setting the print quality of the worksheet to 1200 dpi
worksheet.getPageSetup().setPrintQuality(1200);

// Setting the first page number of the worksheet pages
worksheet.getPageSetup().setFirstPageNumber(2);

// Save the workbook
workbook.save(path.join(dataDir, "PageSetup_out.xlsx"));
```  

### **设置打印选项**  

页面设置还提供了几个打印选项(也称为工作表选项)，允许用户控制工作表页面的打印方式。它们允许用户:  

- 选择工作表的特定打印区域。
- 打印标题。
- 打印网格线。
- 打印行/列标题。
- 获得草稿质量。
- 打印注释。
- 打印单元格错误。
- 定义页面排序。  

下面的示例将打印选项应用于上面示例中创建的文件(PageSetup.xls)。下面的屏幕截图显示了应用新选项之前的默认打印选项。  

|**输入文档**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_3.png)|  
执行代码会更改打印选项。  

|**输出文件**|  
| :- |  
|![todo:image_alt_text](page-setup-and-printing-options_4.png)|  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "PageSetup.xlsx");

// Open the template workbook
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

const pageSetup = worksheet.getPageSetup();

// Specifying the cells range (from A1 cell to E30 cell) of the print area
pageSetup.setPrintArea("A1:E30");

// Defining column numbers A & E as title columns
pageSetup.setPrintTitleColumns("$A:$E");

// Defining row numbers 1 as title rows
pageSetup.setPrintTitleRows("$1:$2");

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

// Setting the printing order of the pages to over then down
pageSetup.setOrder(AsposeCells.PrintOrderType.OverThenDown);

// Save the workbook
workbook.save(path.join(dataDir, "PageSetup_Print_out.xlsx"));
```  

