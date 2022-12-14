---
title: Undvik tom sida i utdata-PDF när det inte finns något att skriva ut
type: docs
weight: 30
url: /sv/java/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
---
## **Möjliga användningsscenarier**

När Excel-filen är tom och användaren sparar den till PDF med Aspose.Cells, renderar den en tom sida i utdata-PDF. Ibland är detta standardbeteende oönskat. Aspose.Cells tillhandahåller[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OutputBlankPageWhenNothingToPrint) egendom för att hantera denna fråga. Om du ställer in det som**falsk**, då[**CellsException**](https://reference.aspose.com/cells/java/com.aspose.cells/CellsException)kommer att inträffa när det inte finns något att skriva ut i den utgående PDF-filen.

## **Undvik tom sida i utdata-PDF när det inte finns något att skriva ut**

Följande exempelkod skapar en tom arbetsbok och sparar den sedan som utdata-PDF efter att ha ställt in[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OutputBlankPageWhenNothingToPrint) egendom som**falsk**. Eftersom det inte finns något att skriva ut i den utgående PDF-filen,[**CellsException**](https://reference.aspose.com/cells/java/com.aspose.cells/CellsException)sker enligt nedan.

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.java" >}}

## **Undantag**

{{< highlight "java" >}}

 Exception in thread "main" com.aspose.cells.CellsException: There is nothing to output/print.

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.Workbook.a(Unknown Source)

	at com.aspose.cells.Workbook.save(Unknown Source)

{{< /highlight >}}
