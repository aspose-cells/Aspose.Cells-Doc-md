---
title: Ignorera fel vid rendering av Excel till PDF med Golang via C++
linktitle: Ignorera fel vid rendering av Excel till PDF
type: docs
weight: 80
url: /sv/go-cpp/ignore-errors-while-rendering-excel-to-pdf/
description: Lär dig hur du ignorerar fel under konvertering av Excel till PDF med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

Ibland uppstår fel eller undantag när du konverterar din Excel-fil till PDF och konverteringen avbryts. Du kan ignorera alla sådana fel under konverteringsprocessen genom att använda egenskapen [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) . På så sätt kan konverteringen genomföras smidigt utan att kasta fel eller undantag men dataloss kan inträffa. Använd denna egenskap endast om dataloss inte är kritiskt för dig.

## **Ignorera fel vid rendering av Excel till PDF**

Följande kod laddar [exempel Excel-fil](55541778.xlsx) men exempel-Excel-filen är felaktig och ger ett fel under [konvertering till PDF](55541779.pdf) i version 17.11, men eftersom vi använder [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) egenskap, ger det inte något fel. Dock förloras en *rundad röd pil-liknande form* som visas i denna skärmdump.

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IgnoreErrorsWhileRenderingExcelToPdf.go" >}}
