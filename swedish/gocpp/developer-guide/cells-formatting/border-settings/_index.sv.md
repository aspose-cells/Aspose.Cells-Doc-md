---
title: Border inställningar med Golang via C++
linktitle: Kantinställningar
description: Hur du använder Aspose.Cells biblioteket i C++ för att sätta kantlinjestil och färg på celler. Genom att justera bredden, stilen och färgen på kanten får du mer kontroll över hur cellerna ser ut och framstår.
keywords: Aspose.Cells, Cell kantinställningar, C++, Kantbredd, Kantstil, Kantfärg
type: docs
weight: 40
url: /sv/go-cpp/cells-border-settings/
---

## **Lägga till ramar till celler**

Microsoft Excel låter användare formatera celler genom att lägga till kanter. Typen av kant beror på var den läggs till. Till exempel är en övre kant en som läggs till i cellens övre position. Användare kan också ändra linjestilen och färgen på kanterna.

Med Aspose.Cells kan utvecklare lägga till kanter och anpassa hur de ser ut på samma flexibla sätt som i Microsoft Excel.

### **Lägga till ramar till celler**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/)-klassen innehåller en [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)-samling som möjliggör åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)-klassen. [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)-klassen tillhandahåller en [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-samling. Varje objekt i [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-samlingen representerar ett objekt av [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)-klassen.

Aspose.Cells tillhandahåller metoden [**GetStyle**](https://reference.aspose.com/cells/go-cpp/cell/getstyle/) i [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)-klassen. Metoden [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) används för att sätta ett cellers formateringsstil. [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)-klassen tillhandahåller egenskaper för att lägga till kanter till celler.

#### **Lägga till ramar till en cell**

Utvecklare kan lägga till kanter till en cell genom att använda [**Style**](https://reference.aspose.com/cells/go-cpp/style/)-objektets [**GetBorders()**](https://reference.aspose.com/cells/go-cpp/style/getborders/)-samling. Kantens typ anges som ett index i [**GetBorders()**](https://reference.aspose.com/cells/go-cpp/style/getborders/)-samlingen. Alla kanttyper är fördefinierade i [**BorderType**](https://reference.aspose.com/cells/cpp/aspose.cells/bordertype/)-enumerationen.

**Kantuppräkning**

| **Kanttyper** | **Beskrivning** |
|------------------|-----------------|
| BottomBorder     | En bottenkantlinje |
| DiagonalDown     | En diagonallinje från övre vänstra till högra nedre |
| DiagonalUp       | En diagonal linje från nedre vänstra till övre högra |
| LeftBorder       | En vänstrekantlinje |
| RightBorder      | En högrekantlinje |
| TopBorder        | En toppkantlinje |

Kollektionssamlingen [**GetBorders()**](https://reference.aspose.com/cells/go-cpp/style/getborders/) innehåller alla kanter. Varje kant i [**GetBorders()**](https://reference.aspose.com/cells/go-cpp/style/getborders/)-kollektionen representeras av ett [**Border**](https://reference.aspose.com/cells/cpp/aspose.cells/border/)-objekt som tillhandahåller två egenskaper, [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/border/getcolor/) och [**GetLineStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/border/getlinestyle/), för att ställa in kantlinjens färg och stil respektive.

För att ställa in kantfärgen, välj en färg med hjälp av Color-enumerationen och tilldela den till kantobjektets Color-egenskap.

Kantlinjens stil anges genom att välja en linje från [**CellBorderType**](https://reference.aspose.com/cells/go-cpp/cellbordertype/)-enumerationen.

**CellBorderType-enumen**

| **Linjestilar**       | **Beskrivning**               |
|------------------------|-------------------------------|
| DashDot               | Tunt streck-dotslinje        |
| DashDotDot            | Tunt streck-dotad linje       |
| Dashed                | Streckad linje               |
| Dotted                | Punkten linje                |
| Double                | Dubbellinje                  |
| Hair                  | Hårlinje                     |
| MediumDashDot         | Medium streck-dotad linje     |
| MediumDashDotDot      | Medium streck-dotad linje     |
| MediumDashed          | Medium streckad linje          |
| None                  | Ingen linje                  |
| Medium                | Medium linje                 |
| SlantedDashDot        | Snedstreckad medium streck-dotad linje |
| Thick                 | Tjock linje                  |
| Thin                  | Tunn linje                   |

Välj en av linjestilarna och tilldela den till [**Border**](https://reference.aspose.com/cells/go-cpp/border/) objektets [**GetLineStyle()**](https://reference.aspose.com/cells/go-cpp/border/getlinestyle/) egenskap.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-BorderSettings.go" >}}
{{% alert color="primary" %}}

Du bör ställa in både linjestil och färg samtidigt. De två diagonala kantlinjerna ska ha samma linjestil och färg.

{{% /alert %}}

#### **Lägga till Gränser till en Rad av Celler**

Det är också möjligt att lägga till ramar till ett cellområde snarare än en enskild cell. För att göra det, först skapa ett cellområde genom att anropa [**Cells**](https://reference.aspose.com/cells/go-cpp/cells/)-samlingens [**CreateRange**](https://reference.aspose.com/cells/go-cpp/cells/createrange/)-metod. Den tar följande parametrar:

- Första rad, den första raden av området.
- Första kolumn, representerar den första kolumnen av området.
- Antal rader, antalet rader i området.
- Antal kolumner, antalet kolumner i området.

Metoden [**CreateRange**](https://reference.aspose.com/cells/go-cpp/cells/createrange_string_string/) returnerar ett [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/)-objekt, som innehåller det angivna cellområdet. [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/)-objektet ger en [**SetOutlineBorder**](https://reference.aspose.com/cells/cpp/aspose.cells/range/setoutlineborder/)-metod som tar följande parametrar för att lägga till en ram till cellområdet:

- **Ramtipo**, ramens typ, vald från [**BorderType**](https://reference.aspose.com/cells/go-cpp/bordertype/) enumarationen.
- **Linjestil**, ramens linjestil, vald från [**CellBorderType**](https://reference.aspose.com/cells/go-cpp/cellbordertype/) enumarationen.
- **Färg**, linjens färg, vald från Färg uppräkningen.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-BorderSettings-1.go" >}}
