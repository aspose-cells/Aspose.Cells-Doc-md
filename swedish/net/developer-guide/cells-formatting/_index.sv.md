---
title: Formatera celler
linktitle: Formatera celler
type: docs
weight: 120
url: /sv/net/cells-formatting/
description: Ställ in talformat, ram och bakgrundsfärg för Excel-filer på .NET Framework, .NET Core, Mono eller Xamarin-plattformar.
---
## **Introduktion**

{{% alert color="primary" %}}

 Aspose.Cells tillhandahåller[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) och[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) metoder för[Cell](https://reference.aspose.com/cells/net/aspose.cells/cell) klass, används för att hämta/ställa in formateringsstilen för en cell. Aspose.Cells tillhandahåller också en[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)klass.

{{% /alert %}}

## **Formatera Cells med metoderna GetStyle och SetStyle**

Använd olika typer av formateringsstilar på celler för att ställa in bakgrunds- eller förgrundsfärger, ramar, teckensnitt, horisontella och vertikala justeringar, indragsnivå, textriktning, rotationsvinkel och mycket mer.

### **Använda metoderna GetStyle och SetStyle**

 Om utvecklare behöver tillämpa olika formateringsstilar på olika celler är det bättre att skaffa[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) av cellen som använder[**Cell.GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) metod, ange stilattributen och tillämpa sedan formateringen med[**Cell.SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle)metod. Ett exempel ges nedan för att demonstrera detta tillvägagångssätt för att tillämpa olika formatering på en cell.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingGetStyleSetStyle-1.cs" >}}

### **Använda stilobjekt för att formatera olika Cells**

 Om utvecklare behöver tillämpa samma formateringsstil på olika celler kan de använda[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) objekt. Följ stegen nedan för att använda[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)objekt:

1.  Lägg till en[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) objekt genom att anropa[**Skapa stil**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle) metod för[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook)klass
1.  Få tillgång till den nyligen tillagda[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)objekt
1.  Ställ in önskade egenskaper/attribut för[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)objekt för att tillämpa önskade formateringsinställningar
1. Tilldela den konfigurerade[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)objekt till dina önskade celler

Detta tillvägagångssätt kan avsevärt förbättra effektiviteten för dina applikationer och spara minne också.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingStyleObject-1.cs" >}}

### **Använda Microsoft Excel 2007 fördefinierade stilar**

Om du behöver använda olika formateringsstilar för Microsoft Excel 2007, tillämpa stilar med Aspose.Cells API. Ett exempel ges nedan för att demonstrera detta tillvägagångssätt för att tillämpa en fördefinierad stil på en cell.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingExcelPredefinedStyles-1.cs" >}}



## **Formatera valda tecken i en Cell**

Att hantera teckensnittsinställningar förklarar hur man formaterar text i celler, men det förklarar bara hur man formaterar allt cellinnehåll. Vad händer om du bara vill formatera valda tecken?

Aspose.Cells stöder också denna funktion. Det här ämnet förklarar hur vi använder den här funktionen effektivt.

### **Formatera valda tecken**

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) som representerar en Microsoft Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass innehåller[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) samling som ger åtkomst till varje kalkylblad i en Excel-fil. Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass. De[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass ger en[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) samling. Varje objekt i[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) samlingen representerar ett föremål för[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)klass.

 De[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)klass ger[**Tecken**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters)metod som använder följande parametrar för att välja ett teckenintervall inuti en cell:

- **Starta index**, indexet för tecknet som valet startar från.
- **Antal tecken**, antalet tecken att välja.

 De[**Tecken**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters) metod returnerar en instans av[**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)klass som tillåter utvecklare att formatera tecknen på samma sätt som de skulle göra en cell som visas nedan i kodexemplet. I utdatafilen, i A1-cellen, kommer ordet 'Besök' att formateras med standardteckensnittet men 'Aspose!' är fet och blå.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormattingSelectedCharacters-1.cs" >}}

{{% alert color="primary" %}}

 Om du är intresserad av att formatera en del av Rich Text i en cell, överväg att använda[**Cell.GetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) & [**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) metoder. De[[**Cell.GetCharacters**]](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) metod ska användas för att komma åt delarna av texten och sedan kan ändringar göras med hjälp av[**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) metoden medan**Skaffa sig**metod returnerar en array av[**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting) objekt som kan manipuleras för att ställa in olika egenskaper såsom teckensnittsnamn, teckensnittsfärg, fetstil, etc. och**Uppsättning** metod kan användas för att tillämpa ändringarna.

{{% /alert %}}

## **Formatera rader och kolumner**

Ibland måste utvecklare använda samma formatering på rader eller kolumner. Att tillämpa formatering på celler en efter en tar ofta längre tid och är ingen bra lösning.
För att lösa detta problem erbjuder Aspose.Cells ett enkelt och snabbt sätt som diskuteras i detalj i den här artikeln.

### **Formatera rader och kolumner**

 Aspose.Cells tillhandahåller en klass, den[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) som representerar en Microsoft Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass innehåller en[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) samling som ger åtkomst till varje kalkylblad i Excel-filen. Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass. De[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass ger en[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) samling. De[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)samling ger en[**Rader**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows)samling.

### **Formatera en rad**

 Varje objekt i[**Rader**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows) samlingen representerar en[**Rad**](https://reference.aspose.com/cells/net/aspose.cells/row) objekt. De[**Rad**](https://reference.aspose.com/cells/net/aspose.cells/row)objekt erbjuder[**ApplyStyle**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle) metod som används för att ställa in radens formatering. För att tillämpa samma formatering på en rad, använd[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)objekt. Stegen nedan visar hur du använder den.

1.  Lägg till en[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) invända mot[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass genom att anropa dess[**Skapa stil**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle)metod.
1.  Ställ in[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)objektets egenskaper för att tillämpa formateringsinställningar.
1.  Gör de relevanta attributen PÅ för[**StilFlagga**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)objekt.
1. Tilldela den konfigurerade[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) invända mot[**Rad**](https://reference.aspose.com/cells/net/aspose.cells/row)objekt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingARow-1.cs" >}}

### **Formatera en kolumn**

 De[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) samling ger också en[**Kolumner**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns) samling. Varje objekt i[**Kolumner**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns) samlingen representerar en[**Kolumn**](https://reference.aspose.com/cells/net/aspose.cells/column) objekt. Liknar en[**Rad**](https://reference.aspose.com/cells/net/aspose.cells/row) objekt, den[**Kolumn**](https://reference.aspose.com/cells/net/aspose.cells/column) objekt erbjuder också[**ApplyStyle**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle)metod för att formatera en kolumn.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingAColumn-1.cs" >}}

## **Förhandsämnen**
- [Justeringsinställningar](/cells/sv/net/cells-alignment-settings/)
- [Kantinställningar](/cells/sv/net/cells-border-settings/)
- [Ställ in villkorliga format för Excel- och ODS-filer.](/cells/sv/net/conditional-formatting/)
- [Excel-teman och färger](/cells/sv/net/excel-themes-and-colors/)
- [Fyll i inställningar](/cells/sv/net/cells-fill-settings/)
- [Teckensnittsinställningar](/cells/sv/net/cells-font-settings/)
- [Formatera kalkylblad Cells i en arbetsbok](/cells/sv/net/format-worksheet-cells-in-a-workbook/)
- [Implementera 1904 års datumsystem](/cells/sv/net/implement-1904-date-system/)
- [Sammanfogning och upphävande Cells](/cells/sv/net/merging-and-unmerging-cells/)
- [Nummerinställningar](/cells/sv/net/cells-number-settings/)
- [Hämta och ställ in stil för celler](/cells/sv/net/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

