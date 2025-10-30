---
title: Återsampling av tillagda bilder  Excel till PDF konvertering
type: docs
weight: 150
url: /sv/python-net/resample-added-images-excel-to-pdf-conversion/
description: Lär dig hur man återsamplar tillagda bilder när du konverterar excel till pdf med Aspose.Cells for Python via .NET API.
keywords: Python Återsampla tillagda bilder när du konverterar Excel till PDF
---

{{% alert color="primary" %}}

När du arbetar med stora Microsoft Excel-filer med många bilder kan du behöva komprimera tillagda bilder för att minska utdata PDF-filstorleken och förbättra den totala konverteringsprestandan. Aspose.Cells for Python via .NET stöder återsampling av tillagda bilder för att minska utdata PDF-filstorleken och förbättra prestandan något.

{{% /alert %}}

Vänligen se följande exempelkod som beskriver hur man utför uppgiften med hjälp av Aspose.Cells for Python via .NET API. Exemplet konverterar en Microsoft Excel-fil till en PDF-fil samtidigt som bilderna i filen komprimeras.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ResamplingAddedImages-1.py" >}}

{{% alert color="primary" %}}

Genom att använda alternativet [**PdfSaveOptions.set_image_resample**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/set_image_resample/#int-int) minimeras storleken på utdata PDF:en men det kan påverka bildkvaliteten lite.

{{% /alert %}} {{% alert color="primary" %}}

Om ditt kalkylblad innehåller formler, är det bäst att anropa [**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) strax innan du renderar kalkylbladet till PDF-format. Genom att göra det säkerställs att formelberoende värden beräknas om och de korrekta värdena renderas i PDF-filen.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
