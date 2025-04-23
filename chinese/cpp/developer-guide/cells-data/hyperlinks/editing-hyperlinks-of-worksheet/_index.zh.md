---
title: 使用C++编辑工作表的超链接
linktitle: 编辑工作表的超链接
type: docs
weight: 330
url: /zh/cpp/editing-hyperlinks-of-worksheet/
description: 通过Aspose.Cells for C++ API学习如何编辑工作表的超链接。
keywords: 编辑超链接，编辑工作表的超链接，编辑单元格的超链接，访问工作表的所有超链接
---

{{% alert color="primary" %}}

Aspose.Cells允许您访问工作表的所有超链接，使用[**GetHyperlinks()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gethyperlinks/)集合。您可以逐个访问此集合中的每个超链接并编辑其属性。

{{% /alert %}}

 以下示例代码访问工作表的所有超链接，并将其[**GetAddress()**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/getaddress/)属性更改为Aspose网站。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook from input file
    Workbook workbook(srcDir + u"Sample.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Iterate through all hyperlinks in the worksheet
    for (int32_t i = 0; i < worksheet.GetHyperlinks().GetCount(); i++)
    {
        Hyperlink hl = worksheet.GetHyperlinks().Get(i);
        hl.SetAddress(u"http://www.aspose.com");
    }

    // Save the modified workbook to the output file
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Hyperlinks updated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
