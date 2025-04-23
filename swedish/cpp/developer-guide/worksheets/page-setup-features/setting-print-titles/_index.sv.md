---
title: Hur man ställer in Utskriftsrubriker med C++
linktitle: Hur man ställer in Utskriftsrubriker
type: docs
weight: 200
url: /sv/cpp/how-to-set-print-titles/
description: Denna artikel visar kod som förklarar hur man ställer in utskriftsrubriker med Aspose.Cells biblioteket i C++.
keywords: Skriv ut rader och kolumner upprepade gånger, C++ Hur man ställer in utskriftstitlar, Ställ in och rensa utskriftstitlar med C++, Hur man rensar utskriftstitlar i C++, Hur man lägger till utskriftstitlar med C++, hur man tar bort utskriftstitlar med C++, Hur man ställer in utskriftstitlar i Excel, Hur man rensar utskriftstitlar i Excel.
---

## **Möjliga användningsscenario**

Att ställa in utskriftstitlar i Excel säkerställer att specifika rader eller kolumner upprepas på varje utskriven sida, vilket är särskilt användbart för stora kalkylblad som sträcker sig över flera sidor. Här är några anledningar till varför du kan ställa in utskriftstitlar:

1. Förbättrad läsbarhet: Utskriftstitlar hjälper läsarna att förstå data genom att hålla rubriker synliga på alla sidor, vilket gör det lättare att tolka informationen på varje sida utan att behöva hänvisa tillbaka till första sidan.

1. Professionell presentation: Att konsekvent visa rubriker eller etiketter på varje sida skapar ett mer polerat och professionellt utseende på utskrivna dokument.

1. Förbättrad navigering: För dokument med omfattande data gör upprepning av rubriker på varje sida snabbare navigering och referens, vilket minskar behovet av att vända fram och tillbaka mellan sidor.

1. Minskade fel: När rubriker är närvarande på varje sida minimeras missförstånd eller datainmatningsfel, eftersom användare lätt kan se sammanhanget för data.

1. Konsekvens: Att säkerställa att viktig information, som kolumnrubriker eller radetiketter, alltid är synlig upprätthåller konsekvens och tydlighet genom hela dokumentet.

## **Hur man ställer in utskriftstitlar i Excel**

Följ dessa steg för att ställa in utskriftstitlar i Excel:

1. Öppna fliken "Sidlayout": Klicka på "Sidlayout"-fliken i menyfliksområdet högst upp i Excel-fönstret.
1. Få tillgång till Utskriftstitlar: I gruppen "Siduppställning" klickar du på "Utskriftstitlar".
1. Ställ in rader att upprepa: I dialogrutan "Siduppställning" går du till fliken "Blad". I avsnittet "Utskriftstitlar" anger du de rader som ska upprepas överst genom att klicka på rutan bredvid "Rader att upprepa längst upp" och välja rad(er) du vill upprepa.
1. Ställ in kolumner att upprepa (om behövs): På liknande sätt kan du ange de kolumner som ska upprepas längst till vänster genom att klicka på rutan bredvid "Kolumner att upprepa till vänster" och välja den eller de kolumner du vill upprepa.
<br>
<img src="3.png" width=60% />

1. Bekräfta och skriv ut: Klicka på "OK" för att tillämpa inställningarna. När du skriver ut kalkylbladet kommer de angivna raderna eller kolumnerna att visas på varje utskriven sida.

## **Hur man rensar utskriftstitlar i Excel**

För att rensa utskriftstitlar i Excel måste du ta bort de rader eller kolumner som är inställda att upprepas på varje utskriven sida. Så här gör du:

1. Öppna fliken "Sidlayout": Klicka på "Sidlayout"-fliken i menyfliksområdet högst upp i Excel-fönstret.
1. Få tillgång till Utskriftstitlar: I gruppen "Siduppställning" klickar du på "Utskriftstitlar".
1. Rensa utskriftstitlar: I dialogrutan "Siduppställning" går du till fliken "Blad". Radera texten i rutorna för "Rader att upprepa längst upp" och "Kolumner att upprepa till vänster" genom att ta bort innehållet i dem.
<br>
<img src="4.png" width=60% />

1. Bekräfta och stäng: Klicka på "OK" för att tillämpa ändringarna.

## **Hur man ställer in utskriftstitlar med Aspose.Cells**

För att ställa in utskriftstitlar i ett angivet kalkylblad: Ladda först [provfilen](input.xlsx), och du behöver sedan ändra egenskaperna [**Worksheet.GetPrintTitleRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinttitlerows/) och [**Worksheet.GetPrintTitleColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinttitlecolumns/) av [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/)-objektet för det önskade kalkylbladet. Att ställa in dessa egenskaper till ett områdesträng kommer att ställa in utskriftstitlarna.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load the workbook
    Workbook workbook(u"input.xlsx");

    // Access the desired worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set rows to repeat at the top (e.g., rows 1 and 2)
    worksheet.GetPageSetup().SetPrintTitleRows(u"$1:$2");

    // Set columns to repeat at the left (e.g., columns A and B)
    worksheet.GetPageSetup().SetPrintTitleColumns(u"$A:$B");

    // Save the workbook
    workbook.Save(u"set_print_titles.pdf");

    std::cout << "Print titles set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Utmatningsresultat:
<br>
<img src="1.png" width=60% />

## **Hur man rensar utskriftstitlar med Aspose.Cells**

För att rensa utskriftstitlar i ett specificerat kalkylblad: Ladda först [provfilen](input.xlsx), och du behöver sedan ändra egenskaperna [**Worksheet.GetPrintTitleRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinttitlerows/) och [**Worksheet.GetPrintTitleColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinttitlecolumns/) av [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/)-objektet för det önskade kalkylbladet. Att ställa in dessa egenskaper till en tom sträng rensar utskriftstitlarna.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load the workbook
    U16String inputFilePath = u"input.xlsx";
    Workbook workbook(inputFilePath);

    // Access the desired worksheet
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet worksheet = sheets.Get(0);

    // Clear the rows and columns set to repeat
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintTitleRows(u"");
    pageSetup.SetPrintTitleColumns(u"");

    // Save the workbook
    U16String outputFilePath = u"clear_print_titles.pdf";
    workbook.Save(outputFilePath);

    Aspose::Cells::Cleanup();
}
```

Utmatningsresultat:
<br>
<img src="2.png" width=60% />
