---
title: 通过C++设置Excel和ODS文件的条件格式
linktitle: 条件格式
type: docs
weight: 60
url: /zh/cpp/conditional-formatting/
description: 如何在C++中对Excel和ODS文件应用条件格式。
keywords: 应用条件格式 
---

## **介绍**

条件格式是Microsoft Excel的高级功能，允许您对单元格或一系列单元格应用格式，并根据单元格的数值或公式的值更改格式。例如，只有当单元格的值大于500时，该单元格才会显示为粗体。当单元格的值满足条件时，会将指定的格式应用到单元格。如果单元格的值不符合格式条件，则使用单元格的默认格式。在Microsoft Excel中，选择**格式**，然后选择**条件格式**以打开条件格式对话框。

Aspose.Cells支持在运行时将条件格式应用于单元格。本文解释了如何实现这一点。它还解释了如何计算Excel用于颜色标度条件格式的颜色。

## **应用条件格式**

Aspose.Cells支持多种方式的条件格式：

- 使用设计师电子表格
- 使用复制方法。
- 在运行时创建条件格式。

### **使用设计者电子表格**

开发人员可以在Microsoft Excel中创建一个包含条件格式的设计师电子表格，然后用Aspose.Cells打开该电子表格。Aspose.Cells加载并保存设计师电子表格，并保留任何条件格式设置。

### **使用复制方法**

Aspose.Cells允许开发人员通过调用[**Range.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/copy/)方法将一个单元格的条件格式设置复制到工作表中的另一个单元格。

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
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Open the Excel file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    int totalRowCount = 0;

    // Iterate through all worksheets in the workbook
    for (int i = 0; i < workbook.GetWorksheets().GetCount(); i++)
    {
        Worksheet sourceSheet = workbook.GetWorksheets().Get(i);

        // Get the maximum display range of the source sheet
        Range sourceRange = sourceSheet.GetCells().GetMaxDisplayRange();

        // Create a destination range in the first worksheet
        Range destRange = worksheet.GetCells().CreateRange(
            sourceRange.GetFirstRow() + totalRowCount, 
            sourceRange.GetFirstColumn(),
            sourceRange.GetRowCount(), 
            sourceRange.GetColumnCount());

        // Copy data from source range to destination range
        destRange.Copy(sourceRange);

        // Update the total row count
        totalRowCount += sourceRange.GetRowCount();
    }

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **在运行时应用条件格式**

Aspose.Cells允许您在运行时添加和删除条件格式。下面的代码示例显示了如何设置条件格式：

1. 实例化一个工作簿。
1. 添加一个空的条件格式。
1. 设置应用格式的范围。
1. 定义格式条件。
1. 保存文件。

在此示例之后还有许多其他小示例，演示如何应用字体设置、边框设置和图案。

Microsoft Excel 2007添加了更高级的条件格式设置，Aspose.Cells也支持。这里的示例说明了如何使用简单的格式设置，而Microsoft Excel 2007的示例则展示了如何应用更高级的条件格式设置。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String filePath = srcDir + u"Book1.xlsx";

    // Instantiating a Workbook object
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Adds an empty conditional formatting
    int index = sheet.GetConditionalFormattings().Add();
    FormatConditionCollection fcs = sheet.GetConditionalFormattings().Get(index);

    // Sets the conditional format range.
    CellArea ca;
    ca.StartRow = 0;
    ca.EndRow = 0;
    ca.StartColumn = 0;
    ca.EndColumn = 0;
    fcs.AddArea(ca);

    ca = CellArea();
    ca.StartRow = 1;
    ca.EndRow = 1;
    ca.StartColumn = 1;
    ca.EndColumn = 1;
    fcs.AddArea(ca);

    // Adds condition.
    int conditionIndex = fcs.AddCondition(FormatConditionType::CellValue, OperatorType::Between, u"=A2", u"100");

    // Adds condition.
    int conditionIndex2 = fcs.AddCondition(FormatConditionType::CellValue, OperatorType::Between, u"50", u"100");

    // Sets the background color.
    FormatCondition fc = fcs.Get(conditionIndex);
    fc.GetStyle().SetBackgroundColor(Color::Red());

    // Saving the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **设置字体**

```c++
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

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Get the style of the cell
    Style style = cell.GetStyle();

    // Set the font weight to bold
    Font font = style.GetFont();
    font.SetIsBold(true);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

您只能更改字体样式、文字颜色、下划线样式和删除线样式。

{{% /alert %}}

### **设置边框**

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

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add an empty conditional formatting
    int index = sheet.GetConditionalFormattings().Add();
    FormatConditionCollection fcs = sheet.GetConditionalFormattings().Get(index);

    // Set the conditional format range
    CellArea ca;
    ca.StartRow = 0;
    ca.EndRow = 5;
    ca.StartColumn = 0;
    ca.EndColumn = 3;
    fcs.AddArea(ca);

    // Add condition
    int conditionIndex = fcs.AddCondition(FormatConditionType::CellValue, OperatorType::Between, u"50", u"100");

    // Set the background color
    FormatCondition fc = fcs.Get(conditionIndex);
    fc.GetStyle().GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Dashed);
    fc.GetStyle().GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Dashed);
    fc.GetStyle().GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Dashed);
    fc.GetStyle().GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Dashed);

    fc.GetStyle().GetBorders().Get(BorderType::LeftBorder).SetColor(Color{0, 255, 255, 255});
    fc.GetStyle().GetBorders().Get(BorderType::RightBorder).SetColor(Color{0, 255, 255, 255});
    fc.GetStyle().GetBorders().Get(BorderType::TopBorder).SetColor(Color{0, 255, 255, 255});
    fc.GetStyle().GetBorders().Get(BorderType::BottomBorder).SetColor(Color{255, 255, 0, 255});

    // Save the workbook
    workbook.Save(outDir + u"output.xlsx");

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

您只能使用细线样式来设置轮廓边框，不允许使用对角线。

{{% /alert %}}

### **设置填充**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Adds an empty conditional formatting
    int index = sheet.GetConditionalFormattings().Add();
    FormatConditionCollection fcs = sheet.GetConditionalFormattings().Get(index);

    // Sets the conditional format range
    CellArea ca;
    ca.StartRow = 0;
    ca.EndRow = 5;
    ca.StartColumn = 0;
    ca.EndColumn = 3;
    fcs.AddArea(ca);

    // Adds condition
    int conditionIndex = fcs.AddCondition(FormatConditionType::CellValue, OperatorType::Between, u"50", u"100");
    FormatCondition fc = fcs.Get(conditionIndex);
    fc.GetStyle().SetPattern(BackgroundType::ReverseDiagonalStripe);
    fc.GetStyle().SetForegroundColor(Color{255, 255, 0, 255});
    fc.GetStyle().SetBackgroundColor(Color{0, 255, 255, 255});

    // Save the workbook
    workbook.Save(outDir + u"output.xlsx");

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **高级主题**
- [添加2色阶和3色阶条件格式](/cells/zh/cpp/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [应用高级条件格式](/cells/zh/cpp/apply-advanced-conditional-formatting/)
- [应用工作表中的条件格式](/cells/zh/cpp/apply-conditional-formatting-in-worksheets/)
- [使用条件格式为交替的行和列添加阴影](/cells/zh/cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)
- [生成条件格式设置数据条图像](/cells/zh/cpp/generate-conditional-formatting-databars-images/)
- [获取在条件格式设置中使用的图标集、数据条或颜色刻度对象](/cells/zh/cpp/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)
{{< app/cells/assistant language="cpp" >}}
