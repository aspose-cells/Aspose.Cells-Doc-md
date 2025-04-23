---
title: ワークシート内の形状の絶対位置を検索
type: docs
weight: 7000
url: /ja/java/finding-absolute-position-of-shape-inside-the-worksheet/
description: Aspose.Cells for JavaのAPIを通じてワークシート内の形状の絶対位置を検索する方法を学びます。
keywords: Javaで形状の絶対位置を検索する方法、Javaを使用して形状の絶対位置を取得する方法、ワークシート内の形状の絶対位置を取得する方法via Java、Javaで形状の絶対位置を測定する方法。
---

{{% alert color="primary" %}}

ワークシート上の形状の絶対位置を知る必要があることがあります。Aspose.Cellsはこの目的のために[**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner)と[**Shape.getTopToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner)プロパティを提供します。これらのプロパティは、ワークシート内の形状の絶対位置をピクセル単位で返します。

{{% /alert %}}

## **Shape.getLeftToCorner()およびShape.getTopToCorner()プロパティの説明**

このスクリーンショットは、[**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner)と[**Shape.getTopToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner)プロパティが測定する距離を説明しています。

絶対位置を測定する方法

![todo:image_alt_text](finding-absolute-position-of-shape-inside-the-worksheet_1.png)

次のサンプルコードは、ワークシート内の最初の形状の絶対位置をピクセル単位で表示します。コードは、コンソールに次の出力を表示します：

{{< highlight java >}}

Absolute Position of this Shape is (320, 180)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindAbsolutePositionOfShape-FindAbsolutePositionOfShape.java" >}}
{{< app/cells/assistant language="java" >}}
