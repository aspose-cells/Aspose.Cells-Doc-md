---
title: リンクされた図形の値を更新
type: docs
weight: 3200
url: /ja/net/refresh-values-of-linked-shapes/
---
{{% alert color="primary" %}}

場合によっては、セルにリンクされたリンクされた図形が Excel ファイルに含まれていることがあります。 Microsoft Excel では、リンクされたセルの値を変更すると、リンクされた図形の値も変更されます。ワークブックを XLS または XLSX 形式で保存する場合、これは Aspose.Cells でも問題なく機能します。ただし、ワークブックを PDF または HTML 形式で保存する場合は、呼び出す必要があります。[**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/updateselectedvalue)リンクされた形状の値を更新するメソッド。

{{% /alert %}}

## 例

次のスクリーンショットは、以下のサンプル コードで使用されるソース Excel ファイルを示しています。セル A1 から E4 にリンクされたリンクされた画像があります。セル B4 の値を Aspose.Cells に変更して呼び出します。[**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/updateselectedvalue)写真の値を更新し、PDF 形式で保存するメソッド。

![todo:画像_代替_文章](refresh-values-of-linked-shapes_1.jpg)

ダウンロードできます[ソースの Excel ファイル](95584291.xlsx)そしてその[出力 PDF](95584292.pdf)指定されたリンクから。

### C# リンクされた図形の値を更新するコード

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-RefreshValueOfLinkedShapes-1.cs" >}}
