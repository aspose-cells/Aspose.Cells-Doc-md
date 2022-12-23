---
title: Arbetsbladsvyer
type: docs
weight: 40
url: /sv/net/worksheet-views/
description:  Den här artikeln kommer att beskriva hur du använder C# och .NET API för att interagera med sidbrytningsförhandsvisningen av en Excel-arbetsbok och kalkylblad. Arbeta med delade rutor, frysta rutor och zoomfaktor också.
---
## **Förhandsvisning av sidbrytning**

Alla kalkylblad kan visas i två lägen:

- Normal vy.
- Förhandsgranskning av sidbrytning.

Normalvy är ett kalkylblads standardvy. Förhandsgranskning av sidbrytning är en redigeringsvy som visar ett kalkylblad när det skrivs ut. Förhandsgranskning av sidbrytningar visar vilken data som kommer att finnas på varje sida så att du kan justera utskriftsområdet och sidbrytningarna. Genom att använda Aspose.Cells kan utvecklare aktivera normala visnings- eller sidbrytningslägen.

### **Styra visningslägen**

Aspose.Cells tillhandahåller en[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass som representerar en Microsoft Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass innehåller en[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)samling som ger åtkomst till varje kalkylblad i en Excel-fil.

 Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass. De[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class tillhandahåller ett brett utbud av egenskaper och metoder för att hantera kalkylblad. För att aktivera normala eller sidbrytningsförhandsvisningslägen, använd[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass[**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) fast egendom.[**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) är en boolesk egenskap, vilket betyder att den bara kan lagra en**Sann** eller a**falsk** värde.

#### **Aktiverar normal vy**

 Ställ in ett kalkylblad till normal vy genom att ställa in[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass[**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) egendom till**falsk**.

#### **Aktiverar förhandsgranskning av sidbrytning**

 Ställ in valfritt kalkylblad till förhandsvisning av sidbrytning genom att ställa in[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass[**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) egendom till**Sann**Om du gör det ändras kalkylbladet från normal vy till förhandsvisning av sidbrytning.

 Ett komplett exempel ges nedan som visar hur man använder[**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview)egenskap för att aktivera förhandsgranskningsläge för sidbrytning för det första kalkylbladet i en Excel-fil.

Book1.xls-filen öppnas genom att skapa en instans av[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass. Vyn växlas till förhandsvisning av sidbrytning för det första kalkylbladet genom att ställa in[**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview)egendom till**Sann**. Den ändrade filen sparas som output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-PageBreakPreview-1.cs" >}}

## **Zoomfaktor**

### **Använder Microsoft Excel**

Microsoft Excel tillhandahåller en funktion som låter användare ställa in ett kalkylblads zoom- eller skalningsfaktor. Den här funktionen hjälper användare att se kalkylbladets innehåll i mindre eller större vyer. Användare kan ställa in zoomfaktorn till valfritt värde.

### **Aspose.Cells & Zoomfaktor**

Aspose.Cells tillåter utvecklare att ställa in kalkylbladets zoomfaktor.
Aspose.Cells tillhandahåller en[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass som representerar en Microsoft Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass innehåller en[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)samling som ger åtkomst till varje kalkylblad i en Excel-fil.

 Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass. De[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class tillhandahåller ett brett utbud av egenskaper och metoder för att hantera kalkylblad. För att ställa in ett kalkylblads zoomfaktor, använd[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass'[**Zoom**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom)fast egendom. Zoomfaktorn ställs in genom att tilldela ett numeriskt värde (heltal).[**Zoom**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom) fast egendom.

Ett komplett exempel ges nedan som visar hur man använder[**Zoom**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom) egenskap för att ställa in zoomfaktorn för det första kalkylbladet i Excel-filen.

Book1.xls-filen öppnas genom att skapa en instans av[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook)klass. Zoomfaktorn för det första kalkylbladet är satt till 75 och den modifierade filen sparas som output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-ZoomFactor-1.cs" >}}

## **Frys rutor**

### **Använder Microsoft Excel**

Frys rutor är en funktion som tillhandahålls av Microsoft Excel. Frysa rutor låter dig välja data som ska förbli synliga när du rullar i ett kalkylblad.

### **Aspose.Cells & Frys rutor**

Aspose.Cells tillåter utvecklare att tillämpa frysrutor på kalkylblad under körning.

Aspose.Cells tillhandahåller en[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook)klass som representerar en Microsoft Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook)klass innehåller en[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)samling som ger åtkomst till varje kalkylblad i en Excel-fil.

Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)klass. De[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class tillhandahåller ett brett utbud av egenskaper och metoder för att hantera kalkylblad. För att konfigurera frysrutor, ring klassen Worksheet'[**FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index)metod. De[**FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index)metoden tar följande parametrar:

- **Rad**, radindexet för cellen som frysningen börjar från.
- **Kolumn**, kolumnindex för cellen som frysningen startar från.
- **Frysta rader**, antalet synliga rader i den övre rutan.
- **Frysta kolonner**, antalet synliga kolumner i den vänstra rutan

 Book1.xls-filen öppnas genom att anropa[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook)class' konstruktor medan den instansieras och några rader och kolumner fryses i det första kalkylbladet. Den ändrade filen sparas som output.xls.

 Ett komplett exempel ges nedan som visar hur man använder[**FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index)metod för att frysa rader och kolumner (med början från C4, representerad av 4:e raden och 3:e kolumnen, där raderna och kolumnerna börjar från 0-indexet) i det första kalkylbladet i Excel-filen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-FreezePanes-1.cs" >}}

## **Delade rutor**

Om du behöver dela skärmen för att få två olika vyer i samma kalkylblad, dela rutor. Microsoft Excel erbjuder en mycket praktisk funktion som låter dig visa mer än en kopia av ditt kalkylblad och för att du ska kunna rulla igenom varje ruta i ditt kalkylblad oberoende av varandra: delade paneler.

Rutorna fungerar samtidigt. Om du gör en ändring i den ena, visas ändringen samtidigt i den andra. Aspose.Cells tillhandahåller funktionen för delade rutor för användarna.

### **Applicera och ta bort delade rutor**

#### **Dela rutor**

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) som representerar en Microsoft Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class tillhandahåller ett brett utbud av egenskaper och metoder för att hantera en Excel-fil. För att implementera delade vyer, använd[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass'[**Dela**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/split) . För att ta bort de delade rutorna, använd[**Ta bort Split**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/removesplit)metod.

exemplet använder vi en enkel mallfil som laddas, sedan tillämpas funktionen för delade paneler på en cell i det första kalkylbladet. Den uppdaterade filen sparas.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-SplitPanes-1.cs" >}}

Efter att ha kört ovanstående kod kommer den genererade filen att ha en delad vy.

#### **Ta bort rutor**

 Ta bort delade rutor med hjälp av[**Ta bort Split**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/removesplit)metod.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-RemovePanes-1.cs" >}}

## **Förhandsämnen**
- [Döljer visningen av nollvärden i arbetsbladet](/cells/sv/net/hiding-the-display-of-zero-values-in-the-worksheet/)
- [Ställ in kalkylbladsflikfärg](/cells/sv/net/set-worksheet-tab-color/)
- [Visa och dölj rutnätslinjer och radkolumnrubriker](/cells/sv/net/show-and-hide-gridlines-and-row-column-headers/)
- [Visa och dölj rader Kolumner och rullningslister](/cells/sv/net/show-and-hide-rows-columns-and-scroll-bars/)
- [Visa och dölj arbetsblad och flikar](/cells/sv/net/show-and-hide-worksheets-and-tabs/)
- [Visa formler istället för värden i ett kalkylblad](/cells/sv/net/show-formulas-instead-of-values-in-a-worksheet/)
- [Använd alternativ för felkontroll](/cells/sv/net/use-error-checking-options/)

