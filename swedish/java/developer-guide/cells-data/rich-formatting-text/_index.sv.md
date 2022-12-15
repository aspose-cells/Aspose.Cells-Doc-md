---
title: Få åtkomst till och uppdatera delarna av Rich Text på Cell
linktitle: Rik formateringstext
type: docs
weight: 440
url: /sv/java/access-and-update-the-portions-of-rich-text-of-cell/
---
{{% alert color="primary" %}} 

Aspose.Cells låter dig komma åt och uppdatera delarna av cellens rich text. För detta ändamål kan du använda metoderna Cell.getCharacters() och Cell.setCharacters(). Dessa metoder kommer att returnera och acceptera mängden FontSetting-objekt som du kan använda för att komma åt och uppdatera olika egenskaper för teckensnitt som teckensnittsnamn, teckensnittsfärg, fetstil etc.

{{% /alert %}} 
## **Få åtkomst till och uppdatera delarna av Rich Text på Cell**
 Följande kod visar användningen av metoderna Cell.getCharacters() och Cell.setCharacters() med hjälp av[källkod excel-fil](5472937.xlsx) som du kan ladda ner från den medföljande länken. Excel-källfilen har en rik text i cellen A1. Den har 3 delar och varje del har olika typsnitt. Vi kommer åt dessa delar och uppdaterar den första delen med ett nytt teckensnittsnamn. Slutligen sparar den arbetsboken som[output excel-fil](5472930.xlsx) . När du öppnar den kommer du att se att teckensnittet för den första delen av texten har ändrats till**"Arial"**.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessAndUpdatePortions-AccessAndUpdatePortions.java" >}}




## **Konsolutgång**
 Här är konsolutgången för ovanstående exempelkod med hjälp av[källkod excel-fil](5472937.xlsx).

{{< highlight "java" >}}

 Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}
