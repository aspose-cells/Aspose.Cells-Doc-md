---
title: Ignorera fel när du renderar Excel till PDF
type: docs
weight: 80
url: /sv/net/ignore-errors-while-rendering-excel-to-pdf/
---
## **Möjliga användningsscenarier**

 Ibland när du konverterar din Excel-fil till PDF uppstår fel eller undantag och konverteringsprocessen avslutas. Du kan ignorera alla sådana fel under konverteringsprocessen genom att använda[**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/ignoreerror)fast egendom. På så sätt kommer konverteringsprocessen att slutföras smidigt utan att skapa några fel eller undantag, men dataförlust kan inträffa. Använd därför den här egenskapen endast om förlusten av data inte är kritisk för dig.

## **Ignorera fel när du renderar Excel till PDF**

 Följande kod laddar[exempel på Excel-fil](55541778.xlsx) men exemplet på Excel-filen är felaktig och ger ett fel under[konvertering till PDF](55541779.pdf) i 17.11 men eftersom vi använder[**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/ignoreerror)egenskapen ger den inget fel. Dock en*rundad röd pilliknande form*som visas i den här skärmdumpen är förlorad.

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-IgnoreErrorsWhileRenderingExcelToPdf.cs" >}}
