---
title: Uppdatera slicer
type: docs
weight: 50
url: /sv/net/updating-slicer/
description: Den här artikeln visar hur du uppdaterar länkade pivottabeller genom att uppdatera snittet med hjälp av Aspose.Cells for .NET API et.
keywords: Aspose.Cells C# Uppdatera snittet, C# hur man ändrar snittet, hur man justerar snittet i C#, hur man väljer eller avmarkerar snittobjekten.
---

## **Möjliga användningsscenario**

Om du vill uppdatera snittet i Microsoft Excel, välj eller avmarkera dess objekt, det kommer sedan att uppdatera snittabellen eller pivottabellen enligt. Använd [**Slicer.SlicerCache.SlicerCacheItems**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicercache/properties/slicercacheitems) för att välja eller avmarkera snittobjekten med Aspose.Cells och ring sedan [**Slicer.Refresh()**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicer/methods/refresh) metoden för att uppdatera snittabellen eller pivottabellen.

## **Hur man uppdaterar snittet**

Följande exempelkod laddar [provmappen](67338475.xlsx) som innehåller en befintlig snitt. Den avmarkerar den 2:a och 3:e objekten i snittet och uppdaterar snittet sedan. Den sparar sedan arbetsboken som [utmatningsmapp](67338476.xlsx). Skärmbilden nedan visar effekten av exempelkoden på provmappen. Som du kan se på skärmbilden, har uppdateringen av snittet med markerade objekt också uppdaterat pivottabellen.

![todo:image_alt_text](updating-slicer_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Slicers-UpdatingSlicer.cs" >}}
