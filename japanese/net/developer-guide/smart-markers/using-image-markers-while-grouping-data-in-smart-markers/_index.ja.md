---
title: スマート マーカーでデータをグループ化する際の画像マーカーの使用
type: docs
weight: 30
url: /ja/net/using-image-markers-while-grouping-data-in-smart-markers/
---
## **スマート マーカーでデータをグループ化する際の画像マーカーの使用**
次のサンプルでは、ワークブックを作成し、セル D2、E2、および F2 にそれぞれ次のスマート マーカー タグを追加します。

{{< highlight "java" >}}

 &=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

次に、データ ソースにデータを入力し、[WorkbookDesigner.Process()](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process)スマート マーカー タグを処理するメソッド。コードはこれらの画像を使用します。[月.png](5115492.png)と[moon2.png](5115491.png)ただし、任意の画像を使用できます。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageMarkersWhileGroupingDataInSmartMarkers-UsingImageMarkersWhileGroupingDataInSmartMarkers.cs" >}}
