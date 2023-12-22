---
title: Uppdaterar Slicer
type: docs
weight: 50
url: /sv/python-net/updating-slicer/
---
##  **Möjliga användningsscenarier**

Om du vill uppdatera slicer i Microsoft Excel, välj eller avmarkera dess objekt, den kommer sedan att uppdatera slicer-tabellen eller pivottabellen i enlighet med detta. Snälla använd[**Slicer.slicer_cache.slicer_cache_items**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicercache/slicer_cache_items/)för att välja eller avmarkera skivningsartiklar med Aspose.Cells for Python via .NET och sedan ringa[**Slicer.refresh()**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicer/refresh/#)metod för att uppdatera skivningstabellen eller pivottabellen.

##  **Uppdaterar Slicer**

 Följande exempelkod laddar[exempel på Excel-fil](67338475.xlsx) som innehåller en befintlig skivare. Det avmarkerar det andra och tredje objektet i skivaren och uppdaterar skivaren. Den sparar sedan arbetsboken som[utdata Excel-fil](67338476.xlsx)Följande skärmdump visar effekten av exempelkoden på exemplet i Excel-filen. Som du kan se på skärmdumpen har även pivottabellen uppdaterats genom att uppdatera skivaren med utvalda föremål.

![todo:image_alt_text](updating-slicer_1.png)

##  **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Slicers-UpdatingSlicer.py" >}}
