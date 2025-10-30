---
title: Resampling av tillagda bilder  Excel till PDF konvertering med Golang via C++
linktitle: Komprimering av tillagda bilder  Konvertering från Excel till PDF
type: docs
weight: 150
url: /sv/go-cpp/resampling-added-images-excel-to-pdf-conversion/
description: Lär dig hur du resamplerar tillagda bilder för att minska PDF storleken med Aspose.Cells och Golang via C++.
---

{{% alert color="primary" %}}

När du arbetar med stora Microsoft Excel-filer med massor av bilder kan du behöva komprimera de tillagda bilderna för att minska storleken på utdata-PDF-filen och förbättra den totala konverteringsprestandan. Aspose.Cells stöder att komprimera tillagda bilder för att minska utdata-PDF-filens storlek och förbättra prestandan något.

{{% /alert %}}

Se följande exempelkod som beskriver hur man utför uppgiften med hjälp av Aspose.Cells API. Exemplet konverterar en Microsoft Excel-fil till en PDF-fil samtidigt som bilderna i filen komprimeras.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ResamplingAddedImagesExcelToPdfConversion.go" >}}
{{% alert color="primary" %}}

Att använda [**SetImageResample**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/setimageresample/)-alternativet minimerar storleken på utmatnings-PDF-filen men det kan påverka bildkvaliteten lite.

{{% /alert %}} 

{{% alert color="primary" %}}

Om ditt kalkylblad innehåller formler, är det bäst att anropa [**CalculateFormula**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) strax innan du renderar kalkylbladet till PDF-format. Genom att göra det säkerställs att formelberoende värden beräknas om och de korrekta värdena renderas i PDF-filen.

{{% /alert %}}

