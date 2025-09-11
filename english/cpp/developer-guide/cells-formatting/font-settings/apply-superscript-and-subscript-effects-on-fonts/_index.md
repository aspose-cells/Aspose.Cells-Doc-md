---
title: Apply Superscript and Subscript Effects on Fonts with C++
linktitle: Apply Superscript and Subscript Effects on Fonts
type: docs
weight: 80
url: /cpp/apply-superscript-and-subscript-effects-on-fonts/
description: The C++ code to apply superscript and subscript effect to text in excel with the use of Aspose.Cells for C++ API.
keywords: excel superscript c++, excel subscript c++, excel superscript and subscript c++, insert subscript and superscript in excel c++, add subscript and superscript in excel c++, add superscript and subscript excel c++, add superscript excel c++, add subscript excel c++
---

{{% alert color="primary" %}}

Aspose.Cells provides the functionality to apply superscript (text above the baseline) and subscript (text below the baseline) effects to text.

{{% /alert %}}

## **Working with Superscript and Subscript**

Apply the superscript effect by setting the [**Style.Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/) object's [**IsSuperscript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issuperscript/) property to **true**. To apply subscript, set the [**Style.Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/) object's [**IsSubscript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issubscript/) property to **true**.

The following code examples show how to apply super and subscript to text.

### C++ code to Apply Superscript effect on text

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

    // Adding a new worksheet to the Excel object
    workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Accessing the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Adding some value to the "A1" cell
    cell.PutValue(u"Hello");

    // Setting the font Superscript
    Style style = cell.GetStyle();
    style.GetFont().SetIsSuperscript(true);
    cell.SetStyle(style);

    // Saving the Excel file
    workbook.Save(outDir + u"Superscript_out.xls", SaveFormat::Auto);

    std::cout << "Excel file saved successfully with superscript text!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### C++ code to Apply Subscript effect on text

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello");

    // Set the font Subscript
    Style style = cell.GetStyle();
    style.GetFont().SetIsSubscript(true);
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"Subscript_out.xls", SaveFormat::Auto);

    std::cout << "File saved successfully with subscript text!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}