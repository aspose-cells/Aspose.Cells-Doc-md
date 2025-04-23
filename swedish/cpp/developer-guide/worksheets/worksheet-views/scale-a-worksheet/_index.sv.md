---
title: Hur man skalar ett kalkylblad med C++
linktitle: Hur man skalar ett kalkylblad
type: docs
weight: 130
url: /sv/cpp/how-to-scale-a-worksheet/
description: Den här artikeln visar kod som förklarar hur man skalar ett kalkylblad med Aspose.Cells biblioteket i C++.
keywords: C++ skala ett arbetsblad, Hur man skalar ett arbetsblad med C++, Skala ett arbetsblad i C++.
---

## **Möjliga användningsscenario**
Att skala ett kalkylblad kan vara användbart av olika skäl, beroende på sammanhanget du arbetar i. Här är några vanliga skäl för att skala ett kalkylblad:
1. Passa på sida: För att säkerställa att allt innehåll får plats på en enda sida eller ett specifikt antal sidor vid utskrift, vilket gör det lättare att läsa och hantera utan att behöva bläddra igenom flera sidor.

1. Presentation: För att få arbetsbladet att se mer organiserat och professionellt ut, särskilt när du delar det med andra i möten eller rapporter.

1. Läslighet: För att justera storleken på texten och andra element för bättre läsbarhet, särskilt för personer som kan ha svårt att läsa mindre teckensnitt.

1. Platsförvaltning: För att optimera användningen av utrymmet på ett arbetsblad, säkerställa att det inte finns onödig tomrum och att all viktig information är synlig utan överdriven scrollning.

1. Data Visualisering: När det gäller diagram och grafer kan skala hjälpa till att göra dem mer förståeliga genom att justera storleken för att passa den tillgängliga platsen lämpligen.

1. Konsekvens: För att upprätthålla ett konsekvent utseende och känsla över flera arbetsblad eller dokument, vilket är särskilt viktigt i professionella och utbildningsinställningar.

## **Hur man skalar ett kalkylblad i Excel**
Att skala ett arbetsblad i Excel kan hjälpa dig att få ditt innehåll att passa på en enda sida eller ett specificerat antal sidor vid utskrift. Här är stegen för att skala ett arbetsblad:

1. Öppna ditt arbetsblad: Öppna Excel-arbetsbladet som du vill skala.

1. Gå till fliken Sidlayout: Klicka på fliken Sidlayout i bandet.

1. Skala för att passa grupp: I fliken Sidlayout, hitta gruppen Skala för att passa. Här har du alternativen för att justera skalan. Bredd: Detta alternativ tillåter dig att specificera hur många sidor bred det utskrivna arbetsbladet ska vara. Höjd: Detta alternativ tillåter dig att specificera hur många sidor högt det utskrivna arbetsbladet ska vara. Skala: Du kan också ange en anpassad procentandel för skalan här.
<br>
<img src="1.png" width=60% />

1. Justera Bredd och Höjd: Ställ in Bredd och Höjd till önskat antal sidor. Till exempel, ställ båda till 1 sida om du vill att arbetsbladet ska passa på en sida.

1. Justera skaleringsprocenten (om nödvändigt): Om du föredrar att ange en specifik skaleringsprocent, justera rutan Skala. Till exempel, att ställa in den till 50% gör att allt blir halvt så stort.


## **Hur man skalar ett arbetsblad med C++**
Aspose.Cells är ett kraftfullt bibliotek för att arbeta med Excel-filer programmatiskt. För att skala ett arbetsblad med Aspose.Cells, måste du följa dessa steg: ladda [exempel fil](sample.xlsx) och justera utskriftsinställningarna så att innehållet passar till det önskade antalet sidor eller en specifik procentuell storlek av originalet.

### **Exempel: Passa till sida**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load the Excel file
    Workbook workbook(u"sample.xlsx");

    // Access the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Access the PageSetup object
    PageSetup pageSetup = sheet.GetPageSetup();

    // Set the worksheet to fit to 1 page wide and 1 page tall
    pageSetup.SetFitToPagesWide(1);
    pageSetup.SetFitToPagesTall(1);

    // Save the modified workbook
    workbook.Save(u"output_fit_to_page.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
<br>
<img src="3.png" width=60% />

### **Exempel: Skala till procentandel**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    // Initialize Aspose.Cells
    Aspose::Cells::Startup();

    // Load the Excel file
    Workbook workbook(u"sample.xlsx");

    // Access the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Access the PageSetup object
    PageSetup pageSetup = sheet.GetPageSetup();

    // Set the scaling to a specific percentage (e.g., 75%)
    pageSetup.SetZoom(75);

    // Save the modified workbook
    workbook.Save(u"output_scaled_percentage.xlsx");

    // Clean up Aspose.Cells resources
    Aspose::Cells::Cleanup();

    return 0;
}
```
<br>
<img src="2.png" width=60% />
