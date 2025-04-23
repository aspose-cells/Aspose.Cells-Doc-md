---
title: Ladda arbetsboken med angiven skrivarpappersstorlek
type: docs
weight: 790
url: /sv/java/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}} 

Du kan specificera valfri pappersstorlek på skrivaren när du laddar din arbetsbok med hjälp av metoden [LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize-int-). Observera, om du skapar en ny fil i MS Excel, kommer pappersstorleken att vara densamma som standardskrivarens inställning i din maskin.

{{% /alert %}} 
## **Ladda arbetsbok med specificerad pappersstorlek**
Följande exempel visar användningen av metoden [LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize-int-). Det skapar först ett arbetsbok, sparar det i en byte-array i XLSX-format. Sedan laddar det det med A5-papper och sparar det i PDF-format. Därefter laddar det det igen med A3-papper och sparar det i PDF-format. Om du öppnar utdata-PDF:erna och kontrollerar deras pappersstorlek, kommer du att se att de är olika. Den ena är A5 och den andra är A3. Vänligen ladda ner [A5 output PDF](5473435.pdf) och [A3 output PDF](5473436.pdf) som genererats av koden för referens.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadWorkbook-LoadWorkbook.java" >}}
{{< app/cells/assistant language="java" >}}
