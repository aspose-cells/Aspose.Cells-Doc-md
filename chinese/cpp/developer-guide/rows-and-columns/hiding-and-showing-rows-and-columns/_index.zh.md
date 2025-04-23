---
title: 用C++隐藏和显示行列
linktitle: 隐藏和显示行和列
type: docs
weight: 60
url: /zh/cpp/hiding-and-showing-rows-and-columns/
description: 学习如何使用Aspose.Cells和C++以编程方式隐藏和显示Excel文件中的行和列。
---

{{% alert color="primary" %}}

有时候，将某些行或列隐藏在工作表中，稍后再显示是有意义的。微软Excel提供了此功能，Aspose.Cells也支持。

{{% /alert %}}

## **控制行和列的可见性**

Aspose.Cells提供了一个代表Microsoft Excel文件的类[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)。[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类包含了一个[**WorksheetCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)，允许开发人员访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类表示。[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类提供了一个[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)集合，表示工作表中的所有单元格。[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)集合提供了几种管理工作表中的行或列的方法。以下介绍了其中的一些。

### **隐藏行和列**

开发人员可以通过调用[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)集合的[**HideRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hiderow/)和[**HideColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hidecolumn/)方法，分别隐藏行或列。两种方法都以行索引或列索引作为参数，以隐藏特定的行或列。

```c++
#include <iostream>
#include <memory>
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

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the 3rd row of the worksheet
    worksheet.GetCells().HideRow(2);

    // Hide the 2nd column of the worksheet
    worksheet.GetCells().HideColumn(1);

    // Save the modified Excel file
    U16String outputFilePath = outDir + u"output.out.xls";
    workbook.Save(outputFilePath);

    std::cout << "Rows and columns hidden successfully. File saved to: " << outputFilePath.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

还可以通过将行高或列宽设置为0来隐藏行或列。

{{% /alert %}}

### **显示行和列**

开发人员可以通过调用[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)集合的[**UnhideRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhiderow/)和[**UnhideColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhidecolumn/)方法，分别显示任何隐藏的行或列。两种方法都需要两个参数：

- 行或列索引 - 用于显示特定行或列的索引。
- 行高或列宽 - 在取消隐藏后分配给行或列的行高或列宽。

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

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Unhide the 3rd row and set its height to 13.5
    worksheet.GetCells().UnhideRow(2, 13.5);

    // Unhide the 2nd column and set its width to 8.5
    worksheet.GetCells().UnhideColumn(1, 8.5);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    workbook.Save(outputFilePath);

    Aspose::Cells::Cleanup();

    std::cout << "File modified and saved successfully!" << std::endl;

    return 0;
}
```

{{% alert color="primary" %}}

在将隐藏列显示出来时，如果你需要恢复到之前的宽度或原始宽度，请用负宽度取消隐藏列。例如：`worksheet.Cells.UnhideColumn(5, -1)`

{{% /alert %}}

### **隐藏多行和列**

开发人员可以通过调用[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)集合的[**HideRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hiderows/)和[**HideColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hidecolumns/)方法，分别一次隐藏多行或列。两种方法都需要起始行或列索引和应该隐藏的行数或列数作为参数。

```cpp
#include <iostream>
#include <memory>
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

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide 3, 4, and 5 rows in the worksheet (zero-based index)
    worksheet.GetCells().HideRows(2, 3);

    // Hide 2 and 3 columns in the worksheet (zero-based index)
    worksheet.GetCells().HideColumns(1, 2);

    // Save the modified Excel file
    workbook.Save(outDir + u"outputxls");

    std::cout << "Rows and columns hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

还可以使用[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)类的[**UnhideRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhiderows/)和[**UnhideColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhidecolumns/)方法来显示多行和列。

{{% /alert %}}
