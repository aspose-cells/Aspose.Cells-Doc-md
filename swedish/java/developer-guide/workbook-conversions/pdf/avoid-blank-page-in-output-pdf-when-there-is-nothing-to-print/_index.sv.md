---
title: Undvik tomt sida i utdata PDF när det finns inget att skriva ut
type: docs
weight: 30
url: /sv/java/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
---

## **Möjliga användningsscenario**

När Excelfilen är tom och användaren sparar den som PDF med hjälp av Aspose.Cells så renderas en tom sida i utdatan PDF. Ibland är detta standardbeteendet oönskat. Aspose.Cells tillhandahåller [**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OutputBlankPageWhenNothingToPrint)-egenskapen för att hantera detta problem. Om du sätter den som falsk, då kommer [**CellsException**](https://reference.aspose.com/cells/java/com.aspose.cells/CellsException) att inträffa när det inte finns något att skriva ut i utdatan PDF.

## **Undvik tom sida i utmatnings-PDF när det inte finns något att skriva ut**

Följande exempelkod skapar en tom arbetsbok och sparar den sedan som utdatan PDF efter att ha satt [**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OutputBlankPageWhenNothingToPrint)-egenskapen som falsk. Eftersom det inte finns något att skriva ut i utdatan PDF, inträffar [**CellsException**](https://reference.aspose.com/cells/java/com.aspose.cells/CellsException) enligt nedan.

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.java" >}}

## **Undantag**

{{< highlight java >}}

 Exception in thread "main" com.aspose.cells.CellsException: There is nothing to output/print.

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.Workbook.a(Unknown Source)

	at com.aspose.cells.Workbook.save(Unknown Source)

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
