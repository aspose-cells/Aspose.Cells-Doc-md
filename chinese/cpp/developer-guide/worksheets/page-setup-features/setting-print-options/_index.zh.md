---
title: 使用C++设置打印选项
linktitle: 设置打印选项
type: docs
weight: 40
url: /zh/cpp/setting-print-options/
description: 本文演示了如何通过C++ API和库以编程方式设置Excel工作表的“页面设置”中的打印选项。你可以设置打印区域、打印标题和页面顺序。
keywords: 设置Excel打印区域C++，设置Excel打印标题C++，设置Excel页面顺序C++
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

Aspose.Cells支持Microsoft Excel提供的所有打印选项，开发者可以使用[**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/)类提供的属性轻松配置这些参数。以下将详细介绍这些属性的使用方式。

### **设置打印区域**

默认情况下，打印区域包括包含数据的工作表的所有区域。开发人员可以为工作表确定特定的打印区域。

要选择特定的打印区域，请使用[**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/)类的[**GetPrintArea()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintarea/)属性。将定义打印区域的单元格范围分配给此属性。

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

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the PageSetup object of the worksheet
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Set the print area to the range A1:T35
    pageSetup.SetPrintArea(u"A1:T35");

    // Save the workbook
    workbook.Save(outDir + u"SetPrintArea_out.xls");

    std::cout << "Print area set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **设置打印标题**

Aspose.Cells允许您指定要在打印的工作表的所有页面上重复显示的行和列标题。为此，请使用[**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/)类的[**GetPrintTitleColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinttitlecolumns/)和[**GetPrintTitleRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinttitlerows/)属性。

要重复显示的行或列是通过传递它们的行号或列号来定义的。例如，行被定义为 $1:$2，列被定义为 $A:$B。

```c++
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

    // Path of output excel file
    U16String outputFilePath = outDir + u"SetPrintTitle_out.xls";

    // Create a new workbook
    Workbook workbook;

    // Obtain the reference of the PageSetup of the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Define column numbers A & B as title columns
    pageSetup.SetPrintTitleColumns(u"$A:$B");

    // Define row numbers 1 & 2 as title rows
    pageSetup.SetPrintTitleRows(u"$1:$2");

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Print titles set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **设置其他打印选项**

[**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/)类还提供了几个其他属性，以设置一般的打印选项，如下：

- [**GetPrintGridlines()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintgridlines/)：布尔属性，定义是否打印网格线。
- [**GetPrintHeadings()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintheadings/)：一个布尔属性，定义是否打印行和列标题或不打印。
- [**GetBlackAndWhite()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getblackandwhite/)：一个布尔属性，定义是否以黑白模式打印工作表或不打印。
- [**GetPrintComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintcomments/)：定义是否在工作表上显示打印批注还是在工作表末尾显示。
- [**GetPrintDraft()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintdraft/)：布尔属性，定义是否无图形打印工作表。
- [**GetPrintErrors()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinterrors/)：定义是否将单元格错误按显示、空白、破折号或N/A打印。

为设置[**GetPrintComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintcomments/)和[**GetPrintErrors()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinterrors/)属性，Aspose.Cells还提供了两个枚举类型，[**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/)和[**PrintErrorsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printerrorstype/)，它们包含预定义的值，可分别赋给[**GetPrintComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintcomments/)和[**GetPrintErrors()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinterrors/)属性。

[**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/)枚举中的预定义值如下所示。

|**打印备注类型**|**描述**|
| :- | :- |
|PrintInPlace|指定将批注打印为显示在工作表上的形式。
|PrintNoComments|指定不打印批注。
|PrintSheetEnd|指定将批注打印在工作表末尾。

[**PrintErrorsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printerrorstype/) 枚举的预定义值如下所示，并附有其描述。

|**打印错误类型**|**描述**|
| :- | :- |
|PrintErrorsBlank|指定不打印错误。|
|PrintErrorsDash|指定打印错误为"--"。|
|PrintErrorsDisplayed|指定打印错误为显示的形式。|
|PrintErrorsNA|指定打印错误为"#N/A"。|

```c++
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

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the PageSetup object of the worksheet
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Set print options
    pageSetup.SetPrintGridlines(true);  // Allow printing gridlines
    pageSetup.SetPrintHeadings(true);   // Allow printing row/column headings
    pageSetup.SetBlackAndWhite(true);   // Allow printing in black & white mode
    pageSetup.SetPrintComments(PrintCommentsType::PrintInPlace);  // Print comments as displayed
    pageSetup.SetPrintDraft(true);      // Print with draft quality
    pageSetup.SetPrintErrors(PrintErrorsType::PrintErrorsNA);  // Print cell errors as N/A

    // Save the workbook
    U16String outputPath = outDir + u"OtherPrintOptions_out.xls";
    workbook.Save(outputPath);

    std::cout << "Workbook saved with print options successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **设置页面顺序**

[**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) 类提供了[**GetOrder()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getorder/) 属性，用于对工作表的多个页面进行打印排序。有两种排序页面的可能性如下。

- **先向下再向右：** 在打印右侧页面之前，将所有页面向下打印。
- **先向右再向下：** 在打印下方页面之前，从左到右打印页面。

Aspose.Cells提供一个枚举[**PrintOrderType**](https://reference.aspose.com/cells/cpp/aspose.cells/printordertype/)，其中包含所有预定义的排序类型。

[**PrintOrderType**](https://reference.aspose.com/cells/cpp/aspose.cells/printordertype/) 枚举的预定义值如下所示。

|**打印顺序类型**|**描述**|
| :- | :- |
|DownThenOver|表示打印顺序为先向下再向右。|
|OverThenDown|表示打印顺序为先向右再向下。|

```c++
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

    // Create a new workbook
    Workbook workbook;

    // Obtain the reference of the PageSetup of the first worksheet
    PageSetup pageSetup = workbook.GetWorksheets().Get(0).GetPageSetup();

    // Set the printing order of the pages to over then down
    pageSetup.SetOrder(PrintOrderType::OverThenDown);

    // Save the workbook
    workbook.Save(outDir + u"SetPageOrder_out.xls");

    std::cout << "Page order set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
