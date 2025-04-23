---
title: Ladda arbetsboken med angiven skrivarpappersstorlek
type: docs
weight: 430
url: /sv/cpp/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}}

Du kan ange skrivarpappersstorlek efter eget val när du laddar din arbetsbok med hjälp av [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setpapersize/) metoden. Observera att om du skapar en ny fil i MS Excel, kommer du att se att papperstorleken är densamma som inställningen för standardskrivaren på din dator.

{{% /alert %}}

Följande exempel kod illustrerar användningen av [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setpapersize/)-metoden. Den skapar först ett arbetsbok, sparar det i en minnesström i XLSX-format. Sedan laddar den det med A5-pappersstorlek och sparar det i PDF-format. Sedan laddar den det igen med A3-pappersstorlek och sparar det på nytt i PDF-format. Om du öppnar utgångs-PDF:erna och kontrollerar deras pappersstorlek, kommer du att se att de är olika. En är A5 och den andra är A3. Vänligen ladda ner [A5 utdata PDF](PrinterSize-a5_out.pdf) och [A3 utdata PDF](PrinterSize-a3_out.pdf) genererade av koden för referens.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadWorkbookWithPrinterSize-1.cpp" >}}
