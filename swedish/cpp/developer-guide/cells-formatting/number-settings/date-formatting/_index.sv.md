---
title: Hur man formaterar nummer som datum med C++
linktitle: Hur man formaterar nummer som datum
type: docs
weight: 10
url: /sv/cpp/format-number-to-date/
description: Denna artikel introducerar hur man formaterar nummer till datum med Aspose.Cells for C++ API et.
keywords: formatera nummer som datum, cellnummerinställningar, formatera nummer till datum, datuminställningar, datumformat.
---

## **Möjliga användningsscenario**
Formatering av nummer som datum i Excel (eller annan kalkylbladsprogramvara) är viktigt av flera skäl, särskilt när du arbetar med data som inkluderar tid eller schemaläggningsinformation. Här är varför det är fördelaktigt att formatera nummer till datum:

1. **Korrekt tolkning av datumvärden**: I Excel lagras datum som serienummer (t.ex. 1 representerar 1 januari 1900 och 44210 representerar 6 september 2021). Om dessa nummer inte är formaterade som datum kan användare se meningslösa nummer i stället för igenkännbara datum. Att formatera dem rätt låter Excel visa dem som faktiska datum (t.ex. 09/06/2021 istället för 44210).
2. **Förenklar tidsrelaterade beräkningar**: Excel kan utföra många beräkningar med datum, som att beräkna antal dagar mellan två datum, addera eller subtrahera dagar eller bestämma veckodagen. Om numren inte är formaterade som datum kan Excel inte utföra dessa operationer effektivt. Till exempel, om du vill veta antalet dagar mellan 01/09/2023 och 01/10/2023, kan Excel enkelt beräkna detta om numren är i datumformat.
3. **Säkerställer konsistens**: När alla datumrelaterade värden är korrekt formaterade, säkerställs att alla datum visas i en enhetlig, läsbar stil. Denna konsistens är viktig i affärsrapporter, projektscheman och databaser där datumkonsistens är avgörande. Olika regioner använder olika datumformat (t.ex. MM/DD/YYYY i USA jämfört med DD/MM/YYYY i många andra länder), så formatering hjälper till att säkerställa att datum tolkas korrekt.
4. **Förbättrar läsbarheten**: Datum som visas i ett standardformat (t.ex. 01/01/2024) är lättare att läsa än råa serienummer som 45000. Korrekt datumformatering gör ditt kalkylblad mer användarvänligt och förhindrar förvirring. Detta är särskilt viktigt vid schemaläggning, tidslinjer, evenemangsplanering eller historiska data.
5. **Hjälper vid sortering och filtrering**: När datum är korrekt formaterade, känner Excel igen dem som faktiska datum, vilket gör det lättare att sortera eller filtrera data kronologiskt. Till exempel kan du sortera en lista av händelser efter datum eller filtrera ett datautdrag för att visa endast poster mellan två specifika datum. Utan korrekt datumformat kan sortering ske baserat på det råa numret i stället för faktiska kalenderdatum.
6. **Möjliggör användning av datumfunktioner**: Excel erbjuder ett brett utbud av kraftfulla datumfunktioner, till exempel: TODAY(), DATEDIF(), WORKDAY(), YEAR(), MONTH(), DAY(). Dessa funktioner kräver att datum är korrekt formaterade för att beräkningar ska bli exakta.
7. **Stöder visualiseringar (diagram/tidslinjer)**: Korrekt formaterade datum kan användas för att skapa diagram och grafer där tid är en nyckelaxel. Till exempel, i en tidslinjegraf, behöver Excel datum i ett erkänt format för att plotta händelser korrekt över tid. Felaktigt formaterade eller oanvända nummer kan leda till diagram som inte är meningsfulla eller visar felaktig information.
8. **Förebygger feltolkningar**: Råa nummer kan lätt missförstås. Till exempel kan 44210 tolkas som ett generellt numeriskt värde, men när det är formaterat som ett datum är det tydligt att det representerar 6 september 2021. Korrekt formaterade datum hjälper till att undvika feltolkning av data.
9. **Underlättar datainmatning**: När celler är formaterade som datum, uppmanas användare att skriva in data i ett giltigt datumformat, vilket förhindrar datainmatningsfel och säkerställer att datumvärden registreras korrekt.
10. **Avgörande för schemaläggning och övervakning**: I alla situationer som involverar schemaläggning, uppföljning eller deadline (som projektledning, finansiell prognostisering eller tidskänsliga rapporter) är formatering av nummer till datum avgörande för noggrannhet och förståelse. Det möjliggör bättre planering och genomförande.

## **Hur man formaterar nummer till datum i Excel**
För att formatera ett nummer som datum i Excel, följ dessa steg:

### **Med hjälp av bandet (Startfliken)**
1. Markera cellerna som innehåller talen du vill formatera som datum.
2. Gå till startfliken i menyfliksområdet.
3. I gruppen Nummer klickar du på nedpilen i rutan Nummerformat (som kan visa "Allmänt" eller "Nummer" som standard).
4. Välj Kort datum eller Långt datum från listan. Kort datum: Visar datum i en kortfattad form, t.ex. MM/DD/YYYY (USA-format) eller DD/MM/YYYY (internationellt format). Långt datum: Visar datum i ett mer beskrivande format, t.ex. måndag, 1 januari 2024.
<br>
<img src="1.png" width=60% />

### **Med hjälp av dialogrutan Formatera celler**
1. Markera cellerna du vill formatera.
2. Högerklicka på de markerade cellerna och välj Formatera celler, eller tryck Ctrl + 1 (Windows) eller Cmd + 1 (Mac).
3. I dialogrutan för Formatera celler, gå till fliken Nummer.
4. Välj Datum från listan till vänster.
5. Välj önskat datumformat från listan till höger (t.ex. MM/DD/ÅÅÅÅ, DD/MM/ÅÅÅÅ eller anpassade format).
<br>
<img src="2.png" width=60% />
6. Klicka på OK för att anpassa datumformatet.

## **Hur man formaterar nummer till datum i Aspose.Cells**

För att formatera nummer som datum i biblioteket Aspose.Cells for C++ för att arbeta med Excel-filer kan du tillämpa datummärkning på celler programmatiskt. Så här gör du med C++ och Aspose.Cells:

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the cell where you want to apply the date format
    Cell a1 = worksheet.GetCells().Get(u"A1");

    // Set a numeric value that represents a date (e.g., 44210 represents 09/06/2021 in Excel)
    a1.PutValue(44210);

    // Create a style object to apply the date format
    Style a1Style = a1.GetStyle();

    // "14" represents a standard date format in Excel (MM/DD/YYYY)
    a1Style.SetNumber(14);

    // Apply the style to the cell
    a1.SetStyle(a1Style);

    // Access the cell where you want to apply the currency format
    Cell a2 = worksheet.GetCells().Get(u"A2");

    // Set a numeric value to the cell
    a2.PutValue(44210);

    // Create a style object to apply the date format
    Style a2Style = a2.GetStyle();

    // Custom format for YYYY-MM-DD
    a2Style.SetCustom(u"YYYY-MM-DD");

    // Apply the style to the cell
    a2.SetStyle(a2Style);

    // Save the workbook
    workbook.Save(u"DateFormatted.xlsx");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
