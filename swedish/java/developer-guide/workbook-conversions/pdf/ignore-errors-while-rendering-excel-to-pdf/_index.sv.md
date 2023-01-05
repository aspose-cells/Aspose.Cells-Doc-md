---
title: Ignorera fel när du renderar Excel till PDF
type: docs
weight: 70
url: /sv/java/ignore-errors-while-rendering-excel-to-pdf/
---
## **Möjliga användningsscenarier**

Ibland när du konverterar din Excel-fil till PDF uppstår fel eller undantag och konverteringsprocessen avslutas. Du kan ignorera alla sådana fel under konverteringsprocessen med hjälp av[**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IgnoreError)fast egendom. På så sätt kommer konverteringsprocessen att slutföras smidigt utan att skapa några fel eller undantag, men dataförlust kan inträffa. Använd därför den här egenskapen endast om förlusten av data inte är kritisk för dig.

## **Ignorera fel när du renderar Excel till PDF**

Följande kod laddar[exempel på Excel-fil](55541813.xlsx)men exemplet i Excel-filen är felaktig och ger ett fel under[konvertering till PDF](55541814.pdf)i 17.11 men eftersom vi använder[**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IgnoreError)egenskapen ger den inget fel. En rundad röd pilliknande form som visas i den här skärmdumpen går dock förlorad.

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-IgnoreErrorsWhileRenderingExcelToPdf.java" >}}
