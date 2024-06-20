---
title: Uppdatera slicer
type: docs
weight: 60
url: /sv/python-java/updating-slicer/
---

## **Uppdatera slicer**
Aspose.Cells för Python via Java stödjer uppdatering av slicers. För detta tillhandahåller API:et egenskapen Slicer.SlicerCache.SlicerCacheItems som används för att välja eller avmarkera slicerobjekt. Följande kodsnutt laddar in [prov Excel-filen](106365050.xlsx) som innehåller en slicer.Den avmarkerar sedan det andra och tredje objektet i slicern och uppdaterar slicern med hjälp av metoden Slicer.refresh(). Den sparar sedan arbetsboken som [utdata Excel-fil](106365051.xlsx). Följande skärmbild visar effekten av exempelkoden på prov Excel-filen. Som du kan se i skärmbilden har uppdateringen av slicerns markerade objekt även uppdaterat pivottabellen på motsvarande sätt.

![todo:image_alt_text](Updating-Slicer-using-Aspose.Cells.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Slicers-UpdatingSlicer.py" >}}
