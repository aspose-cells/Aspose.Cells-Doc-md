---
title: Spara specificerade arbetsblad till PDF
type: docs
weight: 140
url: /sv/python-net/save-specified-worksheets-to-pdf/
description: Lär dig hur du sparar specificerade arbetsblad till PDF med Aspose.Cells for Python via .NET API.
keywords: Python Save Active Worksheet to PDF, Save All Worksheets to PDF, Save Specified Worksheets to PDF
---
 Som standard, Aspose.Cells for Python via .NET spara alla**synlig** Kalkylblad i en arbetsbok till pdf-fil. Med**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)** alternativet kan du spara specificerade kalkylblad till pdf-fil. t.ex. kan du spara aktivt kalkylblad till pdf, spara alla kalkylblad (både synliga och dolda kalkylblad) till pdf, spara anpassade flera kalkylblad till pdf.

##  **Spara aktivt arbetsblad till PDF**

Om du bara vill exportera aktivt ark till pdf kan du uppnå detta genom att godkänna**[`SheetSet.active`](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/active/)** till**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)** alternativ.

 Arket `Sheet2` är det aktiva arket för källfilen[arkuppsättning-exempel.xlsx](sheetset-example.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ActiveSheetToPdf.py" >}}

##  **Spara alla arbetsblad till PDF**

**[`SheetSet.visible`](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/visible/)** indikerar synliga ark i en arbetsbok, och**[`SheetSet.all`](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/all/)** indikerar alla ark inklusive både synliga ark och dolda/osynliga ark i en arbetsbok. Om du vill exportera alla ark till pdf kan du bara passera**[`SheetSet.all`](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/all/)** till**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)** alternativ.

 Källfilen[arkuppsättning-exempel.xlsx](sheetset-example.xlsx) innehåller alla fyra ark med dolt ark `Sheet3`.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AllSheetsToPdf.py" >}}

##  **Spara specificerade arbetsblad till PDF**
 Om du vill exportera önskade/anpassa flera ark till pdf kan du uppnå detta genom att skicka flera arkindex till**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)** alternativ.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-MultiSheetsToPdf.py" >}}

{{% alert color="primary" %}} 

 Om ditt kalkylblad innehåller formler är det bäst att ringa[**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) precis innan du renderar kalkylarket till formatet PDF. Om du gör det säkerställs att de formelberoende värdena räknas om och att de korrekta värdena återges i PDF.

{{% /alert %}}
