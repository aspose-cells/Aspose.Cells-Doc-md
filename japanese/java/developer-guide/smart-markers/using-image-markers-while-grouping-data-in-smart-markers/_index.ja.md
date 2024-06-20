---
title: Smart Markersでデータをグループ化する際に画像マーカーを使用する
type: docs
weight: 630
url: /ja/java/using-image-markers-while-grouping-data-in-smart-markers/
---

{{% alert color="primary" %}} 

この記事では、スマートマーカーを使用してデータをグループ化する際の画像マーカーの使用例を示します。

{{% /alert %}} 
## **Smart Markersでデータをグループ化する際に画像マーカーを使用する**
次のサンプルコードでは、ワークブックを作成し、それからそれぞれのセルD2、E2、F2にスマートマーカータグを追加します。

{{< highlight java >}}

 &=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

その後、データソースにデータを入れ、[WorkbookDesigner.Process()](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process\(\))メソッドを実行してスマートマーカータグを処理します。このコードは[image.png](5472549.png)および[image2.png](5472548.png)を使用していますが、任意の画像を使用できます。以下のスクリーンショットは、このサンプルコードの出力を示しています。D列とE列のデータは、D列のデータに従ってグループ化されていることがわかります。

![todo:image_alt_text](using-image-markers-while-grouping-data-in-smart-markers_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Technical-Articles-SmartMarkerGroupingImage.java" >}}
