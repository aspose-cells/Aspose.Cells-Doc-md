---
title: Undvik tomt sida i utdata PDF när det finns inget att skriva ut
type: docs
weight: 30
url: /sv/python-net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
description: Lär dig hur man undviker tom sida i utdata PDF när det inte finns något att skriva ut med Aspose.Cells för Python via .NET API.
keywords: Python Undvik tom sida i utdata PDF när det inte finns något att skriva ut
---

## **Möjliga användningsscenario**

När Excelfilen är tom och användaren sparar den till PDF med Aspose.Cells för Python via .NET, renderar den en tom sida i utdata-PDF. Ibland är detta standardbeteende oönskat. Aspose.Cells för Python via .NET tillhandahåller egenskapen [**PdfSaveOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/output_blank_page_when_nothing_to_print/) för att hantera detta problem. Om du sätter den som **false**, kommer [**CellsException**](https://reference.aspose.com/cells/python-net/aspose.cells/cellsexception/) att inträffa när det inte finns något att skriva ut i utdata-PDF.

## **Undvik tom sida i utmatnings-PDF när det inte finns något att skriva ut**

Följande exempelkod skapar en tom arbetsbok och sparar den sedan som PDF efter att ha satt egenskapen [**PdfSaveOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/output_blank_page_when_nothing_to_print/) som **false**. Eftersom det inte finns något att skriva ut i utdata-PDF, inträffar [**CellsException**](https://reference.aspose.com/cells/python-net/aspose.cells/cellsexception/) som visas nedan.

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.py" >}}

## **Undantag**

{{< highlight java >}}

 Aspose.Cells.CellsException was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
