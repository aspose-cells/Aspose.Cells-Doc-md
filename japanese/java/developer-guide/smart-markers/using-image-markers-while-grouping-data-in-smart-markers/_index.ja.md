---
title: スマート マーカーでデータをグループ化する際の画像マーカーの使用
type: docs
weight: 630
url: /ja/java/using-image-markers-while-grouping-data-in-smart-markers/
---
{{% alert color="primary" %}} 

この記事では、スマート マーカーでデータをグループ化する際の画像マーカーの使用例を示します。

{{% /alert %}} 
## **スマート マーカーでデータをグループ化する際の画像マーカーの使用**
次のサンプル コードでは、ワークブックを作成し、セル D2、E2、および F2 にそれぞれ次のスマート マーカー タグを追加します。

{{< highlight "java" >}}

 &=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

次に、データ ソースにデータを入力し、[WorkbookDesigner.Process()](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process\(\) ) スマート マーカー タグを処理するメソッド。コードはこれらの画像を使用します。[月.png](5472549.png)と[moon2.png](5472548.png)ただし、任意の画像を使用できます。次のスクリーンショットは、このサンプル コードの出力を示しています。ご覧のとおり、E 列と F 列のデータは、D 列のデータに対してグループ化されています。

![todo:画像_代替_文章](using-image-markers-while-grouping-data-in-smart-markers_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Technical-Articles-SmartMarkerGroupingImage.java" >}}
