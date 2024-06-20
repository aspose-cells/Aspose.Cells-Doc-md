---
title: Spara angivna arkpapper till PDF
type: docs
weight: 140
url: /sv/python-net/save-specified-worksheets-to-pdf/
description: Lär dig hur du sparar specifika kalkylblad till PDF med Aspose.Cells för Python via .NET API.
keywords: Python Spara aktivt kalkylblad till PDF, Spara alla kalkylblad till PDF, Spara specifika kalkylblad till PDF
---

Som standard, spara Aspose.Cells för Python via .NET alla **synliga** kalkylblad i en arbetsbok till PDF-fil. Med [**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)-alternativet kan du spara angivna kalkylblad till PDF-fil. t.ex. du kan spara aktivt kalkylblad till PDF, spara alla kalkylblad (både synliga och dolda kalkylblad) till PDF, spara anpassade flera kalkylblad till PDF.

## **Spara aktivt arkpapp till PDF**

Om du bara vill exportera det aktiva arkpappret till pdf, kan du uppnå detta genom att skicka [**SheetSet.active**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/active/) till [**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/) alternativet.

Arket `Ark2` är det aktiva arkpappret i källfilen [sheetset-example.xlsx](sheetset-example.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ActiveSheetToPdf.py" >}}

## **Spara alla arkpapper till PDF**

[**SheetSet.visible**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/visible/) indikerar synliga ark i en arbetsbok, och [**SheetSet.all**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/all/) indikerar alla ark inklusive både synliga ark och dolda/osynliga ark i en arbetsbok. Om du vill exportera alla ark till pdf, kan du helt enkelt skicka [**SheetSet.all**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/all/) till [**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/) alternativet.

Källfilen [sheetset-example.xlsx](sheetset-example.xlsx) innehåller alla fyra ark med dolt ark `Ark3`.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AllSheetsToPdf.py" >}}

## **Spara angivna arbetsblad som PDF**
Om du vill exportera önskade/anpassade flera ark till pdf, kan du uppnå detta genom att skicka flera arkindex till [**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/) alternativet.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-MultiSheetsToPdf.py" >}}

{{% alert color="primary" %}} 

Om ditt kalkylblad innehåller formler, är det bäst att anropa [**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) strax innan du renderar kalkylbladet till PDF-format. Genom att göra det säkerställs att formelberoende värden beräknas om och de korrekta värdena renderas i PDF-filen.

{{% /alert %}}
