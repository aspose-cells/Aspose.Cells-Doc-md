---
title: 使用C++为交替行和列应用条件格式阴影
linktitle: 为交替行列应用阴影
description: 如何在C++中使用Aspose.Cells库为交替行列的条件格式添加阴影。通过调整这些条件，您可以更好地控制单元格的外观和显示。
keywords: Aspose.Cells，条件格式，C++，交替行，交替列，阴影
type: docs
weight: 30
url: /zh/cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}}

Aspose.Cells API提供了添加和操作 [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) 对象的条件格式规则的方法。这些规则可以以多种方式定制，以根据条件或规则获得所需的格式。本文将演示如何使用Aspose.Cells for C++ API，通过条件格式规则和Excel内置函数，为交替行列添加阴影。

{{% /alert %}}

本文使用Excel内置函数，如ROW、COLUMN和MOD。以下是这些函数的一些详细信息，以便更好地理解提供的代码片段。

- **ROW()**函数返回单元格引用的行号。如果省略引用参数，则假定引用是输入ROW函数的单元格地址。
- **COLUMN()**函数返回单元格引用的列号。如果省略引用参数，则假定引用是输入COLUMN函数的单元格地址。
- **MOD()**函数返回一个数字被除数除后的余数，函数的第一个参数是要查找余数的数值，第二个参数是用来除以数值参数的数。如果除数为0，则会返回#DIV/0!错误。

让我们开始编写一些代码，借助Aspose.Cells for C++ API实现此目标。

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

    // Create an instance of Workbook
    Workbook book;

    // Access the Worksheet on which desired rule has to be applied
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Add FormatConditions to the instance of Worksheet
    int idx = sheet.GetConditionalFormattings().Add();

    // Access the newly added FormatConditions via its index
    auto conditionCollection = sheet.GetConditionalFormattings().Get(idx);

    // Define a CellsArea on which conditional formatting will be applicable
    // The code creates a CellArea ranging from A1 to I20
    CellArea area = CellArea::CreateCellArea(u"A1", u"I20");

    // Add area to the instance of FormatConditions
    conditionCollection.AddArea(area);

    // Add a condition to the instance of FormatConditions
    // For this case, the condition type is expression, which is based on some formula
    idx = conditionCollection.AddCondition(FormatConditionType::Expression);

    // Access the newly added FormatCondition via its index
    FormatCondition formatCondition = conditionCollection.Get(idx);

    // Set the formula for the FormatCondition
    // Formula uses the Excel's built-in functions as discussed earlier in this article
    formatCondition.SetFormula1(u"=MOD(ROW(),2)=0");

    // Set the background color and pattern for the FormatCondition's Style
    formatCondition.GetStyle().SetBackgroundColor(Color::Blue());
    formatCondition.GetStyle().SetPattern(BackgroundType::Solid);

    // Save the result on disk
    book.Save(outDir + u"output_out.xlsx");

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

以下快照显示了加载到Excel应用程序中的结果电子表格。

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

为了将底纹应用于交替列，您只需将公式**=MOD(ROW(),2)=0**更改为**=MOD(COLUMN(),2)=0**，即不再获取行索引，而是修改公式以检索列索引。 
在这种情况下，生成的电子表格将如下所示。

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |
{{< app/cells/assistant language="cpp" >}}
