---
title: 使用C++显示报告筛选页选项
linktitle: 显示报告筛选页选项
type: docs
weight: 110
url: /zh/cpp/show-report-filter-pages-option/
description: 学习如何使用Aspose.Cells for C++在数据透视表中启用“显示报告筛选页”选项。
---

## **显示报告筛选页选项**
Excel支持创建数据透视表、添加报告筛选器，以及启用“显示报告筛选页”选项。Aspose.Cells也支持此功能，在创建的数据透视表上启用“显示报告筛选页”选项。以下是Excel中“显示报告筛选页”选项的截图。

![todo:image_alt_text](show-report-filter-pages-option_1.png)

可从此处下载示例源文件和输出文件以测试示例代码：

` ` [源Excel文件](81920786.xlsx) 

[输出Excel文件](81920787.xlsx)

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

    // Load template file
    Workbook wb(srcDir + u"samplePivotTable.xlsx");

    // Get first pivot table in the worksheet
    PivotTable pt = wb.GetWorksheets().Get(1).GetPivotTables().Get(0);

    // Set pivot field
    pt.ShowReportFilterPage(pt.GetPageFields().Get(0));

    // Set position index for showing report filter pages
    pt.ShowReportFilterPageByIndex(pt.GetPageFields().Get(0).GetPosition());

    // Set the page field name
    pt.ShowReportFilterPageByName(pt.GetPageFields().Get(0).GetName());

    // Save the output file
    wb.Save(outDir + u"outputSamplePivotTable.xlsx");

    std::cout << "Pivot table report filter pages set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
