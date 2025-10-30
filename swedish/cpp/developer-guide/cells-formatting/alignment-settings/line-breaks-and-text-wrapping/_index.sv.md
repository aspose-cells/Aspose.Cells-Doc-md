---
title: Radbrytningar och textomslag i C++
description: Hur man implementerar textomslag och ordwrap i C++ med Aspose.Cells biblioteket. Genom att använda Aspose.Cells kan du enkelt infoga text i celler och ställa in metod för textomslag, såsom manuell ordwrap, ordwrap osv. Detta dokument beskriver hur du implementerar dessa funktioner och ger exempel på kod för din referens.
keywords: Aspose.Cells, radbrytningar, textomslag, textlayout
type: docs
weight: 60
url: /sv/cpp/line-breaks-and-text-wrapping/
---

{{% alert color="primary" %}}

För att säkerställa att texten i en cell kan läsas, kan explicita radbrytningar och textomslag appliceras. Textomslag gör att en rad blir flera i en cell, medan explicita radbrytningar sätts in precis där du vill ha dem.

{{% /alert %}}

## **För att omsluta text i en cell**

För att omsluta text i en cell, använd egenskapen [**Aspose.Cells.Style.IsTextWrapped**](https://reference.aspose.com/cells/cpp/aspose.cells/style/istextwrapped/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create Workbook Object
    Workbook wb;

    // Open first Worksheet in the workbook
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Get Worksheet Cells Collection
    Cells cell = ws.GetCells();

    // Increase the width of the first column
    cell.SetColumnWidth(0, 35);

    // Increase the height of the first row
    cell.SetRowHeight(0, 36);

    // Add text to the first cell
    cell.Get(0, 0).PutValue(u"I am using the latest version of Aspose.Cells to test this functionality");

    // Make the cell's text wrap
    Style style = cell.Get(0, 0).GetStyle();
    style.SetIsTextWrapped(true);
    cell.Get(0, 0).SetStyle(style);

    // Save Excel File
    wb.Save(srcDir + u"WrappingText.out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **För att använda explicita radbrytningar**

Du kan använda '\n' i C++ för att infoga ett explicit radbrytning i en cell.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Create Workbook Object
    Workbook workbook;

    // Open first Worksheet in the workbook
    Worksheet ws = workbook.GetWorksheets().Get(0);

    // Get Worksheet Cells Collection
    Aspose::Cells::Cells cell = ws.GetCells();

    // Increase the width of First Column Width
    cell.SetColumnWidth(0, 35);

    // Increase the height of first row
    cell.SetRowHeight(0, 65);

    // Add Text to the First Cell with Explicit Line Breaks
    cell.Get(0, 0).PutValue(u"I am using\nthe latest version of \nAspose.Cells to \ntest this functionality");

    // Make Cell's Text wrap
    Style style = cell.Get(0, 0).GetStyle();
    style.SetIsTextWrapped(true);
    cell.Get(0, 0).SetStyle(style);

    // Save Excel File
    U16String outputFilePath = u"WrappingText.out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
