---
title: Smart Markersでデータをグループ化する際に画像マーカーを使用する
type: docs
weight: 30
url: /ja/net/using-image-markers-while-grouping-data-in-smart-markers/
---

## **Smart Markersでデータをグループ化する際に画像マーカーを使用する**
次のサンプルでは、ブックを作成し、セルD2、E2、およびF2に次のSmart Markerタグを追加します。

{{< highlight java >}}

 &=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

次に、データソースにデータを入れ、[WorkbookDesigner.Process()](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process) メソッドを呼び出してSmart Markerタグを処理します。コードはこれらの画像 [moon.png](5115492.png) および [moon2.png](5115491.png) を使用していますが、任意の画像を使用できます。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageMarkersWhileGroupingDataInSmartMarkers-UsingImageMarkersWhileGroupingDataInSmartMarkers.cs" >}}
