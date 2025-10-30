---
title: Kopiera sidinställningsinställningar från kälvark till destinationsark med C++
linktitle: Kopiera sidinställningsinställningar
type: docs
weight: 80
url: /sv/cpp/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: Denna artikel förklarar hur man använder C++ API eller bibliotek för att kopiera sidinställningar från kälvark till destinationsark programmatiskt.
keywords: kopiera sidinställningar c++, kopiera sidinställningar till målark c++
---

## **Möjliga användningsscenario**

När du lägger till ett nytt blad i en arbetsbok innehåller den standard *Sidlayoutinställningar*. Det kan finnas tillfällen när du behöver överföra inställningarna ([**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/)) från ett blad till ett annat blad. Detta dokument förklarar hur man kopierar sidlayoutinställningar från ett blad till ett annat med hjälp av Aspose.Cells API:er.

## **Kopiera siduppsättning inställningar från källkalkylblad till destinations kalkylblad**

Följande exempelkod illustrerar hur man kopierar *sidlayoutinställningar* från ett blad till ett annat med hjälp av [**PageSetup.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/copy/)-metoden. Se följande exempelkod och dess konsolresultat som referens.

## **Exempelkod**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    Workbook wb;

    wb.GetWorksheets().Add(u"TestSheet1");
    wb.GetWorksheets().Add(u"TestSheet2");

    Worksheet TestSheet1 = wb.GetWorksheets().Get(u"TestSheet1");
    Worksheet TestSheet2 = wb.GetWorksheets().Get(u"TestSheet2");

    TestSheet1.GetPageSetup().SetPaperSize(PaperSizeType::PaperA3ExtraTransverse);

    std::cout << "Before Paper Size: " << static_cast<int>(TestSheet1.GetPageSetup().GetPaperSize()) << std::endl;
    std::cout << "Before Paper Size: " << static_cast<int>(TestSheet2.GetPageSetup().GetPaperSize()) << std::endl;
    std::cout << std::endl;

    CopyOptions copyOptions;
    TestSheet2.GetPageSetup().Copy(TestSheet1.GetPageSetup(), copyOptions);

    std::cout << "After Paper Size: " << static_cast<int>(TestSheet1.GetPageSetup().GetPaperSize()) << std::endl;
    std::cout << "After Paper Size: " << static_cast<int>(TestSheet2.GetPageSetup().GetPaperSize()) << std::endl;
    std::cout << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Konsoloutput**

{{< highlight java >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
