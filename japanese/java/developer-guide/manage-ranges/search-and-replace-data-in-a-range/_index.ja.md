---
title: 範囲内のデータを検索および置換する
type: docs
weight: 60
url: /ja/java/search-and-replace-data-in-a-range/
description: この記事では、Javaコードを使用してExcelの範囲内でデータを検索および置換する方法を示しています。
keywords: javaでExcel内のデータを検索および置換、javaでExcel内のデータを検索、javaで範囲内のデータを検索および置換、javaで範囲内のデータを検索、javaで範囲内のデータを検索、javaで範囲内のデータを検索、javaで範囲内のデータを検索、javaでExcel内のデータを検索、javaで範囲内のデータを検索、javaでExcel内のデータを範囲内で検索および置換、javaでExcel内のデータを範囲内で検索および置換、javaで範囲内でデータを検索および置換
---

{{% alert color="primary" %}}

時には、特定の範囲内のデータを検索して置換する必要があります。Aspose.Cellsを使用すれば、検索を特定の範囲に制限することができます。この記事ではその方法について説明します。

{{% /alert %}}

Aspose.Cellsではデータを検索する際に範囲を指定するための [**FindOptions.setRange()**](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#setRange(com.aspose.cells.CellArea)) メソッドを提供します。

例えば、「search」という文字列を検索して「replace」に置換したい場合、「E3:H6」という範囲内でのみ置換したいとします。以下のスクリーンショットでは、「search」という文字列がいくつかのセルで見られますが、指定された範囲内だけに置換したいと思います。

**入力ファイル**

![todo:image_alt_text](search-and-replace-data-in-a-range_1.png)

コードの実行後、出力ファイルは以下のようになります。「search」という文字列は範囲内のすべてのセルで「replace」と置換されています。

**出力ファイル**

![todo:image_alt_text](search-and-replace-data-in-a-range_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchReplaceDataInRange-SearchReplaceDataInRange.java" >}}

## 関連記事

- [データの検索](/cells/ja/java/find-or-search-data/)
