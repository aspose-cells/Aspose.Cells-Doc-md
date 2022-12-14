---
title: Arbetsbladsvyer
type: docs
weight: 40
url: /sv/cpp/worksheet-views/
---
## **Förhandsvisning av sidbrytning**
Alla kalkylblad kan visas i två lägen:

- Normal vy.
- Förhandsgranskning av sidbrytning.

Normalvyn är standardvyn för ett kalkylblad. Förhandsgranskning av sidbrytning är en redigeringsvy som visar ett kalkylblad när det skrivs ut. Förhandsgranskning av sidbrytningar visar vilken data som kommer att finnas på varje sida så att du kan justera utskriftsområdet och sidbrytningarna. Genom att använda Aspose.Cells kan utvecklare aktivera normala visnings- eller sidbrytningslägen.
### **Styra visningslägen**
 Aspose.Cells tillhandahåller en klass[IArbetsbok](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) som representerar en Microsoft Excel-fil. De[IArbetsbok](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) klass innehåller en[Arbetsblad](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)samling som ger åtkomst till varje kalkylblad i en Excel-fil.

 Ett arbetsblad representeras av[IArbetsblad](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)klass. De[IArbetsblad](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) klass tillhandahåller ett brett utbud av metoder för att hantera kalkylblad. För att aktivera normala eller sidbrytningsförhandsvisningslägen, använd[IsPageBreakPreview](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892) metod för[IArbetsblad](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) klass.[IsPageBreakPreview](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892) returnerar ett boolvärde, vilket betyder att det bara kan lagra ett**Sann** eller**falsk** värde.
#### **Aktiverar normal vy**
Ställ in ett kalkylblad till normal vy genom att ställa in[IsPageBreakPreview](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892)metod för[IArbetsblad](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) klass till**falsk**.
#### **Aktiverar förhandsgranskning av sidbrytning**
Ställ in valfritt kalkylblad till förhandsvisning av sidbrytning genom att ställa in[IsPageBreakPreview](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892)metod för[IArbetsblad](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) klass till**Sann**Om du gör det ändras kalkylbladet från normal vy till förhandsvisning av sidbrytning.

 Ett komplett exempel ges nedan som visar hur man använder[IsPageBreakPreview](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892)metod för att aktivera förhandsgranskningsläge för sidbrytning för det första kalkylbladet i en Excel-fil.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-EnablingPageBreakPreview.cpp" >}}
## **Zoomfaktor**
### **Använder Microsoft Excel**
Microsoft Excel tillhandahåller en funktion som låter användare ställa in ett kalkylblads zoom- eller skalningsfaktor. Den här funktionen hjälper användare att se kalkylbladets innehåll i mindre eller större vyer. Användare kan ställa in zoomfaktorn till valfritt värde.
### **Aspose.Cells & Zoomfaktor**
 Aspose.Cells tillåter också utvecklare att ställa in kalkylbladets zoomfaktor. Aspose.Cells tillhandahåller en klass[IArbetsbok](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) som representerar en Microsoft Excel-fil. De[IArbetsbok](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) klass innehåller en[Arbetsblad](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)samling som ger åtkomst till varje kalkylblad i en Excel-fil.

 Ett arbetsblad representeras av[IArbetsblad](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) klass. De[IArbetsblad](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)klass tillhandahåller ett brett utbud av metoder för att hantera kalkylblad. För att ställa in ett kalkylblads zoomfaktor, använd[Zoom](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ad94669a93a4324b3a4b7f9582df5b0ec) metod för[IArbetsblad](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) klass Zoomfaktorn ställs in genom att tilldela ett numeriskt (heltal) värde till[Zoom](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ad94669a93a4324b3a4b7f9582df5b0ec)metod.

 Ett komplett exempel ges nedan som visar hur man använder[Zoom](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ad94669a93a4324b3a4b7f9582df5b0ec)metod för att ställa in zoomfaktorn för det första kalkylbladet i Excel-filen.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-ZoomFactor.cpp" >}}
## **Frys rutor**
### **Använder Microsoft Excel**
Frys rutor är en funktion som tillhandahålls av Microsoft Excel. Frysa rutor låter dig välja data som ska förbli synliga när du rullar i ett kalkylblad.
### **Aspose.Cells & Frys rutor**
 Aspose.Cells tillåter också utvecklare att tillämpa frysrutor på kalkylblad under körning. Aspose.Cells tillhandahåller en klass[IArbetsbok](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) som representerar en Microsoft Excel-fil. De[IArbetsbok](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) klass innehåller en[Arbetsblad](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)samling som ger åtkomst till varje kalkylblad i en Excel-fil.

 Ett arbetsblad representeras av[IArbetsblad](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) klass. De[IArbetsblad](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)klass tillhandahåller ett brett utbud av metoder för att hantera kalkylblad. För att konfigurera frysrutor, ring[FreezePanes](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ac4f68dfe9ac219fb8de6d6824ec1aa22)metod för[IArbetsblad](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) klass. De[FreezePanes](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ac4f68dfe9ac219fb8de6d6824ec1aa22)metoden tar följande parametrar:

- **Rad**, radindexet för cellen som frysningen börjar från.
- **Kolumn**, kolumnindex för cellen som frysningen startar från.
- **Frysta rader**, antalet synliga rader i den övre rutan.
- **Frysta kolonner**, antalet synliga kolumner i den vänstra rutan

 Ett komplett exempel ges nedan som visar hur man använder[FreezePanes](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ac4f68dfe9ac219fb8de6d6824ec1aa22)metod för att frysa rader och kolumner (med början från C4, representerade av 4:e raden och 3:e kolumnen, där raderna och kolumnerna börjar från 0-indexet) i det första kalkylbladet i Excel-filen.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-FreezePanes.cpp" >}}
## **Delade rutor**
Om du behöver dela skärmen för att få två olika vyer i samma kalkylblad, dela rutor. Microsoft Excel erbjuder en mycket praktisk funktion som låter dig visa mer än en kopia av ditt kalkylblad och för att du ska kunna rulla igenom varje ruta i ditt kalkylblad oberoende av varandra: delade paneler.

Rutorna fungerar samtidigt. Om du gör en ändring i den ena, visas ändringen samtidigt i den andra. Aspose.Cells tillhandahåller funktionen för delade rutor för användarna.
### **Applicera och ta bort delade rutor**
#### **Dela rutor**
 Aspose.Cells tillhandahåller en klass[IArbetsbok](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) som representerar en Microsoft Excel-fil. De[IArbetsbok](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)klass tillhandahåller ett brett utbud av metoder för att hantera en Excel-fil. För att implementera delade vyer, använd[Dela](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a0e581a3a9528a767c57008521ee02b6f) metod för[IArbetsblad](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) klass. För att ta bort de delade rutorna, använd[Ta bort Split](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a5b554108c91f686e906400c26248eee5)metod.

exemplet använder vi en enkel mallfil som laddas, sedan tillämpas funktionen för delade paneler på en cell i det första kalkylbladet. Den uppdaterade filen sparas.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-SplitPanes.cpp" >}}
#### **Ta bort rutor**
 Ta bort delade rutor med hjälp av[Ta bort Split](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a5b554108c91f686e906400c26248eee5)metod.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-RemovingPanes.cpp" >}}
