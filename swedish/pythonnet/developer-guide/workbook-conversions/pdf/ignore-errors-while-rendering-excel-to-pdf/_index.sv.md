---
title: Ignorera fel vid rendering av Excel till PDF
type: docs
weight: 80
url: /sv/python-net/ignore-errors-while-rendering-excel-to-pdf/
description: Lär dig hur du ignorerar fel vid renderingen av Excel till PDF med Aspose.Cells för Python via .NET API.
keywords: Python Ignorera fel vid renderingen av Excel till PDF, Ignorera fel vid sparande av Excel till PDF med Python, Python Ignorera fel vid konvertering av Excel till PDF, Ignorera fel för Excel till PDF i Python
---

## **Möjliga användningsscenario**

Ibland när du konverterar din Excelfil till PDF uppstår fel eller undantag och konverteringsprocessen avslutas. Du kan ignorera alla sådana fel under konverteringsprocessen genom att använda [**PdfSaveOptions.ignore_error**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/ignore_error/)-egenskapen. På så sätt kommer konverteringsprocessen att slutföras smidigt utan att kasta några fel eller undantag, men dataförlust kan uppstå. Använd därför denna egenskap endast om förlusten av data inte är kritisk för dig.

## **Ignorera fel vid rendering av Excel till PDF**

Följande kod laddar in [prov Excelfil](55541778.xlsx) men den prov Excelfilen är felaktig och kastar ett fel under [konvertering till PDF](55541779.pdf) i 17.11 men eftersom vi använder [**PdfSaveOptions.ignore_error**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/ignore_error/)-egenskapen kastar den inget fel. Dock förloras en *avrundad röd pilform* som visas i denna skärmbild.

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-IgnoreErrorsWhileRenderingExcelToPdf.py" >}}
{{< app/cells/assistant language="python-net" >}}
