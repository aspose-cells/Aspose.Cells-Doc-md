---
title: スタイル付きデータの範囲コピー（C++）
linktitle: スタイル付きの範囲のデータをコピーします。
type: docs
weight: 610
url: /ja/go-cpp/copy-range-data-with-style/
description: セルのスタイルを含む範囲のデータを、Aspose.Cells for C++を使用してコピーします。
---

{{% alert color="primary" %}}

[コピー範囲のデータのみ](/cells/ja/cpp/copy-range-data-only/)では、セル範囲間でセルデータをコピーする方法を説明しています。本記事では、Aspose.Cells for C++を使用してセル範囲をコピーし、その書式スタイルを保持する方法を紹介します。

{{% /alert %}}

Aspose.Cellsは、範囲に関するクラスとメソッド（[**CreateRange()**](https://reference.aspose.com/cells/go-cpp/cells/createrange_string_string/)、[**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/)、[**ApplyStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/)）を提供しています。

この例は、次の操作方法を示しています：

1. ブックを作成
1. セルにデータを入力
1. [**Range**](https://reference.aspose.com/cells/go-cpp/range/)を作成
1. [**Style**](https://reference.aspose.com/cells/go-cpp/style/)オブジェクトを作成および設定
1. 範囲にスタイルを適用
1. 2つ目の範囲を作成
1. 範囲間でフォーマットされたデータをコピー

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyRangeDataWithStyle.go" >}}
