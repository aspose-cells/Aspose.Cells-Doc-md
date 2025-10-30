---
title: Golangを使ったリンクされた図形の値を更新（C++経由）
linktitle: リンクされた形状の値をリフレッシュ
type: docs
weight: 3200
url: /ja/go-cpp/refresh-values-of-linked-shapes/
description: Aspose.Cells for C++を使用してExcelファイル内のリンクされた図形の値を更新する方法を学びます。
---

{{% alert color="primary" %}}

時々、Excelファイルにはセルにリンクされた形状がある場合があります。Microsoft Excelでは、リンクされたセルの値を変更すると、リンクされた形状の値も変更されます。Aspose.Cellsでも、XLSまたはXLSX形式でワークブックを保存する場合には、この動作が適切に機能します。ただし、ワークブックをPDFやHTML形式で保存する場合には、リンクされた形状の値をリフレッシュするために[**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/go-cpp/shapecollection/updateselectedvalue/)メソッドを呼び出さなければなりません。

{{% /alert %}}

## 例

以下のスクリーンショットは、サンプルコードで使用されているソースExcelファイルを示しています。このファイルには、セルA1からE4にリンクされた画像があります。Aspose.Cellsを使ってセルB4の値を変更し、その後[**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/go-cpp/shapecollection/updateselectedvalue/)メソッドを呼び出して画像の値を更新し、PDF形式で保存します。

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

指定されたリンク済みExcelファイル（[ソースExcelファイル](95584291.xlsx)）と出力PDF（[出力PDF](95584292.pdf)）はリンクからダウンロード可能です。

### C++コードによるリンクされた図形の値の更新

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RefreshValuesOfLinkedShapes.go" >}}
