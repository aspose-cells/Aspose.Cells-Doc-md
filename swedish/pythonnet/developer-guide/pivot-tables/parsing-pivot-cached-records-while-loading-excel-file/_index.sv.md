---
title: Parsar pivotcachade poster medan Excel-fil laddas
type: docs
weight: 70
url: /sv/python-net/parsing-pivot-cached-records-while-loading-excel-file/
description: Så här tolkar du Pivot-cache-poster medan du laddar Excel-fil med Aspose.Cells for Python via .NET.
keywords: Parse Pivot Cached Records while loading Excel file.
---
##  **Möjliga användningsscenarier**

När du skapar en pivottabell tar Microsoft Excel en kopia av källdata och lagrar den i pivotcachen. Pivot-cachen hålls i minnet av Microsoft Excel. Du kan inte se det, men det är de data som pivottabellen refererar till när du bygger din pivottabell eller ändrar ett Slicer-val eller flyttar runt rader/kolumner. Detta gör det möjligt för Microsoft Excel att vara mycket lyhörd för ändringar i pivottabellen, men det kan också fördubbla storleken på din fil. När allt kommer omkring är Pivot-cachen bara en dubblett av dina källdata så det är vettigt att din filstorlek potentiellt kommer att vara dubbel.

När du laddar din Excel-fil i Workbook-objektet kan du bestämma om du också vill ladda posterna för Pivot Cache eller inte, med hjälp av[**LoadOptions.parsing_pivot_cached_records**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/parsing_pivot_cached_records/)fast egendom. Standardvärdet för den här egenskapen är *false**. Om Pivot Cache är ganska stor kan det öka prestandan. Men om du också vill ladda posterna för Pivot Cache, bör du ställa in den här egenskapen som *true**.

##  **Parsar pivotcachade poster medan Excel-fil laddas**

Följande exempelkod förklarar användningen av[**LoadOptions.parsing_pivot_cached_records**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/parsing_pivot_cached_records/)fast egendom. Den laddar[exempel på Excel-fil](61767773.xlsx) medan du analyserar de cachade pivotposterna. Sedan uppdaterar den pivottabellen och sparar den som[utdata Excel-fil](61767774.xlsx).

##  **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.py" >}}
