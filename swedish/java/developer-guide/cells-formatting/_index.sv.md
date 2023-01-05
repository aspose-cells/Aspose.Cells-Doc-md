---
title: Cells Format
type: docs
weight: 100
url: /sv/java/cells-formatting/
---
## **Lägger till gränser till Cells**
Microsoft Excel tillåter användare att formatera celler genom att lägga till kanter.

**Kantinställningar i Microsoft Excel** 

![todo:image_alt_text](cells-formatting_1.png)

Typen av bård beror på var den läggs till. Till exempel är en övre kant en som läggs till den översta positionen i en cell. Användare kan också ändra gränsernas linjestil och färg.

Med Aspose.Cells kan utvecklare lägga till ramar och anpassa hur de ser ut på samma flexibla sätt som de kan i Microsoft Excel.
### **Lägger till gränser till Cells**
 Aspose.Cells tillhandahåller en klass,[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) som representerar en Microsoft Excel-fil. De[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) klass innehåller en[Arbetsbladssamling](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)som ger åtkomst till varje kalkylblad i Excel-filen. Ett arbetsblad representeras av[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) klass. De[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) klass ger en[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samling. Varje objekt i[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samlingen representerar ett föremål för[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)klass.

 Aspose.Cells tillhandahåller[setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\) ) metod i[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) klass som används för att ställa in en cells formateringsstil. Också föremålet för[Stil](https://reference.aspose.com/cells/java/com.aspose.cells/Style)klass används och ger egenskaper för att konfigurera teckensnittsinställningar.
#### **Lägger till gränser till en Cell**
 Lägg till kanter till en cell med[Stil](https://reference.aspose.com/cells/java/com.aspose.cells/Style) föremål[setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\) ) metod. Gränstypen skickas som en parameter. Alla kanttyper är fördefinierade i[BorderType](https://reference.aspose.com/cells/java/com.aspose.cells/BorderType)uppräkning.

|**Kanttyper**|**Beskrivning**|
|:- |:- |
|[BOTTOM_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#BOTTOM_BORDER)|Den nedre gränslinjen|
|[DIAGONAL_DOWN](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL_DOWN)|En diagonal linje från övre vänster till höger botten|
|[DIAGONAL_UP](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL_UP)|En diagonal linje från nedre vänster till höger upptill|
|[LEFT_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#LEFT_BORDER)|Den vänstra gränslinjen|
|[RIGHT_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#RIGHT_BORDER)|Den högra gränslinjen|
|[TOP_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#TOP_BORDER)|Den övre gränslinjen|
|[HORISONTELL](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#HORIZONTAL)|Endast för dynamisk stil, till exempel villkorlig formatering.|
|[VERTIKAL](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#VERTICAL)|Endast för dynamisk stil, till exempel villkorlig formatering.|
 För att ställa in linjefärgen, välj en färg med hjälp av[Färg](https://reference.aspose.com/cells/java/com.aspose.cells/Color) uppräkning och skicka den till[Stil](https://reference.aspose.com/cells/java/com.aspose.cells/Style) föremål[setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\) ) metodens färgparameter. Linjestilarna är fördefinierade i[CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType)uppräkning.

|**Linjestilar**|**Beskrivning**|
|:- |:- |
|[DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH_DOT)|Representerar en tunn streckad linje|
|[RUSA_PUNKT_PUNKT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH_DOT_DOT)|Representerar en tunn streckprickad linje|
|[STRÄCKAD](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASHED)|Representerar en streckad linje|
|[PRICKAD](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOTTED)|Representerar en prickad linje|
|[DUBBEL](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOUBLE)|Representerar dubbel linje|
|[HÅR](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#HAIR)|Representerar hårlinje|
|[MEDIUM_RUSA_PUNKT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASH_DOT)|Representerar medelhög streckad linje|
|[MEDIUM_RUSA_DOT_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASH_DOT_DOT)|Representerar medelstor streckprickad linje|
|[MEDIUM_DASHED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASHED)|Representerar medelstreckad linje|
|[INGEN](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#NONE)|Representerar ingen linje|
|[MEDIUM](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM)|Representerar medium linje|
|[SLUTA_RUSA_PUNKT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#SLANTED_DASH_DOT)|Representerar en lutande medelhög streckad linje|
|[TJOCK](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THICK)|Representerar tjock linje|
|[TUNN](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THIN)|Representerar tunn linje|
 Välj en av ovanstående linjestilar och tilldela den sedan till[Stil](https://reference.aspose.com/cells/java/com.aspose.cells/Style)föremål[setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\)) metod.

Följande utdata genereras när koden nedan exekveras.

**Kanter applicerade på alla sidor av en cell** 

![todo:image_alt_text](cells-formatting_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBordersToCells-AddingBordersToCells.java" >}}
#### **Lägger till gränser till ett intervall på Cells**
 Det är möjligt att lägga till gränser till ett cellintervall snarare än bara en enskild cell. Skapa först ett cellområde genom att anropa[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samlingens[skapa Range](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\)) metod, som tar följande parametrar:

- **Första raden**, den första raden i intervallet.
- **Första kolumnen**, den första kolumnen i intervallet.
- **Antal rader**, antalet rader i intervallet.
- **Antal kolumner**, antalet kolumner i intervallet.

 De[skapa Range](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\) ) metod returnerar en[Räckvidd](https://reference.aspose.com/cells/java/com.aspose.cells/Range) objekt, som innehåller det angivna intervallet. De[Räckvidd](https://reference.aspose.com/cells/java/com.aspose.cells/Range) objekt ger en[setOutlineBorders](https://reference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders\(int,%20com.aspose.cells.Color\)) metod som tar följande parametrar:

- **CellBorderType**, kantlinjestilen, vald från[CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType)uppräkning.
- **Färg**, kantlinjefärgen, vald från[Färg](https://reference.aspose.com/cells/java/com.aspose.cells/Color)uppräkning.

Följande utdata genereras när koden nedan exekveras.

**Kanter tillämpas på en rad celler** 

![todo:image_alt_text](cells-formatting_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBorderstoRange-AddingBorderstoRange.java" >}}
## **Färger och palett**
En palett är antalet tillgängliga färger för att skapa en bild. Användningen av en standardiserad palett i en presentation gör att användaren kan skapa ett konsekvent utseende. Varje Microsoft Excel-fil (97-2003) har en palett med 56 färger som kan appliceras på celler, teckensnitt, rutnät, grafiska objekt, fyllningar och linjer i ett diagram.

**Palettinställningar i Microsoft Excel** 

![todo:image_alt_text](cells-formatting_4.png)

Med Aspose.Cells är det inte bara möjligt att använda befintliga färger utan även anpassade färger. Innan du använder en anpassad färg, lägg till den i paletten. Det här avsnittet förklarar hur du lägger till anpassade färger till paletten.
### **Lägga till anpassade färger till paletten**
Aspose.Cells stöder också en palett med 56 färger. En standardfärgpalett visas ovan. Om du vill använda en anpassad färg som inte är definierad i paletten måste du lägga till den färgen i paletten före användning.

{{% alert color="primary" %}} 

Paletten rymmer endast 56 färger. När du lägger till en anpassad färg till paletten ändras paletten och alla element i filen som formaterats med föregående färg ändras. Så var mycket försiktig när du ändrar paletten. Dessutom är detta endast begränsningen i filformatet XLS (Excel 97 - 2003), eftersom det inte finns någon sådan begränsning för XLSX eller andra avancerade MS Excel (2007/2010) filformat.

{{% /alert %}} 

Aspose.Cells tillhandahåller en klass,[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), som representerar en Microsoft Excel-fil. Klassen tillhandahåller[ändra palett](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#changePalette\(com.aspose.cells.Color,%20int\)) metod som tar följande parametrar för att lägga till en anpassad färg för att ändra paletten:

- **Anpassad färg**, den anpassade färgen som ska läggas till i paletten.
- **Index**, indexet för färgen som kommer att ersättas med den anpassade färgen. Bör vara mellan 0-55.

Exemplet nedan lägger till en anpassad färg till paletten innan den appliceras på ett teckensnitt.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ColorsAndPalette-ColorsAndPalette.java" >}}
## **Färger och bakgrundsmönster**
Microsoft Excel kan ställa in förgrunds- (kontur) och bakgrunds- (fyll) färger för celler och bakgrundsmönster som visas nedan.

**Ställa in färger och bakgrundsmönster i Microsoft Excel** 

![todo:image_alt_text](cells-formatting_5.png)

Aspose.Cells stöder även dessa funktioner på ett flexibelt sätt. I det här ämnet lär vi oss att använda dessa funktioner med Aspose.Cells.
### **Ställa in färger och bakgrundsmönster**
Aspose.Cells tillhandahåller en klass,[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), som representerar en Microsoft Excel-fil. De[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)klass innehåller en[Arbetsbladssamling](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)som ger åtkomst till varje kalkylblad i Excel-filen. Ett arbetsblad representeras av[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)klass. De[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)klass ger en[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)samling. Varje objekt i[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)samlingen representerar ett föremål för[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)klass.

Aspose.Cells tillhandahåller[setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)) metod i[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)klass som används för att ställa in en cells formatering. Också föremålet för[Stil](https://reference.aspose.com/cells/java/com.aspose.cells/Style)klass kan användas för att konfigurera teckensnittsinställningar.

{{% alert color="primary" %}} 

 För att ställa in förgrunds- eller bakgrundsfärgen för en cell, använd[Stil](https://reference.aspose.com/cells/java/com.aspose.cells/Style) föremål[setBakgrundsfärg](https://reference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor) eller[setForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) egenskaper. Dessa egenskaper träder i kraft endast om[Stil](https://reference.aspose.com/cells/java/com.aspose.cells/Style) föremål[setPattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) egenskapen är konfigurerad.

{{% /alert %}} 

De[setForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor)egenskapen ställer in cellens skuggfärg.

De[setPattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) egenskapen anger bakgrundsmönster som används för förgrunden eller bakgrundsfärgen. Aspose.Cells tillhandahåller[Bakgrundstyp](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType)uppräkning som innehåller en uppsättning fördefinierade typer av bakgrundsmönster.

|**mönstertyp**|**Beskrivning**|
|:- |:- |
|[DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL_CROSSHATCH)|Representerar diagonalt rutmönster|
|[DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL_STRIPE)|Representerar diagonalt randmönster|
|[GRÅ_6](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_6)|Representerar 6,25 % grått mönster|
|[GRÅ_12](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_12)|Representerar 12,5 % grått mönster|
|[GRÅ_25](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_25)|Representerar 25 % grått mönster|
|[GRÅ_50](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_50)|Representerar 50 % grått mönster|
|[GRÅ_75](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_75)|Representerar 75 % grått mönster|
|[HORIZONTAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#HORIZONTAL_STRIPE)|Representerar horisontellt randmönster|
|[INGEN](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE)|Representerar ingen bakgrund|
|[OMVÄND_DIAGONAL_RAND](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#REVERSE_DIAGONAL_STRIPE)|Representerar omvänt diagonalt randmönster|
|[FAST](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID)|Representerar ett fast mönster|
|[TJOCK_DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THICK_DIAGONAL_CROSSHATCH)|Representerar ett tjockt diagonalt rutmönster|
|[TUNN_DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_DIAGONAL_CROSSHATCH)|Representerar ett tunt diagonalt streckmönster|
|[TUNN_DIAGONAL_RAND](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_DIAGONAL_STRIPE)|Representerar ett tunt diagonalt randmönster|
|[TUNN_HORISONTELL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_HORIZONTAL_CROSSHATCH)|Representerar ett tunt horisontellt streckmönster|
|[TUNN_HORISONTELL_RAND](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_HORIZONTAL_STRIPE)|Representerar ett tunt horisontellt randmönster|
|[TUNN_OMVÄND_DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_REVERSE_DIAGONAL_STRIPE)|Representerar ett tunt omvänt diagonalt randmönster|
|[TUNN_VERTIKAL_RAND](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_VERTICAL_STRIPE)|Representerar ett tunt vertikalt randmönster|
|[VERTICAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#VERTICAL_STRIPE)|Representerar vertikalt randmönster|
I exemplet nedan är förgrundsfärgen för A1-cellen inställd men A2 är konfigurerad att ha både förgrunds- och bakgrundsfärger med ett vertikalt randmönster.

Följande utdata genereras när koden exekveras.

**Förgrunds- och bakgrundsfärger applicerade på celler med bakgrundsmönster** 

![todo:image_alt_text](cells-formatting_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ColorsAndBackground-ColorsAndBackground.java" >}}
### **Viktigt att veta**
{{% alert color="primary" %}} 

-  För att ställa in en cells förgrunds- eller bakgrundsfärg, använd[Stil](https://reference.aspose.com/cells/java/com.aspose.cells/Style) föremål[Förgrundsfärg](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) eller[Bakgrundsfärg](https://reference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor) egenskaper. Båda egenskaperna träder i kraft endast om[Stil](https://reference.aspose.com/cells/java/com.aspose.cells/Style) föremål[Mönster](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) egenskapen är konfigurerad.
-  De[Förgrundsfärg](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) egenskapen anger cellens nyansfärg.
 De[Mönster](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) egenskapen anger typen av bakgrundsmönster som används för förgrunden eller bakgrundsfärgen. Aspose.Cells tillhandahåller en uppräkning,[Bakgrundstyp](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType)som innehåller en uppsättning fördefinierade typer av bakgrundsmönster.
-  Om du väljer[BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE) värde från[Bakgrundstyp](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType) uppräkning tillämpas inte förgrundsfärgen.
 På samma sätt tillämpas inte bakgrundsfärgen om du väljer[BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE) eller[BackgroundType.SOLID](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID) värden.
-  Vid hämtning av cellens skuggnings-/fyllningsfärg, om[Stil.mönster](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) är[BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE), [Style.Förgrundsfärg](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) kommer tillbaka*Färg.Tom*.

{{% /alert %}} 
## **Formatera valda tecken i en Cell**
[Hantera teckensnittsinställningar](/cells/sv/java/dealing-with-font-settings/) förklarade hur man formaterar celler men bara hur man formaterar innehållet i hela cellerna. Vad händer om du bara vill formatera valda tecken?

Aspose.Cells stöder den här funktionen. Det här avsnittet förklarar hur du använder den här funktionen.
### **Formatera valda tecken**
Aspose.Cells tillhandahåller en klass,[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), som representerar en Microsoft Excel-fil. De[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)klass innehåller en[Arbetsbladssamling](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)som ger åtkomst till varje kalkylblad i Excel-filen. Ett arbetsblad representeras av[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)klass. De[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)klass ger en[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)samling. Varje objekt i[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)samlingen representerar ett föremål för[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)klass.

De[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) klass ger[tecken](https://reference.aspose.com/cells/java/com.aspose.cells/cell#characters\(int,%20int\)) metod som använder följande parametrar för att välja ett teckenintervall i en cell:

- **Starta index**, indexet för tecknet att starta valet från.
- **Antal tecken**, antalet tecken att välja.

I utdatafilen, i A1"-cellen, är ordet "Besök" formaterat med standardteckensnittet men "Aspose!" är fet och blå.

**Formatera valda tecken** 

![todo:image_alt_text](cells-formatting_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}

{{% alert color="primary" %}} 

 Om du är intresserad av[formatera en del av Rich Text i en cell](/cells/sv/java/access-and-update-the-portions-of-rich-text-of-cell/) , överväg att använda[Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters\(\) ) & Cell.setCharacters metoder. De[Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters\(\) )-metoden ska användas för att komma åt delarna av texten och sedan kan ändringar göras med metoden Cell.setCharacters medan**skaffa sig**metod returnerar en array av[FontSetting](https://reference.aspose.com/cells/java/com.aspose.cells/FontSetting) objekt som kan manipuleras för att ställa in olika egenskaper såsom teckensnittsnamn, teckensnittsfärg, fetstil, etc.**uppsättning** metod kan användas för att tillämpa ändringarna.

{{% /alert %}}

## **Förhandsämnen**
- [Justeringsinställningar](/cells/sv/java/cells-alignment-settings/)
- [Villkorlig formatering](/cells/sv/java/conditional-formatting/)
- [Dataformatering](/cells/sv/java/data-formatting/)
- [Excel-teman och färger](/cells/sv/java/excel-2007-themes-and-colors/)
- [Hantera teckensnittsinställningar](/cells/sv/java/dealing-with-font-settings/)
- [Formatera kalkylblad Cells i en arbetsbok](/cells/sv/java/format-worksheet-cells-in-a-workbook/)
- [Implementera 1904 års datumsystem](/cells/sv/java/implement-1904-date-system/)
- [Sammanfogning och upphävande Cells](/cells/sv/java/merging-and-unmerging-cells/)
- [Nummerinställningar](/cells/sv/java/cells-number-settings/)
- [Bevara enstaka citatprefix för Cell värde eller intervall](/cells/sv/java/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Styling och dataformatering](/cells/sv/java/styling-and-data-formatting/)
