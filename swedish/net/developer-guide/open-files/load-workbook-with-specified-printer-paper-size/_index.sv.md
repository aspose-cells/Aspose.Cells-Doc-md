---
title: Ladda arbetsbok med angiven skrivarpappersstorlek
type: docs
weight: 430
url: /sv/net/load-workbook-with-specified-printer-paper-size/
---
{{% alert color="primary" %}}

 Du kan ange önskad skrivarpappersstorlek när du laddar din arbetsbok med hjälp av[**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/methods/setpapersize) metod. Observera att om du skapar en ny fil i MS Excel kommer du att se att pappersstorleken är densamma som inställningen för standardskrivaren i din maskin.

{{% /alert %}}

 Följande exempelkod illustrerar användningen av[**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/methods/setpapersize) metod. Den skapar först en arbetsbok och sparar den sedan i minnesström i XLSX-format. Sedan laddar den med A5-pappersstorlek och sparar den i PDF-format. Sedan laddar den igen med A3-pappersstorlek och sparar den igen i PDF-format. Om du öppnar utdata-PDF-filerna och kontrollerar pappersstorleken ser du att de skiljer sig. Den ena är A5 och den andra är A3. Vänligen ladda ner[A5-utgång PDF](5115234.pdf) och[A3-utgång PDF](5115233.pdf) genereras av koden för din referens.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LoadWorkbookWithPrinterSize-1.cs" >}}
