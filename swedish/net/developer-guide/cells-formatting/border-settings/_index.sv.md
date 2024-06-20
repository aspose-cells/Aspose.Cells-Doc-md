---
title: Kantinställningar
description: Hur du använder Aspose.Cells biblioteket i C# för att ställa in cellens kantstil och färg. Genom att justera bredd, stil och färg på kanten har du mer kontroll över hur celler ser ut och visas.
keywords: Aspose.Cells, Cell kantinställningar, C#, Kantbredd, Kantstil, Kantfärg
type: docs
weight: 40
url: /sv/net/cells-border-settings/
---

## **Lägga till ramar till celler**

Microsoft Excel tillåter användare att formatera celler genom att lägga till kanter. Kanttypen beror på var den läggs till. Till exempel är en övre kant en som läggs till på cellens övre position. Användare kan också modifiera kantens linjestil och färg.

Med Aspose.Cells kan utvecklare lägga till kanter och anpassa hur de ser ut på samma flexibla sätt som i Microsoft Excel.

### **Lägga till ramar till celler**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klassen innehåller en [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) samling som tillåter åtkomst till varje arbetsblad i Excel-filen. Ett arbetsblad representeras av [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klassen. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klassen ger en [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) samling. Varje objekt i [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) samlingen representerar ett objekt av [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) klassen.

Aspose.Cells tillhandahåller [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index) metoden i [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) klassen. [**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index) metoden används för att ställa in en cells formateringsstil. [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) klassen tillhandahåller egenskaper för att lägga till kanter till celler.

#### **Lägga till ramar till en cell**

Utvecklare kan lägga till kanter till en cell genom att använda [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) objektets [**Borders**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) samling. Kantttypen skickas som en index till [**Borders**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) samlingen. Alla kanttyper är fördefinierade i [**BorderType**](https://reference.aspose.com/cells/net/aspose.cells/bordertype) uppräkning.

**Kantuppräkning**

|**Ramtyper**|**Beskrivning**|
| :- | :- |
|BottomBorder|En nederkantslinje|
|DiagonalDown|En diagonal linje från övre vänster till höger nedan|
|DiagonalUp|En diagonal linje från nedre vänster till höger upp|
|LeftBorder|En vänsterkantlinje|
|RightBorder|En högerkantlinje|
|TopBorder|En övre kantlinje|

The [**Borders**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) collection stores all borders. Each border in the [**Borders**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) collection is represented by a [**Border**](https://reference.aspose.com/cells/net/aspose.cells/border) object which provides two properties, [**Color**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/color) and [**LineStyle**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle) to set a border's line color and style respectively.

För att ange en kantlinjens färg, välj en färg med hjälp av Color-enumen (en del av .NET Framework) och tilldela den till Border-objektets Color-egenskap.

Kantlinjens linjestil ställs in genom att välja en linjestil från [**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)-uppräkningen.

**CellBorderType-enumen**

|**Linjestilar**|**Beskrivning**|
| :- | :- |
|DashDot|Tunn streckpunktad linje|
|DashDotDot|Tunn streck-punktpunktad linje|
|Dashed|Streckad linje|
|Dotted|Punkterad linje|
|Double|Dubbel linje|
|Hair|Hårlinje|
|MediumDashDot|Medium streckpunktad linje|
|MediumDashDotDot|Medium streck-punktpunktad linje|
|MediumDashed|Medium streckad linje|
|None|Ingen linje|
|Medium|Medium linje|
|SlantedDashDot|Snedstreckad mediumstreckpunktad linje|
|Thick|Tjock linje|
|Thin|Tunn linje|
Välj en av linjestilarna och tilldela den sedan till [**Border**](https://reference.aspose.com/cells/net/aspose.cells/border)-objektets [**LineStyle**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle)-egenskap.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBordersToCells-1.cs" >}}

{{% alert color="primary" %}}

Du bör ställa in både linjestil och färg samtidigt. De två diagonalerna bör ha samma linjestil och färg.

{{% /alert %}}

#### **Lägga till Gränser till en Rad av Celler**

Det är också möjligt att lägga till ramar till en rad celler istället för bara en enskild cell. För att göra det, skapa först en samling av celler genom att anropa [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-objektets [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1)-metod. Den tar följande parametrar:

- Första rad, den första raden av området.
- Första kolumn, representerar den första kolumnen av området.
- Antal rader, antalet rader i området.
- Antal kolumner, antalet kolumner i området.

[**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1)-metoden returnerar ett [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range)-objekt, som innehåller det angivna cellområdet. [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range)-objektet tillhandahåller en [**SetOutlineBorder**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder)-metod som tar följande parametrar för att lägga till en ram till cellområdet:

- **Border Typ**, typen av kant, vald från [**BorderType**](https://reference.aspose.com/cells/net/aspose.cells/bordertype) uppräkningen.
- **Linjestil**, kantens linjestil, vald från [**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype) uppräkningen.
- **Färg**, linjens färg, vald från Färg uppräkningen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBorderstoRange-1.cs" >}}
