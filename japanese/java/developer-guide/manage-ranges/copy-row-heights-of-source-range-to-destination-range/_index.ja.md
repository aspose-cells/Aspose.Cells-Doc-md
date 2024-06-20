---
title: ソース範囲の行の高さを宛先範囲にコピー
type: docs
weight: 250
url: /ja/java/copy-row-heights-of-source-range-to-destination-range/
---

{{% alert color="primary" %}} 

ユーザーは時々、ソース範囲の行の高さを宛先範囲にコピーする必要があります。Aspose.Cellsは、この目的のために[PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW_HEIGHTS)列挙型を提供しています。[PasteOptions.setPasteType()](https://reference.aspose.com/cells/java/com.aspose.cells/pasteoptions#PasteType)プロパティを[PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW_HEIGHTS)列挙型で設定すると、ソース範囲内のすべての行の高さが宛先範囲にコピーされます。

{{% /alert %}} 
## **ソース範囲の行の高さを宛先範囲にコピーします。**
以下のサンプルコードでは、[PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW_HEIGHTS)列挙型を使用して、ソース範囲の行の高さを宛先範囲にコピーする方法について説明しています。このコードで生成された出力エクセルファイルをMicrosoft Excelで開くと、宛先範囲の行の高さがソース範囲の行の高さとまったく同じであることが分かります。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRowHeights-CopyRowHeights.java" >}}
