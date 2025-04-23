---
title: 创建、访问和复制命名范围（C++）
linktitle: 创建、访问和复制命名范围
type: docs
weight: 200
url: /zh/cpp/create-access-and-copy-named-ranges/
description: 学习如何使用 Aspose.Cells 在 Excel 文件中创建、访问和复制命名范围（C++）。
---

## **介绍**

通常，列和行标签用于引用单元格。也可以创建描述性名称来代表单元格、单元格范围、公式或常量值。**名称**一词指的是代表某个单元格、范围、公式或常量的字符串。为范围赋予名称意味着可以通过该名称引用该范围。建议使用易懂的名字，如用 Products 代替难以理解的范围，例如 Sales!C20:C30。标签可以在引用相同工作表数据的公式中使用；如果要表示另一个工作表上的范围，可以使用名称。*命名范围是 Microsoft Excel 最强大的功能之一，特别是用作列表控件、数据透视表、图表等的源范围时。

## **使用Microsoft Excel处理已命名区域**

### **创建已命名范围**

以下步骤描述了如何使用 **MS Excel** 命名单元格或范围。这种方法适用于 **Microsoft Office Excel 2003**、**Excel 97**、**2000** 和 **2002**。

1. 选择你想命名的单元格或单元格范围。
1. 单击公式栏左端的**名称框**。
1. 输入单元格的名称。
1. 按ENTER。

{{% alert color="primary" %}}

在更改单元格内容时，不能为单元格命名。

{{% /alert %}}

## **使用Aspose.Cells处理命名范围**

在这里，我们使用Aspose.Cells API来完成任务。
Aspose.Cells 提供了表示 Microsoft Excel 文件的 [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) 类。[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) 类包含一个 [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) 集合，可访问 Excel 文件中的每个工作表。一个工作表由 [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) 类表示。[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) 类提供一个 [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) 集合。

### **创建已命名范围**

可以通过调用 [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) 集合的重载方法 [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) 来创建命名范围。[**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) 方法的典型参数如下：

- 左上角单元格的名称，范围中左上角单元格的名称。
- 右下角单元格的名称，范围中右下角单元格的名称。

调用 [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) 方法时，它将返回新创建的范围，作为 [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) 类的实例。使用此 [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) 对象来配置命名范围。例如，使用 [**GetName()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/getname/) 属性设置范围的名称。以下示例展示了如何创建跨越 B4:G14 的单元格命名范围。

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating a named range
    Range range = worksheet.GetCells().CreateRange(u"B4", u"G14");

    // Setting the name of the named range
    range.SetName(u"TestRange");

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Named range created and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **将数据输入到命名范围内的单元格**

您可以按照以下模式向范围内的单个单元格插入数据：

- **C++**: 范围(行, 列)

假设你有一个跨越 A1:C4 的命名范围。这个矩阵有 4 * 3=12 个单元格。单个范围的单元格按顺序排列：Range(0, 0)、Range(0, 1)、Range(0, 2)、Range(1, 0)、Range(1, 1)、Range(1, 2)、Range(2, 0)、Range(2, 1)、Range(2, 2)、Range(3, 0)、Range(3, 1)、Range(3, 2)。

使用以下属性来识别范围中的单元格:

- FirstRow 返回命名范围中第一行的索引。
- FirstColumn 返回命名范围中第一列的索引。
- RowCount 返回命名范围中的总行数。
- ColumnCount 返回命名范围中的总列数。

以下示例显示如何向指定范围的单元格输入一些值。

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

    // Instantiate a new Workbook
    Workbook workbook;

    // Get the first worksheet in the workbook
    Worksheet worksheet1 = workbook.GetWorksheets().Get(0);

    // Create a range of cells based on H1:J4
    Range range = worksheet1.GetCells().CreateRange(u"H1", u"J4");

    // Name the range
    range.SetName(u"MyRange");

    // Input some data into cells in the range
    range.Get(0, 0).PutValue(u"USA");
    range.Get(0, 1).PutValue(u"SA");
    range.Get(0, 2).PutValue(u"Israel");
    range.Get(1, 0).PutValue(u"UK");
    range.Get(1, 1).PutValue(u"AUS");
    range.Get(1, 2).PutValue(u"Canada");
    range.Get(2, 0).PutValue(u"France");
    range.Get(2, 1).PutValue(u"India");
    range.Get(2, 2).PutValue(u"Egypt");
    range.Get(3, 0).PutValue(u"China");
    range.Get(3, 1).PutValue(u"Philipine");
    range.Get(3, 2).PutValue(u"Brazil");

    // Save the excel file
    workbook.Save(outDir + u"rangecells.out.xls");

    std::cout << "Range cells created and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **标识命名范围中的单元格**

您可以按照以下模式向范围内的单个单元格插入数据：

- **C++**: 范围(行, 列)

如果你有一个命名范围，覆盖 A1:C4。矩阵由 4 * 3 = 12 个单元格组成。单个范围的单元格按照顺序排列：Range(0, 0), Range(0, 1), Range(0, 2), Range(1, 0), Range(1, 1), Range(1, 2), Range(2, 0), Range(2, 1), Range(2, 2), Range(3, 0), Range(3, 1), Range(3, 2)。

使用以下属性来识别范围中的单元格:

- FirstRow 返回命名范围中第一行的索引。
- FirstColumn 返回命名范围中第一列的索引。
- RowCount 返回命名范围中的总行数。
- ColumnCount 返回命名范围中的总列数。

以下示例显示如何向指定范围的单元格输入一些值。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the specified named range
    Range range = workbook.GetWorksheets().GetRangeByName(u"TestRange");

    // Identify range cells
    std::cout << "First Row : " << range.GetFirstRow() << std::endl;
    std::cout << "First Column : " << range.GetFirstColumn() << std::endl;
    std::cout << "Row Count : " << range.GetRowCount() << std::endl;
    std::cout << "Column Count : " << range.GetColumnCount() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **访问命名范围**

#### **访问特定的命名范围**

调用 [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) 集合的 [**GetRangeByName**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getrangebyname/) 方法，以按指定名称获取范围。典型的 [**GetRangeByName**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getrangebyname/) 方法接受命名范围的名称，并将所指定的命名范围作为 [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) 类的实例返回。以下示例显示如何通过名称访问指定的范围。

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Getting the specified named range
    Range range = workbook.GetWorksheets().GetRangeByName(u"TestRange");

    if (range)
    {
        std::cout << "Named Range : " << range.GetRefersTo().ToUtf8() << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

#### **访问电子表格中的所有命名范围**

调用 [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) 集合的 [**GetNamedRanges**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnamedranges/) 方法以获取电子表格中的所有命名范围。[**GetNamedRanges**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnamedranges/) 方法返回所有命名范围的数组，属于[**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)集合。

以下示例显示如何访问工作簿中的所有命名范围。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = srcDir + u"book1.xls";

    Workbook workbook(inputFilePath);
    WorksheetCollection sheets = workbook.GetWorksheets();
    Vector<Range> ranges = sheets.GetNamedRanges();

    std::cout << "Total Number of Named Ranges: " << ranges.GetLength() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **复制命名范围**

Aspose.Cells 提供 [**Range.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/copy/) 方法，将带格式的单元格范围复制到另一个范围内。

以下示例显示如何将源单元格范围复制到另一个命名范围。

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    Range range1 = worksheet.GetCells().CreateRange(u"E12", u"I12");
    range1.SetName(u"MyRange");

	Color borderColor = Color{ 0,0, 0, 128 };
    range1.SetOutlineBorder(BorderType::TopBorder, CellBorderType::Medium, borderColor);
    range1.SetOutlineBorder(BorderType::BottomBorder, CellBorderType::Medium, borderColor);
    range1.SetOutlineBorder(BorderType::LeftBorder, CellBorderType::Medium, borderColor);
    range1.SetOutlineBorder(BorderType::RightBorder, CellBorderType::Medium, borderColor);

    range1.Get(0, 0).PutValue(u"Test");
    range1.Get(0, 4).PutValue(u"123");

    Range range2 = worksheet.GetCells().CreateRange(u"B3", u"F3");
    range2.SetName(u"testrange");
    range2.Copy(range1);

    workbook.Save(outDir + u"copyranges.out.xls");

    std::cout << "Ranges copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
