---
title: シェイプの調整値を変更する
type: docs
weight: 3200
url: /ja/java/change-adjustment-values-of-the-shape/
---
{{% alert color="primary" %}} 

Aspose.Cells提供[Shape.getGeometry().getShapeAdjustValues()](https://reference.aspose.com/cells/java/com.aspose.cells/geometry#ShapeAdjustValues)プロパティを使用して、シェイプを使用して調整ポイントを変更します。 Microsoft Excel UI では、調整は黄色のひし形ノードとして表示されます。例えば：

- 角丸長方形には、円弧を変更するための調整があります
- 三角形には、ポイントの位置を変更するための調整があります
- 台形には、トップの幅を変更するための調整があります
- 矢印には、頭と尾の形状を変更するための 2 つの調整があります。

この記事では、の使用について説明します。[Shape.getGeometry().getShapeAdjustValues()](https://reference.aspose.com/cells/java/com.aspose.cells/geometry#ShapeAdjustValues)プロパティを使用して、さまざまな形状の調整値を変更します。

{{% /alert %}} 
## **シェイプの調整値を変更する**
次のサンプル コードは、ソース Excel ファイルの最初のワークシートの最初の 3 つの図形にアクセスし、図形の調整値を変更します。以下のスクリーンショットは、調整値を変更する前と調整値を変更した後のシェイプの外観を示しています。
### **調整値を変更する前の形状の描画**
![todo:画像_代替_文章](change-adjustment-values-of-the-shape_1.png)
### **調整値を変更して描画する**
![todo:画像_代替_文章](change-adjustment-values-of-the-shape_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeAdjustmentValuesOfShape-ChangeAdjustmentValuesOfShape.java" >}}
