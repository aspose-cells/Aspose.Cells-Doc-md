---
title: 範囲スタイルのみコピー
type: docs
weight: 350
url: /ja/java/copy-range-style-only/
---
{{% alert color="primary" %}} 

[範囲データのみをコピー](/cells/ja/java/copy-range-data-only/)と[スタイル付きの範囲データをコピー](/cells/ja/java/copy-range-data-with-style/)書式設定の有無にかかわらず、ある範囲から別の範囲にデータをコピーする方法を説明しました。範囲のフォーマットのみをコピーすることも可能です。この記事では、その方法を示します。

{{% /alert %}} 
## **範囲スタイルのみコピー**
この例では、ブックを作成し、それにデータを入力して、範囲のスタイルのみをコピーします。

1. 範囲を作成します。
1. 指定されたフォーマット属性を持つスタイル オブジェクトを作成します。
1. スタイルの書式設定を範囲に適用します。
1. セルの 2 番目の範囲を作成します。
1. 最初の範囲の書式を 2 番目の範囲にコピーします。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRangeStyleOnly-CopyRangeStyleOnly.java" >}}
