---
title: セル値または範囲の接頭辞を保存します
type: docs
weight: 310
url: /ja/nodejs-cpp/preserve-single-quote-prefix-of-cell-value-or-range/
description: セルの値または範囲のシングルクオートプリフィックスを保持する方法をAspose.Cells for Node.js via C++ APIを使って学びます。
keywords: セルの値または範囲のシングルクオートプリフィックスを保持するNode.jsをC++経由で行う。先頭のアポストロフィーまたはシングルクオート記号を非表示にするNode.jsをC++経由で。先頭のアポストロフィーまたはシングルクオート記号を表示するNode.jsをC++経由で。
---

## **可能な使用シナリオ**

先頭にアポストロフィやシングルクォートマークがあるセルに値を入れると、Microsoft Excelはそれを非表示にしますが、セルを選択すると、次のスクリーンショットに示すように、既定の値が表示されます。

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells for Node.js via C++はMicrosoft Excelのように先頭のアポストロフィやシングルクオートを隠しますが、そのセルに [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-) を **true** に設定します。セルのスタイルを空に設定すると、[**Style.getQuotePrefix()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getQuotePrefix--) は再び **false** になります。この問題に対処するため、Aspose.Cells for Node.js via C++は [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-) メソッドを提供しており、これが **false** に設定された場合、[**Style.getQuotePrefix()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getQuotePrefix--) は一切更新されず、古い値が保持されます。つまり、[**Style.getQuotePrefix()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getQuotePrefix--) の古い値が **true** だった場合はそのまま **true** のままになり、**false** だった場合はそのまま **false** のまま維持されます。

## **セル値または範囲の先頭にシングルクォートのプレフィックスを保存**

以下のサンプルコードは、前述の [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-) メソッドの使用例を説明しています。コード内のコメントを読み、下記のコンソール出力を確認してください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-preserve-single-quote-prefix-of-cell-value-or-range.js" >}}



## **コンソール出力**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.quotePrefix is False, it means, do not update the value of Cell.Style.quotePrefix.

Similarly, when StyleFlag.quotePrefix is True, it means, update the value of Cell.Style.quotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
