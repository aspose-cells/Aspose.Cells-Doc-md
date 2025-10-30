---
title: GolangとC++を使用してシート内のシェイプの絶対位置を見つける
linktitle: ワークシート内の形状の絶対位置を検索
type: docs
weight: 8000
url: /ja/go-cpp/finding-absolute-position-of-shape-inside-the-worksheet/
description: Aspose.Cellsを使用してGolangとC++でシート内のシェイプの絶対位置を特定する方法
---

{{% alert color="primary" %}}

時々、ワークシート内の形状の絶対位置を知る必要があります。Aspose.Cellsはこの目的のために[**Shape.GetLeftToCorner()**](https://reference.aspose.com/cells/go-cpp/shape/getlefttocorner/)および[**Shape.GetTopToCorner()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettoptocorner/)プロパティを提供しています。これらのプロパティは、ワークシート内の形状の絶対位置をピクセル単位で返します。

{{% /alert %}}

次のサンプルコードは、ワークシート内の最初の形状の絶対位置をピクセル単位で表示します。サンプルコードは、次のコンソール出力を表示します:

{{< highlight java >}}

Absolute Position of this Shape is (320 , 183)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindingAbsolutePositionOfShapeInsideTheWorksheet.go" >}}
