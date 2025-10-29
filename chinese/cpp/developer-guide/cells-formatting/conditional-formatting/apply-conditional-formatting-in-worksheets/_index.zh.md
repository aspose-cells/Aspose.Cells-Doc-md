---
title: 在工作表中应用条件格式（使用C++）
linktitle: 应用条件格式
description: 如何在C++中使用Aspose.Cells库在工作表中应用条件格式。通过调整这些条件，您可以更好地控制单元格的外观和显示。
keywords: Aspose.Cells，条件格式，C++，工作表，格式化
type: docs
weight: 130
url: /zh/cpp/apply-conditional-formatting-in-worksheets/
---

{{% alert color="primary" %}}

本文旨在详细介绍如何向工作表的一系列单元格添加条件格式。

条件格式是Microsoft Excel中的一个高级功能，允许您对一系列单元格应用格式，并且根据单元格的值或公式的值进行格式更改。例如，单元格的背景可能显示为红色以突出显示负值，或者正值的文字颜色可能为绿色。当单元格的值满足格式条件时，将应用格式。如果单元格的值不满足格式条件，则使用单元格的默认格式。

使用Microsoft Office Automation可以应用条件格式，但这有其缺点。涉及几个原因和问题：例如，安全性，稳定性，可扩展性和速度。寻找另一个解决方案的主要原因是，Microsoft本身强烈建议不要在软件解决方案中使用Office Automation。

本文展示了如何使用Aspose.Cells API在单元格上添加条件格式的几行简单的代码来创建一个控制台应用程序。

{{% /alert %}}

## **使用Aspose.Cells根据单元格值应用条件格式**

1. **下载并安装Aspose.Cells**。
   1. 下载Aspose.Cells for C++。
1. 在您的开发计算机上安装它。
   所有Aspose组件在安装后都处于评估模式。评估模式没有时间限制，只会在生成的文档中插入水印。
1. **创建一个项目**。
    启动您的C++开发环境，创建一个新的控制台应用程序。
1. **添加引用**。
   向项目添加对Aspose.Cells的引用，例如添加对….\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll的引用。
1. **根据单元格值应用条件格式**。
    以下是完成任务所使用的代码。它在单元格上应用了条件格式。

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

    // Instantiating a Workbook object
    Workbook workbook;

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Adds an empty conditional formatting
    int index = sheet.GetConditionalFormattings().Add();

    // Get the FormatConditionCollection
    FormatConditionCollection fcs = sheet.GetConditionalFormattings().Get(index);

    // Sets the conditional format range
    CellArea ca = CellArea::CreateCellArea(0, 0, 0, 0);

    // Add the cell area to the format condition collection
    fcs.AddArea(ca);

    // Adds condition
    int conditionIndex = fcs.AddCondition(FormatConditionType::CellValue, OperatorType::Between, u"50", u"100");

    // Get the format condition
    FormatCondition fc = fcs.Get(conditionIndex);

    // Sets the background color
    fc.GetStyle().SetBackgroundColor(Color::Red());

    // Saving the Excel file
    workbook.Save(outDir + u"output.out.xls", SaveFormat::Auto);

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

 执行上述代码时，将在输出文件（output.xls）第一个工作表的“A1”单元格应用条件格式。所应用的条件格式取决于单元格值。如果A1单元格的值在50到100之间，则背景色由于条件格式而变成红色。

## **使用Aspose.Cells根据公式应用条件格式**

1. **根据公式应用条件格式（代码片段）**
   以下是完成任务的代码。它在B3上应用条件格式。

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

    // Create workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Adds an empty conditional formatting
    int index = sheet.GetConditionalFormattings().Add();

    // Get the conditional formatting collection
    FormatConditionCollection fcs = sheet.GetConditionalFormattings().Get(index);

    // Sets the conditional format range
    CellArea ca = CellArea::CreateCellArea(2, 1, 2, 1);

    // Add the area to the conditional formatting
    fcs.AddArea(ca);

    // Adds condition
    int conditionIndex = fcs.AddCondition(FormatConditionType::Expression);

    // Get the format condition
    FormatCondition fc = fcs.Get(conditionIndex);

    // Set the formula for the condition
    fc.SetFormula1(u"=IF(SUM(B1:B2)>100,TRUE,FALSE)");

    // Set the background color
    Style style = fc.GetStyle();
    style.SetBackgroundColor(Color::Red());
    fc.SetStyle(style);

    // Set the formula for cell B3
    sheet.GetCells().Get(u"B3").SetFormula(u"=SUM(B1:B2)");

    // Set the value for cell C4
    sheet.GetCells().Get(u"C4").PutValue(u"If Sum of B1:B2 is greater than 100, B3 will have RED background");

    // Save the Excel file
    workbook.Save(outDir + u"output.out.xls", SaveFormat::Auto);

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

 执行上述代码时，将在输出文件（output.xls）第一张工作表的“B3”单元格应用条件格式。应用的条件格式取决于计算“B3”值的公式，即B1与B2之和。
{{< app/cells/assistant language="cpp" >}}
