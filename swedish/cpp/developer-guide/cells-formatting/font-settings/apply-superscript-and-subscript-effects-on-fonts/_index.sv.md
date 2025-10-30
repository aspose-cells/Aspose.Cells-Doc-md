---
title: Tillämpa exponent och subscript effekter på teckensnitt med C++
linktitle: Tillämpa överstruken och understreckande effekter på typsnitt
type: docs
weight: 80
url: /sv/cpp/apply-superscript-and-subscript-effects-on-fonts/
description: C++ koden för att tillämpa exponent och subscript effekt på text i Excel med hjälp av Aspose.Cells for C++ API.
keywords: excel exponent c++, excel subscript c++, excel exponent och subscript c++, infoga subscript och superscript i excel c++, lägg till subscript och superscript i excel c++, lägg till exponent och subscript i excel c++, lägg till exponent i excel c++, lägg till subscript i excel c++
---

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller funktionalitet för att tillämpa överstruken (text ovanför baslinjen) och understreckande (text under baslinjen) effekter på text.

{{% /alert %}}

## **Arbeta med överstruken och understreck**

Tillämpa överstruken effekt genom att ställa in [**Style.Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/)-objektets [**IsSuperscript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issuperscript/)-egenskap till **true**. För att tillämpa understreck, ställ in [**Style.Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/)-objektets [**IsSubscript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issubscript/)-egenskap till **true**.

Följande kodexempel visar hur man tillämpar över- och understreck på text.

### C++-kod för att tillämpa exponent-effekt på text

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

### C++-kod för att tillämpa subscript-effekt på text

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
