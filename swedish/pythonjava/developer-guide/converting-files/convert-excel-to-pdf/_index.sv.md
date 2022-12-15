---
title: Konvertera Excel till PDF
type: docs
weight: 50
url: /sv/python-java/convert-excel-to-pdf/
description: Hur man konverterar Excel till PDF med Python. Den här artikeln visar hur man konverterar Excel-filer till PDF med Python och lättanvänd Aspose.Cells for Python via Java API.
keywords: excel to pdf python, python convert excel to pdf, python excel to pdf, convert excel to pdf python, convert excel to pdf in python, convert excel to pdf using python, excel to pdf in python, excel to pdf using python, aspose excel to pdf, aspose convert excel to pdf
---
## **Konvertera Excel till PDF**

PDF-dokument används ofta som ett standardformat för utbyte av dokument mellan organisationer, statliga sektorer och individer. Mjukvaruutvecklare uppmanas ofta att hitta ett sätt att enkelt konvertera Microsoft Excel-filer till PDF-dokument. Aspose.Cells for Python via Java API ger möjlighet att konvertera Excel-filer till PDF-dokument (inklusive PDF/A). Aspose.Cell konverterar kalkylblad till PDF med en hög grad av noggrannhet och trohet.

### **Direkt konvertering**

För att spara en Excel-fil direkt till PDF kan du använda[**Arbetsbok.spara**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions)) metod och godkänt[**SaveFormat.PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF) som den andra parametern.

Följande kodavsnitt visar användningen av[**SaveFormat.PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF)och den[**Arbetsbok.spara**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions)) metod för att konvertera Excel till PDF-format.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToPDFFiles.py" >}}

### **Avancerad konvertering**

För att ha mer kontroll över konverteringen till PDF tillhandahåller API[**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)klass. De[**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)klass kan användas för att ställa in olika attribut för konverteringen. Ställa in olika egenskaper för[**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)klass ger dig kontroll över inställningarna för utskrift, typsnitt, säkerhet och komprimering för den resulterande PDF-filen. Den mest anmärkningsvärda egenskapen är[**Efterlevnad**](https://reference.aspose.com/cells/python/asposecells.api/pdfsaveoptions#Compliance)som gör att du kan spara Excel-filerna till PDF/A-kompatibla PDF-filer.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-AdvancedConversiontoPdf.py" >}}

{{% alert color="primary" %}}

 om ditt kalkylblad innehåller formler, anropa[**Workbook.calculateFormula**](https://reference.aspose.com/cells/python/asposecells.api/workbook#calculateFormula()) -metoden precis innan du renderar kalkylarket till PDF. Detta säkerställer att de formelberoende värdena räknas om och att de korrekta värdena återges i PDF-filen.

{{% /alert %}}
