---
title: Konvertera Excel till PDF
type: docs
weight: 50
url: /sv/python-java/convert-excel-to-pdf/
description: Hur man konverterar Excel till PDF med Python. Denna artikel visar hur man konverterar Excel filer till PDF med hjälp av Python och det enkla att använda Aspose.Cells för Python via Java API.
keywords: excel to pdf python, python convert excel to pdf, python excel to pdf, convert excel to pdf python, convert excel to pdf in python, convert excel to pdf using python, excel to pdf in python, excel to pdf using python, aspose excel to pdf, aspose convert excel to pdf
---

## **Konvertera Excel till PDF**

PDF-dokument används allmänt som ett standardformat för att utbyta dokument mellan organisationer, regeringssektorer och enskilda. Mjukvaruutvecklare ombeds ofta att hitta ett sätt att enkelt konvertera Microsoft Excel-filer till PDF-dokument. Aspose.Cells för Python via Java-API:s ger möjlighet att konvertera Excel-filer till PDF-dokument (inklusive PDF/A). Aspose.Cells omvandlar kalkylblad till PDF med hög noggrannhet och bi-fidicitet.

### **Direkt konvertering**

För att spara en Excel-fil direkt till PDF kan du använda [**Workbook.save**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions))-metoden och skicka [**SaveFormat.PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF) som andra parameter.

Följande kodsnuttvisar användningen av [**SaveFormat.PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF) och [**Workbook.save**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions))-metoden för att konvertera Excel till PDF-format.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToPDFFiles.py" >}}

### **Avancerad konvertering**

För mer kontroll över konvertering till PDF, erbjuder API:n [**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)-klassen. [**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)-klassen kan användas för att inställa olika attribut för konverteringen. Att ställa in olika egenskaper för [**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)-klassen ger dig kontroll över utskrift, typsnitt, säkerhet och komprimeringsinställningar för den resulterande PDF-filen. Den mest märkbara egenskapen är [**Compliance**](https://reference.aspose.com/cells/python/asposecells.api/pdfsaveoptions#Compliance) som gör att du kan spara Excel-filerna till PDF/A-kompatibla PDF-filer.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-AdvancedConversiontoPdf.py" >}}

{{% alert color="primary" %}}

Om din kalkylblad innehåller formler, anropa [**Workbook.calculateFormula**](https://reference.aspose.com/cells/python-java/asposecells.api/workbook#calculateFormula())-metoden precis innan du renderar kalkylbladet till PDF. Detta säkerställer att formelberoende värden omberäknas och de korrekta värdena renderas i PDF-filen.

{{% /alert %}}
