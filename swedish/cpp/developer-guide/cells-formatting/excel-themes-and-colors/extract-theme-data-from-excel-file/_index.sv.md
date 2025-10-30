---
title: Extrahera temadatum från Excel fil med C++
linktitle: Extrahera temadata från Excel fil
description: Aspose.Cells är ett C++ bibliotek för att arbeta med kalkylbladsfiler. Det stödjer att extrahera temadatum från Excel filer, vilket gör det möjligt för användare att få tag på stilen och formateringsinformationen för dokument. Denna artikel introducerar hur man extraherar temadatum från Excel filer med Aspose.Cells biblioteket.
keywords: Aspose.Cells, Excel fil, Temadata, Stil, Format
type: docs
weight: 120
url: /sv/cpp/extract-theme-data-from-excel-file/
---

{{% alert color="primary" %}}

Aspose.Cells tillåter användare att extrahera temarelaterad data från en Excel-fil. Till exempel kan du extrahera temnamnet som tillämpats på arbetsboken och temfärgen som tillämpats på en cell eller dess gränser.

Du kan tillämpa ett tema på din arbetsbok med Microsoft Excel via Kommandot Page Layout > Themes.

{{% /alert %}}

## C++-kod för att extrahera temadata från Excel-fil

Följande kod exempel extraherar temnamnet som tillämpats på källarbetsboken och extraherar sedan temfärgen som tillämpats på cell A1 och temfärgen som tillämpats på bottenlinjen av cellen.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook object
    Workbook workbook(srcDir + u"source.xlsx");

    // Extract theme name applied to this workbook
    std::cout << "Theme: " << workbook.GetTheme().ToUtf8() << std::endl;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Get the style object
    Style style = cell.GetStyle();

    // Check if theme has foreground color defined
    if (style.GetForegroundThemeColor().IsNull())
    {
        std::cout << "Theme has not foreground color defined." << std::endl;
    }
    else
    {
        // Extract theme color applied to this cell
        std::cout << "Foreground Theme Color Type: " << static_cast<int>(style.GetForegroundThemeColor().GetColorType()) << std::endl;
    }

    // Extract theme color applied to the bottom border of the cell
    Border bot = style.GetBorders().Get(BorderType::BottomBorder);
    if (bot.GetThemeColor().IsNull())
    {
        std::cout << "Theme has not Border color defined." << std::endl;
    }
    else
    {
        std::cout << "Border Theme Color Type: " << static_cast<int>(bot.GetThemeColor().GetColorType()) << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
