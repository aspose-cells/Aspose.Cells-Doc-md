---
title: Åtkomst och uppdatering av delar av riktad text från cellen
linktitle: Riktad formateringstext
type: docs
weight: 440
url: /sv/java/access-and-update-the-portions-of-rich-text-of-cell/
---

{{% alert color="primary" %}} 

Aspose.Cells tillåter dig att komma åt och uppdatera delar av den rikta texten i cellen. För detta ändamål kan du använda metoderna Cell.getCharacters() och Cell.setCharacters(). Dessa metoder kommer att returnera och acceptera en array av FontSetting-objekt som du kan använda för att komma åt och uppdatera olika egenskaper hos teckensnitt som teckensnittsnamn, teckenfärg, fetstil etc.

{{% /alert %}} 
## **Åtkomst och uppdatering av delar av riktad text från cellen**
Följande kod demonstrerar användningen av Cell.getCharacters() och Cell.setCharacters() metoden med [källexcelfilen](5472937.xlsx) som du kan ladda ner från den tillhandahållna länken. Källexcelfilen har riktad text i cellen A1. Den har 3 delar och varje del har olika teckensnitt. Vi kommer att komma åt dessa delar och uppdatera den första delen med nytt teckensnittsnamn. Slutligen sparar det arbetsboken som [utdataexcelfilen](5472930.xlsx). När du öppnar det kommer du att märka att teckensnittet för den första delen av texten har ändrats till **"Arial"**.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessAndUpdatePortions-AccessAndUpdatePortions.java" >}}




## **Konsoloutput**
Här är konsolutdatan för den ovanstående exempelkoden med [källexcelfilen](5472937.xlsx).

{{< highlight java >}}

 Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}
