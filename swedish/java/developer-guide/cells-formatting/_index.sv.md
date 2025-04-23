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

Aspose.Cells erbjuder metoden [setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle-com.aspose.cells.Style-) i [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)-klassen som används för att ställa in cellens formateringsstil. Objektet av [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) är också användbart och tillhandahåller egenskaper för att konfigurera teckensnitt.
#### **Lägga till ramar till en cell**
Lägg till ramar till en cell med [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style)s [setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder-int-int-com.aspose.cells.Color-) metod. Randtypen anges som en parameter. Alla randtyper är fördefinierade i [BorderType](https://reference.aspose.com/cells/java/com.aspose.cells/BorderType).

|**Ramtyper**|**Beskrivning**|
| :- | :- |
|[BOTTOM_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#BOTTOM-BORDER)|Den nedre randlinjen|
|[DIAGONAL_DOWN](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL-DOWN)|En diagonal linje från övre vänstra till nedre högra|
|[DIAGONAL_UP](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL-UP)|En diagonal linje från nedre vänstra till övre högra|
|[LEFT_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#LEFT-BORDER)|Vänster randlinje|
|[RIGHT_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#RIGHT-BORDER)|Höger randlinje|
|[TOP_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#TOP-BORDER)|Övre randlinje|
|[HORIZONTAL](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#HORIZONTAL)|Endast för dynamisk stil, såsom villkorlig formatering.|
|[VERTICAL](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#VERTICAL)|Endast för dynamisk stil, såsom villkorlig formatering.|
För att ställa in linjefärgen, välj en färg med [Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color)-enumerationen och skicka den till [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style)-objektets [setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder-int-int-com.aspose.cells.Color-) metods Color-parameter. Linjestilar är fördefinierade i [CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType).

|**Linjestilar**|**Beskrivning**|
| :- | :- |
|[DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH-DOT)|Visar en tunn streck-punkt-linje|
|[DASH_DOT_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH-DOT_DOT)|Visar en tunn streck-punkt-streck-linje|
|[DASHED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASHED)|Representerar streckad linje|
|[DOTTED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOTTED)|Representerar prickad linje|
|[DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOUBLE)|Representerar dubbel linje|
|[HAIR](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#HAIR)|Representerar hårlinje|
|[MEDIUM_DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM-DASH-DOT)|Visar en medium streck-punkt-linje|
|[MEDIUM_DASH_DOT_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM-DASH-DOT_DOT)|Representation av medium streck-punkt-punkt-linje|
|[MEDIUM_DASHED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM-DASHED)|Representation av medium streckad linje|
|[NONE](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#NONE)|Representerar ingen linje|
|[MEDIUM](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM)|Representerar medium linje|
|[SLANTED_DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#SLANTED-DASH-DOT)|Representation av snett medium streck-punkt-punkt-linje|
|[THICK](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THICK)|Representerar tjock linje|
|[THIN](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THIN)|Representerar tunn linje|
Välj en av ovanstående linjestilar och tilldela den sedan till metoden [setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder-int-int-com.aspose.cells.Color-) för [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style)-objektet.

Följande utdata genereras när koden nedan körs.

**Gränser applicerade på samtliga sidor av en cell** 

![todo:image_alt_text](cells-formatting_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBordersToCells-AddingBordersToCells.java" >}}
#### **Lägga till Gränser till en Rad av Celler**
Det är möjligt att lägga till ramar till ett cellområde istället för en enskild cell. Först, skapa ett cellområde genom att anropa metoden [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange-int-int-boolean-) för samlingen [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), som tar följande parametrar:

- **Första Rad**, den första raden av intervallet.
- **Första Kolumn**, den första kolumnen av intervallet.
- **Antal Rader**, antalet rader i intervallet.
- **Antal Kolumner**, antalet kolumner i intervallet.

Metoden [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange-int-int-boolean-) returnerar ett [Range](https://reference.aspose.com/cells/java/com.aspose.cells/Range) objekt, som innehåller det angivna området. [Range](https://reference.aspose.com/cells/java/com.aspose.cells/Range) objektet tillhandahåller en [setOutlineBorders](https://reference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders-int-com.aspose.cells.Color-) metod som tar följande parametrar:

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

Aspose.Cells tillhandahåller en klass, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), som representerar en Microsoft Excel-fil. Klassen tillhandahåller metoden [changePalette](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#changePalette-com.aspose.cells.Color-int-) som tar följande parametrar för att lägga till en anpassad färg för att ändra paletten:

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

Aspose.Cells tillhandahåller metoden [setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle-com.aspose.cells.Style-) i [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)-klassen som används för att ange cellens formatering. Dessutom kan objektet av klassen [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) användas för att konfigurera teckensnittinställningar.

{{% alert color="primary" %}} 

För att ange cellens förgrundsfärg eller bakgrundsfärg, använd objektets [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) [setBackgroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor)- eller [setForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor)-egenskaper. Dessa egenskaper träder endast i kraft om objektets [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) [setPattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern)-egenskap är konfigurerad.

{{% /alert %}} 

Egenskapen [setForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) anger cellens nyansfärg.

Egenskapen [setPattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) specifierar bakgrundsmönstret som används för förgrundsfärgen eller bakgrundsfärgen. Aspose.Cells tillhandahåller [BackgroundType](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType)-uppräkningen som innehåller en rad fördefinierade typer av bakgrundsmönster.

|**Mönstertyp**|**Beskrivning**|
| :- | :- |
|[DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL-CROSSHATCH)|Representation av diagonal korsmönster|
|[DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL-STRIPE)|Representation av diagonal randmönster|
|[GRAY_6](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY-6)|Representation av 6,25% grått mönster|
|[GRAY_12](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY-12)|Representation av 12,5% grått mönster|
|[GRAY_25](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY-25)|Representation av 25% grått mönster|
|[GRAY_50](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY-50)|Representation av 50% grått mönster|
|[GRAY_75](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY-75)|Representation av 75% grått mönster|
|[HORIZONTAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#HORIZONTAL-STRIPE)|Representation av horisontellt randmönster|
|[NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE)|Representerar ingen bakgrund|
|[REVERSE_DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#REVERSE-DIAGONAL-STRIPE)|Representation av omvänt diagonal randmönster|
|[SOLID](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID)|Representerar enfärgat mönster|
|[THICK_DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THICK-DIAGONAL-CROSSHATCH)|Representation av tjockt diagonal korshönster|
|[THIN_DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN-DIAGONAL-CROSSHATCH)|Representation av tunt diagonalt korshönster|
|[THIN_DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN-DIAGONAL-STRIPE)|Representation av tunt diagonalt randmönster|
|[THIN_HORIZONTAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN-HORIZONTAL-CROSSHATCH)|Representation av tunt horisontellt korshönster|
|[THIN_HORIZONTAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN-HORIZONTAL-STRIPE)|Representation av tunt horisontellt randmönster|
|[THIN_REVERSE_DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN-REVERSE-DIAGONAL-STRIPE)|Representation av tunt omvänt diagonalt randmönster|
|[THIN_VERTICAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN-VERTICAL-STRIPE)|Representation av tunt vertikal randmönster|
|[VERTICAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#VERTICAL-STRIPE)|Representation av vertikal randmönster|
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

[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)-klassen tillhandahåller metoden [characters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#characters-int-int-) som tar följande parametrar för att välja ett teckenområde i en cell:

- **Startindex**, index för tecknet att börja urvalet från.
- **Antal tecken**, antalet tecken att välja.

I utdatafilen, i cellen A1, är ordet 'Visit' formaterat med standardtypsnittet men 'Aspose!' är fett och blått.

**Formatering av valda tecken** 

![todo:image_alt_text](cells-formatting_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}

{{% alert color="primary" %}} 

Om du är intresserad av [formatering av en del av rik text i en cell](/cells/sv/java/access-and-update-the-portions-of-rich-text-of-cell/), bör du använda metoderna [Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters--) och Cell.setCharacters. Metoden [Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters--) används för att få åtkomst till delar av texten och sedan kan ändringar göras med metoden Cell.setCharacters, medan **get**-metoden returnerar en array av [FontSetting](https://reference.aspose.com/cells/java/com.aspose.cells/FontSetting)-objekt som kan manipuleras för att ställa in olika egenskaper som teckensnamsval, teckenfärg, fetstil, etc., och **set**-metoden kan användas för att tillämpa ändringarna.

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
{{< app/cells/assistant language="java" >}}
