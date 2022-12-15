---
title: Konvertera en Excel-tabell till en rad data
type: docs
weight: 10
url: /sv/python-java/convert-an-excel-table-to-a-range-of-data/
---
## **Konvertera en Excel-tabell till en rad data**
 Aspose.Cells for Python via Java ger möjlighet att konvertera Excel-tabellen till en rad data. För detta tillhandahåller API[ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(\) ) metod. Följande kodavsnitt visar användningen av[ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(\)metod för att konvertera en Excel-tabell till en rad data.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-ConvertTableToRange.py" >}}
## **Konvertera en Excel-tabell till ett intervall med alternativ**
Du kan tillhandahålla ytterligare alternativ när du konverterar en tabell till ett intervall med[TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions) klass. Du kan passera en instans av[TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions)klass till[ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(com.aspose.cells.TableToRangeOptions\)) metod för att ange ytterligare alternativ. Följande kodavsnitt visar användningen av[TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions)klass för att ställa in det sista radindexet i tabellen. Tabellformateringen kommer att behållas upp till det angivna radindexet och resten av formateringen kommer att tas bort.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-ConvertTableToRangeWithOptions.py" >}}
