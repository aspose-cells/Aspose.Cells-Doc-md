---
title: Återprovning av bilder för konvertering av Excel till PDF
type: docs
weight: 250
url: /sv/java/resample-images-for-excel-to-pdf-conversion/
description: Denna artikel demonstrerar hur man minskar bildstorlekar vid konvertering av Excel filer till PDF
keywords: excel till pdf, återprovning av bilder under konvertering av excel till pdf, komprimera bilder under konvertering av excel till pdf, minska bildstorlekar under konvertering av excel till pdf, konvertera excel till pdf med mindre storlek, excel till pdf konvertering med bild återprovning, excel till pdf konvertering med bildkompression, återprovning av bilder under konvertering av excel till pdf java
---

{{% alert color="primary" %}}

När du arbetar med stora Microsoft Excel-filer med många bilder kan du behöva komprimera bilder som har lagts till för att minska utmatnings-PDF-filstorleken och förbättra den totala konvergeringsprestandan. Aspose.Cells stöder omprovning av tillagda bilder för att minska utmatnings-PDF-filstorleken och förbättra prestandan.

{{% /alert %}}

## **Återprovning av bilder för konvertering av Excel till PDF**

Se följande exempelkod som beskriver hur man utför uppgiften med hjälp av Aspose.Cells API. Exemplet konverterar en Microsoft Excel-fil till en PDF-fil samtidigt som bilderna i filen komprimeras.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ResampleImagesforExceltoPDFConversion-ResampleImagesforExceltoPDFConversion.java" >}}

{{% alert color="primary" %}}

Att använda [**PdfSaveOptions.setImageResample**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#setImageResample(int,%20int))-alternativet minimerar storleken på utmatnings-PDF-filen men det kan påverka bildkvaliteten lite.

{{% /alert %}} {{% alert color="primary" %}}

Om ditt kalkylblad innehåller formler, är det bäst att anropa [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) strax innan du renderar kalkylbladet till PDF-format. Genom att göra det säkerställs att formelberoende värden beräknas om och de korrekta värdena renderas i PDF-filen.

{{% /alert %}}
