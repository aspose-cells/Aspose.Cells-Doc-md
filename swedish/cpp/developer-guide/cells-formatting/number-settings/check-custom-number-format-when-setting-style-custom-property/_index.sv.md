---
title: Kontrollera anpassad nummerformat när du ställer in Style.Custom egenskapen med C++
description: Aspose.Cells är ett C++ bibliotek för att arbeta med kalkylblad, vilket stöder att kontrollera anpassade nummerformat vid formatering. Denna artikel visar hur man använder Aspose.Cells biblioteket för att kontrollera anpassade nummerformat för att säkerställa att formateringen är korrekt.
keywords: Aspose.Cells, C++ bibliotek, kalkylblad, formatering, anpassad nummerformat, kontroll, validering
type: docs
weight: 170
url: /sv/cpp/check-custom-number-format-when-setting-style-custom-property/
---

## **Möjliga användningsscenario**

Om du tilldelar ett ogiltigt anpassat nummerformat till [**Style.GetCustom()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/)-egenskapen kommer Aspose.Cells inte att ge något undantag. Men om du vill att Aspose.Cells ska kontrollera om det tilldelade anpassade nummerformatet är giltigt eller inte, ställ då in [**Workbook.GetCheckCustomNumberFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcustomnumberformat/)-egenskapen till **true**.

## **Kontrollera anpassad nummerformatering vid inställning av Style.Custom-egenskap**

Följande kodexempel tilldelar ett ogiltigt anpassat nummerformat till [**Style.GetCustom()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/)-egenskapen. Eftersom vi redan har ställt in [**Workbook.GetCheckCustomNumberFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcustomnumberformat/)-egenskapen till **true**, kastar den ett undantag, t.ex. ogiltigt nummerformat. Läs kommentarerna i koden för mer hjälp.

## **Exempelkod**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create an instance of Workbook class
    Workbook book;

    // Setting this property to true will make Aspose.Cells to throw exception
    // when invalid custom number format is assigned to Style.Custom property
    book.GetSettings().SetCheckCustomNumberFormat(true);

    // Access first worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Access cell A1 and put some number to it
    Cell cell = sheet.GetCells().Get(u"A1");
    cell.PutValue(2347);

    // Access cell's style and set its Style.Custom property
    Style style = cell.GetStyle();

    // This line will throw exception if Workbook.Settings.CheckCustomNumberFormat is set to true
    style.SetCustom(u"ggg @ fff"); // Invalid custom number format

    std::cout << "Custom number format set." << std::endl;

    Aspose::Cells::Cleanup();
}
```
