---
title: Undvik tom sida i utdata PDF när det inte finns något att skriva ut
type: docs
weight: 30
url: /sv/python-net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
description: Lär dig hur du undviker tom sida i utdata PDF när det inte finns något att skriva ut med Aspose.Cells for Python via .NET API.
keywords: Python Avoid Blank Page in Output PDF when there is Nothing to Print
---
##  **Möjliga användningsscenarier**

När Excel-filen är tom och användaren sparar den till Aspose.Cells med Aspose.Cells for Python via .NET, återger den en tom sida i utdata PDF. Ibland är detta standardbeteende oönskat. Aspose.Cells for Python via .NET tillhandahåller[**PdfSaveOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/output_blank_page_when_nothing_to_print/)egendom för att hantera denna fråga. Om du kommer att ställa in det som *falskt**, då[**CellsException**](https://reference.aspose.com/cells/python-net/aspose.cells/cellsexception/)kommer att inträffa när det inte finns något att skriva ut i utgången PDF.

##  **Undvik tom sida i utdata PDF när det inte finns något att skriva ut**

Följande exempelkod skapar en tom arbetsbok och sparar den sedan som PDF efter att ha ställt in[**PdfSaveOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/output_blank_page_when_nothing_to_print/)egendom som *falsk**. Eftersom det inte finns något att skriva ut i utgången PDF,[**CellsException**](https://reference.aspose.com/cells/python-net/aspose.cells/cellsexception/)sker enligt nedan.

##  **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.py" >}}

##  **Undantag**

{{< highlight "java" >}}

 Aspose.Cells.CellsException was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
