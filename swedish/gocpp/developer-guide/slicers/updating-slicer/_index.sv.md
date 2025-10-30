---
title: Uppdatera Slicer med Golang via C++
linktitle: Uppdatera slicer
type: docs
weight: 50
url: /sv/go-cpp/updating-slicer/
description: Den här artikeln visar hur man uppdaterar länkade pivottabeller genom att uppdatera slicer med API et Aspose.Cells for C++.
keywords: Aspose.Cells C++ Uppdatera slicer, C++ hur man ändrar slicer, hur man justerar slicer i C++, hur man väljer eller avmarkerar slicer objekt.
---

## **Möjliga användningsscenario**

Om du vill uppdatera en slicer i Microsoft Excel, välj eller avmarkera dess objekt, uppdateras slicer-tabellen eller pivottabellen därefter. Använd [**Slicer.GetSlicerCacheItems()**](https://reference.aspose.com/cells/go-cpp/slicercache/getslicercacheitems/) för att välja eller avmarkera slicer objekt med Aspose.Cells och anropa sedan [**Slicer.Refresh()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/refresh/)-metoden för att uppdatera slicer tabellen eller pivottabellen.

## **Hur man uppdaterar snittet**

Följande exempelkod laddar [provmappen](67338475.xlsx) som innehåller en befintlig snitt. Den avmarkerar den 2:a och 3:e objekten i snittet och uppdaterar snittet sedan. Den sparar sedan arbetsboken som [utmatningsmapp](67338476.xlsx). Skärmbilden nedan visar effekten av exempelkoden på provmappen. Som du kan se på skärmbilden, har uppdateringen av snittet med markerade objekt också uppdaterat pivottabellen.

![todo:image_alt_text](updating-slicer_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UpdatingSlicer.go" >}}
