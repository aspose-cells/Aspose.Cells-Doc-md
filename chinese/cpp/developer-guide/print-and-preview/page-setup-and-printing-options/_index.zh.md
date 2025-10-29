---
title: 页面设置与打印选项（C++）
linktitle: 页面设置和打印选项
type: docs
weight: 60
url: /zh/cpp/page-setup-and-printing-options/
description: 配置页面设置和打印参数以控制打印过程，使用Aspose.Cells与C++。
---

{{% alert color="primary" %}}

有时，开发人员需要配置页面设置和打印设置以控制打印过程。页面设置和打印设置提供各种选项，并且在Aspose.Cells中得到充分支持。

本文展示如何在Visual Studio中创建控制台应用程序，并利用少量代码和Aspose.Cells API对工作表应用页面设置和打印参数。

{{% /alert %}}

## **处理页面和打印设置**

在本示例中，我们在Microsoft Excel中创建了一个工作簿，并使用Aspose.Cells来设置页面设置和打印选项。

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
   1. [下载](https://downloads.aspose.com/cells/cpp) Aspose.Cells for C++。
   1. 在您的开发计算机上安装它。
      所有Aspose组件在安装后都处于评估模式。评估模式没有时间限制，只会在生成的文档中插入水印。
1. 创建一个项目：
   1. 启动Visual Studio。
   1. 创建新的控制台应用程序。
      此示例将演示一个C++控制台应用程序。
1. 添加引用：
   1. 此示例使用 Aspose.Cells，因此请向项目添加对该组件的引用。例如：
      …\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. 编写调用 API 的应用程序：

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"CustomerReport.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"PageSetup_out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Setting the orientation to Portrait
    worksheet.GetPageSetup().SetOrientation(PageOrientationType::Portrait);

    // Setting the number of pages to which the length of the worksheet will be spanned
    worksheet.GetPageSetup().SetFitToPagesTall(1);

    // Setting the number of pages to which the width of the worksheet will be spanned
    worksheet.GetPageSetup().SetFitToPagesWide(1);

    // Setting the paper size to A4
    worksheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA4);

    // Setting the print quality of the worksheet to 1200 dpi
    worksheet.GetPageSetup().SetPrintQuality(1200);

    // Setting the first page number of the worksheet pages
    worksheet.GetPageSetup().SetFirstPageNumber(2);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Page setup applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
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

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"PageSetup.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"PageSetup_Print_out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get PageSetup object
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Specifying the cells range (from A1 cell to E30 cell) of the print area
    pageSetup.SetPrintArea(u"A1:E30");

    // Defining column numbers A & E as title columns
    pageSetup.SetPrintTitleColumns(u"$A:$E");

    // Defining row numbers 1 as title rows
    pageSetup.SetPrintTitleRows(u"$1:$2");

    // Allowing to print gridlines
    pageSetup.SetPrintGridlines(true);

    // Allowing to print row/column headings
    pageSetup.SetPrintHeadings(true);

    // Allowing to print worksheet in black & white mode
    pageSetup.SetBlackAndWhite(true);

    // Allowing to print comments as displayed on worksheet
    pageSetup.SetPrintComments(PrintCommentsType::PrintInPlace);

    // Allowing to print worksheet with draft quality
    pageSetup.SetPrintDraft(true);

    // Allowing to print cell errors as N/A
    pageSetup.SetPrintErrors(PrintErrorsType::PrintErrorsNA);

    // Setting the printing order of the pages to over then down
    pageSetup.SetOrder(PrintOrderType::OverThenDown);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Page setup applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
