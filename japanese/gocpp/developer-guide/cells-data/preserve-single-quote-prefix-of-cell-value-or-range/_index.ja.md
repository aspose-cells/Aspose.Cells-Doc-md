---
title: セル値または範囲の先頭にあるシングルクォートを保持（Golang経由のC++）
linktitle: セル値または範囲の接頭辞を保存します
type: docs
weight: 310
url: /ja/go-cpp/preserve-single-quote-prefix-of-cell-value-or-range/
description: Aspose.Cells for C++ APIを通じてセル値や範囲のシングルクオートプレフィックスを保持する方法を学習します。
keywords: セル値または範囲の先頭アポストロフィを保持し、先頭のアポストロフィまたはシングルクォートマークを非表示にする、先頭のアポストロフィまたはシングルクォートマークを表示する
---

## **可能な使用シナリオ**

先頭のアポストロフィまたはシングルクオート記号を持つセルに値を入力すると、Microsoft Excelはそれを隠しますが、セルを選択すると、数式バーに先頭のアポストロフィまたはシングルクオートが表示される例です。

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.CellsはMicrosoft Excelと同様に先頭のアポストロフィまたはシングルクオートを隠しますが、そのセルには[**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/)を**true**に設定します。セルのスタイルを空に設定すると、[**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/)は再び**false**になります。この問題に対処するために、Aspose.Cellsは[**StyleFlag.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/getquoteprefix/)プロパティを提供しており、設定されているときは**false**にされると[**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/)は全く更新されず、古い値が保持されます。これは、[**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/)プロパティの古い値が**true**であった場合は**true**のまま、**false**だった場合はそのままです。

## **セル値または範囲の先頭にシングルクォートのプレフィックスを保存**

以下のサンプルコードは、前述の[**StyleFlag.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/styleflag/getquoteprefix/)プロパティの使用例を説明しています。コード内のコメントを読んで、以下のコードのコンソール出力も確認してください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-PreserveSingleQuotePrefixOfCellValueOrRange.go" >}}
## **コンソール出力**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
