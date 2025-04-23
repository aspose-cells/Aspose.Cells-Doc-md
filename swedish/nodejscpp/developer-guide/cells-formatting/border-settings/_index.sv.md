---  
title: Kantinställningar
linktitle: Kantinställningar  
description: Hur man använder Aspose.Cells biblioteket i Node.js via C++ för att ställa in kantlinjestil och färg på celler. Genom att justera bredden, stilen och färgen på kanten har du mer kontroll över hur cellerna ser ut och framträder.  
keywords: Aspose.Cells, Cellkantinställningar, Node.js via C++, Kantbreda, Kantstil, Kantfärg  
type: docs  
weight: 40  
url: /sv/nodejs-cpp/cells-border-settings/  
---  

## **Lägga till ramar till celler**  

Microsoft Excel låter användare formatera celler genom att lägga till kanter. Typen av kant beror på var den läggs till. Till exempel är en övre kant en som läggs till i cellens övre position. Användare kan också ändra linjestilen och färgen på kanterna.  

Med Aspose.Cells for Node.js via C++ kan utvecklare lägga till kanter och anpassa deras utseende på samma flexibla sätt som i Microsoft Excel.  

### **Lägga till ramar till celler**  

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-klassen innehåller en [**worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)-samling som möjliggör åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen tillhandahåller en [**cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-samling. Varje objekt i [**cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-samlingen representerar ett objekt av [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)-klassen.  

Aspose.Cells tillhandahåller metoden [**getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) i [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)-klassen. Metoden [**setStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) används för att sätta ett cellers formateringsstil. [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-klassen tillhandahåller egenskaper för att lägga till kanter till celler.  

#### **Lägga till ramar till en cell**  

Utvecklare kan lägga till kanter till en cell genom att använda [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-objektets [**borders**](https://reference.aspose.com/cells/nodejs-cpp/style/#getBorders--)-samling. Kantens typ anges som ett index i [**borders**](https://reference.aspose.com/cells/nodejs-cpp/style/#getBorders--)-samlingen. Alla kanttyper är fördefinierade i [**BorderType**](https://reference.aspose.com/cells/nodejs-cpp/bordertype)-enumerationen.  

**Kantuppräkning**  

|**Ramtyper**|**Beskrivning**|  
| :- | :- |  
|BottomBorder|En nederkantslinje|  
|DiagonalDown|En diagonal linje från övre vänster till höger nedan|  
|DiagonalUp|En diagonal linje från nedre vänster till höger upp|  
|LeftBorder|En vänsterkantlinje|  
|RightBorder|En högerkantlinje|  
|TopBorder|En övre kantlinje|  

Kollektionssamlingen [**borders**](https://reference.aspose.com/cells/nodejs-cpp/style/#getBorders--) innehåller alla kanter. Varje kant i [**borders**](https://reference.aspose.com/cells/nodejs-cpp/style/#getBorders--)-kollektionen representeras av ett [**Border**](https://reference.aspose.com/cells/nodejs-cpp/border)-objekt som tillhandahåller två egenskaper, [**setColor**](https://reference.aspose.com/cells/nodejs-cpp/border/#setColor-color-) och [**setLineStyle**](https://reference.aspose.com/cells/nodejs-cpp/border/#setLineStyle-cellbordertype-), för att ställa in kantlinjens färg och stil respektive.  

För att ställa in en kantlins färg, välj en färg med hjälp av Color-uppräkningen (del av Node.js) och tilldela den till Border-objektets color-egenskap.  

Kantlinjens stil anges genom att välja en linje från [**CellBorderType**](https://reference.aspose.com/cells/nodejs-cpp/cellbordertype)-enumerationen.  

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
Välj en av linjestilarna och tilldela den till [**Border**](https://reference.aspose.com/cells/nodejs-cpp/border) objektets [**lineStyle**](https://reference.aspose.com/cells/nodejs-cpp/border/#setLineStyle-cellbordertype-) egenskap.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AddBordersToCell.js" >}}

{{% alert color="primary" %}}  
Du bör ställa in både linjestil och färg samtidigt. De två diagonala kantlinjerna ska ha samma linjestil och färg.  
{{% /alert %}}  

#### **Lägga till Gränser till en Rad av Celler**  

Det är också möjligt att lägga till ramar till ett cellområde snarare än en enskild cell. För att göra det, först skapa ett cellområde genom att anropa [**cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-samlingens [**createRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-)-metod. Den tar följande parametrar:  

- Första rad, den första raden av området.  
- Första kolumn, representerar den första kolumnen av området.  
- Antal rader, antalet rader i området.  
- Antal kolumner, antalet kolumner i området.  

Metoden [**createRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-) returnerar ett [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range)-objekt, som innehåller det angivna cellområdet. [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range)-objektet ger en [**setOutlineBorder**](https://reference.aspose.com/cells/nodejs-cpp/range/#setOutlineBorder-bordertype-cellbordertype-cellscolor-)-metod som tar följande parametrar för att lägga till en ram till cellområdet:  

- **Ramtipo**, ramens typ, vald från [**BorderType**](https://reference.aspose.com/cells/nodejs-cpp/bordertype) enumarationen.  
- **Linjestil**, ramens linjestil, vald från [**CellBorderType**](https://reference.aspose.com/cells/nodejs-cpp/cellbordertype) enumarationen.  
- **Färg**, linjens färg, vald från Färg uppräkningen.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AddBordersToRange.js" >}}


