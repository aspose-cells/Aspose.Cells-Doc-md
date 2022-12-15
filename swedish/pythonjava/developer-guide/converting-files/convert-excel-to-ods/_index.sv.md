---
title: Konvertera Excel till ODS
type: docs
weight: 40
url: /sv/python-java/convert-excel-to-ods/
---
## **Konvertera Excel till ODS**
ODS-filer skapas av programmet Calc som är en del av Apache OpenOffice Suite. ODS-filer lagrar data som är organiserade i rader och kolumner och är formaterade med OASIS OpenDocument XML-baserade standard.

Aspose.Cells for Python via Java stöder fungerande ODS-filer. Följande exempel visar att konvertera Excel till en ODS-fil.
### **Direkt konvertering**
Det enklaste sättet att konvertera en Excel-fil till ODS är att ladda arbetsboken och spara den genom att passera[SaveFormat.ODS](https://reference.aspose.com/cells/python/asposecells.api/saveformat#ODS) som den andra parametern i[Arbetsbok.spara](https://reference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String,%20int\)) metod.

Följande kodavsnitt demonstrerade att konvertera Excel direkt till ODS

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToODSFiles.py" >}}
### **Spara ODS-dokumentet i ODF 1.1 eller 1.2 Specifikationer**
Aspose.Cells for Python via Java stöder att spara ODS-filer i ODF 1.1- och ODF 1.2-specifikationer. För detta tillhandahåller API[OdsSaveOptions.setStrictSchema11()](https://reference.aspose.com/cells/python/asposecells.api/odssaveoptions#IsStrictSchema11) fast egendom. Ställer in den här egenskapen till**Sann** sparar filen med ODF 1.1-specifikationen. Standardvärdet för[OdsSaveOptions.setStrictSchema11()](https://reference.aspose.com/cells/python/asposecells.api/odssaveoptions#IsStrictSchema11) är**falsk**, så ODS-filen som sparas utan speciella inställningar sparas med ODF 1.2-specifikationen.

Följande kodsnutt visade att ODS-filer sparas med ODF 1.1- och 1.2-specifikationer.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-SaveODSFilesWithSpecifications.py" >}}
