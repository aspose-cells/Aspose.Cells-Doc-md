---
title: Uppdaterar Slicer
type: docs
weight: 50
url: /sv/java/updating-slicer/
---
## **Möjliga användningsscenarier**
Om du vill uppdatera slicer i Microsoft Excel, välj eller avmarkera dess objekt, det kommer sedan att uppdatera slicer-tabellen eller pivottabellen därefter. Snälla använd[Slicer.SlicerCache.SlicerCacheItems](https://reference.aspose.com/cells/java/com.aspose.cells/slicercache#SlicerCacheItems)för att välja eller avmarkera skivningsobjekt med Aspose.Cells och sedan ringa[Slicer.refresh()](https://reference.aspose.com/cells/java/com.aspose.cells/slicer#refresh\(\)) metod för att uppdatera skivningstabellen eller pivottabellen.
## **Uppdaterar Slicer**
Följande exempelkod laddar[exempel på Excel-fil](67338506.xlsx)som innehåller en befintlig skivare. Det avmarkerar det andra och tredje objektet i skivaren och uppdaterar skivaren. Den sparar sedan arbetsboken som[utdata Excel-fil](67338505.xlsx). Följande skärmdump visar effekten av exempelkoden på exemplet i Excel-filen. Som du kan se på skärmdumpen har även pivottabellen uppdaterats genom att uppdatera skivaren med utvalda föremål.

![todo:image_alt_text](updating-slicer_1.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-UpdatingSlicer.java" >}}
