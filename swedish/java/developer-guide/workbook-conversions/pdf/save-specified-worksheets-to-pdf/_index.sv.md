---
title: Spara angivna arkpapper till PDF
type: docs
weight: 51
url: /sv/java/save-specified-worksheets-to-pdf/
---

Som standard sparar Aspose.Cells alla **synliga** arkpapper i en arbetsbok till en pdf-fil. Med [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-) alternativet kan du spara angivna arkpapper till en pdf-fil. t.ex. kan du spara aktivt arkpapp till pdf, spara alla arkpapper (både synliga och dolda arkpapper) till pdf, spara anpassade flera arkpapper till pdf.

## **Spara aktivt arkpapp till PDF**

Om du bara vill exportera det aktiva arkpappret till pdf, kan du uppnå detta genom att skicka [**SheetSet.Active**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getActive--) till [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-) alternativet.

Arket `Ark2` är det aktiva arkpappret i källfilen [sheetset-example.xlsx](sheetset-example.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-ActiveSheetToPdf.java" >}}

## **Spara alla arkpapper till PDF**

[**SheetSet.Visible**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getVisible--) indikerar synliga ark i en arbetsbok, och [**SheetSet.All**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getAll--) indikerar alla ark inklusive både synliga ark och dolda/osynliga ark i en arbetsbok. Om du vill exportera alla ark till pdf, kan du helt enkelt skicka [**SheetSet.All**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getAll--) till [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-) alternativet.

Källfilen [sheetset-example.xlsx](sheetset-example.xlsx) innehåller alla fyra ark med dolt ark `Ark3`.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-AllSheetsToPdf.java" >}}

## **Spara angivna arbetsblad som PDF**
Om du vill exportera önskade/anpassade flera ark till pdf, kan du uppnå detta genom att skicka flera arkindex till [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-) alternativet.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-MultiSheetsToPdf.java" >}}

{{% alert color="primary" %}} 

Om ditt kalkylblad innehåller formler, är det bäst att anropa [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook/#calculateFormula--) strax innan du renderar kalkylbladet till PDF-format. Genom att göra det säkerställs att formelberoende värden beräknas om och de korrekta värdena renderas i PDF-filen.

{{% /alert %}}
