---
title: Ladda arbetsboken med angiven skrivarpappersstorlek
type: docs
weight: 430
url: /sv/cpp/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}}

Du kan ange skrivarpappersstorlek efter eget val när du laddar din arbetsbok med hjälp av [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setpapersize/) metoden. Observera att om du skapar en ny fil i MS Excel, kommer du att se att papperstorleken är densamma som inställningen för standardskrivaren på din dator.

{{% /alert %}}

Följande provkod illustrerar användningen av [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setpapersize/)-metoden. Den skapar först en arbetsbok, sparar den sedan i minnesström i XLSX-format. Därefter laddas den med pappersstorleken A5 och sparas i PDF-format. Sedan laddas den igen med pappersstorleken A3 och sparas igen i PDF-format. Om du öppnar de genererade PDF-filerna och kontrollerar deras pappersstorlek kommer du att se att de är olika. En är A5 och den andra är A3. Vänligen ladda ner [A5 output PDF](PrinterSize-a5_out.pdf) och [A3 output PDF](PrinterSize-a3_out.pdf) genererade av koden för din referens.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadWorkbookWithPrinterSize-1.cpp" >}}
