---
title: Konvertera en Excel tabell till en datamängd.
type: docs
weight: 10
url: /sv/python-java/convert-an-excel-table-to-a-range-of-data/
---

## **Konvertera en Excel-tabell till en dataområde**
Aspose.Cells för Python via Java ger möjlighet att konvertera en Excel-tabell till en dataområde. API:et erbjuder metoden [ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(\)). Följande kodsnutt visar användningen av [ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(\)) -metoden för att konvertera en Excel-tabel till en dataområde.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-ConvertTableToRange.py" >}}
## **Konvertera en Excel-tabell till en område med alternativ**
Du kan ange ytterligare alternativ när du konverterar en tabell till en område med hjälp av klassen [TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions). Du kan skicka en instans av [TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions) -klassen till metoden [ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(com.aspose.cells.TableToRangeOptions\)) för att ange ytterligare alternativ. Följande kodsnutt visar användningen av [TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions) -klassen för att ställa in den sista radindex av tabellen. Tabellformateringen behålls upp till det angivna radindexet och resten av formateringen tas bort.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-ConvertTableToRangeWithOptions.py" >}}
