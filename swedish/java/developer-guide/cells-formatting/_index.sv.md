---
title: Cellers format
type: docs
weight: 100
url: /sv/java/cells-formatting/
---

## **Lägga till ramar till celler**
Microsoft Excel låter användare formatera celler genom att lägga till ramar.

**Ramarinställningar i Microsoft Excel** 

![todo:image_alt_text](cells-formatting_1.png)

Ramentypen beror på var den läggs till. Till exempel är en översta kant en som läggs till överst i en cell. Användare kan också ändra ramar linjestil och färg.

Med Aspose.Cells kan utvecklare lägga till ramar och anpassa hur de ser ut på samma flexibla sätt de kan i Microsoft Excel.
### **Lägga till ramar till celler**
Aspose.Cells tillhandahåller en klass, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) som representerar en Microsoft Excel-fil. [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)-klassen innehåller en [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) som möjliggör åtkomst till varje arbetsblad i Excel-filen. Ett arbetsblad representeras av [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)-klassen. [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)-klassen tillhandahåller en [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-samling. Varje objekt i [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-samlingen representerar en [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)-klass.

Aspose.Cells tillhandahåller metoden [setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)) i [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)-klassen som används för att ställa in en cells formateringsstil. Även [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style)-klassens objekt används och tillhandahåller egenskaper för att konfigurera typsnittinställningar.
#### **Lägga till ramar till en cell**
Lägg till ramar till en cell med [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style)-objektets [setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\)) metod. Ramtypen skickas som en parameter. Alla ramtyper är fördefinierade i [BorderType](https://reference.aspose.com/cells/java/com.aspose.cells/BorderType)-enumet.

|**Ramtyper**|**Beskrivning**|
| :- | :- |
|[BOTTOM_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#BOTTOM_BORDER)|Den undre kantlinjen|
|[DIAGONAL_DOWN](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL_DOWN)|En diagonal linje från övre vänster till höger nedre|
|[DIAGONAL_UP](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL_UP)|En diagonal linje från nedre vänster till höger upp|
|[LEFT_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#LEFT_BORDER)|Vänster kantlinje|
|[RIGHT_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#RIGHT_BORDER)|Höger kantlinje|
|[TOP_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#TOP_BORDER)|Övre kantlinje|
|[HORIZONTAL](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#HORIZONTAL)|Endast för dynamisk stil, såsom villkorlig formatering.|
|[VERTICAL](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#VERTICAL)|Endast för dynamisk stil, såsom villkorlig formatering.|
För att ställa in linjefärg, välj en färg med hjälp av [Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color)-enumet och skicka den till [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style)-objektets [setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\)) metods Color-parameter. Linjestilar är fördefinierade i [CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType)-enumet.

|**Linjestilar**|**Beskrivning**|
| :- | :- |
|[DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH_DOT)|Representerar tunn sträck-priklina|
|[DASH_DOT_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH_DOT_DOT)|Representerar tunn sträck-prick-priklina|
|[DASHED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASHED)|Representerar streckad linje|
|[DOTTED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOTTED)|Representerar prickad linje|
|[DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOUBLE)|Representerar dubbel linje|
|[HAIR](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#HAIR)|Representerar hårlinje|
|[MEDIUM_DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASH_DOT)|Representerar medium prickad linje|
|[MEDIUM_DASH_DOT_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASH_DOT_DOT)|Representerar medium punkt-streckad punktad linje|
|[MEDIUM_DASHED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASHED)|Representerar medium streckad linje|
|[NONE](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#NONE)|Representerar ingen linje|
|[MEDIUM](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM)|Representerar medium linje|
|[SLANTED_DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#SLANTED_DASH_DOT)|Representerar sned medium prickad linje|
|[THICK](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THICK)|Representerar tjock linje|
|[THIN](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THIN)|Representerar tunn linje|
Välj en av ovanstående linjestilar och tilldela den sedan till [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) objektets [setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\)) metod.

Följande utdata genereras när koden nedan körs.

**Gränser applicerade på samtliga sidor av en cell** 

![todo:image_alt_text](cells-formatting_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBordersToCells-AddingBordersToCells.java" >}}
#### **Lägga till Gränser till en Rad av Celler**
Det är möjligt att lägga till gränser till en rad av celler istället för bara en enskild cell. Först skapar du en rad av celler genom att anropa [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) kollektionens [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\)) metod, som tar följande parametrar:

- **Första Rad**, den första raden av intervallet.
- **Första Kolumn**, den första kolumnen av intervallet.
- **Antal Rader**, antalet rader i intervallet.
- **Antal Kolumner**, antalet kolumner i intervallet.

Metoden [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\)) returnerar en [Range](https://reference.aspose.com/cells/java/com.aspose.cells/Range) objekt, som innehåller det angivna intervallet. [Range](https://reference.aspose.com/cells/java/com.aspose.cells/Range) objektet tillhandahåller en [setOutlineBorders](https://reference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders\(int,%20com.aspose.cells.Color\)) metod som tar följande parametrar:

- **CellBorderType**, linjestilen för gränslinjen, vald från [CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType) uppräkningen.
- **Färg**, linjefärg, vald från [Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color) uppräkningen.

Följande utdata genereras när koden nedan körs.

**Gränser applicerade på en rad av celler** 

![todo:image_alt_text](cells-formatting_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBorderstoRange-AddingBorderstoRange.java" >}}
## **Färger och Palett**
En palett är antalet färger som är tillgängliga för att skapa en bild. Användningen av en standardiserad palett i en presentation gör att användaren kan skapa en enhetlig look. Varje Microsoft Excel (97-2003) fil har en palett med 56 färger som kan tillämpas på celler, teckensnitt, rutnät, grafiska objekt, fyllningar och linjer i en graf.

**Palettinställningar i Microsoft Excel** 

![todo:image_alt_text](cells-formatting_4.png)

Med Aspose.Cells är det inte bara möjligt att använda befintliga färger, utan också anpassade färger. Innan du använder en anpassad färg, lägg till den i paletten. Detta ämne förklarar hur du lägger till anpassade färger i paletten.
### **Lägga till Anpassade Färger i Paletten**
Aspose.Cells stöder också en palett med 56 färger. En standard färgpalett visas ovan. Om du vill använda en anpassad färg som inte är definierad i paletten måste du lägga till den färgen i paletten innan du använder den.

{{% alert color="primary" %}} 

Paletten håller endast 56 färger. När du lägger till en anpassad färg i paletten ändras paletten och vilket element som helst i filen som formaterats med den tidigare färgen ändras. Så, när du ändrar paletten, var mycket försiktig. Dessutom är detta begränsningen endast i XLS (Excel 97 - 2003) filformat eftersom det inte finns någon sådan begränsning för XLSX eller andra avancerade MS Excel (2007/2010) filformat.

{{% /alert %}} 

Aspose.Cells tillhandahåller en klass, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), som representerar en Microsoft Excel-fil. Klassen tillhandahåller metoden [changePalette](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#changePalette\(com.aspose.cells.Color,%20int\)) som tar följande parametrar för att lägga till en anpassad färg för att modifiera paletten:

- **Anpassad färg**, den anpassade färgen som ska läggas till paletten.
- **Index**, index för färgen som kommer att ersättas med den anpassade färgen. Ska vara mellan 0-55.

Exemplet nedan lägger till en anpassad färg i paletten innan den tillämpas på en font.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ColorsAndPalette-ColorsAndPalette.java" >}}
## **Färger och bakgrundsmönster**
Microsoft Excel kan ange cellernas förgrund (omriss) och bakgrundsfärger samt bakgrundsmönster enligt nedan.

**Ange färger och bakgrundsmönster i Microsoft Excel** 

![todo:image_alt_text](cells-formatting_5.png)

Aspose.Cells stöder även dessa funktioner på ett flexibelt sätt. I det här avsnittet lär vi oss att använda dessa funktioner med hjälp av Aspose.Cells.
### **Ange färger & bakgrundsmönster**
Aspose.Cells tillhandahåller en klass, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), som representerar en Microsoft Excel-fil. Klassen [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) innehåller en [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) som tillåter åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av klassen [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). Klassen [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) tillhandahåller en [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-samling. Varje objekt i [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-samlingen representerar ett objekt av klassen [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell).

Aspose.Cells tillhandahåller metoden [setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)) i klassen [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) som används för att ange en cells formatering. Dessutom kan objektet av klassen [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) användas för att konfigurera teckensnittsinställningar.

{{% alert color="primary" %}} 

För att ange cellens förgrundsfärg eller bakgrundsfärg, använd objektets [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) [setBackgroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor)- eller [setForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor)-egenskaper. Dessa egenskaper träder endast i kraft om objektets [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) [setPattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern)-egenskap är konfigurerad.

{{% /alert %}} 

Egenskapen [setForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) anger cellens nyansfärg.

Egenskapen [setPattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) specifierar bakgrundsmönstret som används för förgrundsfärgen eller bakgrundsfärgen. Aspose.Cells tillhandahåller [BackgroundType](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType)-uppräkningen som innehåller en rad fördefinierade typer av bakgrundsmönster.

|**Mönstertyp**|**Beskrivning**|
| :- | :- |
|[DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL_CROSSHATCH)|Representerar diagonal krysstackmönster|
|[DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL_STRIPE)|Representerar diagonalt randigt mönster|
|[GRAY_6](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_6)|Representerar 6,25% grått mönster|
|[GRAY_12](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_12)|Representerar 12,5% grått mönster|
|[GRAY_25](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_25)|Representerar 25% grått mönster|
|[GRAY_50](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_50)|Representerar 50% grått mönster|
|[GRAY_75](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_75)|Representerar 75% grått mönster|
|[HORIZONTAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#HORIZONTAL_STRIPE)|Representerar horisontellt randigt mönster|
|[NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE)|Representerar ingen bakgrund|
|[REVERSE_DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#REVERSE_DIAGONAL_STRIPE)|Representerar omvänt diagonalt randigt mönster|
|[SOLID](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID)|Representerar enfärgat mönster|
|[THICK_DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THICK_DIAGONAL_CROSSHATCH)|Representerar tjockt diagonalt krysstackmönster|
|[THIN_DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_DIAGONAL_CROSSHATCH)|Representerar tunt diagonalt krysstackmönster|
|[THIN_DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_DIAGONAL_STRIPE)|Representerar tunt diagonalt randigt mönster|
|[THIN_HORIZONTAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_HORIZONTAL_CROSSHATCH)|Representerar tunt horisontellt krysstackmönster|
|[THIN_HORIZONTAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_HORIZONTAL_STRIPE)|Representerar tunn horisontell randig mönster|
|[THIN_REVERSE_DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_REVERSE_DIAGONAL_STRIPE)|Representerar tunn omvänd diagonal randigt mönster|
|[THIN_VERTICAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_VERTICAL_STRIPE)|Representerar tunn vertikal randigt mönster|
|[VERTICAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#VERTICAL_STRIPE)|Representerar vertikal randigt mönster|
I exemplet nedan är förgrundsfärgen för cellen A1 inställd men A2 är konfigurerad för att ha både förgrund och bakgrundsfärger med ett bakgrundsmönster med vertikal rand.

Följande utdata genereras vid körning av koden.

**Förgrund och bakgrundsfärger applicerade på celler med bakgrundsmönster** 

![todo:image_alt_text](cells-formatting_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ColorsAndBackground-ColorsAndBackground.java" >}}
### **Viktigt att veta**
{{% alert color="primary" %}} 

- För att ställa in en cells förgrund eller bakgrundsfärg, använd [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style)-objektets [ForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) eller [BackgroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor) egenskaper. Båda egenskaperna kommer att träda i kraft endast om [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style)-objektets [Pattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) egenskap är konfigurerad.
- Egenskapen [ForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) ställer in cellens nyansfärg.
  Egenskapen [Pattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) specifierar typ av bakgrundsmönster som används för förgrund eller bakgrundsfärg. Aspose.Cells tillhandahåller en uppräkning, [BackgroundType](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType), som innehåller en uppsättning fördefinierade typer av bakgrundsmönster.
- Om du väljer [BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE) värde från [BackgroundType](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType)-uppräkningen, tillämpas inte förgrundsfärgen.
  På samma sätt tillämpas inte bakgrundsfärgen om du väljer värdena [BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE) eller [BackgroundType.SOLID](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID).
- När du hämtar cellers skugg/fyllfärg, om [Style.Pattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) är [BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE), kommer [Style.ForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) att returnera *Color.Empty*.

{{% /alert %}} 
## **Formatera valda tecken i en cell**
[Hantering av typsnittsinställningar](/cells/sv/java/dealing-with-font-settings) förklarade hur man formaterar celler men bara hur man formaterar innehållet i hela cellerna. Vad gör du om du vill formatera endast valda tecken?

Aspose.Cells stöder denna funktion. Detta ämne förklarar hur man använder denna funktion.
### **Formatera valda tecken**
Aspose.Cells tillhandahåller en klass, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), som representerar en Microsoft Excel-fil. Klassen [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) innehåller en [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) som tillåter åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av klassen [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). Klassen [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) tillhandahåller en [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-samling. Varje objekt i [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-samlingen representerar ett objekt av klassen [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell).

Klassen [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) tillhandahåller en [characters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#characters(int,%20int)) metoden som tar följande parametrar för att välja en rad tecken i en cell:

- **Startindex**, index för tecknet att börja urvalet från.
- **Antal tecken**, antalet tecken att välja.

I utdatafilen, i cellen A1, är ordet 'Visit' formaterat med standardtypsnittet men 'Aspose!' är fett och blått.

**Formatering av valda tecken** 

![todo:image_alt_text](cells-formatting_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}

{{% alert color="primary" %}} 

Om du är intresserad av [formatering av en del av Rich-text i en cell](/cells/sv/java/access-and-update-the-portions-of-rich-text-of-cell), överväg att använda [Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters\(\)) & Cell.setCharacters metoder. [Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters\(\)) metoden används för att få tillgång till textens delar och sedan kan ändringar göras med hjälp av Cell.setCharacters metoden medan **get** metoden returnera en matris av [FontSetting](https://reference.aspose.com/cells/java/com.aspose.cells/FontSetting) objekt som kan manipuleras för att ställa in olika egenskaper som teckensnitts namn, teckenfärg, fetstil osv och **set** metoden kan användas för att tillämpa ändringarna.

{{% /alert %}}

## **Fortsatta ämnen**
- [Justering inställningar](/cells/sv/java/cells-alignment-settings/)
- [Villkorlig formatering](/cells/sv/java/conditional-formatting/)
- [Dataformatering](/cells/sv/java/data-formatting/)
- [Excel-teman och färger](/cells/sv/java/excel-2007-themes-and-colors/)
- [Hantera teckensnittsinställningar](/cells/sv/java/dealing-with-font-settings/)
- [Formatera kalkylbladsceller i en arbetsbok](/cells/sv/java/format-worksheet-cells-in-a-workbook/)
- [Implementera 1904 Datasystem](/cells/sv/java/implement-1904-date-system/)
- [Sammanfoga och dela upp celler](/cells/sv/java/merging-and-unmerging-cells/)
- [Antalseinställningar](/cells/sv/java/cells-number-settings/)
- [Bevara enskild citattecken prefiks av cellvärde eller område](/cells/sv/java/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Styling och dataformatering](/cells/sv/java/styling-and-data-formatting/)
