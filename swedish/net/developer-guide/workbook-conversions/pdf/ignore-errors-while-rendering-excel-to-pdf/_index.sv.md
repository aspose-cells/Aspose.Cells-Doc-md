---
title: Ignorera fel vid rendering av Excel till PDF
type: docs
weight: 80
url: /sv/net/ignore-errors-while-rendering-excel-to-pdf/
---

## **Möjliga användningsscenario**

Ibland när du konverterar din Excelfil till PDF uppstår fel eller undantag och konverteringsprocessen avslutas. Du kan ignorera alla sådana fel under konverteringsprocessen genom att använda [**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/ignoreerror)-egenskapen. På så sätt kommer konverteringsprocessen att slutföras smidigt utan att kasta några fel eller undantag, men dataförlust kan uppstå. Använd därför denna egenskap endast om förlusten av data inte är kritisk för dig.

## **Ignorera fel vid rendering av Excel till PDF**

Följande kod laddar in [prov Excelfil](55541778.xlsx) men den prov Excelfilen är felaktig och kastar ett fel under [konvertering till PDF](55541779.pdf) i 17.11 men eftersom vi använder [**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/ignoreerror)-egenskapen kastar den inget fel. Dock förloras en *avrundad röd pilform* som visas i denna skärmbild.

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-IgnoreErrorsWhileRenderingExcelToPdf.cs" >}}
{{< app/cells/assistant language="csharp" >}}
