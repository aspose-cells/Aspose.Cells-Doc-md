---
title: Använda bildmarkörer samtidigt som data grupperas i smarta markörer
type: docs
weight: 30
url: /sv/net/using-image-markers-while-grouping-data-in-smart-markers/
---
## **Använda bildmarkörer samtidigt som data grupperas i smarta markörer**
Följande exempel skapar en arbetsbok och lägger sedan till följande smarta markörtaggar i cellerna D2, E2 respektive F2.

{{< highlight "java" >}}

 &=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

 Sedan fyller den datakällan med data och anropar[WorkbookDesigner.Process()](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process) metod för att bearbeta smarta markörtaggar. Koden använder dessa bilder dvs[moon.png](5115492.png) och[moon2.png](5115491.png) men du kan använda vilken bild som helst.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageMarkersWhileGroupingDataInSmartMarkers-UsingImageMarkersWhileGroupingDataInSmartMarkers.cs" >}}
