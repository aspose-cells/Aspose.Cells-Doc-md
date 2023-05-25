---
title: Ställa in utskriftsalternativ
type: docs
weight: 40
url: /sv/net/setting-print-options/
description: Den här artikeln visar hur du programmässigt ställer in utskriftsalternativen för Excel-kalkylbladsutskriftsfunktionen med hjälp av biblioteket C# API och .NET. Du kan ställa in utskriftsområde, utskriftsrubriker och sidordning.
keywords: set excel print area c#, set exce print titles c#, set excel page order c#
---
{{% alert color="primary" %}}

Microsoft Excels sidinställningar ger flera utskriftsalternativ (även kallade arkalternativ) som låter användare styra hur kalkylbladssidor skrivs ut.

{{% /alert %}}

##  **Ställa in utskriftsalternativ**

Dessa utskriftsalternativ tillåter användare att:

- Välj ett specifikt utskriftsområde på ett kalkylblad.
- Skriv ut titlar.
- Skriv ut rutnät.
- Skriv ut rad-/kolumnrubriker.
- Uppnå dragkvalitet.
- Skriv ut kommentarer.
- Utskriftscellfel.
- Definiera sidordning.

 Aspose.Cells stöder alla utskriftsalternativ som erbjuds av Microsoft Excel och utvecklare kan enkelt konfigurera dessa alternativ för kalkylblad med hjälp av egenskaperna som erbjuds av[**Utskriftsformat**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)klass. Hur dessa egenskaper används diskuteras mer i detalj nedan.

###  **Ställ in utskriftsområde**

Som standard innehåller utskriftsområdet alla delar av kalkylbladet som innehåller data. Utvecklare kan skapa ett specifikt utskriftsområde i kalkylbladet.

 För att välja ett specifikt utskriftsområde, använd[**Utskriftsformat**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) klass'[**PrintArea**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printarea)fast egendom. Tilldela den här egenskapen ett cellområde som definierar utskriftsområdet.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintArea-1.cs" >}}

###  **Ställ in utskriftsrubriker**

 Aspose.Cells låter dig ange rad- och kolumnrubriker som ska upprepas på alla sidor i ett utskrivet kalkylblad. För att göra det, använd[**Utskriftsformat**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) klass'[**PrintTitleColumns**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlecolumns) och[**PrintTitleRows**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlerows)egenskaper.

Raderna eller kolumnerna som kommer att upprepas definieras genom att skicka deras rad- eller kolumnnummer. Till exempel definieras rader som $1:$2 och kolumner definieras som $A:$B.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintTitle-1.cs" >}}

###  **Ställ in andra utskriftsalternativ**

 De[**Utskriftsformat**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)class tillhandahåller även flera andra egenskaper för att ställa in allmänna utskriftsalternativ enligt följande:

- [**PrintGridlines**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printgridlines): en boolesk egenskap som definierar om rutnät ska skrivas ut eller inte.
- [**Utskriftsrubriker**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printheadings): en boolesk egenskap som definierar om rad- och kolumnrubriker ska skrivas ut eller inte.
- [**Svartvitt**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/blackandwhite): en boolesk egenskap som definierar om kalkylbladet ska skrivas ut i svartvitt läge eller inte.
- [**Skriv ut Kommentarer**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments): definierar om utskriftskommentarerna ska visas på kalkylbladet eller i slutet av kalkylbladet.
- [**PrintDraft**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printdraft): en boolesk egenskap som definierar om arket ska skrivas ut utan grafik.
- [**PrintErrors**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors): definierar om cellfel ska skrivas ut som visas, tomt, streck eller ej.

 För att ställa in[**Skriv ut Kommentarer**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments) och[**PrintErrors**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors)egenskaper, Aspose.Cells ger också två uppräkningar,[**PrintCommentsType**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype) , och[**PrintErrorsType**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype) som innehåller fördefinierade värden som ska tilldelas till[**Skriv ut Kommentarer**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments) och[**PrintErrors**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors)fastigheter respektive.

 De fördefinierade värdena i[**PrintCommentsType**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype)uppräkningar listas nedan med deras beskrivningar.

|**Skriv ut Kommentarstyper**|**Beskrivning**|
| :- | :- |
|PrintInPlace|Anger att kommentarer ska skrivas ut som de visas på kalkylbladet.|
|Skriv ut Inga kommentarer|Anger att kommentarer inte ska skrivas ut.|
|PrintSheetEnd|Anger att kommentarer ska skrivas ut i slutet av kalkylbladet.|

 De fördefinierade värdena för[**PrintErrorsType**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype)uppräkningar listas nedan med deras beskrivningar.



|**Typer av utskriftsfel**|**Beskrivning**|
| :- | :- |
|PrintErrorsBlank|Anger att inte skriva ut fel.|
|PrintErrorsDash|Anger utskriftsfel som "--".|
|PrintErrorsVisade|Anger utskriftsfel som visas.|
|PrintErrorsNA|Anger utskriftsfel som "#N/A".|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-OtherPrintOptions-1.cs" >}}

###  **Ställ in sidordning**

 De[**Utskriftsformat**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) klass ger[**Beställa**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/order)egenskap som används för att beställa flera sidor i ditt kalkylblad som ska skrivas ut. Det finns två möjligheter att beställa sidorna enligt följande.

- **Ner och sedan över:** skriver ut alla sidor innan du skriver ut några sidor till höger.
- **Över sedan ner:** skriver ut sidor från vänster till höger innan du skriver ut sidorna nedan.

 Aspose.Cells tillhandahåller en uppräkning,[**PrintOrderType**](https://reference.aspose.com/cells/net/aspose.cells/printordertype)som innehåller alla fördefinierade ordertyper.

 De fördefinierade värdena för[**PrintOrderType**](https://reference.aspose.com/cells/net/aspose.cells/printordertype)uppräkningar listas nedan.

|**Skriv ut beställningstyper**|**Beskrivning**|
| :- | :- |
|DownThenOver|Representerar utskriftsorder som nedåt sedan över.|
|ÖverThenDown|Representerar utskriftsorder som över sedan ner.|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPageOrder-1.cs" >}}
