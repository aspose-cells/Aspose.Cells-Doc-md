---
title: ソース範囲の行の高さを宛先範囲にコピー
type: docs
weight: 590
url: /ja/net/copy-row-heights-of-source-range-to-destination-range/
---

{{% alert color="primary" %}}

ユーザーは時々、ソース範囲の行の高さを宛先の範囲にコピーする必要があります。Aspose.Cellsはこの目的のために[**PasteType.RowHeights**](https://reference.aspose.com/cells/net/aspose.cells/pastetype)列挙型を提供しています。[**PasteOptions.PasteType**](https://reference.aspose.com/cells/net/aspose.cells/pasteoptions/properties/pastetype)プロパティを[**PasteType.RowHeights**](https://reference.aspose.com/cells/net/aspose.cells/pastetype)列挙型で設定すると、ソース範囲内のすべての行の高さが宛先範囲にコピーされます。

{{% /alert %}}

次のサンプルコードは、[**PasteType.RowHeights**](https://reference.aspose.com/cells/net/aspose.cells/pastetype) 列挙型を使用して、ソース範囲の行の高さを宛先範囲にコピーする方法を説明しています。このコードで生成された出力エクセルファイルをMicrosoft Excelで開くと、宛先範囲の行の高さがソース範囲の行の高さとまったく同じであることがわかります。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetRowHeights-GetRowHeightsOfSourceRangeToDestinationRange.cs" >}}
