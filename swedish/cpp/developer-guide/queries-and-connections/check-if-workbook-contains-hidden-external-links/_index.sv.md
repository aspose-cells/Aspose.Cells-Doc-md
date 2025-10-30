---
title: Kontrollera om arbetsboken innehåller dolda externa länkar med C++
linktitle: Kontrollera om arbetsboken innehåller dolda externa länkar
type: docs
weight: 230
url: /sv/cpp/check-if-workbook-contains-hidden-external-links/
description: Lär dig hur man upptäcker dolda externa länkar i Excel arbetsböcker med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**
Ibland innehåller arbetsboken externa länkar som är dolda och inte kan visas i Microsoft Excel. Aspose.Cells hämtar alla externa länkar oavsett om de är visa eller dolda. Dock kan du kontrollera [ExternalLink.IsVisible](https://reference.aspose.com/cells/cpp/aspose.cells/externallink/isvisible/) egenskapen för att se om den externa länken är synlig eller inte.

## **Kontrollera om arbetsboken innehåller dolda externa länkar**
Följande exempel laddar [källexcelfilen](5115413.xlsx) som innehåller dolda externa länkar. Dessa länkar kan inte ses i Microsoft Excel men finns i arbetsboken. Efter att ha skrivit ut [ExternalLink.GetDataSource()](https://reference.aspose.com/cells/cpp/aspose.cells/externallink/getdatasource/) och [ExternalLink.IsReferred](https://reference.aspose.com/cells/cpp/aspose.cells/externallink/isreferred/) egenskaper, skriver den ut [ExternalLink.IsVisible](https://reference.aspose.com/cells/cpp/aspose.cells/externallink/isvisible/) egenskapen. I nedanstående konsolutmatning kan du se att alla externa länkar inte är synliga.

### **Exempelkod**
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Loads the workbook which contains hidden external links
    Workbook workbook(srcDir + u"sample.xlsx");

    // Access the external link collection of the workbook
    ExternalLinkCollection links = workbook.GetWorksheets().GetExternalLinks();

    // Print all the external links and check their IsVisible property
    for (int i = 0; i < links.GetCount(); i++)
    {
        ExternalLink link = links.Get(i);
        std::cout << "Data Source: " << link.GetDataSource().ToUtf8() << std::endl;
        std::cout << "Is Visible: " << (link.IsVisible() ? "true" : "false") << std::endl;
        std::cout << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

### **Konsoloutput**
Här är konsoloutputen av ovanstående kodexempel när den körs med den angivna [prov-Excel-filen](5115413.xlsx).

{{< highlight java >}}

Data Source: C:\International\DDB\FAS 133\Swap Rates\GS_1M_3M_1_2_5_¥$_(B)IRSwaps_0400.xls

Is Referred: True

Is Visible: False

Data Source: C:\DIST DAY\MAY TEMPLATES\030601t.xls

Is Referred: True

Is Visible: False

Data Source: C:\AREVIEW\2002 Controllable\Autobrct.xls

Is Referred: True

Is Visible: False

Data Source: C:\CARDSFO\Main Files\Rate Forecast\FY 11\IFR 11 01 (New Model REPORTS 11.08.07).xls

Is Referred: True

Is Visible: False

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
