---
title: Komprimering av tillagda bilder  Konvertering från Excel till PDF
type: docs
weight: 150
url: /sv/net/resampling-added-images-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

När du arbetar med stora Microsoft Excel-filer med massor av bilder kan du behöva komprimera de tillagda bilderna för att minska storleken på utdata-PDF-filen och förbättra den totala konverteringsprestandan. Aspose.Cells stöder att komprimera tillagda bilder för att minska utdata-PDF-filens storlek och förbättra prestandan något.

{{% /alert %}}

Se följande exempelkod som beskriver hur man utför uppgiften med hjälp av Aspose.Cells API. Exemplet konverterar en Microsoft Excel-fil till en PDF-fil samtidigt som bilderna i filen komprimeras.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ResamplingAddedImages-1.cs" >}}

{{% alert color="primary" %}}

Genom att använda alternativet [**SetImageResample**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/methods/setimageresample) minimeras storleken på utdata PDF:en men det kan påverka bildkvaliteten lite.

{{% /alert %}} {{% alert color="primary" %}}

Om ditt kalkylblad innehåller formler, är det bäst att anropa [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) strax innan du renderar kalkylbladet till PDF-format. Genom att göra det säkerställs att formelberoende värden beräknas om och de korrekta värdena renderas i PDF-filen.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
