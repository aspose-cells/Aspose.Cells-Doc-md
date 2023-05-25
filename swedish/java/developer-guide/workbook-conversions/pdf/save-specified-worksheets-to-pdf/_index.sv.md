---
title: Spara specificerade arbetsblad till PDF
type: docs
weight: 51
url: /sv/java/save-specified-worksheets-to-pdf/
---
 Som standard sparar Aspose.Cells alla**synlig** Kalkylblad i en arbetsbok till pdf-fil. Med**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)** alternativet kan du spara specificerade kalkylblad till pdf-fil. t.ex. kan du spara aktivt kalkylblad till pdf, spara alla kalkylblad (både synliga och dolda kalkylblad) till pdf, spara anpassade flera kalkylblad till pdf.

##  **Spara aktivt arbetsblad till PDF**

 Om du bara vill exportera aktivt ark till pdf kan du uppnå detta genom att godkänna**[`SheetSet.Active`](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getActive--)** till**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)** alternativ.

 Arket `Sheet2` är det aktiva arket för källfilen[arkuppsättning-exempel.xlsx](sheetset-example.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-ActiveSheetToPdf.java" >}}

##  **Spara alla arbetsblad till PDF**

**[`SheetSet.Visible`](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getVisible--)** indikerar synliga ark i en arbetsbok, och**[`SheetSet.All`](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getAll--)** indikerar alla ark inklusive både synliga ark och dolda/osynliga ark i en arbetsbok. Om du vill exportera alla ark till pdf kan du bara passera**[`SheetSet.All`](https://reference.aspose.com/cells/java/com.aspose.cells/sheetset/#getAll--)** till**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)** alternativ.

 Källfilen[arkuppsättning-exempel.xlsx](sheetset-example.xlsx) innehåller alla fyra ark med dolt ark `Sheet3`.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-AllSheetsToPdf.java" >}}

##  **Spara specificerade arbetsblad till PDF**
 Om du vill exportera önskade/anpassa flera ark till pdf kan du uppnå detta genom att skicka flera arkindex till**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)** alternativ.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-MultiSheetsToPdf.java" >}}

{{% alert color="primary" %}} 

Om ditt kalkylblad innehåller formler är det bäst att ringa [`Workbook.CalculateFormula()`](https://reference.aspose.com/cells/java/com.aspose.cells/workbook/#calculateFormula--) precis innan du renderar kalkylarket till PDF-format. Om du gör det säkerställer du att de formelberoende värdena räknas om och att de korrekta värdena återges i PDF.

{{% /alert %}}
