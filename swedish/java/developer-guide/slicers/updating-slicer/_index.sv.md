---
title: Uppdatera slicer
type: docs
weight: 50
url: /sv/java/updating-slicer/
---

## **Möjliga användningsscenario**
Om du vill uppdatera slicern i Microsoft Excel, välj eller avmarkera dess objekt, då kommer slicertabellen eller pivottabellen att uppdateras. Använd [Slicer.SlicerCache.SlicerCacheItems](https://reference.aspose.com/cells/java/com.aspose.cells/slicercache#SlicerCacheItems) för att välja eller avmarkera slicerobjekt med Aspose.Cells och ring sedan [Slicer.refresh()](https://reference.aspose.com/cells/java/com.aspose.cells/slicer#refresh\(\)) metoden för att uppdatera slicertabellen eller pivottabellen. 
## **Uppdatera slicer**
Följande provkod laddar in [provmappen](67338506.xlsx) som innehåller en befintlig slicer. Den avmarkerar den 2:a och 3:e objekten i slicern och uppdaterar slicern. Den sparar sedan arbetsboken som [output Excel-fil](67338505.xlsx). Skärmbilden visar effekten av provkoden på den prov Excel-filen. Som du kan se på skärmbilden har uppdateringen av slicern med valda objekt också uppdaterat pivottabellen i enlighet med det valda.

![todo:image_alt_text](updating-slicer_1.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-UpdatingSlicer.java" >}}
