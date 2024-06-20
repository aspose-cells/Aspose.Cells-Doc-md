---
title: Undvik tomt sida i utdata PDF när det finns inget att skriva ut
type: docs
weight: 30
url: /sv/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
---

## **Möjliga användningsscenario**

När Excelfilen är tom och användaren sparar den som PDF med hjälp av Aspose.Cells så renderas en tom sida i utdatan PDF. Ibland är detta standardbeteendet oönskat. Aspose.Cells tillhandahåller [**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint)-egenskapen för att hantera detta problem. Om du sätter den som falsk, då kommer [**CellsException**](https://reference.aspose.com/cells/net/aspose.cells/cellsexception) att inträffa när det inte finns något att skriva ut i utdatan PDF.

## **Undvik tom sida i utmatnings-PDF när det inte finns något att skriva ut**

Följande exempelkod skapar en tom arbetsbok och sparar den sedan som PDF efter att ha satt egenskapen [**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint) som **false**. Eftersom det inte finns något att skriva ut i utdata-PDF, inträffar [**CellsException**](https://reference.aspose.com/cells/net/aspose.cells/cellsexception) som visas nedan.

## **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.cs" >}}

## **Undantag**

{{< highlight java >}}

 Aspose.Cells.CellsException was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
