---
title: Golangを使用したC++でソース範囲の行の高さを宛先範囲にコピー
linktitle: ソース範囲の行の高さを宛先範囲にコピー
type: docs
weight: 590
url: /ja/go-cpp/copy-row-heights-of-source-range-to-destination-range/
description: Aspose.Cells for C++を使用して、ソース範囲の行の高さを宛先範囲にコピーする方法を学びましょう。
---

{{% alert color="primary" %}}

時々、ユーザーはソース範囲の行の高さを宛先範囲にコピーする必要があります。Aspose.Cellsは、この目的のために[**PasteType::RowHeights**](https://reference.aspose.com/cells/go-cpp/pastetype/)列挙型を提供しています。[**GetPasteType()**](https://reference.aspose.com/cells/cpp/aspose.cells/pasteoptions/getpastetype/)プロパティに[**PasteType::RowHeights**](https://reference.aspose.com/cells/go-cpp/pastetype/)列挙型を設定すると、ソース範囲内のすべての行の高さが宛先範囲にコピーされます。

{{% /alert %}}

次のサンプルコードは、[**PasteType::RowHeights**](https://reference.aspose.com/cells/go-cpp/pastetype/) 列挙型を使用してソース範囲から宛先範囲に行の高さをコピーする方法を説明しています。このコードによって生成された出力ExcelファイルをMicrosoft Excelで開くと、宛先範囲の行の高さがソース範囲の行の高さと正確に一致していることがわかります。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyRowHeightsOfSourceRangeToDestinationRange.go" >}}
