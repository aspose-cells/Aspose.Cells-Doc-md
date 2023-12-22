---
title: Anpassa alla kalkylbladskolumner på en PDF sida
type: docs
weight: 160
url: /sv/python-net/fit-all-worksheet-columns-on-single-pdf-page/
description: Lär dig hur du passar alla kalkylbladskolumner på enstaka PDF sida med Aspose.Cells for Python via .NET API.
keywords: Python Fit All Worksheet Columns on Single PDF Page, Fit Worksheet Columns on Single PDF Page using Python, Python Save All Worksheet Columns to a PDF Page, Save All Columns to single PDF Page in Python
---
{{% alert color="primary" %}}

Ibland vill du skapa en PDF-fil som passar alla ett kalkylblads kolumner på en sida. De[**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/) egenskapen tillhandahåller denna funktion på ett mycket lättanvänt sätt. Komplexa beräkningar som höjd och bredd på utdata PDF hanteras internt och baseras på uppgifterna i arbetsbladet.

{{% /alert %}}

##  **Anpassa kalkylbladskolumner på enstaka PDF sida**

[**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/)ser till att alla kolumner i ett kalkylblad renderas till en enda PDF-sida, även om rader kan utökas till flera sidor beroende på data i kalkylbladet.

Exempelkoden nedan visar hur du använder[**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/)egenskap för att återge ett stort kalkylblad med 100 kolumner.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-FitAllWorksheetColumns-1.py" >}}

{{% alert color="primary" %}}

När ett givet kalkylblad har många kolumner kan den renderade PDF-filen visa innehållet i en mycket liten storlek. Det är fortfarande läsbart när det skalas upp i ett visningsprogram som Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

 Om ditt kalkylblad innehåller formler är det bäst att ringa[Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) metod precis innan du renderar kalkylarket till formatet PDF. Om du gör det säkerställs att de formelberoende värdena räknas om och att de korrekta värdena återges i PDF.

{{% /alert %}}
