---
title: Arbetsboks vy
type: docs
weight: 40
url: /sv/net/worksheet-views/
description: Den här artikeln beskriver hur man använder C# och .NET API et för att interagera med sidbrytningsvyn för en Excel arbetsbok och arbetsblad. Arbeta med delade fönster, frysta rutor och zoomfaktor. 
---

## **Sidbrytning Förhandsgranskning**

Alla arbetsblad kan visas i två lägen:

- Normal vy.
- Sidbrytningsvy.

Normal vy är standardvyn för ett arbetsblad. Sidbrytningsvyn är en redigeringsvy som visar ett arbetsblad som det kommer att skrivas ut. Sidbrytningsvyn visar vilka data som kommer att hamna på varje sida så att du kan justera utskriftsområdet och sidbrytningarna. Med Aspose.Cells kan utvecklare aktivera läget för normal vy eller sidbrytningsvy.

### **Styra vynlägen**

Aspose.Cells tillhandahåller en [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)-klass som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)-klassen innehåller en [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)-samling som möjliggör åtkomst till varje arbetsblad i en Excel-fil.

Ett arbetsblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) tillhandahåller ett brett utbud av egenskaper och metoder för att hantera arbetsblad. För att aktivera normal vy eller sidbrytningsvy används [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-klassens [**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview)-egenskap. [**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) är en boolesk egenskap, vilket innebär att den bara kan lagra ett värde **true** eller **false**.

#### **Aktivera normal vy**

Ställ in ett arbetsblad till normal vy genom att ange [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-klassens [**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview)-egenskap till **false**.

#### **Aktivera sidbrytningsvy**

Ställ in valfritt arbetsblad till sidbrytningsvy genom att ange [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-klassens [**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview)-egenskap till **true**. Detta gör att arbetsbladet byts från normal vy till sidbrytningsvy.

Ett komplett exempel visas nedan som demonstrerar hur man använder [**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview)-egenskapen för att aktivera sidbrytningsvy för det första arbetsbladet i en Excel-fil.

Filen book1.xls öppnas genom att skapa en instans av klassen [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook). Vyn byts till sidbrytningsvy för det första arbetsbladet genom att ange att [**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview)-egenskapen är **true**. Den modifierade filen sparas som output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-PageBreakPreview-1.cs" >}}

## **Zoomfaktor**

### **Använda Microsoft Excel**

Microsoft Excel har en funktion som låter användare sätta en arbetsblads zoom- eller skalfaktor. Denna funktion hjälper användare att se arbetsbladsinnehållet i mindre eller större visningar. Användare kan sätta zoom-faktorn till vilket värde som helst.

### **Aspose.Cells och Zoom Faktor**

Aspose.Cells tillåter utvecklare att sätta arbetsblads zoom-faktor.
Aspose.Cells tillhandahåller en [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klassen innehåller en [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) samling som tillåter åtkomst till varje arbetsblad i en Excel-fil.

Ett arbetsblad representeras av [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klassen. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klassen tillhandahåller ett brett utbud av egenskaper och metoder för att hantera arbetsblad. För att sätta en arbetsblads zoom-faktor använder man egenskapen [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) i [**Zoom**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom) klassen. Zoom-faktorn sätts genom att tilldela ett numeriskt (heltals) värde till egenskapen [**Zoom**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom).

Ett fullständigt exempel som demonstrerar hur man använder [**Zoom**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom) egenskapen till att sätta zoom-faktorn på det första arbetsbladet i Excel-filen nedan.

book1.xls-filen öppnas genom att skapa en instans av [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)-klassen. Zoom-faktorn på det första arbetsbladet sätts till 75 och den modifierade filen sparas som output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-ZoomFactor-1.cs" >}}

## **Frys Fönsterpaneler**

### **Använda Microsoft Excel**

Frysa rutor är en funktion som tillhandahålls av Microsoft Excel. Att frysa rutor gör att man kan välja data som ska förbli synlig när man rullar i ett arbetsblad.

### **Aspose.Cells och Frysa rutor**

Aspose.Cells tillåter utvecklare att applicera frysfönster på arbetsblad vid körning.

Aspose.Cells tillhandahåller en [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klassen innehåller en [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) samling som tillåter åtkomst till varje arbetsblad i en Excel-fil.

Ett arbetsblad representeras av [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klassen. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klassen tillhandahåller ett brett utbud av egenskaper och metoder för att hantera arbetsblad. För att konfigurera frysrutor kallar man på [**FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index) metoden i Worksheet-klassen. [**FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index) metoden tar följande parametrar:

- **Rad**, radindexet för cellen som frysen ska starta från.
- **Kolumn**, kolumnindexet för cellen som frysen ska starta från.
- **Frusna rader**, antalet synliga rader i toppfönstret.
- **Frusna kolumner**, antalet synliga kolumner i vänstra fönstret.

book1.xls-filen öppnas genom att man kallar på konstruktorn till [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)-klassen medan man instansierar den och några rader och kolumner frysas i det första arbetsbladet. Den modifierade filen sparas som output.xls.

Ett komplett exempel nedan visar hur man använder sig av [**FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index) metoden för att frysa rader och kolumner (som börjar från C4, representerat av den fjärde raden och tredje kolumnen, där raderna och kolumnerna börjar från index 0) på det första arbetsbladet i Excel-filen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-FreezePanes-1.cs" >}}

## **Dela rutor**

Om du behöver dela skärmen för att få två olika vyer i samma arbetsblad, dela rutor. Microsoft Excel erbjuder en mycket praktisk funktion som gör att du kan se mer än en kopia av ditt arbetsblad och för dig att kunna bläddra igenom varje ruta av ditt arbetsblad oberoende av varandra: dela rutor.

Fönstren fungerar samtidigt. Om du gör en förändring i ett, visas förändringen samtidigt i den andra. Aspose.Cells tillhandahåller split panes-funktionen för användarna.

### **Sätta på och Ta bort Delade paneler**

#### **Dela Fönster**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klassen tillhandahåller ett brett utbud av egenskaper och metoder för att hantera en Excel-fil. För att implementera split vyer använder man sig av [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) metoden. För att ta bort delade rutor, använder man sig av [**Split**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/split) metoden.

I exemplet använder vi en enkel mallfil som laddas, sedan används inställningar för att dela rutor på en cell i det första arbetsbladet. Den uppdaterade filen sparas.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-SplitPanes-1.cs" >}}

Efter att ovanstående kod har körts, kommer den genererade filen ha en delad vy.

#### **Ta bort rutor**

Ta bort delade rutor med metoden [**RemoveSplit**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/removesplit).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-RemovePanes-1.cs" >}}

## **Fortsatta ämnen**
- [Dölja visning av nollvärden i kalkylbladet](/cells/sv/net/hiding-the-display-of-zero-values-in-the-worksheet/)
- [Ange färg på kalkylbladsflik](/cells/sv/net/set-worksheet-tab-color/)
- [Visa och dölj rutnät och radkolumnhuvuden](/cells/sv/net/show-and-hide-gridlines-and-row-column-headers/)
- [Visa och dölj rader kolumner och skrollbar](/cells/sv/net/show-and-hide-rows-columns-and-scroll-bars/)
- [Visa och dölj arbetsblad och flikar](/cells/sv/net/show-and-hide-worksheets-and-tabs/)
- [Visa formler istället för värden i ett arbetsblad](/cells/sv/net/show-formulas-instead-of-values-in-a-worksheet/)
- [Använd felkontrollalternativ](/cells/sv/net/use-error-checking-options/)

