---
title: Inställning av utskriftsalternativ
type: docs
weight: 40
url: /sv/python-net/setting-print-options/
description: Den här artikeln demonstrerar hur man programmatiskt ställer in utskriftsalternativ för Excel kalkylarks siduppsättningsfunktion med hjälp av Aspose.Cells för Python via .NET API. Du kan ange utskriftsområdet, utskriftstitlar och sidordning.
keywords: Python Excel Library, ställ in Excel utskriftsområde med Python, ställ in Excel utskriftstitlar med Python, Python hur man ställer in excelsidor, Python hur man ställer in utskriftsalternativ, Python hur man ställer in utskriftsområde, Python hur man ställer in utskriftstitlar. 
---

{{% alert color="primary" %}}

Microsoft Excels sidoinställningsinställningar ger flera utskriftsalternativ (även kallade kalkylblad) som låter användare styra hur kalkylbladssidor skrivs ut.

{{% /alert %}}

## **Hur man ställer in utskriftsalternativ**

Dessa utskriftsalternativ låter användare:

- Välja ett specifikt utskriftsområde på en arbetsbok.
- Skriv ut rubriker.
- Skriv ut rutnät.
- Skriv ut rad-/kolumnrubriker.
- Uppnå utkasts kvalitet
- Skriv ut kommentarer.
- Skriv ut cellfel.
- Definiera sidordning.

Aspose.Cells för Python via .NET stödjer alla utskriftsalternativ som erbjuds av Microsoft Excel och utvecklare kan enkelt konfigurera dessa alternativ för kalkylblad med hjälp av egenskaperna som erbjuds av klassen [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup). Hur dessa egenskaper används diskuteras mer detaljerat nedan.

## **Hur man ställer in utskriftsområde**

Som standard omfattar utskriftsområdet alla områden på kalkylbladet som innehåller data. Utvecklare kan skapa ett specifikt utskriftsområde för kalkylbladet.

För att välja ett specifikt utskriftsområde, använd klassens [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) [**print_area**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_area/)-egenskap. Tilldela en cellintervall som definierar utskriftsområdet till denna egenskap.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetPrintArea-1.py" >}}

## **Hur man ställer in utskriftstitlar**

Aspose.Cells för Python via .NET gör att du kan ange rad- och kolumnrubriker som ska upprepas på alla sidor i ett utskrivet kalkylblad. För att göra det, använd egenskaperna [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) och [**print_title_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_title_columns/) i klassen [**print_title_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_title_rows).

Rader eller kolumner som kommer att upprepas definieras genom att ange deras rad- eller kolumnnummer. Till exempel definieras rader som $1:$2 och kolumner definieras som $A:$B.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetPrintTitle-1.py" >}}

## **Hur du ställer in andra utskriftsalternativ**

Klassen [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) erbjuder också flera andra egenskaper för att ställa in generella utskriftsalternativ enligt följande:

- [**print_grid_lines**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_gridlines/): en boolesk egenskap som definierar om rutnät ska skrivas ut eller inte.
- [**print_headings**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_headings/): en boolesk egenskap som definierar om rad- och kolumnrubriker ska skrivas ut eller inte.
- [**black_and_white**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/black_and_white/): en boolesk egenskap som definierar om kalkylbladet ska skrivas ut i svartvitt läge eller inte.
- [**print_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_comments/): definierar om utskriftskommentarerna ska visas på kalkylbladet eller i slutet av kalkylbladet.
- [**print_draft**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_draft/): en boolesk egenskap som definierar om kalkylbladet ska skrivas ut utan grafik.
- [**print_errors**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_errors): definierar om cellfel ska skrivas ut som visas, tom, streck eller N/A.

För att ställa in [**print_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_comments/) och [**print_errors**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_errors)-egenskaperna tillhandahåller även Aspose.Cells två uppräkningar, [**PrintCommentsType**](https://reference.aspose.com/cells/python-net/aspose.cells/printcommentstype) och [**PrintErrorsType**](https://reference.aspose.com/cells/python-net/aspose.cells/printerrorstype) som innehåller fördefinierade värden att tilldela till [**print_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_comments/) och [**print_errors**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_errors)-egenskaperna respektive.

De fördefinierade värdena i uppräkningen [**PrintCommentsType**](https://reference.aspose.com/cells/python-net/aspose.cells/printcommentstype) listas nedan med deras beskrivningar.

|**Kommentarstyper för utskrift**|**Beskrivning**|
| :- | :- |
|PRINT_IN_PLACE|Ange att skriva ut kommentarer som visas på arbetsbladet.|
|PRINT_NO_COMMENTS|Ange att inte skriva ut kommentarer.|
|PRINT_SHEET_END|Ange att skriva ut kommentarer i slutet av arbetsbladet.|

De fördefinierade värdena i uppräkningen [**PrintErrorsType**](https://reference.aspose.com/cells/python-net/aspose.cells/printerrorstype) listas nedan med deras beskrivningar.



|**Feltyper för utskrift**|**Beskrivning**|
| :- | :- |
|PRINT_ERRORS_BLANK|Ange att inte skriva ut fel.|
|PRINT_ERRORS_DASH|Ange att skriva ut fel som "--".|
|PRINT_ERRORS_DISPLAYED|Ange att skriva ut fel som visas.|
|PRINT_ERRORS_NA|Ange att skriva ut fel som "#N/A".|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-OtherPrintOptions-1.py" >}}

## **Hur du ställer in sidordning**

[**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) klassen tillhandahåller [**Order**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/order) egenskapen som används för att ordna flera sidor av din kalkyl att skrivas ut. Det finns två möjligheter att beställa sidorna enligt följande.

- **Nedåt sedan över:** skriver ut alla sidor nedåt innan några sidor till höger skrivs ut.
- **Över sedan nedåt:** skriver sidor från vänster till höger innan sidorna nedanför skrivs ut.

Aspose.Cells tillhandahåller en uppräkning, [**PrintOrderType**](https://reference.aspose.com/cells/python-net/aspose.cells/printordertype) som innehåller alla fördefinierade ordningstyper.

De fördefinierade värdena i [**PrintOrderType**](https://reference.aspose.com/cells/python-net/aspose.cells/printordertype) uppräkningen listas nedan.

|**Utskriftsordningstyper**|**Beskrivning**|
| :- | :- |
|NER_SÅ_ÖVER|Representerar utskriftsordning som ner sedan över.|
|ÖVER_SÅ_NER|Representerar utskriftsordning som över sedan ner.|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetPageOrder-1.py" >}}
