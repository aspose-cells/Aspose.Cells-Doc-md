---
title: Uppdaterar Slicer
type: docs
weight: 60
url: /sv/python-java/updating-slicer/
---
## **Uppdaterar Slicer**
Aspose.Cells för Python via Java stöder uppdatering av slicers. För detta tillhandahåller API:t egenskapen Slicer.SlicerCache.SlicerCacheItems som används för att välja eller avmarkera skivobjekt. Följande kodavsnitt laddar[exempel på Excel-fil](106365050.xlsx)som innehåller en skivare. Det avmarkerar de andra och tredje objekten i skivaren och uppdaterar skivaren med metoden Slicer.refresh() . Den sparar sedan arbetsboken som[utdata Excel-fil](106365051.xlsx). Följande skärmdump visar effekten av exempelkoden på exemplet i Excel-filen. Som du kan se på skärmdumpen har även pivottabellen uppdaterats genom att uppdatera skivaren med utvalda föremål.

![todo:image_alt_text](Updating-Slicer-using-Aspose.Cells.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Slicers-UpdatingSlicer.py" >}}
