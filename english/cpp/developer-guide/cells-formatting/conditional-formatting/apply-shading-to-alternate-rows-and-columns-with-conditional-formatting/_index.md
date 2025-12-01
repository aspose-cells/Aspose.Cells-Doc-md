---
title: Apply Shading to Alternate Rows and Columns with Conditional Formatting with C++
linktitle: Apply Shading to Alternate Rows and Columns
description: How to use the Aspose.Cells library in C++ to apply conditional formatting shadows for alternating rows and columns. By adjusting these criteria, you have more control over how cells look and appear.
keywords: Aspose.Cells, Conditional Formatting, C++, Alternate Rows, Alternate Columns, Shadows
type: docs
weight: 30
url: /cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells APIs provide the means to add & manipulate conditional formatting rules for the [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) object. These rules can be tailored in a number of ways to get the desired formatting based on conditions or rules. This article will demonstrate the use of Aspose.Cells for C++ APIs to apply shading to alternate rows & columns with the help of conditional formatting rules and Excel's built-in functions.

{{% /alert %}}

This article makes use of Excel's built-in functions such as ROW, COLUMN & MOD. Here are some details of these functions for a better understanding of the code snippet provided ahead.

- **ROW()** function returns the row number of a cell reference. If the reference parameter is omitted, it assumes that the reference is the cell address in which the ROW function has been entered in.
- **COLUMN()** function returns the column number of a cell reference. If the reference parameter is omitted, it assumes that the reference is the cell address in which the COLUMN function has been entered in.
- **MOD()** function returns the remainder after a number is divided by a divisor, where the first parameter to the function is the numeric value whose remainder you wish to find and the second parameter is the number used to divide into the number parameter. If the divisor is 0, then it will return the #DIV/0! error.

Let's start writing some code to accomplish this goal with the help of Aspose.Cells for C++ API.

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

The following snapshot shows the resultant spreadsheet loaded in Excel application.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

In order to apply the shading to alternative columns, all you have to do is to change the formula **=MOD(ROW(),2)=0** as **=MOD(COLUMN(),2)=0**, that is; instead of getting the row index, modify the formula to retrieve the column index. 
The resultant spreadsheet, in this case, will look as follow.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |
{{< app/cells/assistant language="cpp" >}}
