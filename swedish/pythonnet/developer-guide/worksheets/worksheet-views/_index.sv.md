---
title: Arbetsboks vy
type: docs
weight: 40
url: /sv/python-net/worksheet-views/
description: Den här artikeln beskriver hur man använder Aspose.Cells för Python via .NET API för att interagera med utskriftsavsnitts och kalkylbladsgränssnittet i ett Excel arbetsbok och kalkylblad. Hantera delade fanor, låsta fönster och zoomfaktor också. 
keywords: Python Excel bibliotek, Python hur man ställer in sidbrytarpreview, Python hur man aktiverar Normalvy, Python hur man ställer in zoomfaktor, Python hur man låser fönster, Python hur man delar fönster, Python hur man tar bort fönster.
---

## **Sidbrytning Förhandsgranskning**

Alla arbetsblad kan visas i två lägen:

- Normal vy.
- Sidbrytningsvy.

Normalvy är ett kalkylblads standardvyn. Sida-brytapiesturn är en redigeringsvy som visar ett kalkylblad så som det kommer att skrivas ut. Sida-brytapiesturn visar vilken data som kommer att hamna på varje sida så att du kan justera utskriftsområdet och sidbrytningar. Med Aspose.Cells för Python via .NET kan utvecklare aktivera normalvy eller sida-brytvyer.

### **Styra vynlägen**

Aspose.Cells för Python via .NET tillhandahåller en [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) klass som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) klassen innehåller en [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) samling som ger tillgång till varje kalkylblad i en Excel-fil.

Ett arbetsblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) tillhandahåller ett brett utbud av egenskaper och metoder för att hantera arbetsblad. För att aktivera normal vy eller sidbrytningsvy används [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)-klassens [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview)-egenskap. [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview) är en boolesk egenskap, vilket innebär att den bara kan lagra ett värde **true** eller **false**.

#### **Aktivera normal vy**

Ställ in ett arbetsblad till normal vy genom att ange [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)-klassens [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview)-egenskap till **false**.

#### **Aktivera sidbrytningsvy**

Ställ in valfritt arbetsblad till sidbrytningsvy genom att ange [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)-klassens [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview)-egenskap till **true**. Detta gör att arbetsbladet byts från normal vy till sidbrytningsvy.

Ett komplett exempel visas nedan som demonstrerar hur man använder [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview)-egenskapen för att aktivera sidbrytningsvy för det första arbetsbladet i en Excel-fil.

Filen book1.xls öppnas genom att skapa en instans av klassen [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook). Vyn byts till sidbrytningsvy för det första arbetsbladet genom att ange att [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview)-egenskapen är **true**. Den modifierade filen sparas som output.xls.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-PageBreakPreview-1.py" >}}

## **Zoomfaktor**

### **Använda Microsoft Excel**

Microsoft Excel har en funktion som låter användare sätta en arbetsblads zoom- eller skalfaktor. Denna funktion hjälper användare att se arbetsbladsinnehållet i mindre eller större visningar. Användare kan sätta zoom-faktorn till vilket värde som helst.

### **Aspose.Cells och Zoom Faktor**

Aspose.Cells tillåter utvecklare att sätta arbetsblads zoom-faktor.
Aspose.Cells tillhandahåller en [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) klass som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) klassen innehåller en [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) samling som tillåter åtkomst till varje arbetsblad i en Excel-fil.

Ett arbetsblad representeras av [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) klassen. [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) klassen tillhandahåller ett brett utbud av egenskaper och metoder för att hantera arbetsblad. För att sätta en arbetsblads zoom-faktor använder man egenskapen [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) i [**zoom**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/zoom) klassen. Zoom-faktorn sätts genom att tilldela ett numeriskt (heltals) värde till egenskapen [**zoom**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/zoom).

Ett fullständigt exempel som demonstrerar hur man använder [**zoom**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/zoom) egenskapen till att sätta zoom-faktorn på det första arbetsbladet i Excel-filen nedan.

book1.xls-filen öppnas genom att skapa en instans av [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)-klassen. Zoom-faktorn på det första arbetsbladet sätts till 75 och den modifierade filen sparas som output.xls.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-ZoomFactor-1.py" >}}

## **Frys Fönsterpaneler**

### **Använda Microsoft Excel**

Frysa rutor är en funktion som tillhandahålls av Microsoft Excel. Att frysa rutor gör att man kan välja data som ska förbli synlig när man rullar i ett arbetsblad.

### **Aspose.Cells och Frysa rutor**

Aspose.Cells tillåter utvecklare att applicera frysfönster på arbetsblad vid körning.

Aspose.Cells tillhandahåller en [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) klass som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) klassen innehåller en [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) samling som tillåter åtkomst till varje arbetsblad i en Excel-fil.

Ett arbetsblad representeras av [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) klassen. [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) klassen tillhandahåller ett brett utbud av egenskaper och metoder för att hantera arbetsblad. För att konfigurera frysrutor kallar man på [**freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#int-int-int-int) metoden i Worksheet-klassen. [**freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#int-int-int-int) metoden tar följande parametrar:

- **row**, radindex för cellen där fryset börjar.
- **column**, kolumnindex för cellen där fryset börjar.
- **frozen_rows**, antalet synliga rader i den övre panelen.
- **frozen_columns**, antalet synliga kolumner i den vänstra panelen

book1.xls-filen öppnas genom att man kallar på konstruktorn till [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)-klassen medan man instansierar den och några rader och kolumner frysas i det första arbetsbladet. Den modifierade filen sparas som output.xls.

Ett komplett exempel nedan visar hur man använder sig av [**freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#str-int-int) metoden för att frysa rader och kolumner (som börjar från C4, representerat av den fjärde raden och tredje kolumnen, där raderna och kolumnerna börjar från index 0) på det första arbetsbladet i Excel-filen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-FreezePanes-1.py" >}}

## **Dela rutor**

Om du behöver dela skärmen för att få två olika vyer i samma arbetsblad, dela rutor. Microsoft Excel erbjuder en mycket praktisk funktion som gör att du kan se mer än en kopia av ditt arbetsblad och för dig att kunna bläddra igenom varje ruta av ditt arbetsblad oberoende av varandra: dela rutor.

Fönstren fungerar samtidigt. Om du gör en förändring i ett, visas förändringen samtidigt i den andra. Aspose.Cells tillhandahåller split panes-funktionen för användarna.

### **Sätta på och Ta bort Delade paneler**

#### **Dela Fönster**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) klassen tillhandahåller ett brett utbud av egenskaper och metoder för att hantera en Excel-fil. För att implementera split vyer använder man sig av [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) metoden. För att ta bort delade rutor, använder man sig av [**split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/split) metoden.

I exemplet använder vi en enkel mallfil som laddas, sedan används inställningar för att dela rutor på en cell i det första arbetsbladet. Den uppdaterade filen sparas.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-SplitPanes-1.py" >}}

Efter att ovanstående kod har körts, kommer den genererade filen ha en delad vy.

#### **Ta bort rutor**

Ta bort delade rutor med metoden [**remove_split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/remove_split).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-RemovePanes-1.py" >}}

## **Fortsatta ämnen**
- [Dölja visning av nollvärden i kalkylbladet](/cells/sv/python-net/hiding-the-display-of-zero-values-in-the-worksheet/)
- [Ange färg på kalkylbladsflik](/cells/sv/python-net/set-worksheet-tab-color/)
- [Visa och dölj rutnät och radkolumnhuvuden](/cells/sv/python-net/show-and-hide-gridlines-and-row-column-headers/)
- [Visa och dölj rader kolumner och skrollbar](/cells/sv/python-net/show-and-hide-rows-columns-and-scroll-bars/)
- [Visa och dölj arbetsblad och flikar](/cells/sv/python-net/show-and-hide-worksheets-and-tabs/)
- [Visa formler istället för värden i ett arbetsblad](/cells/sv/python-net/show-formulas-instead-of-values-in-a-worksheet/)
- [Använd felkontrollalternativ](/cells/sv/python-net/use-error-checking-options/)

{{< app/cells/assistant language="python-net" >}}
