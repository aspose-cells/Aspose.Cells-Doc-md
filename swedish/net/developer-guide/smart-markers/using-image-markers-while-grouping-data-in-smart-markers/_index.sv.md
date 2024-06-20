---
title: Använda bildenkoder vid gruppering av data i Smart Markers
type: docs
weight: 30
url: /sv/net/using-image-markers-while-grouping-data-in-smart-markers/
---

## **Använda bildenkoder vid gruppering av data i Smart Markers**
Följande exempel skapar en arbetsbok och lägger sedan till följande smarta markör-taggar i cellerna D2, E2 och F2 respektive.

{{< highlight java >}}

 &=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

Sedan fylls datakällan med data och [WorkbookDesigner.Process()](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process)-metoden anropas för att bearbeta smarta markör-taggar. Koden använder dessa bilder dvs [moon.png](5115492.png) och [moon2.png](5115491.png) men du kan använda vilken bild som helst.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageMarkersWhileGroupingDataInSmartMarkers-UsingImageMarkersWhileGroupingDataInSmartMarkers.cs" >}}
