---
title: Kantinställningar
description: Hur man använder Aspose.Cells-biblioteket i C# för att ställa in kantstil och färg på celler. Genom att justera kantens bredd, stil och färg har du mer kontroll över hur celler ser ut och visas.
keywords: Aspose.Cells, Cell Border Settings, C#, Border Width, Border Style, Border Color
type: docs
weight: 40
url: /sv/net/cells-border-settings/
---
##  **Lägger till gränser till Cells**

Microsoft Excel tillåter användare att formatera celler genom att lägga till kanter. Typen av bård beror på var den läggs till. Till exempel är en övre kant en som läggs till den översta positionen i en cell. Användare kan också ändra gränsernas linjestil och färg.

Med Aspose.Cells kan utvecklare lägga till ramar och anpassa hur de ser ut på samma flexibla sätt som i Microsoft Excel.

###  **Lägger till gränser till Cells**

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) som representerar en Microsoft Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass innehåller en[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) samling som ger åtkomst till varje kalkylblad i Excel-filen. Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass. De[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass ger[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) samling. Varje objekt i[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) samlingen representerar ett föremål för[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)klass.

 Aspose.Cells tillhandahåller[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index)metod i[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)klass. De[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index)metod används för att ställa in en cells formateringsstil. De[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)klass tillhandahåller egenskaper för att lägga till kanter till celler.

####  **Lägger till gränser till en Cell**

Utvecklare kan lägga till gränser till en cell genom att använda[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) föremål[**Gränser**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) samling. Gränstypen skickas som ett index till[**Gränser**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) samling. Alla kanttyper är fördefinierade i[**BorderType**](https://reference.aspose.com/cells/net/aspose.cells/bordertype) uppräkning.

**Gränsuppräkning**

|**Kanttyper**|**Beskrivning**|
| :- | :- |
|BottomBorder|En nedre kantlinje|
|DiagonalDown|En diagonal linje från övre vänster till höger botten|
|DiagonalUp|En diagonal linje från nedre vänster till höger upptill|
|LeftBorder|En vänster gränslinje|
|RightBorder|En höger gränslinje|
|TopBorder|En övre kantlinje|

De[**Gränser**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders)samling lagrar alla gränser. Varje gräns i[**Gränser**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) samlingen representeras av en[**Gräns**](https://reference.aspose.com/cells/net/aspose.cells/border) objekt som ger två egenskaper,[**Färg**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/color) och[**LineStyle**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle)för att ställa in en kantlinjes färg respektive stil.

För att ställa in en rams linjefärg, välj en färg med färguppräkningen (en del av .NET Framework) och tilldela den till Border-objektets Color-egenskap.

 Ramens linjestil ställs in genom att välja en linjestil från[**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)uppräkning.

**CellBorderType-uppräkning**

|**Linjestilar**|**Beskrivning**|
| :- | :- |
|DashDot|Tunn streckad linje|
|DashDotDot|Tunn streckprickad linje|
|Streckad|Streckad linje|
|Prickad|Prickad linje|
|Dubbel|Dubbel linje|
|Hår|Hårfäste|
|MediumDashDot|Mellanstor streckad linje|
|MediumDashDotDot|Mellanstor streckprickad linje|
|Medelstreckad|Medelstreckad linje|
|Ingen|Ingen linje|
|Medium|Medium linje|
|SlantedDashDot|Lutande medelhög streckprickad linje|
|Tjock|Tjock linje|
|Tunn|Tunn linje|
Välj en av linjestilarna och tilldela den sedan till[**Gräns**](https://reference.aspose.com/cells/net/aspose.cells/border) föremål[**LineStyle**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle) fast egendom.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBordersToCells-1.cs" >}}

{{% alert color="primary" %}}

Du bör ställa in både linjestil och färg samtidigt. De två diagonala kantlinjerna ska ha samma linjestil och färg.

{{% /alert %}}

####  **Lägger till gränser till ett intervall på Cells**

 Det är också möjligt att lägga till gränser till ett cellintervall snarare än bara en enskild cell. För att göra det, skapa först ett cellintervall genom att anropa[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) samlingens[**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) metod. Den kräver följande parametrar:

- Första raden, den första raden i intervallet.
- Första kolumnen, representerar den första kolumnen i intervallet.
- Antal rader, antalet rader i intervallet.
- Antal kolumner, antalet kolumner i intervallet.

 De[**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) metod returnerar en[**Räckvidd**](https://reference.aspose.com/cells/net/aspose.cells/range) objekt, som innehåller det angivna cellintervallet. De[**Räckvidd**](https://reference.aspose.com/cells/net/aspose.cells/range) objekt ger en[**SetOutlineBorder**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder) metod som använder följande parametrar för att lägga till en kantlinje till cellområdet:

-  *Border Type**, kanttypen, vald från[**BorderType**](https://reference.aspose.com/cells/net/aspose.cells/bordertype)uppräkning.
-  *Linjestil**, kantlinjestilen, vald från[**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)uppräkning.
- *Färg**, linjefärgen, vald från färguppräkningen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBorderstoRange-1.cs" >}}
