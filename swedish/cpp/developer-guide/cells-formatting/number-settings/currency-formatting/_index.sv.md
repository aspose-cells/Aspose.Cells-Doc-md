---
title: Hur man formaterar nummer som valuta med C++
linktitle: Hur man formaterar nummer som valuta
type: docs
weight: 10
url: /sv/cpp/format-number-to-currency/
description: Denna artikel kommer att introducera hur man formaterar nummer till valuta med Aspose.Cells for C++ API.
keywords: format nummer som valuta, cellnummerinställningar, formatera nummer till valuta, valutasättningar, valutaformat.
---

## **Möjliga användningsscenario**
Att formatera nummer till valuta i Excel är viktigt av flera skäl, särskilt när man arbetar med finansiella data. Här är varför valutaanpassning är fördelaktigt:

1. **Tydliggör finansiella värden**: att formatera ett nummer som valuta gör det tydligt att värdet representerar pengar. Exempelvis, istället för att se 1000, vilket kan betyda vad som helst, visar $1 000 tydligt att det är ett monetärt belopp.
1. **Inkluderar valutasymboler**: när man hanterar internationella eller flera valutor, klargör formateringen av nummer med lämplig valutasymbol (t.ex. $, €, £) vilken valuta som används, vilket minskar förvirring i multinationella finansiella rapporter eller transaktioner.
1. **Förbättrar professionell presentation**: välformaterade valutavärden ser polerade och professionella ut, vilket är särskilt viktigt för rapporter, presentationer och affärsdokument. $10 000,00 ser mer trovärdigt och organiserat ut än ett enkelt 10000.
1. **Förbättrar läsbarheten**: valutaförformatering lägger till komma som tusentalsseparator och decimaler, vilket gör stora tal lättare att läsa. Exempelvis blir 1 000 000 till $1 000 000,00, vilket är mer läsbart och lättare att förstå vid en snabb blick.
1. **Ser till konsekvens**: genom att tillämpa konsekvent valutaförformatering säkerställer du att alla monetära värden i ett dataset visas i samma format. Denna konsekvens är viktig för finansiell noggrannhet och för professionell kommunikation, särskilt i stora kalkylblad med många siffror.
1. **Visar precision**: valutaförformatering inkluderar vanligtvis två decimaler, vilket gör det lätt att se exakta monetära belopp. Exempelvis, $100,50 är tydligt skilt från $100,00, vilket är viktigt i finansiella rapporter där precision är avgörande.
1. **Förenklar finansiella beräkningar**: när du utför finansiella beräkningar (som att addera summor eller genomsnitt av kostnader), hjälper valutaförformatering Excel och användare att förstå att data är i monetära termer. Det hjälper Excel att tillämpa passande formatering i formler och funktioner, så att resultaten förblir konsekventa.
1. **Minskar missförstånd**: utan valutaförformatering kan nummer misstolkas som allmänt numeriska värden snarare än belopp av pengar. Till exempel, 500 kan misstas för en mängd varor eller enheter, medan $500,00 tydligt representerar ett finansiellt belopp.
1. **Fungerar med redovisningsfunktioner**: valutaförformatering är i linje med redovisningsfunktioner i Excel, såsom balansräkningar eller kassaflödesrapporter. Det gör värdena enklare att använda i finansiella rapporter där pengar är huvudfokuset.
<br>
Sammanfattningsvis hjälper formatering av nummer som valuta att skilja monetära värden från andra typer av nummer, ökar tydligheten och gör data lättare att tolka, särskilt i finansiella sammanhang.

## **Hur man formaterar nummer till valuta i Excel**
Följ dessa steg för att formatera nummer som valuta i Excel:

### **Använda valutaformatalternativet**
1. Markera cellerna du vill formatera som valuta.
1. Gå till fliken Hem i menyfliksområdet.
1. I gruppen Nummer, klicka på nedåtpilen bredvid rutan för nummerformat (det kan visa "Allmänt" som standard).
<br>
<img src="1.png" width=60% />
1. Välj Valuta från listan.

### **Med hjälp av dialogrutan Formatera celler**
1. Markera cellerna du vill formatera.
1. Högerklicka på de valda cellerna och välj Formatera celler för att öppna dialogrutan Formatera celler.
1. I fliken Nummer, välj Valuta från listan till vänster.
<br>
<img src="2.png" width=60% />
1. Du kan anpassa följande: Decimala platser, Symbol, Negativa tal.
1. Klicka på OK för att tillämpa formateringen.

## **Hur man formaterar nummer till valuta i Aspose.Cells**

För att formatera nummer som valuta i biblioteket Aspose.Cells for C++ för att arbeta med Excel-filer kan du tillämpa valutafomatning på cellerna programmässigt. Så här gör du med C++ och Aspose.Cells:

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the cell where you want to apply the currency format
    Cell a1 = worksheet.GetCells().Get(u"A1");

    // Set a numeric value to the cell
    a1.PutValue(1234.56);

    // Create a style object to apply the currency format
    Style a1Style = a1.GetStyle();
    // "7" is the currency format in Excel
    a1Style.SetNumber(7);

    // Apply the style to the cell
    a1.SetStyle(a1Style);

    // Access the cell where you want to apply the currency format
    Cell a2 = worksheet.GetCells().Get(u"A2");

    // Set a numeric value to the cell
    a2.PutValue(3456.78);

    // Create a style object to apply the currency format
    Style a2Style = a2.GetStyle();
    // Custom format for dollar currency
    a2Style.SetCustom(u"$#,##0.00");

    // Apply the style to the cell
    a2.SetStyle(a2Style);

    // Save the workbook
    workbook.Save(u"CurrencyFormatted.xlsx");

    std::cout << "Workbook saved successfully with currency formatting!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
