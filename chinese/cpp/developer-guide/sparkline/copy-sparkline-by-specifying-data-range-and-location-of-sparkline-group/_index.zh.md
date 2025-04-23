---
title: 通过C++指定数据区域和切片器组位置复制Sparkline
linktitle: 通过指定数据区域和位置复制Sparkline
type: docs
weight: 300
url: /zh/cpp/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
description: 学习如何通过指定数据区域和位置使用Aspose.Cells for C++复制sparkline。
---

{{% alert color="primary" %}}

Microsoft Excel允许您通过指定火花线组的数据范围和位置来复制火花线。Aspose.Cells支持此功能。

{{% /alert %}}

在Microsoft Excel中复制火花线到其他单元格：

1. 选择包含火花线的单元格。
1. 从**设计**选项卡的**火花线**部分选择**编辑数据**。
1. 选择**编辑组位置和数据**。
1. 指定数据范围和位置。
1. 点击**确定**。

Aspose.Cells提供`SparklineCollection.Add(dataRange, row, column)`方法，用于指定sparkline组的数据区域和位置。以下示例加载带有示意图中的源Excel文件，然后访问第一个sparkline组，添加数据区域和位置，最后将修改后的Excel文件写入磁盘，效果如上图所示。

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

    // Create workbook from source Excel file
    Workbook workbook(srcDir + u"source.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first sparkline group
    SparklineGroup group = worksheet.GetSparklineGroups().Get(0);

    // Add Data Ranges and Locations inside this sparkline group
    group.GetSparklines().Add(u"D5:O5", 4, 15);
    group.GetSparklines().Add(u"D6:O6", 5, 15);
    group.GetSparklines().Add(u"D7:O7", 6, 15);
    group.GetSparklines().Add(u"D8:O8", 7, 15);

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Sparklines added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
