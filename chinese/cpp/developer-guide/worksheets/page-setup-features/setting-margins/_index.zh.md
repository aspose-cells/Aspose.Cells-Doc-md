---
title: 用C++设置边距
linktitle: 设置边距
type: docs
weight: 20
url: /zh/cpp/setting-margins/
description: 学习如何使用C++设置Excel工作表的边距。本指南涵盖了设置页面边距、居中内容以及以编程方式配置页眉和页脚边距的方法，使用Aspose.Cells for C++。
keywords: 使用C++设置Excel工作表边距（居中）、设置页眉页脚边距
---

{{% alert color="primary" %}}

Aspose.Cells 完全支持微软 Excel 的页面设置选项。开发人员可能需要为工作表配置页面设置以控制打印过程。本主题讨论如何使用 Aspose.Cells 配置页面边距。

{{% /alert %}}

## **设置页边距**

Aspose.Cells 提供一个[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类，它代表一个Excel文件。 [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类包含[**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)集合，可以访问Excel文件中的每个工作表。一个工作表由[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类表示。

[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类提供用于设置工作表页面设置选项的[**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/)属性。[**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/)属性是[**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/)类的对象，允许开发者为打印的工作表设置不同的页面布局选项。[**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/)类提供各种属性和方法，用于设置页面布局。

### **页面边距**

使用[**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/)类成员设置页面边距（左、右、上、下）。以下列出一些用于指定页面边距的方法：

- [**GetLeftMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getleftmargin/)
- [**GetRightMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getrightmargin/)
- [**GetTopMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/gettopmargin/)
- [**GetBottomMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getbottommargin/)

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

    // Create a workbook object
    Workbook workbook;

    // Get the worksheets in the workbook
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first (default) worksheet
    Worksheet worksheet = worksheets.Get(0);

    // Get the pagesetup object
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Set bottom, left, right, and top page margins
    pageSetup.SetBottomMargin(2);
    pageSetup.SetLeftMargin(1);
    pageSetup.SetRightMargin(1);
    pageSetup.SetTopMargin(3);

    // Save the Workbook
    workbook.Save(outDir + u"SetMargins_out.xls");

    std::cout << "Margins set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **页面居中**

可以在页面上水平和垂直居中某个内容。为此，有一些有用的 [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) 类成员，如 [**GetCenterHorizontally()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getcenterhorizontally/) 和 [**GetCenterVertically()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getcentervertically/)。

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

    // Create a workbook object
    Workbook workbook;

    // Get the worksheets in the workbook
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first (default) worksheet
    Worksheet worksheet = worksheets.Get(0);

    // Get the pagesetup object
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Specify Center on page Horizontally and Vertically
    pageSetup.SetCenterHorizontally(true);
    pageSetup.SetCenterVertically(true);

    // Save the Workbook
    workbook.Save(outDir + u"CenterOnPage_out.xls");

    std::cout << "Workbook saved successfully with centered page setup!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **页眉和页脚边距**

使用 [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) 类成员（如 [**GetHeaderMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getheadermargin/) 和 [**GetFooterMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getfootermargin/)）设置页眉和页脚边距。

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

    // Create a workbook object
    Workbook workbook;

    // Get the worksheets in the workbook
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first (default) worksheet
    Worksheet worksheet = worksheets.Get(0);

    // Get the pagesetup object
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Specify Header / Footer margins
    pageSetup.SetHeaderMargin(2);
    pageSetup.SetFooterMargin(2);

    // Save the Workbook
    workbook.Save(outDir + u"CenterOnPage_out.xls");

    std::cout << "Workbook saved successfully with centered header and footer margins!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
