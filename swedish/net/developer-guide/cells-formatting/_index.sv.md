---
title: Formatera celler
description: Lär dig hur man formaterar och stylar celler i Aspose.Cells for .NET, inklusive nummerformatering, datumformatering, typsnittsstilar och andra cellstilsalternativ. Vår guide hjälper dig att skapa attraktiva och professionellt utseende kalkylblad.
keywords: Aspose.Cells for .NET, cellformatering, stil, nummerformatering, datumformatering, typsnitt, cellstil alternativ, kalkylblad, skapa, professionellt utseende, formatera rader och kolumner.
linktitle: Formatera celler
type: docs
weight: 120
url: /sv/net/cells-formatting/
---

## **Introduktion**

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) och [**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) metoder för klassen [Cell](https://reference.aspose.com/cells/net/aspose.cells/cell), som används för att hämta/ställa in formateringsstilen för en cell. Aspose.Cells tillhandahåller även en [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) klass.

{{% /alert %}}

## **Hur man formaterar celler med hjälp av GetStyle och SetStyle-metoderna**

Tillämpa olika typer av formateringsstilar på celler för att ställa in bakgrund eller förgrundsfärger, ramar, typsnitt, horisontell och vertikal justering, indenteringsnivå, textriktning, rotationsvinkel och mycket mer.

### **Hur man använder GetStyle och SetStyle-metoderna**

Om utvecklare behöver tillämpa olika formateringsstilar på olika celler är det bättre att hämta [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) för cellen med hjälp av [**Cell.GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle)-metoden, specificera stilstilarna och sedan tillämpa formateringen med hjälp av [**Cell.SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle)-metoden. Ett exempel ges nedan för att visa denna metod att tillämpa olika formatering på en cell.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingGetStyleSetStyle-1.cs" >}}

### **Hur man använder Style-objektet för att formatera olika celler**

Om utvecklare behöver tillämpa samma formateringsstil på olika celler kan de använda [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)-objekt. Följ stegen nedan för att använda [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)-objektet:

1. Lägg till ett [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)-objekt genom att anropa [**CreateStyle**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle)-metoden från [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)-klassen
1. Få tillgång till det nytt tillagda [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)-objektet
1. Ange de önskade egenskaperna/attributen för [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)-objektet för att tillämpa önskade formateringsinställningar
1. Tilldela konfigurerat [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)-objekt till önskade celler

Denna metod kan avsevärt förbättra effektiviteten i dina applikationer och spara minne också.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingStyleObject-1.cs" >}}

### **Hur man använder Microsoft Excel 2007 Fördefinierade Stilar**

Om du behöver tillämpa olika formateringsstilar för Microsoft Excel 2007, tillämpa stilar med hjälp av Aspose.Cells API. Ett exempel ges nedan för att visa denna metod att tillämpa en fördefinierad stil på en cell.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingExcelPredefinedStyles-1.cs" >}}



## **Hur man formaterar valda tecken i en cell**

Hantera typsnittsinställningar förklarar hur man formaterar text i celler, men det förklarar bara hur man formaterar allt cellinnehåll. Vad händer om du vill formatera endast utvalda tecken?

Aspose.Cells stöder också denna funktion. Detta ämne förklarar hur vi använder denna funktion effektivt.

### **Hur man formaterar valda tecken**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klassen innehåller en [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)-samling som tillåter åtkomst till varje kalkylblad i en Excel-fil. Ett kalkylblad representeras av [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klassen. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-klassen tillhandahåller en [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)-samling. Varje objekt i [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)-samlingen representerar ett objekt av [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)-klassen.

[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)-klassen tillhandahåller [**Characters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters)-metoden som tar följande parametrar för att välja ett teckenintervall inne i en cell:

- **Startindex**, index för tecknet som urvalet börjar från.
- **Antal tecken**, antalet tecken att välja.

[**Characters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters)-metoden returnerar en instans av [**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)-klassen som låter utvecklare formatera tecknen på samma sätt som de skulle göra med en cell enligt exemplet nedan. I utdatat endast ordet 'Besök' i cellen A1 kommer att formateras med standardtypsnittet men 'Aspose!' är fetstil och blått.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormattingSelectedCharacters-1.cs" >}}

{{% alert color="primary" %}}

Om du är intresserad av att formatera en del av Rich Text i en cell, överväg att använda metoderna [**Cell.GetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) och [**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters). [[**Cell.GetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters)-metoden ska användas för att få tillgång till textdelarna och sedan kan ändringar göras med hjälp av metoden [**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters), medan **Get**-metoden returnerar en array av [**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)-objekt som kan manipuleras för att ange olika egenskaper som typsnitt, typsnittsfärg, fetstil, osv. och **Set**-metoden kan användas för att tillämpa ändringarna.

{{% /alert %}}

## **Hur man formaterar rader och kolumner**

Ibland behöver utvecklare tillämpa samma formatering på rader eller kolumner. Att tillämpa formatering på celler en i taget tar ofta längre tid och är inte en bra lösning.
För att lösa detta problem tillhandahåller Aspose.Cells ett enkelt, snabbt sätt som diskuteras utförligt i den här artikeln.

### **Formatering av rader & kolumner**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) innehåller en [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)-samling som gör det möjligt att komma åt varje kalkylblad i Excel-filen. Ett kalkylblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) tillhandahåller en [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)-samling. [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)-samlingen tillhandahåller en [**Rows**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows)-samling.

### **Hur man formaterar en rad**

Varje objekt i [**Rows**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows)-samlingen representerar ett [**Row**](https://reference.aspose.com/cells/net/aspose.cells/row)-objekt. [**Row**](https://reference.aspose.com/cells/net/aspose.cells/row)-objektet erbjuder metoden [**ApplyStyle**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle) som används för att ange radens formatering. För att tillämpa samma formatering på en rad använder man [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)-objektet. Nedanstående steg visar hur man använder det.

1. Lägg till ett [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)-objekt i [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)-klassen genom att anropa dess [**CreateStyle**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle)-metod.
1. Ange [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)-objektets egenskaper för att tillämpa formateringsinställningar.
1. Gör de relevanta attributen PÅ för [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)-objektet.
1. Tilldela det konfigurerade [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)-objektet till [**Row**](https://reference.aspose.com/cells/net/aspose.cells/row)-objektet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingARow-1.cs" >}}

### **Hur man formaterar en kolumn**

[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)-samlingen tillhandahåller även en [**Columns**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns)-samling. Varje objekt i [**Columns**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns)-samlingen representerar ett [**Column**](https://reference.aspose.com/cells/net/aspose.cells/column)-objekt. Liknande ett [**Row**](https://reference.aspose.com/cells/net/aspose.cells/row)-objekt erbjuder även [**Column**](https://reference.aspose.com/cells/net/aspose.cells/column)-objektet [**ApplyStyle**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle)-metoden för att formatera en kolumn.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingAColumn-1.cs" >}}

## **Fortsatta ämnen**
- [Justering inställningar](/cells/sv/net/cells-alignment-settings/)
- [Kantinställningar](/cells/sv/net/cells-border-settings/)
- [Ställa in villkorlig formatering av Excel och ODS-filer.](/cells/sv/net/conditional-formatting/)
- [Excel-teman och färger](/cells/sv/net/excel-themes-and-colors/)
- [Fyllinställningar](/cells/sv/net/cells-fill-settings/)
- [Typsnittinställningar](/cells/sv/net/cells-font-settings/)
- [Formatera kalkylbladsceller i en arbetsbok](/cells/sv/net/format-worksheet-cells-in-a-workbook/)
- [Implementera 1904 Datasystem](/cells/sv/net/implement-1904-date-system/)
- [Sammanfoga och dela upp celler](/cells/sv/net/merging-and-unmerging-cells/)
- [Antalseinställningar](/cells/sv/net/cells-number-settings/)
- [Hämta och ange stil för celler](/cells/sv/net/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

{{< app/cells/assistant language="csharp" >}}
