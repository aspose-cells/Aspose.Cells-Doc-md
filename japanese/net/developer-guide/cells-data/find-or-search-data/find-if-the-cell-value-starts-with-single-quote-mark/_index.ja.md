---
title: セルの値がシングルクォートマークで始まるかどうかを検索
type: docs
weight: 270
url: /ja/net/find-if-the-cell-value-starts-with-single-quote-mark/
description: Aspose.Cells for .NET APIを介してセルの値がシングルクォーテーション記号で始まるかどうかを見つける方法を学びます。
keywords: シングルクォーテーション記号で始まるセルの値を見つける、シングルクォーテーション記号で始まるセルの値を検索する
---

{{% alert color="primary" %}}

Aspose.Cellsは、セルの値がシングルクォーテーション記号で始まるかどうかを見つけるための[**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)プロパティを提供します。このプロパティがなかった場合、sampleと 'sampleなどの文字列を区別する方法はありません。

{{% /alert %}}

以下のサンプルコードは、sampleと 'sampleのような文字列を[**Cell.StringValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/stringvalue)プロパティで区別できないことを説明します。そのため、それらを区別するには[**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)プロパティを使用する必要があります。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindIfCellValueStartsWithSingleQuote-FindIfCellValueStartsWithSingleQuote.cs" >}}
