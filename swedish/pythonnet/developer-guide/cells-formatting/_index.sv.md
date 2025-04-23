---
title: Formatera celler
description: Lär dig hur man formaterar och stylar celler i Aspose.Cells för Python via .NET, inklusive nummerformattering, datumformattering, typsnittsstilar och andra cellstilsalternativ. Vår guide hjälper dig att skapa attraktiva och professionella kalkylblad.
keywords: Aspose.Cells för Python via .NET, cellformatering, styling, nummerformat, datumformat, typsnittstil, cellstilalternativ, kalkylblad, skapa, professionell look, formatera rader och kolumner.
linktitle: Formatera celler
type: docs
weight: 120
url: /sv/python-net/cells-formatting/
---

## **Introduktion**

{{% alert color="primary" %}}

Aspose.Cells för Python via .NET tillhandahåller [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) och [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) metoder av [Cell](https://reference.aspose.com/cells/python-net/aspose.cells/cell) klassen, används för att få/sett formateringsstil för en cell. Aspose.Cells för Python via .NET ger också en [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) klass.

{{% /alert %}}

## **Hur man formaterar celler med hjälp av GetStyle och SetStyle-metoderna**

Tillämpa olika typer av formateringsstilar på celler för att ställa in bakgrund eller förgrundsfärger, ramar, typsnitt, horisontell och vertikal justering, indenteringsnivå, textriktning, rotationsvinkel och mycket mer.

### **Hur man använder GetStyle och SetStyle-metoderna**

Om utvecklare behöver tillämpa olika formateringsstilar på olika celler är det bättre att hämta [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) för cellen med hjälp av [**Cell.get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style)-metoden, specificera stilstilarna och sedan tillämpa formateringen med hjälp av [**Cell.set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style)-metoden. Ett exempel ges nedan för att visa denna metod att tillämpa olika formatering på en cell.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApproachesToFormatData-UsingGetStyleSetStyle-1.py" >}}

### **Hur man använder Style-objektet för att formatera olika celler**

Om utvecklare behöver tillämpa samma formateringsstil på olika celler kan de använda [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)-objekt. Följ stegen nedan för att använda [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)-objektet:

1. Lägg till ett [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)-objekt genom att anropa [**create_style**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/create_style)-metoden från [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)-klassen
1. Få tillgång till det nytt tillagda [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)-objektet
1. Ange de önskade egenskaperna/attributen för [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)-objektet för att tillämpa önskade formateringsinställningar
1. Tilldela konfigurerat [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)-objekt till önskade celler

Denna metod kan avsevärt förbättra effektiviteten i dina applikationer och spara minne också.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApproachesToFormatData-UsingStyleObject-1.py" >}}

### **Hur man använder Microsoft Excel 2007 Fördefinierade Stilar**

Om du behöver tillämpa olika formateringsstilar för Microsoft Excel 2007, använd stilar via Aspose.Cells för Python via .NET API. Ett exempel nedan demonstrerar denna metod för att tillämpa en fördefinierad stil på en cell.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApproachesToFormatData-UsingExcelPredefinedStyles-1.py" >}}



## **Hur man formaterar valda tecken i en cell**

Hantera typsnittsinställningar förklarar hur man formaterar text i celler, men det förklarar bara hur man formaterar allt cellinnehåll. Vad händer om du vill formatera endast utvalda tecken?

Aspose.Cells för Python via .NET stöder denna funktion också. Denna artikel förklarar hur man använder denna funktion effektivt.

### **Hur man formaterar valda tecken**

Aspose.Cells för Python via .NET tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) klassen innehåller en [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) samling som ger åtkomst till varje kalkylblad i en Excel-fil. Ett kalkylblad representeras av [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) klassen. [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) klassen tillhandahåller en [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) samling. Varje objekt i [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) samlingen representerar ett objekt av [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) klassen.

[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)-klassen tillhandahåller [**characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/characters)-metoden som tar följande parametrar för att välja ett teckenintervall inne i en cell:

- **Startindex**, index för tecknet som urvalet börjar från.
- **Antal tecken**, antalet tecken att välja.

[**characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/characters)-metoden returnerar en instans av [**FontSetting**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsetting)-klassen som låter utvecklare formatera tecknen på samma sätt som de skulle göra med en cell enligt exemplet nedan. I utdatat endast ordet 'Besök' i cellen A1 kommer att formateras med standardtypsnittet men 'Aspose!' är fetstil och blått.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-FormattingSelectedCharacters-1.py" >}}

{{% alert color="primary" %}}

Om du är intresserad av att formatera en del av Rich Text i en cell, överväg att använda metoderna [**Cell.get_characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_characters) & [**Cell.set_characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_characters). [**Cell.get_characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_characters) metoden används för att komma åt textdelarna och sedan kan ändringar göras med [**Cell.set_characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_characters) metoden medan **Get**-metoden returnerar en array av [**FontSetting**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsetting) objekt som kan manipuleras för att sätta olika egenskaper som typsnitt, färg, fetstil, etc. och **Set**-metoden kan användas för att tillämpa ändringarna.

{{% /alert %}}

## **Hur man formaterar rader och kolumner**

Ibland behöver utvecklare tillämpa samma formatering på rader eller kolumner. Att tillämpa formatering på celler en i taget tar ofta längre tid och är inte en bra lösning.
För att åtgärda detta ger Aspose.Cells för Python via .NET ett enkelt, snabbt sätt som diskuteras i detalj i denna artikel.

### **Formatering av rader & kolumner**

Aspose.Cells för Python via .NET tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) klassen innehåller en [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) samling som ger åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) klassen. [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) klassen tillhandahåller en [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) samling. [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) samlingen ger en [**rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/rows) samling.

### **Hur man formaterar en rad**

Varje objekt i [**rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/rows)-samlingen representerar ett [**Row**](https://reference.aspose.com/cells/python-net/aspose.cells/row)-objekt. [**Row**](https://reference.aspose.com/cells/python-net/aspose.cells/row)-objektet erbjuder metoden [**apply_style**](https://reference.aspose.com/cells/python-net/aspose.cells/row/apply_style) som används för att ange radens formatering. För att tillämpa samma formatering på en rad använder man [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)-objektet. Nedanstående steg visar hur man använder det.

1. Lägg till ett [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)-objekt i [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)-klassen genom att anropa dess [**create_style**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/create_style)-metod.
1. Ange [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)-objektets egenskaper för att tillämpa formateringsinställningar.
1. Gör de relevanta attributen PÅ för [**StyleFlag**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag)-objektet.
1. Tilldela det konfigurerade [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)-objektet till [**Row**](https://reference.aspose.com/cells/python-net/aspose.cells/row)-objektet.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-FormatRowsColumns-FormattingARow-1.py" >}}

### **Hur man formaterar en kolumn**

[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)-samlingen tillhandahåller även en [**columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/columns)-samling. Varje objekt i [**columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/columns)-samlingen representerar ett [**Column**](https://reference.aspose.com/cells/python-net/aspose.cells/column)-objekt. Liknande ett [**Row**](https://reference.aspose.com/cells/python-net/aspose.cells/row)-objekt erbjuder även [**Column**](https://reference.aspose.com/cells/python-net/aspose.cells/column)-objektet [**apply_style**](https://reference.aspose.com/cells/python-net/aspose.cells/row/apply_style)-metoden för att formatera en kolumn.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-FormatRowsColumns-FormattingAColumn-1.py" >}}

## **Fortsatta ämnen**
- [Justering inställningar](/cells/sv/python-net/cells-alignment-settings/)
- [Kantinställningar](/cells/sv/python-net/cells-border-settings/)
- [Ställa in villkorlig formatering av Excel och ODS-filer.](/cells/sv/python-net/conditional-formatting/)
- [Excel-teman och färger](/cells/sv/python-net/excel-themes-and-colors/)
- [Fyllinställningar](/cells/sv/python-net/cells-fill-settings/)
- [Typsnittinställningar](/cells/sv/python-net/cells-font-settings/)
- [Formatera kalkylbladsceller i en arbetsbok](/cells/sv/python-net/format-worksheet-cells-in-a-workbook/)
- [Implementera 1904 Datasystem](/cells/sv/python-net/implement-1904-date-system/)
- [Sammanfoga och dela upp celler](/cells/sv/python-net/merging-and-unmerging-cells/)
- [Antalseinställningar](/cells/sv/python-net/cells-number-settings/)
- [Hämta och ange stil för celler](/cells/sv/python-net/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

