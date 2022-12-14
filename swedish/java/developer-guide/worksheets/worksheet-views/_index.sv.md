---
title: Arbetsbladsvyer
type: docs
weight: 10
url: /sv/java/worksheet-views/
---
## **Förhandsvisning av sidbrytning**
Alla kalkylblad kan visas i två lägen:

- Normal vy.
- Förhandsgranskning av sidbrytning.

En normal vy är ett kalkylblads standardvy. Förhandsgranskning av sidbrytning är en redigeringsvy som visar ett kalkylblad när det skrivs ut. Förhandsgranskning av sidbrytningar visar vilken data som kommer att finnas på varje sida så att du kan justera utskriftsområdet och sidbrytningarna. Genom att använda Aspose.Cells kan utvecklare aktivera normala visnings- eller sidbrytningslägen.
### **Styra visningslägen**
 Aspose.Cells tillhandahåller en[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) klass som representerar en Microsoft Excel-fil. De[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) klass innehåller en[Arbetsbladssamling](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)som ger åtkomst till varje kalkylblad i en Excel-fil.

 Ett arbetsblad representeras av[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass. De[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) class tillhandahåller ett brett utbud av egenskaper och metoder för att hantera kalkylblad. För att aktivera normala eller sidbrytningsförhandsvisningslägen, använd[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass'[setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)metod.
#### **Aktiverar normal vy**
Ställ in valfritt kalkylblad till normal vy med hjälp av[setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview) metod för[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass och godkänt**falsk** som en parameter.
#### **Aktiverar förhandsgranskning av sidbrytning**
Ställ in valfritt kalkylblad till förhandsvisning av sidbrytning med hjälp av[setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)metod för[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass och godkänt**Sann**som en parameter.

 Ett komplett exempel ges nedan som visar användningen av[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass'[setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)metod för att aktivera förhandsgranskningsläget för sidbrytning för det första kalkylbladet i Excel-filen.

På skärmdumpen nedan kan du se att filen Book1.xls är i normalvy.

**Book1.xls: Arbetsblad före modifiering** 

![todo:image_alt_text](worksheet-views_1.png)

 Book1.xls öppnas med[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)klass och läget växlas till förhandsvisning av sidbrytning för det första kalkylbladet. Den ändrade filen sparas som output.xls.

**Output.xls: kalkylblad efter modifiering** 

![todo:image_alt_text](worksheet-views_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-PageBreakPreview-PageBreakPreview.java" >}}
## **Zoomfaktor**
Microsoft Excel tillhandahåller en funktion som låter användare ställa in ett kalkylblads zoom- eller skalningsfaktor. Den här funktionen hjälper användare att se kalkylbladets innehåll i mindre eller större vyer. Användare kan ställa in zoomfaktorn till valfritt värde.

**Ställa in zoomfaktorn med Microsoft Excel** 

![todo:image_alt_text](worksheet-views_3.png)

Aspose.Cells tillåter också utvecklare att ställa in kalkylbladets zoomfaktor.
### **Styra zoomfaktorn**
Aspose.Cells tillhandahåller en[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) klass som representerar en Microsoft Excel-fil. De[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) klass innehåller en[Arbetsbladssamling](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)som ger åtkomst till varje kalkylblad i en Excel-fil.

 Ett arbetsblad representeras av[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass. De[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) class tillhandahåller ett brett utbud av egenskaper och metoder för att hantera kalkylblad. För att ställa in ett kalkylblads zoomfaktor, använd[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass'[setZoom](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Zoom)metod.

 Ett komplett exempel ges nedan som visar hur man använder[setZoom](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Zoom)metod för att ställa in zoomfaktorn för det första kalkylbladet i en Excel-fil.

I skärmdumpen nedan kan du se Book1.xls-filen i standardvyn.

**Book1.xls: kalkylblad före ändring** 

![todo:image_alt_text](worksheet-views_4.png)

 Book1.xls-filen öppnas med[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)klass och zoomfaktorn för det första kalkylbladet är satt till 75. Den modifierade filen sparas som output.xls.

**Output.xls: kalkylblad efter modifiering** 

![todo:image_alt_text](worksheet-views_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ZoomFactor-ZoomFactor.java" >}}
## **Frys rutor**
Frys rutor är en funktion som tillhandahålls av Microsoft Excel. Frysa rutor låter dig välja data som ska förbli synliga när du rullar i ett kalkylblad.

**Använda frysrutor i Microsoft Excel** 

![todo:image_alt_text](worksheet-views_6.png)

Aspose.Cells tillåter också utvecklare att tillämpa frysrutor på kalkylblad under körning.

Aspose.Cells tillhandahåller en[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) klass som representerar en Microsoft Excel-fil. De[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) klass innehåller en[Arbetsbladssamling](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)som ger åtkomst till varje kalkylblad i en Excel-fil.

 Ett arbetsblad representeras av[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass. De[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) class tillhandahåller ett brett utbud av egenskaper och metoder för att hantera kalkylblad. För att konfigurera frysrutor, ring[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass'[freezePanes](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\) ) metod. De[freezePanes](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\)) metod tar följande parametrar:

- **Rad**, radindexet för cellen som frysningen börjar från.
- **Kolumn**, kolumnindex för cellen som frysningen startar från.
- **Frysta rader**, antalet synliga rader i den övre rutan.
- **Frysta kolonner**, antalet synliga kolumner i den vänstra rutan

 Ett komplett exempel ges nedan som visar hur man använder[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass'[freezePanes](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\)) metod för att frysa rader och kolumner (med början från C4, representerade av 4:e raden och 3:e kolumnen, där raderna och kolumnerna börjar från 0 index) i det första kalkylbladet i Excel-filen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-FreezePanes-FreezePanes.java" >}}


I skärmdumpen nedan kan du se filen Book1.xls utan frysrutor.

**Book1.xls: kalkylbladsvy före eventuell ändring** 

![todo:image_alt_text](worksheet-views_7.png)

 Book1.xls-filen öppnas med[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)klass och sedan fryses några rader och kolumner på det första kalkylbladet. Den ändrade filen sparas som output.xls.

**Outlook.xls: kalkylbladsvy efter ändring** 

![todo:image_alt_text](worksheet-views_8.png)
## **Delade rutor**
Om du behöver dela skärmen för att få två olika vyer i samma kalkylblad, dela rutor. Microsoft Excel erbjuder en mycket praktisk funktion som låter dig visa mer än en kopia av ditt kalkylblad och för att du ska kunna rulla igenom varje ruta i ditt kalkylblad oberoende av varandra: delade paneler.

Rutorna fungerar samtidigt. Om du gör en ändring i den ena, visas ändringen samtidigt i den andra. Aspose.Cells tillhandahåller funktionen för delade rutor för användarna.
### **Applicera och ta bort delade rutor**
#### **Dela rutor**
Aspose.Cells tillhandahåller en[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) klass som representerar en Microsoft Excel-fil. De[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)class tillhandahåller ett brett utbud av egenskaper och metoder för att hantera Excel-filer. För att implementera delade vyer, använd[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass'[dela](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#split\(\) ) metod. För att ta bort delade rutor, använd[ta bort Split](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#removeSplit\(\)) metod.

exemplet använder vi en enkel mallfil som laddas, sedan tillämpas funktionen för delade paneler på en cell i det första kalkylbladet. Den uppdaterade filen sparas.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SplitPanes-SplitPanes.java" >}}



Efter att ha kört ovanstående kod har den genererade filen en delad vy.

**Dela rutor i utdatafilen** 

![todo:image_alt_text](worksheet-views_9.png)
#### **Ta bort rutor**
 Utvecklare kan ta bort delade rutor med hjälp av[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass'[ta bort Split](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#removeSplit\(\)) metod.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovePanes-RemovePanes.java" >}}


## **Förhandsämnen**
- [Döljer visningen av nollvärden i arbetsbladet](/cells/sv/java/hiding-the-display-of-zero-values-in-the-worksheet/)
- [Ställ in kalkylbladsflikfärg](/cells/sv/java/set-worksheet-tab-color/)
- [Visa och dölj element](/cells/sv/java/show-and-hide-elements/)
- [Visa formler istället för värden i ett kalkylblad](/cells/sv/java/show-formulas-instead-of-values-in-a-worksheet/)
- [Använd alternativ för felkontroll](/cells/sv/java/use-error-checking-options/)
