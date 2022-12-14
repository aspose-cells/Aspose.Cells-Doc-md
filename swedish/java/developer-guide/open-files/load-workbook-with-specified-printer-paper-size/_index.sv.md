---
title: Ladda arbetsbok med angiven skrivarpappersstorlek
type: docs
weight: 790
url: /sv/java/load-workbook-with-specified-printer-paper-size/
---
{{% alert color="primary" %}} 

 Du kan ange önskad skrivarpappersstorlek när du laddar din arbetsbok med hjälp av[LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize\(int\)) metod. Observera att om du skapar en ny fil i MS Excel kommer du att se att pappersstorleken är densamma som inställningen för standardskrivaren i din maskin.

{{% /alert %}} 
## **Ladda arbetsbok med angiven skrivarpappersstorlek**
 Följande exempelkod illustrerar användningen av[LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize\(int\) metod. Den skapar först en arbetsbok och sparar den sedan i byte-arrayström i XLSX-format. Sedan laddar den med A5-pappersstorlek och sparar den i PDF-format. Sedan laddar den igen med A3-pappersstorlek och sparar den igen i PDF-format. Om du öppnar utdata-PDF-filerna och kontrollerar pappersstorleken ser du att de skiljer sig. Den ena är A5 och den andra är A3. Vänligen ladda ner[A5 utdata pdf](5473435.pdf) och[A3 utdata som PDF](5473436.pdf) genereras av koden för din referens.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadWorkbook-LoadWorkbook.java" >}}
