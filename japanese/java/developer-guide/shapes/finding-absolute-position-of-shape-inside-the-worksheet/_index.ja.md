---
title: ワークシート内の形状の絶対位置を見つける
type: docs
weight: 7000
url: /ja/java/finding-absolute-position-of-shape-inside-the-worksheet/
---
{{% alert color="primary" %}}

場合によっては、ワークシート上の図形の絶対位置を知る必要があります。 Aspose.Cells は[**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner)と[**Shape.getTopToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner)この目的のためのプロパティ。これらのプロパティは、ワークシート内の図形の絶対位置をピクセル単位で返します。

{{% /alert %}}

## **Shape.getLeftToCorner() および Shape.getTopToCorner() プロパティの説明**

このスクリーンショットは、[**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner)と[**Shape.getTopToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner)プロパティ測定。

**絶対位置測定**

![todo:画像_代替_文章](finding-absolute-position-of-shape-inside-the-worksheet_1.png)

次のサンプル コードは、ワークシート内の最初の図形の絶対位置をピクセル単位で表示します。このコードは、コンソールに次の出力を表示します。

{{< highlight "java" >}}

Absolute Position of this Shape is (320, 180)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindAbsolutePositionOfShape-FindAbsolutePositionOfShape.java" >}}
