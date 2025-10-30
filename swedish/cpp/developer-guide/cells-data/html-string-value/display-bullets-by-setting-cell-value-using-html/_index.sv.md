---
title: Visa punkter genom att ställa in Cell värdet med HTML med C++
linktitle: Visa punkter genom att ställa in cellvärde med hjälp av HTML
type: docs
weight: 130
url: /sv/cpp/display-bullets-by-setting-cell-value-using/
description: Lägg till punkter i Excel celler med HTML och den lättanvända API n Aspose.Cells for C++.
keywords: lägg till punkter i excel, lägg till punkter i excel c++, visa punkter i excel, visa punkter i excel c++, lägg till punkter i excel med HTML, lägg till punkter i excel med HTML c++, visa punkter i excel med HTML, visa punkter i excel med HTML c++, visa punkter i excel med HTML, lägg till punkter i excel med HTML
---

{{% alert color="primary" %}}

Aspose.Cells stödjer att visa punkter med HTML-kod. Den här artikeln förklarar hur du visar punkter genom att ställa in cellvärde med hjälp av HTML. Vi kommer att använda egenskapen [**Cell.GetHtmlString()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/) för att ställa in cellvärdet med vårt HTML.

{{% /alert %}}

## C++ kod för att visa punkter genom att ställa in cellvärdet med HTML

Följande kod använder HTML-koden för att ställa in cellvärdet. När du kör denna kod får du utdata som visas på bilden nedan.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Create workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get("A1");

    // Set the HTML string
    cell.SetHtmlString(u"<font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'>Text 1 </font>"
                       u"<font style='font-family:Wingdings;font-size:8.0pt;color:#009DD9;mso-font-charset:2;'>l</font>"
                       u"<font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'> Text 2 </font>"
                       u"<font style='font-family:Wingdings;font-size:8.0pt;color:#009DD9;mso-font-charset:2;'>l</font>"
                       u"<font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'> Text 3 </font>"
                       u"<font style='font-family:Wingdings;font-size:8.0pt;color:#009DD9;mso-font-charset:2;'>l</font>"
                       u"<font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'> Text 4 </font>");

    // Auto fit the Columns
    worksheet.AutoFitColumns();

    // Save the workbook
    U16String outputFilePath = u"BulletsInCells_out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## Utdata genererad av provkoden

Följande skärmbild visar utdata av ovanstående provkod.

![todo:image_alt_text](display-bullets-by-setting-cell-value-using-html_1.png)
{{< app/cells/assistant language="cpp" >}}
