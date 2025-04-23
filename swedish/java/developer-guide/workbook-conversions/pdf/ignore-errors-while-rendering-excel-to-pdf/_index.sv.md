---
title: Ignorera fel vid rendering av Excel till PDF
type: docs
weight: 70
url: /sv/java/ignore-errors-while-rendering-excel-to-pdf/
---

## **Möjliga användningsscenario**

Ibland när du konverterar din Excel-fil till PDF, uppstår fel eller undantag och konverteringsprocessen avbryts. Du kan ignorera alla sådana fel under konverteringsprocessen med hjälp av egenskapen [**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IgnoreError). På så sätt kommer konverteringsprocessen att slutföras smidigt utan att kasta några fel eller undantag, men dataloss kan inträffa. Använd denna egenskap endast om dataloss inte är kritisk för dig.

## **Ignorera fel vid rendering av Excel till PDF**

Följande kod laddar den [prov Excel-filen](55541813.xlsx) men den prov Excel-filen är felaktig och kastar ett fel under [konvertering till PDF](55541814.pdf) i 17.11 men eftersom vi använder egenskapen [**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IgnoreError), kastar den inte ett fel. Dock går en rundad röd pil-liknande form, som visas på den här skärmbilden, förlorad.

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-IgnoreErrorsWhileRenderingExcelToPdf.java" >}}
{{< app/cells/assistant language="java" >}}
