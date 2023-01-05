---
title: Omsampling av tillagda bilder - Konvertering av Excel till PDF
type: docs
weight: 150
url: /sv/net/resampling-added-images-excel-to-pdf-conversion/
---
{{% alert color="primary" %}}

När du arbetar med stora Microsoft Excel-filer med många bilder kan du behöva komprimera bilder som har lagts till för att minska utdatafilstorleken PDF och förbättra den övergripande konverteringsprestanda. Aspose.Cells stöder omsampling av tillagda bilder för att minska utdatafilstorleken PDF och förbättra prestandan något.

{{% /alert %}}

Se följande exempelkod som beskriver hur du utför uppgiften med Aspose.Cells API. Exemplet konverterar en Microsoft Excel-fil till en PDF-fil samtidigt som bilderna i filen komprimeras.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ResamplingAddedImages-1.cs" >}}

{{% alert color="primary" %}}

 Med hjälp av den[**SetImageResample**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/methods/setimageresample)alternativet minimerar storleken på utdata PDF men det kan påverka bildkvaliteten lite.

{{% /alert %}} {{% alert color="primary" %}}

Om ditt kalkylblad innehåller formler är det bäst att ringa[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)precis innan du renderar kalkylarket till formatet PDF. Om du gör det säkerställs att de formelberoende värdena räknas om och att de korrekta värdena återges i PDF.

{{% /alert %}}
