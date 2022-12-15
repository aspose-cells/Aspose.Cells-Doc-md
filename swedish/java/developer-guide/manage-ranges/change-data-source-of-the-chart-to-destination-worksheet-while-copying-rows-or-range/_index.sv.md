---
title: Ändra datakälla för diagrammet till målarbetsblad medan du kopierar rader eller intervall
type: docs
weight: 850
url: /sv/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---
## **Möjliga användningsscenarier**
När du kopierar rader eller intervall som innehåller diagram till ett nytt kalkylblad, ändras inte datakällan för diagrammet. Till exempel, om datakällan för diagrammet är =Sheet1!$A$1:$B$4, efter kopiering av rader eller intervall till nytt kalkylblad, kommer datakällan att förbli densamma, dvs. =Sheet1!$A$1:$B$4. Det hänvisar fortfarande till det gamla kalkylbladet, dvs. Sheet1. Detta är också Microsoft Excel-beteendet. Men om du vill att det hänvisar till det nya målarbetsbladet, använd egenskapen CopyOptions.ReferToDestinationSheet och ställ in det som sant medan du anropar metoden Cells.CopyRows(). Om ditt målark är DestSheet kommer datakällan för ditt diagram att ändras från =Sheet1!$A$1:$B$4 till =DestSheet!$A$1:$B$4.
## **Ändra datakälla för diagrammet till målarbetsblad medan du kopierar rader eller intervall**
Följande exempelkod förklarar användningen av CopyOptions.ReferToDestinationSheet-egenskapen när du kopierar rader eller intervall som innehåller diagram till ett nytt kalkylblad. Koden använder[exempel på excel-fil](5472284.xlsx) och genererar[output excel-fil](5472283.xlsx) . Skärmdumpen visar att datakällan för diagrammet in[output excel-fil](5472283.xlsx) hänvisar nu till DestSheet istället för Sheet1.

![todo:image_alt_text](change-data-source-of-the-chart_1.png)







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeDataSource-ChangeDataSource.java" >}}






