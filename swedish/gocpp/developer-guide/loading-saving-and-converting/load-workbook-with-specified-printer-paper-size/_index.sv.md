---
title: Ladda arbetsboken med angiven skrivarpappersstorlek
type: docs
weight: 430
url: /sv/go-cpp/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}}

Du kan specificera pappersstorleken för skrivaren du vill medan du laddar din arbetsbok med metoden [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/go-cpp/loadoptions/setpapersize/). Vänligen observera att om du skapar en ny fil i MS Excel, kommer du att se att pappersstorleken är densamma som inställningen för standardskrivaren på din maskin.

{{% /alert %}}

Följande exempel visar användningen av [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/go-cpp/loadoptions/setpapersize/) metoden. Den först skapar en arbetsbok och sparar den i en minnesström i XLSX-format. Sedan laddar den den med A5-pappersstorlek och sparar den i PDF-format. Därefter laddar den om den med A3-pappersstorlek och sparar igen i PDF. Om du öppnar de genererade PDF:erna och kontrollerar deras pappersstorlek, kommer du att se att de är olika. En är A5 och den andra är A3. Vänligen ladda ner [A5 PDF](PrinterSize-a5_out.pdf) och [A3 PDF](PrinterSize-a3_out.pdf) som genererats av koden för referens.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LoadWorkbookWithPrinterSize.go" >}}
