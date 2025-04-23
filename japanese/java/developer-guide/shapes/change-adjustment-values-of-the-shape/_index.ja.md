---
title: シェイプの調整値の変更
type: docs
weight: 3200
url: /ja/java/change-adjustment-values-of-the-shape/
---

{{% alert color="primary" %}} 

Aspose.Cellsは、形状の調整ポイントを変更するために [Shape.getGeometry().getShapeAdjustValues()](https://reference.aspose.com/cells/java/com.aspose.cells/geometry#ShapeAdjustValues) プロパティを提供しています。Microsoft ExcelのUIでは、調整は黄色のダイヤモンドノードとして表示されます。たとえば:

- 角丸四角形は、円弧を変更するための調整があります
- 三角形は、ポイントの位置を変更するための調整があります
- 台形には、上部の幅を変更する調整があります
- 矢印には、頭部と末尾の形状を変更するための2つの調整があります

この記事では、異なる形状の調整値を変更する [Shape.getGeometry().getShapeAdjustValues()](https://reference.aspose.com/cells/java/com.aspose.cells/geometry#ShapeAdjustValues) プロパティの使用方法について説明します。

{{% /alert %}} 
## **図形の調整値を変更**
次のサンプルコードでは、ソースのExcelファイルの最初のワークシートの最初の3つの図形にアクセスし、その後、図形の調整値を変更します。以下のスクリーンショットは、調整値を変更する前の図形の外観と、調整値を変更した後の図形の外観を示しています。
### **調整値を変更する前の図形描画**
![todo:image_alt_text](change-adjustment-values-of-the-shape_1.png)
### **調整値を変更した後の図形描画**
![todo:image_alt_text](change-adjustment-values-of-the-shape_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeAdjustmentValuesOfShape-ChangeAdjustmentValuesOfShape.java" >}}
{{< app/cells/assistant language="java" >}}
