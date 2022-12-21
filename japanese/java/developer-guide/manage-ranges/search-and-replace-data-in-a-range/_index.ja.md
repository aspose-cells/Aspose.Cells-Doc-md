---
title: 範囲内のデータの検索と置換
type: docs
weight: 60
url: /ja/java/search-and-replace-data-in-a-range/
description: この記事では、Java コードを使用して、Excel で範囲内のデータを検索および置換する方法を示します。
keywords: java search and replace data in excel, java search data in excel, java search and replace data in a range, java search data in a range, java searching data in a range, java searching data in range, java searching data in excel, java search data in range, search and replace data in excel with java, search and replace data in a range with java, search and replace data in range with java
---
{{% alert color="primary" %}}

場合によっては、目的の範囲外のセル値を無視して、範囲内の特定のデータを検索して置換する必要があります。 Aspose.Cells を使用すると、検索を特定の範囲に制限できます。この記事では、その方法について説明します。

{{% /alert %}}

Aspose.Cells は[**FindOptions.setRange()**](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#setRange(com.aspose.cells.CellArea)) データ検索時の範囲指定方法。

文字列を検索するとします。**"探す"**そしてそれを**"交換"**範囲内**E3:H6**.以下のスクリーンショットでは、文字列「検索」が複数のセルに表示されていますが、ここでは黄色で強調表示されている特定の範囲でのみ置き換えたいと考えています。

**入力ファイル**

![todo:画像_代替_文章](search-and-replace-data-in-a-range_1.png)

コードの実行後、出力ファイルは次のようになります。範囲内のすべての「検索」文字列は「置換」に置き換えられました。

**出力ファイル**

![todo:画像_代替_文章](search-and-replace-data-in-a-range_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchReplaceDataInRange-SearchReplaceDataInRange.java" >}}

## 関連記事

- [データの検索または検索](/cells/ja/java/find-or-search-data/)
