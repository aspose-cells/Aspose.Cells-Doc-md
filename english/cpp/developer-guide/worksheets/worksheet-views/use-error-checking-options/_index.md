---
title: Use Error Checking Options with C++
linktitle: Use Error Checking Options
type: docs
weight: 140
url: /cpp/use-error-checking-options/
description: In this article, you will find sample code that will programmatically use error checking options of Excel worksheets e.g. Numbers stored as Text using C++ API or Library.
keywords: store number as text in excel using C++, error check excel options C++
---

{{% alert color="primary" %}}

Microsoft Excel allows users to define error checking options and rules. Users often see error checks when creating formulas, a small triangle at the top right corner of a cell highlights when there's a problem with a cell. Excel provides information that helps users to correct common problems.

{{% /alert %}}

## **Types of Errors**

Errors that mean that the formula cannot return a result - such as dividing a number by zero - require immediate attention and an error value is displayed in the cell. Clicking on the green triangle shows an exclamation mark, clicking this opens a list of options.

The error can be resolved using the options, or be ignored. Ignoring an error means that that error will not appear in further error checks.

Aspose.Cells provides error checking option features. The [**ErrorCheckOption**](https://reference.aspose.com/cells/cpp/aspose.cells/errorcheckoption/) class manages different types of error checks, for example, numbers stored as text, formula calculation errors, and validation errors. Use the [**ErrorCheckType**](https://reference.aspose.com/cells/cpp/aspose.cells/errorchecktype/) enumeration to set the desired error checking.

## **Numbers Stored as Text**

Occasionally, numbers might be formatted and stored in cells as text. This can cause problems with calculations or produce confusing sort orders. Numbers that are formatted as text are left-aligned instead of right-aligned in the cell. If a formula that should perform a mathematical operation on cells doesn't return a value, check the alignment in the cells that the formula refers to – some or all of those cells might be numbers formatted as text.

You can use the error checking options to quickly convert numbers stored as text to real numbers. In Microsoft Excel 2003:

1. On the **Tools** menu, click **Options**.
1. Select the Error Checking tab.
   **Number stored as text** option is checked by default.
1. Disable it.

The following sample code shows how to disable the numbers stored as text error checking option for a worksheet in the template XLS file using the Aspose.Cells APIs.

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
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create a workbook and open the template spreadsheet
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Instantiate the error checking options
    ErrorCheckOptionCollection opts = sheet.GetErrorCheckOptions();

    // Add a new error check option
    int index = opts.Add();
    ErrorCheckOption opt = opts.Get(index);

    // Disable the numbers stored as text option
    opt.SetErrorCheck(ErrorCheckType::NumberStoredAsText, false);

    // Set the range
    CellArea area = CellArea::CreateCellArea(0, 0, 1000, 50);
    opt.AddRange(area);

    // Path of output excel file
    U16String outputFilePath = outDir + u"out_test.out.xlsx";

    // Save the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Error check options applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}