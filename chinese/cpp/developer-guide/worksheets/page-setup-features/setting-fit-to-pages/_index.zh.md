---
title: 如何用C++将Excel打印为宽度和高度适应的页面
linktitle: 如何将Excel打印为宽度和高度适应的页面
type: docs
weight: 200
url: /zh/cpp/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: 本文提供代码，说明如何使用Aspose.Cells库用C++设置FitToPagesWide和F intoToPagesTall。
keywords: 用C++设置FitToPagesWide和F itToPagesTall，添加到C++中的FitToPagesWide和FitToPagesTall，设置Excel中的FitToPagesWide和FitToPagesTall，清除Excel中的FitToPagesWide和FitToPagesTall，将Excel打印为宽度和高度适应的页面，将工作表打印为一页，将所有列打印在一页。
---

## **介绍**

FitToPagesWide和FitToPagesTall设置用于电子表格应用（如Microsoft Excel），用于控制打印时电子表格的缩放方式。这些设置确保你的打印输出在水平和垂直方向上都在指定的页数内。以下是每个设置的详细说明：

1. FitToPagesWide：此设置指定打印输出应适合的页宽。例如，将FitToPagesWide设置为1，表示内容缩放至适合一页宽，无论电子表格有多宽。
1. 适合页面高度：该设置指定打印输出应适应的页面总数。例如，将适合页面高度设置为1意味着内容将缩放以适应单个页面高度，无论行数多少。

## **为什么使用适合页面宽度和高度**
以下是设置适合页面宽度和高度的一些原因：
1. 控制打印布局：通过指定页面宽度和高度的页数，可以确保打印的文档易于阅读且布局合理，没有列或行被尴尬地拆分到不同的页面上。
1. 一致性：如果你需要打印多个工作表或报告，使用这些设置可以帮助保持格式一致，使打印的文档更易于比较和分析。
1. 专业呈现：正确缩放和适应内容到指定页面数可以使你的数据呈现更专业、更精致。

## **如何在Excel中将文件打印为宽度和高度都适合的页面**

要在Microsoft Excel中设置适合页面宽度和高度的设置，请按照以下步骤操作：

1. 打开你的Excel工作簿，转到你想打印的工作表。
1. 转到功能区上的页面布局标签。
1. 在页面设置组中，点击右下角的小箭头以打开页面设置对话框。
1. 在页面设置对话框中，转到页面标签。
1. 在缩放部分，选择“适合”选项，然后指定你想要的宽度和高度的页面数：在第一个框中输入你想要的宽度页面数（适合x页宽），在第二个框中输入你想要的高度页面数（适合y页高）。
<br>
<img src="2.png" width=60% />

1. 点击确定以应用设置。

## **如何使用Aspose.Cells将Excel的宽度和高度适合页面打印**

若要在指定工作表中设置适合页面宽度和高度：首先，加载[示例文件](input.xlsx)，然后需要修改目标工作表的[**Worksheet.GetFitToPagesTall()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getfittopagestall/)和[**Worksheet.GetFitToPagesWide()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getfittopageswide/)属性中的[**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/)对象。以下是C++示例：

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a Workbook object
    Workbook workbook(U16String(u"input.xlsx"));

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the number of pages to which the length of the worksheet will be spanned
    worksheet.GetPageSetup().SetFitToPagesTall(1);

    // Set the number of pages to which the width of the worksheet will be spanned
    worksheet.GetPageSetup().SetFitToPagesWide(1);

    // Save the workbook
    workbook.Save(U16String(u"out_net.pdf"));

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

输出结果：
<br>
<img src="1.png" width=60% />

## **如何使用Aspose.Cells将工作表打印为一页**

若要将工作表打印为一页：首先，加载[示例文件](sample.xlsx)，然后需要设置[**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)对象的[**PdfSaveOptions.GetOnePagePerSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getonepagepersheet/)属性。以下是C++示例：

```cpp
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/PdfSaveOptions.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiating a Workbook object
    Workbook workbook(u"sample.xlsx");

    // Create PdfSaveOptions object
    PdfSaveOptions options;

    // Set options for exporting PDF
    options.SetOnePagePerSheet(true);

    // Save the workbook to a PDF file
    workbook.Save(u"OnePagePerSheet.pdf", options);

    std::cout << "Workbook saved as OnePagePerSheet.pdf!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

输出结果：
<br>
<img src="3.png" width=60% />

## **如何使用Aspose.Cells将工作表的所有列打印在一页中**

若要将工作表的所有列打印在一页中：首先，加载[示例文件](sample.xlsx)，然后需要设置[**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)对象的[**PdfSaveOptions.GetAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getallcolumnsinonepagepersheet/)属性。以下是C++示例：

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/PdfSaveOptions.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a Workbook object with the specified file.
    Workbook workbook(u"sample.xlsx");

    // Create PdfSaveOptions instance.
    PdfSaveOptions options;

    // Set options for saving the workbook as a PDF.
    options.SetAllColumnsInOnePagePerSheet(true);

    // Save the workbook as a PDF file with the specified options.
    workbook.Save(u"AllColumnsInOnePagePerSheet.pdf", options);

    std::cout << "Workbook saved successfully as PDF!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

输出结果：
<br>
<img src="4.png" width=60% />
{{< app/cells/assistant language="cpp" >}}
