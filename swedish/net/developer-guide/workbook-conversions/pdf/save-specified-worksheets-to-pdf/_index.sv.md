---
title: Spara specificerade arbetsblad till PDF
type: docs
weight: 140
url: /sv/net/save-specified-worksheets-to-pdf/
---
 Som standard sparar Aspose.Cells alla**synlig** Kalkylblad i en arbetsbok till pdf-fil. Med**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)** alternativet kan du spara specificerade kalkylblad till pdf-fil. t.ex. kan du spara aktivt kalkylblad till pdf, spara alla kalkylblad (både synliga och dolda kalkylblad) till pdf, spara anpassade flera kalkylblad till pdf.

##  **Spara aktivt arbetsblad till PDF**

 Om du bara vill exportera aktivt ark till pdf kan du uppnå detta genom att godkänna**[`SheetSet.Active`](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/active/)** till**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)** alternativ.

 Arket `Sheet2` är det aktiva arket för källfilen[arkuppsättning-exempel.xlsx](sheetset-example.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-ActiveSheetToPdf.cs" >}}

##  **Spara alla arbetsblad till PDF**

**[`SheetSet.Visible`](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/visible/)** indikerar synliga ark i en arbetsbok, och**[`SheetSet.All`](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/all/)** indikerar alla ark inklusive både synliga ark och dolda/osynliga ark i en arbetsbok. Om du vill exportera alla ark till pdf kan du bara passera**[`SheetSet.All`](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/all/)** till**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)** alternativ.

 Källfilen[arkuppsättning-exempel.xlsx](sheetset-example.xlsx) innehåller alla fyra ark med dolt ark `Sheet3`.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-AllSheetsToPdf.cs" >}}

##  **Spara specificerade arbetsblad till PDF**
 Om du vill exportera önskade/anpassa flera ark till pdf kan du uppnå detta genom att skicka flera arkindex till**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)** alternativ.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-MultiSheetsToPdf.cs" >}}

{{% alert color="primary" %}} 

Om ditt kalkylblad innehåller formler är det bäst att ringa [`Workbook.CalculateFormula()`](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) precis innan du renderar kalkylarket till PDF-format. Om du gör det säkerställer du att de formelberoende värdena räknas om och att de korrekta värdena återges i PDF.

{{% /alert %}}
