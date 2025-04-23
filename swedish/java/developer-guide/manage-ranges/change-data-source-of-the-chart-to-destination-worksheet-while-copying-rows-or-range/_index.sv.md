---
title: Ändra datakällan för diagrammet till destinationskalkylbladet samtidigt som du kopierar rader eller område
type: docs
weight: 850
url: /sv/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **Möjliga användningsscenario**
När du kopierar rader eller område som innehåller diagram till ny arbetsblad, ändras inte datakällan för diagrammet. Till exempel, om datakällan för diagrammet är =Ark1!$A$1:$B$4, kommer efter kopiering av rader eller område till nytt arbetsblad, kommer datakällan fortfarande förbli densamma dvs =Ark1!$A$1:$B$4. Det hänvisar fortfarande till det gamla arbetsbladet dvs. Ark1. Detta är också Microsoft Excel-beteendet. Men om du vill att det ska hänvisa till det nya destinationsarket, vänligen använd CopyOptions.ReferToDestinationSheet-egenskapen och ställa in den till true vid anropet Cells.CopyRows() metoden. Nu om ditt destinationsark är DestSheet, kommer datakällan för ditt diagram att ändra från =Ark1!$A$1:$B$4 till =DestSheet!$A$1:$B$4.
## **Ändra datakällan för diagrammet till destinationskalkylbladet samtidigt som du kopierar rader eller område**
Följande exempelkod förklarar användningen av CopyOptions.ReferToDestinationSheet-egenskapen när du kopierar rader eller område som innehåller diagram till nytt arbetsblad. Koden använder den [prov Excel-filen](5472284.xlsx) och genererar den [utdata Excel-filen](5472283.xlsx). Skärmbilden visar att datakällan för diagrammet i [utdata Excel-filen](5472283.xlsx) nu hänvisar till DestSheet istället för Sheet1.

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeDataSource-ChangeDataSource.java" >}}






{{< app/cells/assistant language="java" >}}
