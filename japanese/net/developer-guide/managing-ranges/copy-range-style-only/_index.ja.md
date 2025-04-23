---
title: スタイルのみをコピーします。
type: docs
weight: 620
url: /ja/net/copy-range-style-only/
---

{{% alert color="primary" %}}

[Copy Range Data Only](/cells/ja/net/copy-range-data-only/)および[Copy Range Data with Style](/cells/ja/net/copy-range-data-with-style/)では、範囲のデータを単独でコピーする方法や書式を含めてコピーする方法について説明しました。また、書式のみをコピーすることも可能です。この記事ではその方法について説明します。

{{% /alert %}} 

この例では、ワークブックを作成し、データで埋め、範囲のスタイルのみをコピーします。

1. 範囲を作成します。
1. 指定した書式属性で[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)を作成します。
1. 範囲にスタイルを適用します。
1. 別のセルの範囲を作成します。
最初の範囲の書式を2番目の範囲にコピーします。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRangeStyleOnly-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
