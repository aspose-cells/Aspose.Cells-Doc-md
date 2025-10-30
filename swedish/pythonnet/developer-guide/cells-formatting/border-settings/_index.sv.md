---
title: Kantinställningar
description: Hur man använder Aspose.Cells för Python via .NET biblioteket i Python för att ställa in borderstil och färg på celler. Genom att justera bredd, stil och färg på kanten, får du mer kontroll över hur celler ser ut och visas.
keywords: Aspose.Cells för Python via .NET, Cellgränsinställningar, Python Border Width, Border Style, Border Color
type: docs
weight: 40
url: /sv/python-net/cells-border-settings/
---

## **Lägga till ramar till celler**

Microsoft Excel tillåter användare att formatera celler genom att lägga till kanter. Kanttypen beror på var den läggs till. Till exempel är en övre kant en som läggs till på cellens övre position. Användare kan också modifiera kantens linjestil och färg.

Med Aspose.Cells för Python via .NET kan utvecklare lägga till gränser och anpassa hur de ser ut på samma flexibla sätt som i Microsoft Excel.

### **Lägga till ramar till celler**

Aspose.Cells för Python via .NET tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) innehåller en [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) samling som ger åtkomst till varje arbetsblad i Excel-filen. Ett arbetsblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) tillhandahåller [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) samlingen. Varje objekt i [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) samlingen representerar ett objekt av klassen [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

Aspose.Cells för Python via .NET tillhandahåller [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) metoden i [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) klassen. [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) metoden används för att ställa in cellens formateringsstil. Klassen [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) tillhandahåller egenskaper för att lägga till gränser till celler.

#### **Lägga till ramar till en cell**

Utvecklare kan lägga till kanter till en cell genom att använda [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) objektets [**borders**](https://reference.aspose.com/cells/python-net/aspose.cells/style/borders) samling. Kantttypen skickas som en index till [**borders**](https://reference.aspose.com/cells/python-net/aspose.cells/style/borders) samlingen. Alla kanttyper är fördefinierade i [**BorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/bordertype) uppräkning.

**Kantuppräkning**

|**Ramtyper**|**Beskrivning**|
| :- | :- |
|BOTTOM_BORDER|En bottenlinje|
|DIAGONAL_DOWN|En diagonal linje från övre vänstra till nedre högra|
|DIAGONAL_UP|En diagonal linje från nedre vänstra till övre högra|
|LEFT_BORDER|En vänstergräns|
|RIGHT_BORDER|En högerrand|
|TOP_BORDER|En övre rand|

The [**borders**](https://reference.aspose.com/cells/python-net/aspose.cells/style/borders) collection stores all borders. Each border in the [**Borders**](https://reference.aspose.com/cells/python-net/aspose.cells/style/borders) collection is represented by a [**Border**](https://reference.aspose.com/cells/python-net/aspose.cells/border) object which provides two properties, [**color**](https://reference.aspose.com/cells/python-net/aspose.cells/border/color) and [**line_style**](https://reference.aspose.com/cells/python-net/aspose.cells/border/line_style) to set a border's line color and style respectively.

För att ange en kantlinjens färg, välj en färg med hjälp av Color-enumen (en del av .NET Framework) och tilldela den till Border-objektets Color-egenskap.

Kantlinjens linjestil ställs in genom att välja en linjestil från [**CellBorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/cellbordertype)-uppräkningen.

**CellBorderType-enumen**

|**Linjestilar**|**Beskrivning**|
| :- | :- |
|DASH_DOT|Tunn streck-punkt-linje|
|DASH_DOT_DOT|Tunn streck-punkt-punkt-linje|
|DASHED|Streckad linje|
|DOTTED|Prickad linje|
|DOUBLE|Dubbel linje|
|HAIR|Hårlinje|
|MEDIUM_DASH_DOT|Medelstreck-punkt-linje|
|MEDIUM_DASH_DOT_DOT|Medium streck-punkt-punkt-linje|
|MEDIUM_DASHED|Medium streckad linje|
|NONE|Ingen linje|
|MEDIUM|Medellinj|
|SLANTED_DASH_DOT|Vinklad mediumstreck-punkt-linje|
|THICK|Tjock linje|
|THIN|Tunn linje|
Välj en av linjestilarna och tilldela den sedan till [**Border**](https://reference.aspose.com/cells/python-net/aspose.cells/border)-objektets [**line_style**](https://reference.aspose.com/cells/python-net/aspose.cells/border/line_style)-egenskap.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Borders-AddingBordersToCells-1.py" >}}

{{% alert color="primary" %}}

Du bör ställa in både linjestil och färg samtidigt. De två diagonalerna bör ha samma linjestil och färg.

{{% /alert %}}

#### **Lägga till Gränser till en Rad av Celler**

Det är också möjligt att lägga till ramar till en rad celler istället för bara en enskild cell. För att göra det, skapa först en samling av celler genom att anropa [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)-objektets [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range)-metod. Den tar följande parametrar:

- Första rad, den första raden av området.
- Första kolumn, representerar den första kolumnen av området.
- Antal rader, antalet rader i området.
- Antal kolumner, antalet kolumner i området.

[**create_range**](hhttps://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str)-metoden returnerar ett [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range)-objekt, som innehåller det angivna cellområdet. [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range)-objektet tillhandahåller en [**set_outline_border**](https://reference.aspose.com/cells/python-net/aspose.cells/range/set_outline_border)-metod som tar följande parametrar för att lägga till en ram till cellområdet:

- **Border Typ**, typen av kant, vald från [**BorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/bordertype) uppräkningen.
- **Linjestil**, kantens linjestil, vald från [**CellBorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/cellbordertype) uppräkningen.
- **Färg**, linjens färg, vald från Färg uppräkningen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Borders-AddingBorderstoRange-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
