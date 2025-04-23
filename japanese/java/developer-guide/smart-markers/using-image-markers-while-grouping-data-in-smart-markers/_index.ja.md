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

次に、データソースにデータを入力し、[WorkbookDesigner.Process()](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process--) メソッドを呼び出してスマートマーカータグを処理します。コードでは、[moon.png](5472549.png)と[moon2.png](5472548.png)を使用していますが、任意の画像を使用可能です。このサンプルコードの出力結果は以下のスクリーンショットに示されており、列EおよびFのデータが列Dのデータに基づいてグループ化されています。

![todo:image_alt_text](using-image-markers-while-grouping-data-in-smart-markers_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Technical-Articles-SmartMarkerGroupingImage.java" >}}
{{< app/cells/assistant language="java" >}}
