---
title: Anpassa alla kalkylbladskolumner på en enda PDF sida
type: docs
weight: 160
url: /sv/python-net/fit-all-worksheet-columns-on-single-pdf-page/
description: Lär dig hur du anpassar alla kalkylbladskolumner på en enda PDF sida med Aspose.Cells för Python via .NET API.
keywords: Python Passa alla kalkylbladskolumner på en enda PDF sida, Passa kalkylbladskolumner på en enda PDF sida med Python, Python Spara alla kolumner till en PDF sida, Spara alla kolumner till en enda PDF sida i Python
---

{{% alert color="primary" %}}

Ibland vill du generera en PDF-fil där alla kalkylbladets kolumner passar på en sida. Egenskapen [**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/) tillhandahåller denna funktion på ett mycket lättanvänt sätt. Komplexa beräkningar som höjden och bredden på utdata-PDF:en hanteras internt och baseras på data i kalkylbladet.

{{% /alert %}}

## **Anpassa kalkylbladskolumner på en enda PDF-sida**

[**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/) ser till att alla kolumner i ett kalkylblad renderas till en enda PDF-sida, även om rader kan expandera till flera sidor beroende på data i kalkylbladet.

Exempelkoden nedan visar hur du använder [**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/)-egenskapen för att rendera ett stort kalkylblad med 100 kolumner.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-FitAllWorksheetColumns-1.py" >}}

{{% alert color="primary" %}}

När ett givet kalkylblad har många kolumner kan den genererade PDF-filen visa innehållet i väldigt liten storlek. Det är fortfarande läsbart när det skalas upp i en visningsapplikation som Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

Om din kalkylblad innehåller formler är det bäst att anropa [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) metoden precis innan kalkylbladet renderas till PDF-format. På så sätt säkerställs att formelberoende värden omräknas och de korrekta värdena renderas i PDF:en.

{{% /alert %}}
