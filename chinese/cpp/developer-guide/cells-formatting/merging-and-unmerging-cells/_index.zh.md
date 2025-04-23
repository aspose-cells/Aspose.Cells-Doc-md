---
title: 使用 C++ 合并与取消合并单元格
linktitle: 合并和分割单元格
description: Aspose.Cells 是一个处理电子表格文件的 C++ 库，支持合并和取消合并单元格。本文将介绍如何使用Aspose.Cells库进行单元格的合并与取消合并，以及如何自定义合并单元格的样式。
keywords: Aspose.Cells、C++库、电子表格、合并单元格、取消合并、样式设置、自定义样式
type: docs
weight: 190
url: /zh/cpp/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells支持此功能，还可以在工作表中合并单元格。您还可以取消合并或拆分合并的单元格。合并单元格的单元格引用是原始选择范围中左上角单元格的引用。

{{% /alert %}} 

## **介绍**
并非总是希望每行或每列中都有相同数量的单元格。例如，您可能希望在一个跨越多个列的单元格中放置标题。或者，如果创建发票，则可能希望总计列中的列数较少。将两个或多个单元格合并成一个单元格，以实现此目的。Microsoft Excel允许用户选择文件并将其合并以按照自己的方式构造电子表格。

{{% alert color="primary" %}} 

请注意，当单元格合并时，只有范围中左上角单元格中的数据被保留。如果范围中的其他单元格中有数据，则此数据将被删除。
同样，格式基于参考单元格，因此当合并单元格时，范围中左上角单元格的格式设置将应用于合并单元格。当单元格拆分时，新单元格将保留其原始格式设置。

{{% /alert %}} 

## **在工作表中合并单元格**
### **在Microsoft Excel中合并单元格**
以下步骤描述如何在MS Excel中合并工作表中的单元格。

1. 将要复制的数据复制到范围内左上角的单元格中。
1. 选择要合并的单元格。
1. 要合并行或列中的单元格并将单元格内容居中，点击**合并和居中**图标上的**格式**工具栏。

### **使用Aspose.Cells合并单元格**
 `Aspose::Cells::Cells` 类提供了一些有用的方法。例如，`Merge()` 方法可以将指定范围内的单元格合并成一个单元格。

以下示例显示了如何在工作表中合并单元格（C6:E7）。

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

    // Create a Workbook
    Workbook wbk;

    // Create a Worksheet and get the first sheet
    Worksheet worksheet = wbk.GetWorksheets().Get(0);

    // Create a Cells object to fetch all the cells
    Cells cells = worksheet.GetCells();

    // Merge some Cells (C6:E7) into a single C6 Cell
    cells.Merge(5, 2, 2, 3);

    // Input data into C6 Cell
    worksheet.GetCells().Get(5, 2).PutValue(u"This is my value");

    // Create a Style object to fetch the Style of C6 Cell
    Style style = worksheet.GetCells().Get(5, 2).GetStyle();

    // Create a Font object
    Font font = style.GetFont();

    // Set the name
    font.SetName(u"Times New Roman");

    // Set the font size
    font.SetSize(18);

    // Set the font color
    font.SetColor(Color::Blue());

    // Bold the text
    font.SetIsBold(true);

    // Make it italic
    font.SetIsItalic(true);

    // Set the background color of C6 Cell to Red
    style.SetForegroundColor(Color::Red());
    style.SetPattern(BackgroundType::Solid);

    // Apply the Style to C6 Cell
    worksheet.GetCells().Get(5, 2).SetStyle(style);

    // Save the Workbook
    wbk.Save(outDir + u"mergingcells.out.xls");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **取消合并（拆分）合并的单元格**
### **使用Microsoft Excel**
以下是使用Microsoft Excel拆分合并单元格的步骤。

1. 选择已合并的单元格。
   当单元格已合并时，在**格式**工具栏上选择**合并和居中**。
1. 在**格式**工具栏上点击**合并和居中**。

### **使用Aspose.Cells**
 `Aspose::Cells::Cells` 类具有 `UnMerge()` 方法，可以将单元格拆分回原始状态。该方法通过合并单元格的引用进行取消合并。

以下示例显示了如何拆分合并的单元格（C6）。该示例使用上一个示例中创建的文件，并拆分了合并的单元格。

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"mergingcells.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"unmergingcells.out.xls";

    // Create a Workbook and open the excel file
    Workbook wbk(inputFilePath);

    // Get the first worksheet
    Worksheet worksheet = wbk.GetWorksheets().Get(0);

    // Get the Cells object to fetch all the cells
    Cells cells = worksheet.GetCells();

    // Unmerge the cells
    cells.UnMerge(5, 2, 2, 3);

    // Save the file
    wbk.Save(outputFilePath);

    std::cout << "Cells unmerged successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **高级主题**
- [在工作表中检测合并的单元格](/cells/zh/cpp/detect-merged-cells-in-a-worksheet/)
