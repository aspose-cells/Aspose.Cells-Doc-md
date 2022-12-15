---
title: Sampla om bilder för konvertering av Excel till PDF
type: docs
weight: 250
url: /sv/java/resample-images-for-excel-to-pdf-conversion/
description: Den här artikeln visar hur du minskar bildstorlekar när du konverterar Excel-filer till PDF
keywords: excel to pdf, resample images during excel to pdf conversion, compress images during excel to pdf conversion, reduce image sizes during excel to pdf conversion, convert excel to pdf with smaller size, excel to pdf conversion with image resampling, excel to pdf conversion with image compression, resample images during excel to pdf conversion java
---
{{% alert color="primary" %}}

När du arbetar med stora Microsoft Excel-filer med många bilder kan du behöva komprimera bilder som har lagts till för att minska storleken på PDF-filen och förbättra den övergripande konverteringsprestanda. Aspose.Cells stöder omsampling av tillagda bilder för att minska storleken på PDF-filen och förbättra prestandan.

{{% /alert %}}

## **Sampla om bilder för konvertering av Excel till PDF**

Se följande exempelkod som beskriver hur du utför uppgiften med hjälp av Aspose.Cells API. Exemplet konverterar en Microsoft Excel-fil till en PDF-fil samtidigt som bilderna i filen komprimeras.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ResampleImagesforExceltoPDFConversion-ResampleImagesforExceltoPDFConversion.java" >}}

{{% alert color="primary" %}}

 Använda[**PdfSaveOptions.setImageResample**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#setImageResample(int,%20int))-alternativet minimerar storleken på PDF-filen men det kan påverka bildkvaliteten lite.

{{% /alert %}} {{% alert color="primary" %}}

 Om ditt kalkylblad innehåller formler är det bäst att ringa[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()precis innan du renderar kalkylarket till PDF-format. Om du gör det säkerställer du att de formelberoende värdena räknas om och att de korrekta värdena återges i PDF-filen.

{{% /alert %}}
