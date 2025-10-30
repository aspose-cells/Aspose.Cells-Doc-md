---
title: Uppdatera slicer
type: docs
weight: 50
url: /sv/python-net/updating-slicer/
description: Lär dig hur du uppdaterar slicer med Aspose.Cells för Python via .NET.
keywords: Aspose.Cells för Python Excel, Excel Python bibliotek, Python uppdatera Slicer utan Excel, Uppdatera Slicer med Aspose.Cells för Python.
---

## **Möjliga användningsscenario**

Om du vill uppdatera slicer i Microsoft Excel, välj eller avmarkera dess objekt, så kommer det att uppdatera slicer-tabellen eller pivot-tabellen i enlighet därmed. Använd [**Slicer.slicer_cache.slicer_cache_items**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicercache/slicer_cache_items/) för att välja eller avmarkera slicer-objekt med Aspose.Cells för Python via .NET och ring sedan in [**Slicer.refresh()**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicer/refresh/#) funktionen för att uppdatera slicer-tabellen eller pivot-tabellen.

## **Hur man uppdaterar slicer med Aspose.Cells för Python Excel-bibliotek**

Följande exempelkod laddar [provmappen](67338475.xlsx) som innehåller en befintlig snitt. Den avmarkerar den 2:a och 3:e objekten i snittet och uppdaterar snittet sedan. Den sparar sedan arbetsboken som [utmatningsmapp](67338476.xlsx). Skärmbilden nedan visar effekten av exempelkoden på provmappen. Som du kan se på skärmbilden, har uppdateringen av snittet med markerade objekt också uppdaterat pivottabellen.

![todo:image_alt_text](updating-slicer_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Slicers-UpdatingSlicer.py" >}}
{{< app/cells/assistant language="python-net" >}}
