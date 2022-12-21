---
title: 特定のスタイルのセルを見つける
type: docs
weight: 80
url: /ja/java/find-cells-with-specific-style/
description: この記事では、MS Excel と Aspose.Cells for Java API を使用して特定のスタイルのセルを検索する方法を示します。
keywords: find cells with specific style, find cells with specific style excel, find cells with specific style excel java, search cells with specific style, search cells with specific style excel, search cells with specific style excel java, how to find cells with specific style, how to find cells with specific style excel, how to find cells with specific style excel java
---
{{% alert color="primary" %}}

場合によっては、特定のスタイルを持つセルを見つける必要があります。この記事では、Microsoft Excel と Aspose.Cells for Java API を使用してこれを実現する方法を示します。

{{% /alert %}}

## Microsoft エクセルを使う

これらは、MS Excel で特定のスタイルのセルを検索するために必要な手順です。

1. 選択する**検索と選択**の中に**ホームタブ**.
1. 選択する**探す**.
1. クリック**オプション**詳細オプションが表示されない場合。
1. 選択する**Cell からフォーマットを選択...**から**フォーマット**落ちる。
1. 検索するスタイルのセルを選択します。
1. クリック**すべてを検索**選択したセルに似たスタイルのすべてのセルを検索します。

## Aspose.Cells for Java を使用

 Aspose.Cells for Java は、特定のスタイルでワークシート内のセルを検索する機能を提供します。このために、API が提供します。[**FindOptions.setStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#Style)財産。

### サンプルコード

次のコード スニペットは、セルのスタイルと同じスタイルを持つすべてのセルを検索します。**A1**それらのセル内のテキストを変更します。ソース ファイルと出力ファイルのスクリーンショットを参照して、サンプル コードの出力を分析してください。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindCellsWithSpecificStyle-FindCellsWithSpecificStyle.java" >}}

コードの実行後、セル A1 と同じスタイルを持つすべてのセルに "Found" というテキストが表示されます。

### スクリーンショット

![todo:画像_代替_文章](find-cells-with-specific-style_1.png)

**形：**スタイルを持つセルを含むソース ファイル

次のコードによって生成された出力ファイルを次に示します。のセルと同じスタイルを持つすべてのセルを見ることができます**A1**「見つかりました」というテキストがあります

![todo:画像_代替_文章](find-cells-with-specific-style_2.png)

**形：**検索後に見つかったセルを含む出力ファイル**A1**スタイル
