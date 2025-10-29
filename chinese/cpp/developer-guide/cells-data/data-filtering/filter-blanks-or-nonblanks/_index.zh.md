---
title: 如何使用C++筛选空白或非空白
linktitle: 如何筛选空白或非空白
type: docs
weight: 85
url: /zh/cpp/how-to-filter-blanks-and-non-blanks/
description: 学习如何使用Aspose.Cells for C++ API筛选空白和非空白。
keywords: 筛选空白，筛选非空白，工作表中筛选空白，工作表中筛选非空白，Excel中筛选空白，Excel中筛选非空白，Excel中筛选空白和非空白
---

## **可能的使用场景**
在 Excel 中对数据进行筛选是一项有价值的工具，通过使用户能够根据其条件专注于特定数据子集, 提升了数据分析、探索和演示功能, 使整体的数据处理和解释过程更加高效和有效。

## **如何在 Excel 中筛选空白或非空白**
在 Excel 中，您可以轻松地使用筛选选项来筛选空白或非空白。以下是操作步骤：

### **如何在 Excel 中筛选空白**
1. 选择范围：点击列标题的字母以选择整个列或选择要筛选空白的范围。
1. 打开筛选菜单：转到功能区中的“数据”选项卡。
<br>
<image src="1.png" width="70%" />
1. 筛选选项：单击“筛选”按钮。这将在所选范围添加筛选箭头。
1. 筛选空白：点击要筛选空白的列中的筛选箭头。取消选择除“空白”之外的所有选项，然后单击“确定”。这将仅显示该列中的空白单元格。
<br>
<image src="2.png" width="70%" />
1. 结果如下：
<br>
<image src="3.png" width="70%" />

### **如何在 Excel 中筛选非空白**
1. 选择范围：单击列标题的字母以选择整个列，或选择要筛选非空的范围。
1. 打开筛选菜单：转到功能区中的“数据”选项卡。
<br>
<image src="1.png" width="70%" />
1. 筛选选项：单击“筛选”按钮。这将在所选范围添加筛选箭头。
1. 筛选非空：单击要筛选非空的列中的筛选箭头。取消选择除“非空”或“自定义”之外的所有选项，并相应设置条件。单击“确定”。这将仅显示该列中非空的单元格。
<br>
<image src="4.png" width="70%" />
1. 结果如下：
<br>
<image src="5.png" width="70%" />

## **如何使用Aspose.Cells进行筛选空白**
如果一列包含文本，且少数单元格为空，需要筛选出仅包含空白单元格的行，可以使用 [AutoFilter.MatchBlanks(int fieldIndex)](https://reference.aspose.com/cells/cpp/aspose.cells/autofilter/matchblanks/) 和 [AutoFilter.AddFilter(int fieldIndex, string criteria)](https://reference.aspose.com/cells/cpp/aspose.cells/autofilter/addfilter/) 函数，如下所示。 

请参阅以下示例代码，该代码加载包含一些虚拟数据的[示例Excel文件](sample.xlsx)。示例代码使用三种方法来筛选空白。然后，将工作簿另存为[输出Excel文件](FilteredBlanks.xlsx)。 

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Open the Excel file
    Workbook workbook(u"sample.xlsx");

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Method 1: Call MatchBlanks function to apply the filter
    // worksheet.GetAutoFilter().MatchBlanks(1);

    // Method 2: Call AddFilter function and set criteria to ""
    // worksheet.GetAutoFilter().AddFilter(1, u"");

    // Method 3: Call AddFilter function and set criteria to nullptr
    worksheet.GetAutoFilter().AddFilter(1, nullptr);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(u"FilteredBlanks.xlsx");

    std::cout << "Excel file modified and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **如何使用Aspose.Cells进行非空白过滤**

请参考以下示例代码，加载包含一些虚拟数据的[示例Excel文件](sample.xlsx)。加载后，调用 [AutoFilter.MatchNonBlanks(int fieldIndex)](https://reference.aspose.com/cells/cpp/aspose.cells/autofilter/matchnonblanks/) 函数筛选非空数据，并最终将工作簿保存为[输出Excel文件](FilteredNonBlanks.xlsx)。 

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook by opening an existing Excel file
    Workbook workbook(u"sample.xlsx");

    // Access the first worksheet in the workbook
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call MatchNonBlanks function to apply the filter on the second column (index 1)
    worksheet.GetAutoFilter().MatchNonBlanks(1);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(u"FilteredNonBlanks.xlsx");

    std::cout << "Filtered non-blanks saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```


{{< app/cells/assistant language="cpp" >}}
