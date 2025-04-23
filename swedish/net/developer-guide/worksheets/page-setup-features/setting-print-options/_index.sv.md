---
title: Inställning av utskriftsalternativ
type: docs
weight: 40
url: /sv/net/setting-print-options/
description: Denna artikel visar hur man via C# API och .NET biblioteket programpreparativt ställer in utskriftsalternativen för Excel Arborgruppsfunktionen. Du kan ställa in utskriftssektorn, utskriftstitlar och sidordning.
keywords: ställa in excel utskriftsområde c#, ställa excel utskriftstitlar c#, ställa excel sidordning c#
---

{{% alert color="primary" %}}

Microsoft Excels sidoinställningsinställningar ger flera utskriftsalternativ (även kallade kalkylblad) som låter användare styra hur kalkylbladssidor skrivs ut.

{{% /alert %}}

## **Ställa in utskriftsalternativ**

Dessa utskriftsalternativ låter användare:

- Välja ett specifikt utskriftsområde på en arbetsbok.
- Skriv ut rubriker.
- Skriv ut rutnät.
- Skriv ut rad-/kolumnrubriker.
- Uppnå utkasts kvalitet
- Skriv ut kommentarer.
- Skriv ut cellfel.
- Definiera sidordning.

Aspose.Cells stöder alla utskriftsalternativ som erbjuds av Microsoft Excel och utvecklare kan enkelt konfigurera dessa alternativ för kalkylblad med hjälp av egenskaperna som erbjuds av klassen [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup). Hur dessa egenskaper används diskuteras nedan mer i detalj.

### **Ange utskriftsområde**

Som standard omfattar utskriftsområdet alla områden på kalkylbladet som innehåller data. Utvecklare kan skapa ett specifikt utskriftsområde för kalkylbladet.

För att välja ett specifikt utskriftsområde, använd klassens [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) [**PrintArea**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printarea)-egenskap. Tilldela en cellintervall som definierar utskriftsområdet till denna egenskap.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintArea-1.cs" >}}

### **Ställ in utskriftstitlar**

Aspose.Cells låter dig ange rad- och kolumnrubriker som ska upprepas på alla sidor av ett utskrivet kalkylblad. Gör så genom att använda klassens [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) [**PrintTitleColumns**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlecolumns) och [**PrintTitleRows**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlerows)-egenskaper.

Rader eller kolumner som kommer att upprepas definieras genom att ange deras rad- eller kolumnnummer. Till exempel definieras rader som $1:$2 och kolumner definieras som $A:$B.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintTitle-1.cs" >}}

### **Ange andra utskriftsalternativ**

Klassen [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) erbjuder också flera andra egenskaper för att ställa in generella utskriftsalternativ enligt följande:

- [**PrintGridlines**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printgridlines): en boolesk egenskap som definierar om rutnät ska skrivas ut eller inte.
- [**PrintHeadings**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printheadings): en boolesk egenskap som definierar om rad- och kolumnrubriker ska skrivas ut eller inte.
- [**BlackAndWhite**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/blackandwhite): en boolesk egenskap som definierar om kalkylbladet ska skrivas ut i svartvitt läge eller inte.
- [**PrintComments**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments): definierar om utskriftskommentarerna ska visas på kalkylbladet eller i slutet av kalkylbladet.
- [**PrintDraft**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printdraft): en boolesk egenskap som definierar om kalkylbladet ska skrivas ut utan grafik.
- [**PrintErrors**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors): definierar om cellfel ska skrivas ut som visas, tom, streck eller N/A.

För att ställa in [**PrintComments**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments) och [**PrintErrors**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors)-egenskaperna tillhandahåller även Aspose.Cells två uppräkningar, [**PrintCommentsType**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype) och [**PrintErrorsType**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype) som innehåller fördefinierade värden att tilldela till [**PrintComments**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments) och [**PrintErrors**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors)-egenskaperna respektive.

De fördefinierade värdena i uppräkningen [**PrintCommentsType**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype) listas nedan med deras beskrivningar.

|**Kommentarstyper för utskrift**|**Beskrivning**|
| :- | :- |
|PrintInPlace|Specificerar att skriva ut kommentarer som visas på kalkylbladet.|
|PrintNoComments|Specificerar att inte skriva ut kommentarer.|
|PrintSheetEnd|Specificerar att skriva ut kommentarer i slutet av kalkylbladet.|

De fördefinierade värdena i uppräkningen [**PrintErrorsType**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype) listas nedan med deras beskrivningar.



|**Feltyper för utskrift**|**Beskrivning**|
| :- | :- |
|PrintErrorsBlank|Anger inte att skriva ut felmeddelanden.|
|PrintErrorsDash|Anger att skriva ut fel som "--".|
|PrintErrorsDisplayed|Anger att skriva ut fel som visas.|
|PrintErrorsNA|Anger att skriva ut fel som "#N/A".|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-OtherPrintOptions-1.cs" >}}

### **Ange sidordning**

[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) klassen tillhandahåller [**Order**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/order) egenskapen som används för att ordna flera sidor av din kalkyl att skrivas ut. Det finns två möjligheter att beställa sidorna enligt följande.

- **Nedåt sedan över:** skriver ut alla sidor nedåt innan några sidor till höger skrivs ut.
- **Över sedan nedåt:** skriver sidor från vänster till höger innan sidorna nedanför skrivs ut.

Aspose.Cells tillhandahåller en uppräkning, [**PrintOrderType**](https://reference.aspose.com/cells/net/aspose.cells/printordertype) som innehåller alla fördefinierade ordningstyper.

De fördefinierade värdena i [**PrintOrderType**](https://reference.aspose.com/cells/net/aspose.cells/printordertype) uppräkningen listas nedan.

|**Utskriftsordningstyper**|**Beskrivning**|
| :- | :- |
|DownThenOver|Representerar utskriftsordning nedåt och sedan över.|
|OverThenDown|Representerar utskriftsordning över och sedan nedåt.|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPageOrder-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
