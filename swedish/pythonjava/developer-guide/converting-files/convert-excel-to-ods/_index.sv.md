---
title: Konvertera Excel till ODS
type: docs
weight: 40
url: /sv/python-java/convert-excel-to-ods/
---

## **Konvertera Excel till ODS**
ODS-filer skapas av programmet Calc som är en del av Apache OpenOffice Suite. ODS-filer lagrar data som är organiserade i rader och kolumner och är formaterade med hjälp av OASIS OpenDocument XML-baserad standard.

Aspose.Cells för Python via Java stöder arbete med ODS-filer. Följande exempel demonstrerar konvertering av Excel till en ODS-fil.
### **Direkt konvertering**
Det enklaste sättet att konvertera en Excel-fil till ODS är att ladda arbetsboken och spara den genom att ange [SaveFormat.ODS](https://reference.aspose.com/cells/python/asposecells.api/saveformat#ODS) som andra parameter för [Workbook.save](https://reference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String,%20int\))-metoden.

Följande kodsnutt demonstrerade hur man konverterar Excel direkt till ODS

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToODSFiles.py" >}}
### **Spara ODS-dokumentet enligt specifikationerna för ODF 1.1 eller 1.2**
Aspose.Cells för Python via Java stöder att spara ODS-filer i ODF 1.1- och ODF 1.2-specifikationerna. För detta tillhandahåller API:n egenskapen [OdsSaveOptions.setStrictSchema11()](https://reference.aspose.com/cells/python/asposecells.api/odssaveoptions#IsStrictSchema11). Genom att sätta denna egenskap till **true** kommer filen att sparas enligt ODF 1.1-specifikationen. Standardvärdet för [OdsSaveOptions.setStrictSchema11()](https://reference.aspose.com/cells/python/asposecells.api/odssaveoptions#IsStrictSchema11) är **false**, så ODS-filen som sparas utan speciella inställningar sparas enligt ODF 1.2-specifikationen.

Följande kodsnutt demonstrerar hur man sparar ODS-filer med ODF 1.1- och 1.2-specifikationer.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-SaveODSFilesWithSpecifications.py" >}}
