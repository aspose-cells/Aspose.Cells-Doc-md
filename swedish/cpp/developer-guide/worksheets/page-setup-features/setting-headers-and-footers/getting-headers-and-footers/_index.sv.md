---
title: Hämtar rubriker eller sidfötter med C++
linktitle: Att få headers eller footers
type: docs
weight: 30
url: /sv/cpp/get-headers-or-footers/
description: Denna artikel förklarar hur man programmässigt hämtar rubriker och sidfötter från Excel eller OpenOffice filer med hjälp av C++ API eller bibliotek.
---

{{% alert color="primary" %}}

Headers och footers visas endast i vy för sidlayout, utskriftsvisning och på utskrifter. 

Du kan också använda dialogrutan Sidlayout om du vill visa headers eller footers för mer än ett kalkylblad åt gången. 

För andra bladtyper, såsom kalkylblad eller diagram, kan du infoga headers och footers endast genom att använda dialogrutan Sidlayout.

{{% /alert %}}

## **Hämta sidhuvuden och sidfötter i MS Excel**
1. Klicka på kalkylarket där du vill visa eller ändra sidhuvuden eller sidfötter.
2. På fliken Visa, i gruppen arbetsboksvisningar, klicka på Sidlayout.
  Excel visar kalkylarket i Sidlayoutvy.
3. För att visa eller redigera en sidhuvud eller sidfot, klicka i vänster-, mitt- eller höger sidhuvud- eller sidfotstextruta längst upp eller längst ned på kalkylarket (under Sidhuvud eller ovanför Sidfot).


## **Hämtar rubriker och sidfötter med Aspose.Cells for C++**
Med [**Worksheet.PageSetup.GetHeader**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getheader/) och [**Worksheet.PageSetup.GetFooter**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getfooter/) metoder kan C++ utvecklare enkelt hämta rubriker eller sidfötter från filen.

1. Konstruera Arbetsbok för att öppna filen.
2. Hämta kalkylarket där du vill hämta sidhuvuden eller sidfot.
3. Hämta sidhuvud eller sidfot med specifik avsnitts-id.

```c++
#include <iostream>
#include <codecvt>
#include <locale>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook workbook(srcDir + u"HeaderFooter.xlsx");
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    std::cout << sheet.GetPageSetup().GetHeader(0).ToUtf8() << std::endl;
    std::cout << sheet.GetPageSetup().GetHeader(1).ToUtf8() << std::endl;
    std::cout << sheet.GetPageSetup().GetHeader(2).ToUtf8() << std::endl;
    std::cout << sheet.GetPageSetup().GetFooter(1).ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Parera sidhuvuden och sidfötter till kommandolista**
Sidhuvud- eller sidfotstexten kan innehålla specialkommandon, till exempel en platshållare för sidnumret, aktuellt datum eller textformateringsattribut.

Specialkommandon representeras av en enda bokstav med en ledande och-symbol ("&").

Rubrik- och sidföttersträngarna konstrueras med ABNF-grammatik. Det är inte lätt att förstå utan en visare.

Aspose.Cells for C++ tillhandahåller [**Worksheet.PageSetup.GetCommands**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getcommands/) metod för att tolka rubriker och sidfötter som kommando lista.

Följande kod visar hur man tolkar rubrik eller sidfot som kommando lista och bearbetar kommandon:

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    Workbook workbook(u"HeaderFooter.xlsx");

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get left section of header
    U16String headerSection = sheet.GetPageSetup().GetHeader(0);

    // Get commands from the header section
    Vector<HeaderFooterCommand> commands = sheet.GetPageSetup().GetCommands(headerSection);

    // Iterate through each command
    for (int i = 0; i < commands.GetLength(); ++i)
    {
        HeaderFooterCommand c = commands[i];
        switch (c.GetType())
        {
            case HeaderFooterCommandType::SheetName:
                // Embedded the name of the sheet to header or footer
                break;
            default:
                break;
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
