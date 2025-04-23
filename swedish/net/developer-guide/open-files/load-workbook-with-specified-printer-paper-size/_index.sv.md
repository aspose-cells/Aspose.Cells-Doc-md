---
title: Ladda arbetsboken med angiven skrivarpappersstorlek
type: docs
weight: 430
url: /sv/net/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}}

Du kan ange skrivarpappersstorlek efter eget val när du laddar din arbetsbok med hjälp av [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/methods/setpapersize) metoden. Observera att om du skapar en ny fil i MS Excel, kommer du att se att papperstorleken är densamma som inställningen för standardskrivaren på din dator.

{{% /alert %}}

Följande exempelkod illustrerar användningen av [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/methods/setpapersize) metoden. Det skapar först en arbetsbok, sparar den sedan i minnesström i XLSX-format. Sedan laddar den den med pappersstorleken A5 och sparar den i PDF-format. Sedan laddar den den igen med pappersstorleken A3 och sparar den igen i PDF-format. Om du öppnar utdatans PDF:er och kontrollerar deras papperstorlek, kommer du att se att de är olika. En är A5 och den andra är A3. Ladda ned [A5 utdatan PDF](5115234.pdf) och [A3 utdatan PDF](5115233.pdf) genererad av koden för din referens.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LoadWorkbookWithPrinterSize-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
