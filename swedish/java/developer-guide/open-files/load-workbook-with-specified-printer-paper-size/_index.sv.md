---
title: Ladda arbetsboken med angiven skrivarpappersstorlek
type: docs
weight: 790
url: /sv/java/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}} 

Du kan ange skrivarformatsstorleken för ditt val när du laddar din arbetsbok med metoden [LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize\(int\)). Vänligen notera, om du skapar en ny fil i MS Excel kommer du att upptäcka att pappersstorleken är densamma som inställningen för standard skrivaren i din dator.

{{% /alert %}} 
## **Ladda arbetsbok med specificerad pappersstorlek**
Följande exempelkod visar användningen av [LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize\(int\)) metoden. Det skapar först en arbetsbok, sparar den sedan i byte array-ström i XLSX-format. Sedan laddar den den med A5 pappersstorlek och sparar den i PDF-format. Sedan laddar den den igen med A3 pappersstorlek och sparar den igen i PDF-format. Om du öppnar de utdata PDF:erna och kontrollerar deras pappersstorlek kommer du att se att de är olika. En är A5 och den andra är A3. Var god ladda ner [A5 utdata PDF](5473435.pdf) och [A3 utdata PDF](5473436.pdf) genererade av koden för din referens.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadWorkbook-LoadWorkbook.java" >}}
