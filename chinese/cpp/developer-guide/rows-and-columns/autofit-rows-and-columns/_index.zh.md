---
title: 用C++自动调整行列宽
linktitle: 自动调整行和列
type: docs
weight: 20
url: /zh/cpp/autofit-rows-and-columns/
description: 本文展示如何使用Aspose.Cells for C++ API自动调整行、列、合并单元格的行，以及范围内的行。
keywords: 自动调整行，自动调整列，自动调整单元格范围中的行，自动调整合并单元格中的行
---

{{% alert color="primary" %}}

Microsoft Excel允许根据内容自动调整单元格的宽度和高度。此功能也通过Aspose.Cells实现，开发者可以在运行时自动调整单元格的尺寸。

{{% /alert %}}

## **自动调整**

Aspose.Cells提供了表示Microsoft Excel文件的[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类。[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类包含一个[**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)集合，可以访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类表示。[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类提供了管理工作表的多种方法。本文介绍了使用[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类自动调整行或列的方法。

### **自动调整行 - 简单**

最简单的自动调整行宽和列高的方法是调用[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类的[**AutoFitRow**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrow/)方法。[**AutoFitRow**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrow/)方法以行索引作为参数，调整特定行。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Auto-fit the 2nd row (index 1) of the worksheet
    worksheet.AutoFitRow(1);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Row auto-fitted and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **如何在单元格范围内自动调整行**

一行由多个列组成。Aspose.Cells允许开发者通过调用[**AutoFitRow**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrow/)方法的重载版本，根据该行中某个范围的单元格内容自动调整行高。参数如下：

- **行索引**，即要自动调整的行的索引。
- **第一个列索引**，即行的第一个列的索引。
- **最后列索引**，指行的最后一列的索引。

[**AutoFitRow**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrow/)方法会检查该行所有列的内容，然后自动调整行高。

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
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xlsx";

    // Open the Excel file
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Auto-fitting the 3rd row of the worksheet
    worksheet.AutoFitRow(1, 0, 5);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Row auto-fitted and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **如何在一系列单元格中自动调整列**

一列由多个行组成。可以通过调用[**AutoFitColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitcolumn/)方法的重载版本，根据列中某个范围的单元格内容自动调整列宽。参数如下：

- **列索引**，要自动调整的列的索引。
- **第一行索引**，列的第一行的索引。
- **最后行索引**，列的最后一行的索引。

[**AutoFitColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitcolumn/)方法会检查该列所有行的内容，然后自动调整列宽。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Auto-fit the 5th column (index 4) from row 4 to 6
    worksheet.AutoFitColumn(4, 4, 6);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Column auto-fitted and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **如何为合并单元格自动调整行高**

使用Aspose.Cells，即使对合并的单元格，也可以自动调整行高。[**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/)类提供了[**GetAutoFitMergedCellsType()**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getautofitmergedcellstype/)属性，可用于自动调整合并单元格的行高。[**GetAutoFitMergedCellsType()**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getautofitmergedcellstype/)接受包含以下成员的[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitmergedcellstype/)枚举：

- None：忽略合并的单元格。
- FirstLine：只扩展第一行的高度。
- 最后一行：只扩展最后一行的高度。
- 每行：只扩展每一行的高度。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook wb;

    // Get the first (default) worksheet
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // Create a range A1:B1
    Range range = worksheet.GetCells().CreateRange(0, 0, 1, 2);

    // Merge the cells
    range.Merge();

    // Insert value to the merged cell A1
    worksheet.GetCells().Get(0, 0).SetValue(u"A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end");

    // Create a style object
    Style style = worksheet.GetCells().Get(0, 0).GetStyle();

    // Set wrapping text on
    style.SetIsTextWrapped(true);

    // Apply the style to the cell
    worksheet.GetCells().Get(0, 0).SetStyle(style);

    // Create an object for AutoFitterOptions
    AutoFitterOptions options;

    // Set auto-fit for merged cells
    options.SetAutoFitMergedCellsType(AutoFitMergedCellsType::EachLine);

    // Autofit rows in the sheet (including the merged cells)
    worksheet.AutoFitRows(options);

    // Save the Excel file
    wb.Save(outDir + u"AutofitRowsforMergedCells.xlsx");

    std::cout << "Autofit rows for merged cells completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

你也可以尝试使用重载的 [**AutoFitRows**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitrows/) 和 [**AutoFitColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitcolumns/) 方法，接受行/列范围和 [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) 实例，以根据你的需要自动适应所选的行/列的 [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) 。

上述方法的签名如下：

1. AutoFitRows(int startRow, int endRow, [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) 选项)
1. AutoFitColumns(int firstColumn, int lastColumn, [**AutoFitterOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/) 选项)

{{% /alert %}}

## **重要知识**

{{% alert color="primary" %}}

如果单元格已合并，则不会应用自动适应方法，这与微软Excel中的行为相同。你可以使用自动筛选API解决此问题。此外，如果单元格的文本被换行，则 [**AutoFitColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/autofitcolumn/) 方法也不会被应用。另一个需要知道的事情是，*AutoFit* 方法耗时较长。因此，为了确保应用程序的效率，你应尽可能少调用这些方法。

{{% /alert %}}

## **高级主题**
- [为合并单元格自动调整行高](/cells/zh/cpp/autofit-rows-for-merged-cells/)
