---
title: Arbetsbladsvyer
type: docs
weight: 40
url: /sv/cpp/worksheet-views/
---
##  **Förhandsvisning av sidbrytning**
Alla kalkylblad kan visas i två lägen:

- Normal vy.
- Förhandsgranskning av sidbrytning.

Normalvyn är standardvyn för ett kalkylblad. Förhandsgranskning av sidbrytning är en redigeringsvy som visar ett kalkylblad när det skrivs ut. Förhandsgranskning av sidbrytningar visar vilken data som kommer att finnas på varje sida så att du kan justera utskriftsområdet och sidbrytningarna. Genom att använda Aspose.Cells kan utvecklare aktivera normala visnings- eller sidbrytningslägen.
###  **Styra visningslägen**
 Aspose.Cells tillhandahåller en klass[Arbetsbok](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) som representerar en Microsoft Excel-fil. De[Arbetsbok](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) klass innehåller en[Arbetsblad](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)samling som ger åtkomst till varje kalkylblad i en Excel-fil.

Ett arbetsblad representeras av[Arbetsblad](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)klass. De[Arbetsblad](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klass tillhandahåller ett brett utbud av metoder för att hantera kalkylblad. För att aktivera normala eller sidbrytningsförhandsvisningslägen, använd[SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) metod för[Arbetsblad](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klass.[IsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/ispagebreakpreview/) returnerar ett boolvärde, vilket betyder att det bara kan lagra ett**Sann** eller**falsk** värde.
####  **Aktiverar normal vy**
Ställ in ett kalkylblad till normal vy genom att ställa in[SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/)metod för[Arbetsblad](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)klass till *falskt**.
####  **Aktiverar förhandsgranskning av sidbrytning**
Ställ in valfritt kalkylblad till förhandsvisning av sidbrytning genom att ställa in[SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/)metod för[Arbetsblad](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)klass till *sant**. Om du gör det ändras kalkylbladet från normal vy till förhandsvisning av sidbrytning.

Ett komplett exempel ges nedan som visar hur man använder[SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/)metod för att aktivera förhandsgranskningsläge för sidbrytning för det första kalkylbladet i en Excel-fil.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-EnablingPageBreakPreview-new.cpp" >}}
##  **Zoomfaktor**
###  **Använder Microsoft Excel**
Microsoft Excel tillhandahåller en funktion som låter användare ställa in ett kalkylblads zoom- eller skalningsfaktor. Den här funktionen hjälper användare att se kalkylbladets innehåll i mindre eller större vyer. Användare kan ställa in zoomfaktorn till valfritt värde.
###  **Aspose.Cells & Zoomfaktor**
 Aspose.Cells tillåter också utvecklare att ställa in kalkylbladets zoomfaktor. Aspose.Cells tillhandahåller en klass[Arbetsbok](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) som representerar en Microsoft Excel-fil. De[Arbetsbok](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) klass innehåller en[Arbetsblad](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)samling som ger åtkomst till varje kalkylblad i en Excel-fil.

Ett arbetsblad representeras av[Arbetsblad](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klass. De[Arbetsblad](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)klass tillhandahåller ett brett utbud av metoder för att hantera kalkylblad. För att ställa in ett kalkylblads zoomfaktor, använd[Ställ inZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/) metod för[Arbetsblad](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klass. Zoomfaktorn ställs in genom att tilldela ett numeriskt värde (heltal).[Ställ inZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/)metod.

Ett komplett exempel ges nedan som visar hur man använder[Ställ inZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/)metod för att ställa in zoomfaktorn för det första kalkylbladet i Excel-filen.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-ZoomFactor-new.cpp" >}}
##  **Frys rutor**
###  **Använder Microsoft Excel**
Frys rutor är en funktion som tillhandahålls av Microsoft Excel. Frysa rutor låter dig välja data som ska förbli synliga när du rullar i ett kalkylblad.
###  **Aspose.Cells & Frys rutor**
 Aspose.Cells tillåter också utvecklare att tillämpa frysrutor på kalkylblad under körning. Aspose.Cells tillhandahåller en klass[Arbetsbok](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) som representerar en Microsoft Excel-fil. De[Arbetsbok](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) klass innehåller en[Arbetsblad](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)samling som ger åtkomst till varje kalkylblad i en Excel-fil.

Ett arbetsblad representeras av[Arbetsblad](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klass. De[Arbetsblad](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)klass tillhandahåller ett brett utbud av metoder för att hantera kalkylblad. För att konfigurera frysrutor, ring[FreezePanes](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/)metod för[Arbetsblad](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klass. De[FreezePanes](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/)metoden tar följande parametrar:

- *Rad**, radindexet för cellen som frysningen startar från.
- *Kolumn**, kolumnindex för cellen som frysningen startar från.
- *Frysta rader**, antalet synliga rader i den övre rutan.
- *Frysta kolumner**, antalet synliga kolumner i den vänstra rutan

 Ett komplett exempel ges nedan som visar hur man använder[FreezePanes](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/)metod för att frysa rader och kolumner (med början från C4, representerade av 4:e raden och 3:e kolumnen, där raderna och kolumnerna börjar från 0-indexet) i det första kalkylbladet i Excel-filen.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-FreezePanes-new.cpp" >}}
##  **Delade rutor**
Om du behöver dela skärmen för att få två olika vyer i samma kalkylblad, dela rutor. Microsoft Excel erbjuder en mycket praktisk funktion som låter dig visa mer än en kopia av ditt kalkylblad och för att du ska kunna rulla igenom varje ruta i ditt kalkylblad oberoende av varandra: delade paneler.

Rutorna fungerar samtidigt. Om du gör en ändring i den ena, visas ändringen samtidigt i den andra. Aspose.Cells tillhandahåller funktionen för delade rutor för användarna.
###  **Applicera och ta bort delade rutor**
####  **Dela rutor**
 Aspose.Cells tillhandahåller en klass[Arbetsbok](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) som representerar en Microsoft Excel-fil. De[Arbetsbok](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)klass tillhandahåller ett brett utbud av metoder för att hantera en Excel-fil. För att implementera delade vyer, använd[Dela](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/) metod för[Arbetsblad](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klass. För att ta bort de delade rutorna, använd[Ta bort Split](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/)metod.

I exemplet använder vi en enkel mallfil som laddas, sedan tillämpas funktionen för delade paneler på en cell i det första kalkylbladet. Den uppdaterade filen sparas.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-SplitPanes-new.cpp" >}}
####  **Ta bort rutor**
 Ta bort delade rutor med hjälp av[Ta bort Split](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/)metod.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-RemovingPanes-new.cpp" >}}
