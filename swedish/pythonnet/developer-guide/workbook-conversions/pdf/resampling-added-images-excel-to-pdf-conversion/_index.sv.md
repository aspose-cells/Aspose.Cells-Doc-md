---
title: Sampla om tillagda bilder - Konvertering av Excel till PDF
type: docs
weight: 150
url: /sv/python-net/resample-added-images-excel-to-pdf-conversion/
description: Lär dig hur du samplar om tillagda bilder när du konverterar Excel till pdf med Aspose.Cells for Python via .NET API.
keywords: Python Resample Added Images when Convert Excel to PDF
---
{{% alert color="primary" %}}

När du arbetar med stora Microsoft Excel-filer med många bilder kan du behöva komprimera bilder som har lagts till för att minska utdatafilstorleken PDF och förbättra den övergripande konverteringsprestanda. Aspose.Cells for Python via .NET stöder omsampling av tillagda bilder för att minska utdatafilstorleken PDF och förbättra prestandan något.

{{% /alert %}}

Se följande exempelkod som beskriver hur du utför uppgiften med Aspose.Cells for Python via .NET API. Exemplet konverterar en Microsoft Excel-fil till en PDF-fil samtidigt som bilderna i filen komprimeras.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ResamplingAddedImages-1.py" >}}

{{% alert color="primary" %}}

 Med hjälp av den[**PdfSaveOptions.set_image_resample**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/set_image_resample/#int-int)alternativet minimerar storleken på utdata PDF men det kan påverka bildkvaliteten lite.

{{% /alert %}} {{% alert color="primary" %}}

 Om ditt kalkylblad innehåller formler är det bäst att ringa[**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) precis innan du renderar kalkylarket till formatet PDF. Om du gör det säkerställs att de formelberoende värdena räknas om och att de korrekta värdena återges i PDF.

{{% /alert %}}
