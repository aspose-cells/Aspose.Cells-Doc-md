---
title: Arbetsboks vy
type: docs
weight: 10
url: /sv/java/worksheet-views/
---

## **Sidbrytning Förhandsgranskning**
Alla arbetsblad kan visas i två lägen:

- Normal vy.
- Sidbrytningsvy.

En normal vy är ett kalkylblads standardvy. Sidbrytningsgranskning är en redigeringsvy som visar ett kalkylblad som det kommer att skrivas ut. Sidbrytningsgranskning visar vilka data som kommer att hamna på varje sida så att du kan justera utskriftsområdet och sidbrytningarna. Med Aspose.Cells kan utvecklare aktivera normal vy eller sidbrytningsgranskningslägen.
### **Styra vynlägen**
Aspose.Cells tillhandahåller en [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-klass som representerar en Microsoft Excel-fil. [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-klassen innehåller en [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) som gör det möjligt att komma åt varje kalkylblad i en Excel-fil.

Ett kalkylblad representeras av klassen [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)-klassen tillhandahåller ett brett utbud av egenskaper och metoder för att hantera kalkylblad. För att aktivera normal eller sidbrytningsgranskningslägen, använd [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)-klassens [setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)-metod.
#### **Aktivera normal vy**
Ställ in vilket kalkylblad som helst till normal vy genom att använda [setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)-metoden i [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)-klassen och skicka **false** som parameter.
#### **Aktivera sidbrytningsvy**
Ställ in vilket kalkylblad som helst till sidbrytningsgranskningsläge med hjälp av [setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)-metoden i [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)-klassen och skicka **true** som parameter.

Ett komplett exempel ges nedan som demonstrerar användningen av [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)-klassens [setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)-metod för att aktivera sidbrytningsgranskningsläge för den första kalkylbladet i Excel-filen.

På skärmbilden nedan kan se att filen Book1.xls är i Normal vy.

**Book1.xls: Kalkylblad före ändring** 

![todo:image_alt_text](worksheet-views_1.png)

Book1.xls öppnas med [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-klassen och läget ändras till sidbrytningsgranskningsläge för det första kalkylbladet. Den ändrade filen sparas som output.xls.

**Ouput.xls: kalkylblad efter ändring** 

![todo:image_alt_text](worksheet-views_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-PageBreakPreview-PageBreakPreview.java" >}}
## **Zoomfaktor**
Microsoft Excel har en funktion som låter användare sätta en arbetsblads zoom- eller skalfaktor. Denna funktion hjälper användare att se arbetsbladsinnehållet i mindre eller större visningar. Användare kan sätta zoom-faktorn till vilket värde som helst.

**Inställning av zoomfaktor med Microsoft Excel** 

![todo:image_alt_text](worksheet-views_3.png)

Aspose.Cells tillåter också utvecklare att ange kalkylbladets zoomfaktor.
### **Kontrollera zoomfaktorn**
Aspose.Cells tillhandahåller en [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-klass som representerar en Microsoft Excel-fil. [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-klassen innehåller en [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) som gör det möjligt att komma åt varje kalkylblad i en Excel-fil.

Ett kalkylblad representeras av [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klassen. [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klassen ger ett brett utbud av egenskaper och metoder för att hantera kalkylblad. För att ställa in ett kalkylblads zoom-faktor, använd [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klassens [setZoom](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Zoom) metod.

Ett komplett exempel ges nedan som visar hur man använder [setZoom](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Zoom) metoden för att ställa in zoom-faktorn för det första kalkylbladet i en Excel-fil.

På skärmbilden nedan kan du se att filen Book1.xls är i standardvy.

**Book1.xls: arbetsblad före modifiering** 

![todo:image_alt_text](worksheet-views_4.png)

Filen Book1.xls öppnas med [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-klassen och zoomfaktorn för det första kalkylbladet ställs in till 75. Den ändrade filen sparas som output.xls.

**Output.xls: kalkylblad efter ändring** 

![todo:image_alt_text](worksheet-views_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ZoomFactor-ZoomFactor.java" >}}
## **Frys Fönsterpaneler**
Frysa rutor är en funktion som tillhandahålls av Microsoft Excel. Att frysa rutor gör att man kan välja data som ska förbli synlig när man rullar i ett arbetsblad.

**Att använda frysfönster i Microsoft Excel** 

![todo:image_alt_text](worksheet-views_6.png)

Aspose.Cells tillåter också utvecklare att tillämpa frysfönster på kalkylblad dynamiskt.

Aspose.Cells tillhandahåller en [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-klass som representerar en Microsoft Excel-fil. Workbook-klassen innehåller en [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) som ger åtkomst till varje kalkylblad i en Excel-fil.

Ett kalkylblad representeras av [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klassen. [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klassen ger ett brett utbud av egenskaper och metoder för att hantera kalkylblad. För att konfigurera frysningar, använd [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klassens [freezePanes](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes-int-int-int-int-) metod. [freezePanes](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes-int-int-int-int-) metoden tar följande parametrar:

- **Rad**, radindexet för cellen som frysen ska starta från.
- **Kolumn**, kolumnindexet för cellen som frysen ska starta från.
- **Frusna rader**, antalet synliga rader i toppfönstret.
- **Frusna kolumner**, antalet synliga kolumner i vänstra fönstret.

Ett fullständigt exempel ges nedan som visar hur man använder [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klassens [freezePanes](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes-int-int-int-int-) metod för att frysa rader och kolumner (från C4, som är representerad av rad 4 och kolumn 3, där rader och kolumner börjar från index 0) i det första kalkylbladet i Excel-filen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-FreezePanes-FreezePanes.java" >}}


På skärmdumpen nedan kan du se filen Book1.xls utan frysta rutor.

**Book1.xls: kalkylbladsvisning före eventuell ändring** 

![todo:image_alt_text](worksheet-views_7.png)

Fil1.xls bok öppnas med klassen [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) and then a few rows and columns are frozen on the first worksheet. The modified file is saved as output.xls.

**Outlook.xls: kalkylbladsvy efter ändring** 

![todo:image_alt_text](worksheet-views_8.png)
## **Dela rutor**
Om du behöver dela skärmen för att få två olika vyer i samma arbetsblad, dela rutor. Microsoft Excel erbjuder en mycket praktisk funktion som gör att du kan se mer än en kopia av ditt arbetsblad och för dig att kunna bläddra igenom varje ruta av ditt arbetsblad oberoende av varandra: dela rutor.

Fönstren fungerar samtidigt. Om du gör en förändring i ett, visas förändringen samtidigt i den andra. Aspose.Cells tillhandahåller split panes-funktionen för användarna.
### **Sätta på och Ta bort Delade paneler**
#### **Dela Fönster**
Aspose.Cells tillhandahåller en [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) klass som representerar en Microsoft Excel-fil. Klassen [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) erbjuder ett brett utbud av egenskaper och metoder för att hantera Excel-filer. För att implementera split view, använd [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klassens [split](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#split--) metod. För att ta bort split-vyer, använd [removeSplit](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#removeSplit--) metod.

I exemplet använder vi en enkel mallfil som laddas, sedan används inställningar för att dela rutor på en cell i det första arbetsbladet. Den uppdaterade filen sparas.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SplitPanes-SplitPanes.java" >}}



Efter att ha kört ovanstående kod har den genererade filen en delad vy.

**Delade rutor i output-filen** 

![todo:image_alt_text](worksheet-views_9.png)
#### **Ta bort rutor**
Utvecklare kan ta bort split-vyer med hjälp av [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klassens [removeSplit](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#removeSplit--) metod.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovePanes-RemovePanes.java" >}}


## **Fortsatta ämnen**
- [Dölja visning av nollvärden i kalkylbladet](/cells/sv/java/hiding-the-display-of-zero-values-in-the-worksheet/)
- [Ange färg på kalkylbladsflik](/cells/sv/java/set-worksheet-tab-color/)
- [Visa och Dölj Element](/cells/sv/java/show-and-hide-elements/)
- [Visa formler istället för värden i ett kalkylblad](/cells/sv/java/show-formulas-instead-of-values-in-a-worksheet/)
- [Använd felkontrollalternativ](/cells/sv/java/use-error-checking-options/)
{{< app/cells/assistant language="java" >}}
