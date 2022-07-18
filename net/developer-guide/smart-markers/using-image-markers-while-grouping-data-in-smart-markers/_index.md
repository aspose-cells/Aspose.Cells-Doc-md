---
title: Using Image Markers while Grouping Data in Smart Markers
type: docs
weight: 30
url: /net/using-image-markers-while-grouping-data-in-smart-markers/
---

## **Using Image Markers while Grouping Data in Smart Markers**
The following sample creates a workbook and then adds the following smart marker tags in cells D2, E2 and F2 respectively.

{{< highlight java >}}

 &=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

Then it fills the data source with data and calls the [WorkbookDesigner.Process()](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process) method to process smart marker tags. The code uses these images i.e [moon.png](5115492.png) and [moon2.png](5115491.png) but you can use any image.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageMarkersWhileGroupingDataInSmartMarkers-UsingImageMarkersWhileGroupingDataInSmartMarkers.cs" >}}
