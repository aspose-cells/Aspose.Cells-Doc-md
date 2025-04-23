---
title: セルの値がシングルクォートマークで始まるかどうかを検索
type: docs
weight: 270
url: /ja/nodejs-cpp/find-if-the-cell-value-starts-with-single-quote-mark/
description: Aspose.Cells for Node.js via C++ APIを通じて、セルの値が先頭にシングルクォートを持つかどうかを調べる方法を学びましょう。
keywords: セルの値がシングルクォートで始まるかどうかを検索（Node.js via C++）、セルの値がシングルクォートで始まるかどうかを調べる（Node.js via C++）
---

{{% alert color="primary" %}}

Aspose.Cellsは、セルの値がシングルクォートで始まるかどうかを調べる[**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-)メソッドを提供しています。この機能以前は、sampleや'sample'のような文字列を区別する方法はありませんでした。

{{% /alert %}}

次のサンプルコードは、sampleや'sample'のような文字列を[**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--)メソッドだけでは区別できないことを説明しています。そのため、区別するには[**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-)メソッドを使う必要があります。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-SearchCellStartsWithSingleQuote.js" >}}

