---
title: C++を使用してGolangでセルの値がシングルクォート記号（ ）で始まるかどうかを確認します
linktitle: セルの値がシングルクォートマークで始まるかどうかを検索
type: docs
weight: 270
url: /ja/go-cpp/find-if-the-cell-value-starts-with-single-quote-mark/
description: Aspose.Cells for C++ APIを通じてセル値がシングルクォートマークで始まるかどうかを調べる方法を学習します。
keywords: シングルクォーテーション記号で始まるセルの値を見つける、シングルクォーテーション記号で始まるセルの値を検索する
---

{{% alert color="primary" %}}

Aspose.Cellsは、セルの値がシングルクォーテーション記号で始まるかどうかを見つけるための[**Style::QuotePrefix**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/)プロパティを提供します。このプロパティがなかった場合、sampleと 'sampleなどの文字列を区別する方法はありません。

{{% /alert %}}

以下のサンプルコードは、sampleと 'sampleのような文字列を[**Cell::GetStringValue**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/)プロパティで区別できないことを説明します。そのため、それらを区別するには[**Style::QuotePrefix**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getquoteprefix/)プロパティを使用する必要があります。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindIfTheCellValueStartsWithSingleQuoteMark.go" >}}
