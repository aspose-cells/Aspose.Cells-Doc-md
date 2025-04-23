---
title: Spara angivna arkpapper till PDF
type: docs
weight: 140
url: /sv/net/save-specified-worksheets-to-pdf/
---

Som standard sparar Aspose.Cells alla **synliga** arkpapper i en arbetsbok till en pdf-fil. Med [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/) alternativet kan du spara angivna arkpapper till en pdf-fil. t.ex. kan du spara aktivt arkpapp till pdf, spara alla arkpapper (både synliga och dolda arkpapper) till pdf, spara anpassade flera arkpapper till pdf.

## **Spara aktivt arkpapp till PDF**

Om du bara vill exportera det aktiva arkpappret till pdf, kan du uppnå detta genom att skicka [**SheetSet.Active**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/active/) till [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/) alternativet.

Arket `Ark2` är det aktiva arkpappret i källfilen [sheetset-example.xlsx](sheetset-example.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-ActiveSheetToPdf.cs" >}}

## **Spara alla arkpapper till PDF**

[**SheetSet.Visible**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/visible/) indikerar synliga ark i en arbetsbok, och [**SheetSet.All**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/all/) indikerar alla ark inklusive både synliga ark och dolda/osynliga ark i en arbetsbok. Om du vill exportera alla ark till pdf, kan du helt enkelt skicka [**SheetSet.All**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetset/all/) till [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/) alternativet.

Källfilen [sheetset-example.xlsx](sheetset-example.xlsx) innehåller alla fyra ark med dolt ark `Ark3`.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-AllSheetsToPdf.cs" >}}

## **Spara angivna arbetsblad som PDF**
Om du vill exportera önskade/anpassade flera ark till pdf, kan du uppnå detta genom att skicka flera arkindex till [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/) alternativet.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-MultiSheetsToPdf.cs" >}}

## **Omordna arbetsblad till PDF**

Om du vill omordna blad (t.ex. i omvänd ordning) till PDF utan att modifiera källdokumentet kan du göra detta genom att skicka omordnade bladindex till [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/) alternativet.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-ReorderSheetsToPdf.cs" >}}

{{% alert color="primary" %}} 

Om ditt kalkylblad innehåller formler, är det bäst att anropa [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) strax innan du renderar kalkylbladet till PDF-format. Genom att göra det säkerställs att formelberoende värden beräknas om och de korrekta värdena renderas i PDF-filen.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
