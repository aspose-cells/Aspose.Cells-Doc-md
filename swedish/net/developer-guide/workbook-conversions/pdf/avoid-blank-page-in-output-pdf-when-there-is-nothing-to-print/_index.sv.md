---
title: Undvik tom sida i utdata-PDF när det inte finns något att skriva ut
type: docs
weight: 30
url: /sv/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
---
## **Möjliga användningsscenarier**

När Excel-filen är tom och användaren sparar den till PDF med Aspose.Cells, renderar den en tom sida i utdata-PDF. Ibland är detta standardbeteende oönskat. Aspose.Cells tillhandahåller[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint) egendom för att hantera denna fråga. Om du ställer in det som**falsk**, då[**CellsException**](https://reference.aspose.com/cells/net/aspose.cells/cellsexception)kommer att inträffa när det inte finns något att skriva ut i den utgående PDF-filen.

## **Undvik tom sida i utdata-PDF när det inte finns något att skriva ut**

Följande exempelkod skapar en tom arbetsbok och sparar den sedan som PDF efter att ha ställt in[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint) egendom som**falsk**. Eftersom det inte finns något att skriva ut i den utgående PDF-filen,[**CellsException**](https://reference.aspose.com/cells/net/aspose.cells/cellsexception)sker enligt nedan.

## **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.cs" >}}

## **Undantag**

{{< highlight "java" >}}

 Aspose.Cells.CellsException was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
